import asyncio
import configparser
import datetime
import json
import math
import os
import os.path
import random
import re
import shlex
import sys
import time
import urllib.request
from datetime import date, datetime
from io import BytesIO
from operator import add, mul, pow, sub, truediv

import aiohttp
import discord
import mysql
import PIL
import pytz
import requests
import urllib3
import youtube_dl
from discord import Guild, Intents, Member
from discord.ext import commands, tasks
from discord.ext.commands import *
from discord.utils import get
from discord.voice_client import VoiceClient
from mysql import connector
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

operators = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv,
    ':': truediv

}
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from xml.etree import cElementTree

from packages.all import *
from packages.p_mysql import *
client=discord.Client


class MOD(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def help_mods(self, ctx): 
        embed=discord.Embed(title="Help Menu - <a:ay_mods:803690249041084446>Moderation<a:ay_mods:803690249041084446>", color=0xff0000)
        embed.add_field(name="p!warn", value="Warne einen User <user> <reason>")
        embed.add_field(name="p!kick", value="Kicke einen User <user> <reason>", inline=False)
        embed.add_field(name="p!ban", value="Banne einen User <user> <reason>", inline=False)
        embed.add_field(name="p!purge", value="Säubere den Chat <amount>", inline=False)
        embed.add_field(name='p!banlist', value='Zeige alle gebannten User', inline=False)
        embed.add_field(name="p!warncheck", value="Sehe alle Warns von <member>", inline=False)
        message = await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def warn(self, ctx, member:discord.Member, *, reason:str="no reason"):
        sql = "INSERT INTO pinto.warn(guildid, userid, count, reason, authors, tbid) VALUES(%s, %s, %s, %s, %s, %s)"
        val = (f"{ctx.guild.id}", f"{member.id}", f"1", f"{reason}", f"{ctx.author.id}", f"{ctx.guild.id}.{member.id}")
        try:
            cur.execute(sql, val)
            await utils.send_embed(ctx=ctx, client=self.client, title="Verwarnung", desc=f"{member.mention} wurde verwarnt🛡")
        except:
            print(
            utils.get_warn(ctx=ctx, member=member))
            count = utils.get_warn(ctx=ctx, member=member)[2]
            reasons = utils.get_warn(ctx=ctx, member=member)[3]
            authors = utils.get_warn(ctx=ctx, member=member)[4]
            sql = f"UPDATE pinto.warn SET count='{int(count)+1}'WHERE tbid='{ctx.guild.id}.{member.id}'"
            cur.execute(sql)
            sql = f"UPDATE pinto.warn SET reason='{str(reasons)} ---;--- {reason}'WHERE tbid='{ctx.guild.id}.{member.id}'"
            cur.execute(sql)
            sql = f"UPDATE pinto.warn SET authors='{str(authors)} ---;--- {ctx.author.id}'WHERE tbid='{ctx.guild.id}.{member.id}'"
            cur.execute(sql)
            await utils.send_embed(ctx=ctx, client=self.client, title="Verwarnung", desc=f"{member.mention}  wurde verwarnt🛡")
            await ctx.message.add_reaction("<:JQY:802700281087262770>")

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.Member, *, reason=None):
        if member == ctx.author:
            embed=discord.Embed(title="Error", description=f"{ctx.author.mention} was versuchst du? Du kannst dich nicht selbst kicken.", color=0xff0000)
            embed.timestamp=datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await member.kick(reason=reason)
            embed = discord.Embed(title=f"{ctx.author.name} hat {member.name} gekickt", 
                                description=reason, 
                                color=0xff0000)
            channel=discord.channel
            embed.set_footer(text="Zeitpunkt des Kicks", 
                            icon_url="https://cdn.discordapp.com/avatars/809824051773177917/c1cb4b1dab35f99d7162b69e623e9ea6.png?size=256")
            embed.timestamp=datetime.utcnow()
            await ctx.send(embed=embed)
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.Member, *, reason=None):
        if member == ctx.author:
            embed=discord.Embed(title="Error", description=f"{ctx.author.mention} was versuchst du? Du kannst dich nicht selbst bannen.", color=0xff0000)
            embed.timestamp=datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            await member.ban(reason=reason, delete_message_days=3)
            embed = discord.Embed(title=f"{ctx.author.name} hat {member.name} dauerhaft von {ctx.guild.name} verbannt", description=reason, color=utils.embed_color(ctx=ctx, client=self.client))
            channel=discord.channel
            embed.set_footer(text="Zeitpunkt des Bans", icon_url="https://cdn.discordapp.com/avatars/809824051773177917/c1cb4b1dab35f99d7162b69e623e9ea6.png?size=256")
            embed.timestamp=datetime.utcnow()
            await ctx.send(embed=embed)
    @commands.command(aliases=['clear'])
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int, reason=None):
        await ctx.channel.purge(limit=amount+1)
        embed = discord.Embed(title=f"{ctx.author.name} hat {amount} Nachricht/en in {ctx.channel.name} gelöscht", description=reason, color=utils.embed_color(ctx=ctx, client=self.client))
        channel=discord.channel
        embed.set_footer(text="Purge", icon_url="https://cdn.discordapp.com/avatars/809824051773177917/c1cb4b1dab35f99d7162b69e623e9ea6.png?size=256")
        embed.timestamp=datetime.utcnow()
        message = await ctx.send(embed=embed)
        await asyncio.sleep(15)
        await message.delete()
    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def info(self,ctx, *, message):
        embed=discord.Embed(title="🚨INFO🚨", description=f"{message}", color=0xff2300)
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_footer(text=f"Adminbenachrichtigung")
        embed.add_field(value=f"[Bot Invite](https://discord.com/api/oauth2/authorize?client_id=809824051773177917&permissions=8&scope=bot\n \r) | [Support Server](https://discord.gg/S86cwzDxgq)", name="᲼᲼")
        embed.timestamp=datetime.utcnow()
        embed.set_footer(text=f"Gesendet von {ctx.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/809824051773177917/c1cb4b1dab35f99d7162b69e623e9ea6.png?size=256")
        await ctx.send(embed=embed)
        await ctx.message.delete()
    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel) and message.author.id == 792839933387472918:
            embed=discord.Embed(title="🔰INFORMATION🔰", description=f"{message.content}", color=0xff0000)
            embed.set_footer(text=f"Offizielle Serverbenachrichtigung")
            embed.add_field(value=f"[Bot Invite](https://discord.com/api/oauth2/authorize?client_id=809824051773177917&permissions=8&scope=bot\n \r) | [Support Server](https://discord.gg/kZp6zYA7xz)", name="᲼᲼")
            embed.timestamp=datetime.utcnow()
            await message.add_reaction("<a:JQY:802700281087262770>")
            await message.channel.send(embed=embed)
            cur.execute(f"SELECT * FROM pinto.server")
            a = cur.fetchall()
            for x in a:
                guild: discord.Guild = self.client.get_guild(x[0])
                if guild:
                    channel: discord.TextChannel = self.client.get_channel(x[1])
                    if channel:
                        try:
                            await channel.send(embed=embed)
                        except:
                            pass
    @commands.command()
    async def unban(self, ctx, *, member):
        if ctx and member and ctx.author.guild_permissions.ban_members:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Der User {user.mention} wurde erfolgreich entbannt')
                return
    @commands.command()
    async def php(self, ctx, message):
        embed=discord.Embed(title="REGELN", color=0xff2300)
        embed.add_field(name=f"{message}", value="_____________")
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        embed.timestamp=datetime.utcnow()
        embed.set_footer(text=f"{ctx.guild.name}")
        await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command()
    async def banlist(self, ctx,):

        if ctx.message.author.guild_permissions.ban_members:
            x = await ctx.message.guild.bans()
            x = '\n'.join([str(y.user) for y in x])
            embed = discord.Embed(title="Liste aller gebannten Member", description=x, colour=0xff0000)
            return await ctx.send(embed=embed)
    @commands.command()  
    async def warncheck(self, ctx, member: discord.Member):
        await ctx.send(embed=utils.get_member_warns(ctx=ctx, member=member))
    
    @commands.command()
    async def getinvite(self, ctx, id: int):
        if ctx.author.id == 792839933387472918:
            guild: discord.Guild = self.client.get_guild(id)
            if not guild:
                channel: discord.TextChannel = self.client.get_channel(id)
                if not channel:
                    embed = discord.Embed(title=f'Ein Fehler ist aufgetreten',
                                          description=f'Ich konnte nix mit dieser ID finden!')
                    embed.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)
                else:
                    link: discord.Invite = await channel.create_invite()
                    if link:
                        embed = discord.Embed(title=f'Hier ist dein Invite', color=0xffc585)
                        embed.add_field(name=f'Guild', value=f'{channel.guild} | {channel.guild.id}')
                        embed.add_field(name=f'Channel', value=f'{channel.name} | {channel.id}')
                        embed.add_field(name=f'Members', value=f'{len(channel.guild.members)}')
                        embed.add_field(name=f'link', value=f'{link}')
                        await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title=f'Ein Fehler ist aufgetreten',
                                              description=f'Ich konnte keinen Invite erstellen!')
                        embed.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar_url)
                        await ctx.send(embed=embed)
            else:
                ilink = ''
                ichannel = 0
                for channelx in guild.text_channels:
                    try:
                        if ilink == '':
                            link: discord.Invite = await channelx.create_invite()
                            if link:
                                ilink = f'**{link}**'
                                ichannel = channelx
                    except:
                        pass
                if ilink != '':
                    embed = discord.Embed(title=f'Hier ist dein Invite', color=0xffc585)
                    embed.add_field(name=f'Guild', value=f'{guild} | {guild.id}')
                    embed.add_field(name=f'Channel', value=f'{ichannel.name} | {ichannel.id}')
                    embed.add_field(name=f'Members', value=f'{len(guild.members)}')
                    embed.add_field(name=f'link', value=f'{ilink}')
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title=f'Ein Fehler ist aufgetreten',
                                          description=f'Ich konnte keinen Invite erstellen!')
                    embed.set_author(name=f'{ctx.author}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=embed)





def setup(client):
    client.add_cog(MOD(client))