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
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from xml.etree import cElementTree



client=discord.Client

class MISC(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help_misc(self, ctx):
        embed=discord.Embed(title="Help Menu - ⚙️Misc⚙️", color=0xffc585)
        embed.add_field(name="p!whois <member>", value="Zeige die Info zu einem Member", inline=False)
        embed.add_field(name="p!serverinfo", value="Zeigt dir die Info zum Server an", inline=False)
        embed.add_field(name="p!channelinfo <channel>", value="Zeigt dir die Info zu einem Channel an", inline=False)
        embed.add_field(name='p!perms', value='Zeige deine Rechte', inline=False)
        message = await ctx.send(embed=embed)
        await ctx.message.delete()




    @commands.command(aliases=['who'])
    async def whois(self, ctx, member:discord.Member =  None):

        if member is None:
            member = ctx.author
            roles = [role for role in ctx.author.roles]

        else:
            roles = [role for role in member.roles]

        embed = discord.Embed(title=f"> <:info:819237494033088523>  User Info: {member}", colour=0xffc585, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        
        embed.add_field(name="ID:", value=member.id, inline=True)
        embed.add_field(name="User Name:",value=member.display_name, inline=True)
        embed.add_field(name="Discriminator:",value=member.discriminator, inline=True)
        embed.add_field(name="Current Status:", value=str(member.status).replace('dnd', '<:dnd:829034594397323344>Bitte nicht stören').replace('idle', '<:away:829034805722611803>Abwesend').replace('online', '<:online:829034538859495475>Online').replace('offline', '<:offline:829034841143377952>Offline').replace('streaming', '<:Pointstream:829035881947201556>Streaming'), inline=True)
        embed.add_field(name="Current Activity:", value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}".replace('Custom', '') if member.activity is not None else "None", inline=True)
        embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=True)
        embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=True)
        roles1 = [role.mention for role in member.roles if role != ctx.guild.default_role]
        embed.add_field(name=f"Roles ({len(roles1)}):", value=' | '.join(roles1), inline=False)
        embed.add_field(name="Top Role:", value=member.top_role.mention, inline=True)
        await ctx.send(embed=embed)
        return
    @commands.command(aliases=['uinfo'])
    async def userinfo(self, ctx, member:discord.Member =  None):

        if member is None:
            member = ctx.author
            roles = [role for role in ctx.author.roles]

        else:
            roles = [role for role in member.roles]

        embed = discord.Embed(title=f"> <:info:819237494033088523>  User Info: {member}", colour=0xffc585, timestamp=ctx.message.created_at)
        embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=f"{member.avatar_url}")
        embed.add_field(name="ID:", value=member.id, inline=True)
        embed.add_field(name="User Name:",value=member.display_name, inline=True)
        embed.add_field(name="Discriminator:",value=member.discriminator, inline=True)
        embed.add_field(name="Beigetreten:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=True)
        embed.add_field(name="Erstellt:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=True)
        embed.add_field(name="Top Rolle:", value=member.top_role.mention, inline=True)
        await ctx.send(embed=embed)
        return

    @commands.command(aliases=['sinfo'])
    async def serverinfo(self, ctx):
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)

        embed = discord.Embed(
           title="<:info:819237494033088523> " + name + " Server Information",
           description=description,
           color=0xffc585
        )
        embed.add_field(name='👑 |Owner:', value=owner, inline=True)
        embed.add_field(name='📌 | Server ID:', value=id, inline=True)
        embed.add_field(name='🌎 | Region:', value=region, inline=True)
        embed.add_field(name='👥 | Member Count', value=memberCount, inline=True)
        await ctx.send(embed=embed)
    @commands.command(aliases=["cinfo"])
    async def channelinfo(self, ctx, channel: discord.TextChannel = None):
        if channel == None:
            channel = ctx.channel
        nsfw = self.client.get_channel(channel.id).is_nsfw()
        news = self.client.get_channel(channel.id).is_news()
        embed = discord.Embed(title='> <:info:819237494033088523> Channel Information: ' + str(channel),
                              colour=0xffc585)
        embed.add_field(name='Channel Name: ', value=str(channel.name))
        embed.add_field(name="Channel's NSFW Status: ", value=str(nsfw))
        embed.add_field(name="Channel's id: ", value=str(channel.id))
        embed.add_field(name='Channel Created At: ',
                        value=str(channel.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.add_field(name='Channel Type: ', value=str(channel.type))
        embed.add_field(name="Channel's Announcement Status: ", value=str(news))
        await ctx.send(embed=embed)
    @commands.Cog.listener()
    async def on_message_deleted(self, message):
        client.sniped_messages[message.guild.id] = (message.content, message.author, message.created_at)

    @commands.command()
    async def snipe(self, ctx):
        client.sniped_messages[message.guild.id] = (ctx.message.content, ctx.message.author, ctx.message.created_at)
        contents, author, time = client.sniped_messages[ctx.guild.id]

        embed = discord.Embed(description=contents, color=0xffc585, timestamp=time)
        embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
        await ctx.channel.send(embed=embed)

    @commands.command()
    async def embed(self, ctx):
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        await ctx.send('**__Gebe die Argumente für das Embed an. Bitte gebe alles genau an!__**\n **-------------------------------------------------**')

        await asyncio.sleep(3)

        await ctx.send('**Gebe hier den Title an!**')
        title = await self.client.wait_for('message', check=check)
    
        await ctx.send('**Gebe hier die Beschreibung an!**')
        desc = await self.client.wait_for('message', check=check)

        await ctx.send('**Gebe hier deine Fußzeile an!**')
        footer = await self.client.wait_for('message', check=check)


        embed = discord.Embed(title=title.content, description=desc.content, color=0xffc585)
        embed.set_footer(text=footer.content)
        
        await ctx.send(embed=embed)
        await ctx.send("Hier ist dein Fertiges Embed. Viel Spaß")


    @commands.command()
    async def prefix(self, ctx):
        command_prefix = ("`p!`, `P!`, <@809824051773177917>")
        await ctx.send(f'Meine Prefixe sind: {command_prefix}')

    @commands.command()
    async def icon(self, ctx):
        embed = discord.Embed(title=f'{ctx.guild.name}')
        embed.set_image(url=f"{ctx.guild.icon_url}")
        await ctx.send(embed=embed)

    @commands.command()
    async def status(self, ctx, member:discord.Member = None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(color=0xffc585)
        embed.add_field(name=f'Aktivität: {member.name}', value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}".replace('Custom', '').replace('Streaming', '<:Twitch:829039928947900489>Streamt').replace('Playing', '<:6controller:829039173876842537>Spielt') if member.activity is not None else "Dieser User hat keinen Custom Status :(", inline=True)
        embed.add_field(name=f'Status:', value=str(member.status).replace('dnd', '<:dnd:829034594397323344>Bitte nicht stören').replace('idle', '<:away:829034805722611803>Abwesend').replace('online', '<:online:829034538859495475>Online').replace('offline', '<:offline:829034841143377952>Offline').replace('streaming', '<:Pointstream:829035881947201556>Streaming'), inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(MISC(client))