import asyncio
import discord
from discord.ext import commands
import random
import time
from discord \
    import Member, Guild
import datetime
from datetime import datetime
from datetime import date
import configparser
import os, os.path
import json
from discord.ext.commands import *
from discord.voice_client import VoiceClient
from discord.utils import get
import youtube_dl
import pytz
import sys
from discord.ext import tasks
import requests
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter
import sys
import re
import PIL
from io import BytesIO
import urllib3
import urllib.request
import mysql
import re
from mysql import connector
from operator import pow, truediv, mul, add, sub
import aiohttp
import shlex
from discord import Intents
import math

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
from packages.p_mysql import *
from packages.all import *


class KNAST(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.botname = 'Knast'

    @commands.command()
    
    async def help_knast(self, ctx):
        embed = discord.Embed(title=f'Help Menü - <a:Knast:820795752708177971>Knast<a:Knast:820795752708177971>',
                              color=utils.embed_color(ctx=ctx, client=self.client))
        prefix = 'p!'
        embed.add_field(name=f'{prefix}ksetup',
                        value=f'Folge den Schritten um den Knast einzurichten.', inline=False)
        embed.add_field(name=f'{prefix}kadd <member> (<time> <reason>)',
                        value=f'Sperre einen User ein, der sich nicht an die Regeln hält!', inline=False)
        embed.add_field(
                        name=f'{prefix}kremove <member> <reason>',
                        value=f'Entlasse einen User frühzeitig.', inline=False)
        embed.add_field(
            name=f'{prefix}kcheck',
            value=f'Sehe alle User, die derzeit im Knast sitzen.', inline=False)
        embed.add_field(name=f'Ich unterstütze die folgenden Zeiten:',
                        value=f'Minute - `m`\rStunde - `h`\rTag - `d`\rWoche - `w`\rMonat - `M`\rJahr - `y`\rFür immer - `perma` / `permanent`',
                        inline=False)
        message = await ctx.send(embed=embed)
        await ctx.message.delete()
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild:discord.Guild = member.guild
        if utils.get_knast_user(guild=guild, member=member):
            for yrole in member.roles:
                if not yrole.name == '@everyone':
                    try:
                        await member.remove_roles(yrole)
                    except:
                        pass
            roleid = utils.get_knast_role(guild=guild)
            channelid = utils.get_knast_log(guild=guild)
            if channelid:
                try:
                    channel = guild.get_channel(channelid)
                    if roleid:
                        krole = guild.get_role(roleid)
                        try:
                            await member.add_roles(krole)
                            embed = discord.Embed(title=f'{self.botname} - Rejoin Protection',
                                                  description=f'{member.mention} wurde wieder in den Knast gesteckt!',
                                                  color=discord.Color.from_rgb(255, 131, 0))
                            await channel.send(embed=embed)
                        except:
                            embed = discord.Embed(title=f'{self.botname} - Rejoin Protection',
                                                  description=f'Ich konnte {member.mention} nicht die Knast Rolle geben!',
                                                  color=discord.Color.from_rgb(255, 0, 0))
                            await channel.send(embed=embed)
                except:
                    pass

    @commands.command()
    
    async def kcheck(self, ctx):
        await self.client.wait_until_ready()
        if permissions.has_admin:
            lyricsx = []
            lyricsxx = []
            lr = ''
            lr2 = ''
            cur.execute(f"SELECT * FROM pinto.knastusers")
            a = cur.fetchall()
            for x in a:
                if x[2] == ctx.guild.id:
                    member = ctx.guild.get_member(x[0])
                    if int(x[5]) !=1:
                        timex = f'bis **{time.strftime("%d.%m.%Y %H:%M", time.localtime(x[5]))}** eingesperrt\r\n'
                    else:
                        timex = '**permanent** geknastet\r\n'
                    if member:
                        if len(lr) + len(timex)+3 <= 1000:
                            lr += F'{member.mention} • {timex}'
                        else:
                            lyricsx.append(lr)
                            lr = f'{x}'
                    else:
                        if len(lr) + len(timex)+3 <= 1000:
                            lr2 += F'{x[0]} • {timex}'
                        else:
                            lyricsxx.append(lr)
                            lr2 = f'{x}'
            lyricsx.append(lr)
            lyricsxx.append(lr2)
            count = 0
            embed = discord.Embed(title=F'Knast User - {ctx.guild}')
            embed.set_thumbnail(url=ctx.guild.icon_url)
            for x in lyricsx:
                if x != '':
                    embed.add_field(name=f'{INVIS}', value=x, inline=False)
                    count+=1
            for x in lyricsxx:
                if x != '':
                    embed.add_field(name=f'{INVIS}', value=x, inline=False)
                    count += 1
            if count == 0:
                embed.add_field(name=f'{INVIS}', value='Derzeit sind keine User im Knast.', inline=False)
            await ctx.send(embed=embed)
        else:
            await permissions.no_perms(ctx=ctx)
    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    
    async def ksetup(self, ctx):
        await self.client.wait_until_ready()
        if permissions.has_admin:
            def check(message):
                return message.author == ctx.author and message.channel == ctx.channel
            try:
                embed = discord.Embed(title=f'{self.botname} - setup',
                                      description=f'Bitte gebe eine Rollen ID an oder erwähne eine Rolle, die du als Knast-rolle verwenden möchtest. Bitte gehe sicher, dass ich die Rolle vergeben kann!',
                                      color=discord.Color.purple())
                await ctx.send(embed=embed)
                msg = await self.client.wait_for('message', check=check, timeout=60)
                roleid = msg.content.replace('@&', '').replace('<', '').replace('>', '')
                role = ctx.guild.get_role(int(roleid))
                if not role:
                    return await utils.send_error(ctx=ctx,client=self.client,desc=f'Du musst eine exestierende Rolle angeben!')
                embed = discord.Embed(title=f'{self.botname} - setup',
                                      description=f'Bitte gebe eine Channel ID an oder erwähne einen Channel, den du als Knast-log verwenden möchtest.',
                                      color=discord.Color.purple())
                await ctx.send(embed=embed)
                msg = await self.client.wait_for('message', check=check, timeout=60)
                channelid = msg.content.replace('#', '').replace('<', '').replace('>', '')
                channel = self.client.get_channel(int(channelid))
                if not channel:
                    return await utils.send_error(ctx=ctx,client=self.client,desc=f'Du musst einen existierenden Channel angeben!')
                embed = discord.Embed(title=f'{self.botname} - setup',
                                      description=f'Bitte gebe eine Channel ID an oder erwähne einen Channel, den du als Knast-chat verwenden möchtest.',
                                      color=discord.Color.purple())
                await ctx.send(embed=embed)
                msg = await self.client.wait_for('message', check=check, timeout=60)
                prisonchatid = msg.content.replace('#', '').replace('<', '').replace('>', '')
                prisonchat = self.client.get_channel(int(prisonchatid))
                if not prisonchat:
                    return await utils.send_error(ctx=ctx,client=self.client,desc=f'Du musst einen existierenden Channel angeben!')
                embed = discord.Embed(title=f'{self.botname} - setup',
                                      description=f'Bitte habe etwas geduld.',
                                      color=utils.embed_color(ctx=ctx, client=self.client))
                message = await ctx.send(embed=embed)
                for chx in ctx.guild.channels:
                    if not chx.id == prisonchat.id:
                        await chx.set_permissions(role, send_messages=False, read_messages=False, view_channel=False)
                    else:
                        await chx.set_permissions(role, send_messages=True, read_messages=True, view_channel=True)
                sql = f"INSERT INTO pinto.knastsetup(guildid, channelid, roleid) VALUES (%s, %s, %s)"
                val = (f"{ctx.guild.id}", f"{channel.id}", f"{role.id}")
                try:
                    cur.execute(sql, val)
                    embed = discord.Embed(title=f'{self.botname} - setup',
                                          description=f'Der Knast-log wurde in {channel.mention} mit der Rolle {role.mention} gesetzt. Die Gefangenen können in {prisonchat.mention} miteinander schreiben.',
                                          color=utils.embed_color(ctx=ctx, client=self.client))
                    await message.edit(embed=embed)
                except:
                    cur.execute(f"UPDATE pinto.knastsetup SET channelid = '{channel.id}' WHERE guildid = '{ctx.guild.id}'")
                    cur.execute(f"UPDATE pinto.knastsetup SET roleid = '{role.id}' WHERE guildid = '{ctx.guild.id}'")
                    embed = discord.Embed(title=f'{self.botname} - setup',
                                          description=f'Der Knast-log wurde in {channel.mention} mit der Rolle {role.mention} gesetzt. Die Gefangenen können in {prisonchat.mention} miteinander schreiben.',
                                          color=utils.embed_color(ctx=ctx, client=self.client))
                    await message.edit(embed=embed)
            except:
                return await utils.send_error(ctx=ctx, client=self.client, desc=f'Bitte überprüfe deine Eingaben!')
        else:
            await permissions.no_perms(ctx=ctx)

    @commands.command()
    
    async def kupdate(self, ctx, member: discord.Member, zeit: str = 'perma', *, reason='No reason'):
        await self.client.wait_until_ready()
        if permissions.has_admin(ctx=ctx):
            itime = utils.time_of_string(ctx=ctx, zeit=zeit)
            if itime == 'x0x':
                embed = discord.Embed(title=f'{self.botname} - add',
                                      description=f'Bitte gebe eine gültige Zeit an',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embed)
                return
            if permissions.member_has_admin(member=member, ctx=ctx):
                embed = discord.Embed(title=f'{self.botname} - add',
                                      description=f'Du kannst keinen Moderator in den Knast stecken!',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embed)
                return
            k = False
            cur.execute(f"SELECT * FROM pinto.knastusers")
            a = cur.fetchall()
            for x in a:
                if x[0] == member.id:
                    if x[2] == ctx.guild.id:
                        k = True
            if k == False:
                embed = discord.Embed(title=f'{self.botname} - update',
                                      description=f'{member.mention} ist nicht im Knast!',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embed)
                return
            sql = f'UPDATE pinto.knastusers SET time = "{itime}" WHERE tbid = "{ctx.guild.id}.{member.id}"'
            cur.execute(sql)
            sql = F'UPDATE pinto.knastusers SET reason = "{reason}" WHERE tbid = "{ctx.guild.id}.{member.id}"'
            cur.execute(sql)
            channelid = utils.get_knast_log(guild=ctx.guild)
            if channelid:
                channel = self.client.get_channel(channelid)
                xtime = utils.rltime_of_string(zeit=zeit)
                embed = discord.Embed(timestamp=datetime.now().astimezone(tz=pytz.timezone('Europe/Berlin')),
                                      title=f'{self.botname} - log',
                                      description=f'{member.mention} wurde für den Knast geupdated!\r\rGeupdated von von {ctx.author.mention}\rfür {xtime}\r Grund: {reason}',
                                      color=0x00e0ff)
                await channel.send(embed=embed)
                embed = discord.Embed(title=f'{self.botname} - update',
                                      description=f'{member.mention} wurde geupdated!',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title=f'{self.botname} - update',
                                      description=f'Ich konnte den Log channel nicht finden',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embed)
                return
        else:
            await permissions.no_perms(ctx=ctx)
    @commands.command()
    
    async def kadd(self, ctx, member: discord.Member, zeit: str = 'perma', *, reason='No reason'):
        await self.client.wait_until_ready()
        if permissions.has_admin(ctx=ctx):
            itime = utils.time_of_string(ctx=ctx, zeit=zeit)
            if itime == 'x0x':
                embed = discord.Embed(title=f'{self.botname} - add',
                                      description=f'Bitte gebe eine gültige Zeit an',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embed)
                return
            if permissions.member_has_admin(member=member, ctx=ctx):
                embed = discord.Embed(title=f'{self.botname} - add',
                                      description=f'Du kannst keinen Moderator in den Knast stecken!',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embed)
                return
            embed = discord.Embed(title=f'{self.botname} - add',
                                  description=f'Bitte habe etwas geduld.',
                                  color=utils.embed_color(ctx=ctx, client=self.client))
            message = await ctx.send(embed=embed)
            rollen = []
            notroles = ''
            allroles = ''
            for yrole in member.roles:
                if not yrole.name == '@everyone':
                    rollen.append(yrole.id)
                    try:
                        await member.remove_roles(yrole)
                        allroles += F'{yrole.mention}, '
                    except:
                        notroles += F'{yrole.mention}, '
            if len(notroles) > 0:
                notroles = notroles[:-2]
            if len(allroles) > 0:
                allroles = allroles[:-2]
            roleid = utils.get_knast_role(guild=ctx.guild)
            channelid = utils.get_knast_log(guild=ctx.guild)
            if roleid:
                krole = ctx.guild.get_role(roleid)
                try:
                    await member.add_roles(krole)
                except:
                    embed = discord.Embed(title=f'{self.botname} - add',
                                          description=f'Ich habe keine Rechte die Knastrolle zu vergeben!',
                                          color=discord.Color.from_rgb(255, 0, 0))
                    await message.edit(embed=embed)
                    return
            else:
                embed = discord.Embed(title=f'{self.botname} - add',
                                      description=f'Ich konnte die Knastrolle nicht finden!',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await message.edit(embed=embed)
                return
            if len(reason) > 100:
                xreason = reason[:100] + "..."
            else:
                xreason = reason

            sql = f"INSERT INTO pinto.knastusers (userid, username, guildid,roles, author, time, reason, tbid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            val = (
                f"{member.id}", f"{member}", f"{ctx.guild.id}", f'{rollen}', f'{ctx.author.id}', f'{itime}', f'{xreason}',
                f'{ctx.guild.id}.{member.id}')
            try:
                cur.execute(sql, val)
            except:
                embed = discord.Embed(title=f'{self.botname} - add',
                                      description=f'{member.mention} ist bereits im Knast!',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await message.edit(embed=embed)
                return
            if channelid:
                channel = self.client.get_channel(channelid)
                xtime = utils.rltime_of_string(zeit=zeit)
                embed = discord.Embed(timestamp=datetime.now().astimezone(tz=pytz.timezone('Europe/Berlin')),
                                      title=f'{self.botname} - log',
                                      description=f'{member.mention} wurde in den Knast gesteckt!\r\rEingesperrt von {ctx.author.mention}\rfür {xtime}\r Grund: {xreason}\r\rRollen: \r{allroles}',
                                      color=0x2F3136)
                await channel.send(embed=embed)
            else:
                embed = discord.Embed(title=f'{self.botname} - add',
                                      description=f'Ich konnte den Log channel nicht finden',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await message.edit(embed=embed)
                return
            text = ''
            if notroles != '':
                text = f'Die folgenden Rollen konnten nicht entfernt werden: \r\r{notroles}'
            embed = discord.Embed(title=f'{self.botname} - add',
                                  description=f'{member.mention} wurde in den Knast gesteckt! {text}',
                                  color=utils.embed_color(ctx=ctx, client=self.client))
            await message.edit(embed=embed)
        else:
            await permissions.no_perms(ctx=ctx)

    @commands.command()
    
    async def kremove(self, ctx, member: discord.Member, *, reason='Kein Grund angegeben'):
        await self.client.wait_until_ready()
        if permissions.has_admin(ctx=ctx):
            if utils.get_knast_user(guild=ctx.guild, member=member):
                if len(reason) > 100:
                    xreason = reason[:100] + "..."
                else:
                    xreason = reason
                roleid = utils.get_knast_role(guild=ctx.guild)
                if roleid:
                    embed = discord.Embed(title=f'{self.botname} - remove',
                                          description=f'Bitte habe etwas gedult!',
                                          color=utils.embed_color(ctx=ctx, client=self.client))
                    message = await ctx.send(embed=embed)
                    krole = ctx.guild.get_role(roleid)
                    try:
                        cur.execute(f"SELECT * FROM pinto.knastusers")
                        a = cur.fetchall()
                        for x in a:
                            if x[0] == member.id:
                                if x[2] == ctx.guild.id:
                                    rolles = x[3]
                                    for char in rolles:
                                        if char in "[]":
                                            rolles = rolles.replace(char, '')
                                    rolles = rolles.split(',')
                        notroles = ''
                        for srole in rolles:
                            if srole.replace(' ', '') != '':
                                zrole = ctx.guild.get_role(role_id=int(srole))
                                try:
                                    await member.add_roles(zrole)
                                except:
                                    notroles += f'{ctx.guild.get_role(role_id=int(srole)).mention}\r'
                                    pass
                        await member.remove_roles(krole)
                    except:
                        embed = discord.Embed(title=f'{self.botname} - remove',
                                              description=f'Ich habe keine Rechte die Knastrolle zu entfernen!',
                                              color=discord.Color.from_rgb(255, 0, 0))
                        await message.edit(embed=embed)
                        return
                else:
                    embed = discord.Embed(title=f'{self.botname} - remove',
                                          description=f'Ich konnte die Knastrolle nicht finden!',
                                          color=discord.Color.from_rgb(255, 0, 0))
                    await ctx.send(embed=embed)
                    return

                cur.execute(f"DELETE FROM pinto.knastusers WHERE tbid = '{ctx.guild.id}.{member.id}'")
                channelid = utils.get_knast_log(guild=ctx.guild)
                if channelid:
                    channel = self.client.get_channel(channelid)
                    embed = discord.Embed(title=f'{self.botname} - log',
                                          timestamp=datetime.now().astimezone(tz=pytz.timezone('Europe/Berlin')),
                                          description=f'{member.mention} wurde aus dem Knast entlassen!\r\rEntlassen von {ctx.author.mention}\rGrund: {xreason}',
                                          color=0x7c00ff)
                    await channel.send(embed=embed)
                else:
                    embed = discord.Embed(title=f'{self.botname} - remove',
                                          description=f'Ich konnte den Log channel nicht finden',
                                          color=discord.Color.from_rgb(255, 0, 0))
                    await message.edit(embed=embed)
                    return
                text = ''
                if notroles != '':
                    text = f'Die folgenden Rollen konnten nicht hinzugefügt werden: \r\r{notroles}'
                embed = discord.Embed(title=f'{self.botname} - remove',
                                      description=f'{member.mention} wurde entlassen. {text}',
                                      color=utils.embed_color(ctx=ctx, client=self.client))
                await message.edit(embed=embed)
            else:
                embed = discord.Embed(title=f'{self.botname} - remove',
                                      description=f'{member.mention} ist nicht im Knast!',
                                      color=discord.Color.from_rgb(255, 0, 0))
                await ctx.send(embed=embed)
        else:
            await permissions.no_perms(ctx=ctx)



def setup(client):
    client.add_cog(KNAST(client))


