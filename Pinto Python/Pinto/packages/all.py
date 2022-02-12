
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
from packages.p_mysql import cur
from discord.ext.commands import DisabledCommand, check, Bot
class DisabledInChannel(DisabledCommand):
    pass
def command_is_disabled(command, channelid, ctx):
    roleids = []
    for role in ctx.author.roles:
        roleids.append(role.id)
    cur.execute(f"SELECT * FROM cv2.blockedchannels")
    a = cur.fetchall()
    for x in a:
        if str(x[0]) == str(command):
            if int(x[1]) == channelid:
                return True
        if str(x[0]) == 'all':
            if int(x[1]) == channelid:
                return True
    cur.execute(f"SELECT * FROM cv2.disabledcommands")
    a = cur.fetchall()
    for x in a:
        if int(x[3]) == ctx.guild.id:
            if int(x[1]) == int(ctx.author.id) or int(x[1]) in roleids:
                if str(x[2]) == 'enable':
                    if str(x[0]) == str(ctx.command.name):
                        return False
                    if str(x[0]) == 'giveaway' and str(ctx.command.name) in ['greroll', 'gstart']:
                        return False
                    if str(x[0]) == 'invite' and str(ctx.command.name) in ['setinvitechannel', 'removeinvitechannel']:
                        return False
                    if str(x[0]) == 'knast' and str(ctx.command.name) in ['ksetup', 'kadd', 'kremove']:
                        return False
                    if str(x[0]) == 'moderation' and str(ctx.command.name) in ['ban', 'unban', 'kick', 'clear']:
                        return False
                    if str(x[0]) == 'music' and str(ctx.command.name) in ['radio']:
                        return False
                    if str(x[0]) == 'rr' and str(ctx.command.name) in ['rradd', 'rrremove', 'mradd', 'mrremove', 'aradd', 'arremove', 'arignoreadd', 'arignoreremvoe']:
                        return False
                    if str(x[0]) == 'secure' and str(ctx.command.name) in ['sk', 'bypass']:
                        return False
                    if str(x[0]) == 'voice' and str(ctx.command.name) in ['settempchannel', 'removetempchannel', 'setvoicerole', 'removevoicerole']:
                        return False
        if str(x[0]) == 'all':
            if int(x[3]) == ctx.guild.id:
                if int(x[1]) == ctx.author.id or int(x[1]) in roleids:
                    if str(x[2]) == 'enable':
                        return False
    cur.execute(f"SELECT * FROM cv2.disabledcommands")
    a = cur.fetchall()
    for x in a:
        if int(x[3]) == ctx.guild.id:
            if int(x[1]) == int(ctx.author.id) or int(x[1]) in roleids:
                if str(x[2]) == 'disable':
                    if str(x[0]) == str(ctx.command.name):
                        return True
                    if str(x[0]) == 'giveaway' and str(ctx.command.name) in ['greroll', 'gstart']:
                        return True
                    if str(x[0]) == 'invite' and str(ctx.command.name) in ['setinvitechannel', 'removeinvitechannel']:
                        return True
                    if str(x[0]) == 'knast' and str(ctx.command.name) in ['ksetup', 'kadd', 'kremove']:
                        return True
                    if str(x[0]) == 'moderation' and str(ctx.command.name) in ['ban', 'unban', 'kick', 'clear']:
                        return True
                    if str(x[0]) == 'music' and str(ctx.command.name) in ['radio']:
                        return True
                    if str(x[0]) == 'rr' and str(ctx.command.name) in ['rradd', 'rrremove', 'mradd', 'mrremove', 'aradd', 'arremove', 'arignoreadd', 'arignoreremvoe']:
                        return True
                    if str(x[0]) == 'secure' and str(ctx.command.name) in ['sk', 'bypass']:
                        return True
                    if str(x[0]) == 'voice' and str(ctx.command.name) in ['settempchannel', 'removetempchannel', 'setvoicerole', 'removevoicerole']:
                        return True
        if str(x[0]) == 'all':
            if int(x[3]) == ctx.guild.id:
                if int(x[1]) == ctx.author.id or int(x[1]) in roleids:
                    if str(x[2]) == 'disable':
                        return True
    return False
def check_disabled():
    def predicate(ctx):
        if command_is_disabled(ctx.command.name, ctx.channel.id, ctx):
            raise DisabledInChannel(f"{ctx.command.name} is disabled in {ctx.channel.name}")
        if utils.is_banned(id=ctx.author.id):
            raise DisabledInChannel(f"{ctx.author.name} is banned")
        if utils.is_banned(id=ctx.guild.owner_id):
            raise DisabledInChannel(f"{ctx.guild.owner.name} is banned")
        if utils.is_banned(id=ctx.guild.id):
            raise DisabledInChannel(f"{ctx.guild.name} is banned")
        return True
    return check(predicate)

class casino():
    def __init__(self):
        self._channels = {}
    @staticmethod
    async def question(ctx,client, desc):
        embed=discord.Embed(description=f'{desc}', color=utils.embed_color(ctx=ctx,client=client))
        embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
        await ctx.send(embed=embed)
    @staticmethod
    async def addjob(ctx, client):
        if casino.max_job(ctx=ctx) == False:
            return await utils.send_error(ctx=ctx, client=client, desc=f'Du bist am Job Limit angekommen!')
        def checkmaxstring(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200
        def checkint(message):
            return message.author == ctx.author and message.channel == ctx.channel and int(message.content)
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        jobname = ''
        roleid = 0
        cost = 0
        earning = 0
        skillname = ''
        skilllevel = 0
        secskillname = ''
        secskilllevel = 0
        guildid = ctx.guild.id
        await casino.question(ctx=ctx,client=client, desc=F'Wie soll der Job heißen? (Maximal 200 Zeichen)')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        jobname = str(msg.content)
        if casino.is_job(ctx=ctx,name=jobname):
            return await utils.send_error(ctx=ctx, client=client, desc=f'Es exestiert bereits ein Job mit diesem Namen! Bitte editiere ihn!')

        await casino.question(ctx=ctx, client=client, desc=F'Welche Rolle soll vergeben werden? (Falls nein gebe `0` an)')
        msg = await client.wait_for('message', check=check, timeout=60)
        roleid = int(msg.content.replace('@&', '').replace('<', '').replace('>', ''))
        if str(msg.content) == '0':
            roleid = 0
        else:
            role = ctx.guild.get_role(roleid)
            if not role:
                return await utils.send_error(ctx=ctx, client=client, desc=f'Ich konnte die Rolle nicht finden!')
            else:
                roleid = role.id


        await casino.question(ctx=ctx, client=client, desc=F'Kostet es etwas um sich zu bewerben? (Falls nein gebe `0` an)')
        msg = await client.wait_for('message', check=checkint, timeout=60)
        cost = int(msg.content)

        await casino.question(ctx=ctx, client=client, desc=F'Wie viel soll man mit dem Job verdienen?')
        msg = await client.wait_for('message', check=checkint, timeout=60)
        earning = int(msg.content)

        await casino.question(ctx=ctx, client=client, desc=F'Wird ein Skill benötigt? (Falls nein gebe `0` an)')
        msg = await client.wait_for('message', check=check, timeout=60)
        skillname = str(msg.content)
        if not casino.is_skill(ctx=ctx,skill=skillname) and skillname != '' and skillname != '0':
            return await utils.send_error(ctx=ctx, client=client, desc=f'Ich konnte den Skill nicht finden!')

        if str(skillname) != '' and str(skillname) != '0':
            await casino.question(ctx=ctx, client=client, desc=F'Auf welchem Level?')
            msg = await client.wait_for('message', check=checkint, timeout=60)
            skilllevel = int(msg.content)
            await casino.question(ctx=ctx, client=client, desc=F'Wird ein weiterer Skill benötigt? (Falls nein gebe `0` an)')
            msg = await client.wait_for('message', check=check, timeout=60)
            secskillname = str(msg.content)
            if not casino.is_skill(ctx=ctx, skill=secskillname) and secskillname != '' and secskillname != '0':
                return await utils.send_error(ctx=ctx, client=client, desc=f'Ich konnte den Skill nicht finden!')
            if str(secskillname) == '' or str(secskillname) == '0':
                secskillname = ''
            else:
                await casino.question(ctx=ctx, client=client, desc=F'Auf welchem Level?')
                msg = await client.wait_for('message', check=checkint, timeout=60)
                secskilllevel = int(msg.content)
        else:
            skillname = ''

        try:
            tbid = f'{guildid}.{jobname.lower()}'
            sql = "INSERT INTO cv2.c_jobs (jobname, roleid, cost, earning, skillname, skilllevel, secskillname, secskilllevel, visible, guildid, tbid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (jobname, roleid, cost, earning, skillname, skilllevel, secskillname, secskilllevel, 1, guildid, tbid)
            cur.execute(sql, val)
            await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! Der Job wurde erstellt.')
        except Exception as e:
            await utils.send_error(ctx=ctx, client=client, desc=f'Merkwürdig! Irgendetwas ist schief gelaufen.')
            print(e)
            raise e
    @staticmethod
    async def removejob(ctx, client):
        def checkdelete(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200 and str(message.content) in ['delete', 'invisible']
        def checkmaxstring(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200
        guildid = ctx.guild.id
        delete = 'invisible'
        await casino.question(ctx=ctx, client=client, desc=F'Welchen Job möchtest du entfernen?')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        jobname = str(msg.content)
        if casino.is_job(ctx=ctx, name=jobname):
            await casino.question(ctx=ctx, client=client, desc=F'Möchtest du ihn komplett löschen oder nur auf Unsichbar setzten? (`delete`, `invisible`)')
            msg = await client.wait_for('message', check=checkdelete, timeout=60)
            delete = str(msg.content)
            tbid = f'{guildid}.{jobname.lower()}'
            if delete == 'delete':
                cur.execute(f"DELETE FROM cv2.c_jobs WHERE tbid = '{tbid}'")
                await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! Der Job wurde gelöscht.')
            else:
                cur.execute(f"UPDATE cv2.c_jobs SET visible = '{0}' WHERE tbid = '{tbid}'")
                await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! Der Job wurde auf Unsichtbar gestellt.')
        else:
            return await utils.send_error(ctx=ctx, client=client, desc=f'Es exestiert kein ein Job mit diesem Namen!')
    @staticmethod
    async def editjob(ctx, client):
        def checkmaxstring(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200
        def checkint(message):
            return message.author == ctx.author and message.channel == ctx.channel and int(message.content)
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        def checktype(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200 and str(message.content) in ['name', 'role', 'cost', 'payout', 'skill']
        guildid = ctx.guild.id
        await casino.question(ctx=ctx, client=client, desc=F'Welchen Job möchtest du bearbeiten?')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        jobname = str(msg.content)
        if casino.is_job(ctx=ctx, name=jobname):
            tbid = f'{guildid}.{jobname.lower()}'
            await casino.question(ctx=ctx, client=client, desc=F'Was möchtest du bearbeiten?\r(`name`, `role`, `cost`, `payout`, `skill`)')
            msg = await client.wait_for('message', check=checktype, timeout=60)
            type = str(msg.content)
            if type == 'name':
                await casino.question(ctx=ctx, client=client, desc=F'Wie soll der Job heißen?')
                msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
                newjobname = str(msg.content)
                if not casino.is_job(ctx=ctx, name=newjobname):
                    cur.execute(f"UPDATE cv2.c_jobs SET jobname = '{newjobname}' WHERE tbid = '{tbid}'")
                    cur.execute(f"UPDATE cv2.c_jobs SET tbid = '{guildid}.{newjobname.lower()}' WHERE tbid = '{guildid}.{jobname.lower()}'")
                    await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! der Job heißt nun {utils.escape(newjobname)}')
                else:
                    return await utils.send_error(ctx=ctx, client=client, desc=f'Es exestiert bereits ein Job mit diesem Namen!')
            if type == 'role':
                await casino.question(ctx=ctx, client=client, desc=F'Welche Rolle soll vergeben werden? (Falls nein gebe `0` an)')
                msg = await client.wait_for('message', check=check, timeout=60)
                roleid = int(msg.content.replace('@&', '').replace('<', '').replace('>', ''))
                if str(msg.content) == '0':
                    roleid = 0
                else:
                    role = ctx.guild.get_role(roleid)
                    if not role:
                        return await utils.send_error(ctx=ctx, client=client, desc=f'Ich konnte die Rolle nicht finden!')
                    else:
                        roleid = role.id
                cur.execute(f"UPDATE cv2.c_jobs SET roleid = '{roleid}' WHERE tbid = '{tbid}'")
                if roleid == 0:
                    await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! Es wird ab jetzt keine Rolle vergeben.')
                else:
                    await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! Es wird ab jetzt die Rolle {role.mention} vergeben.')
            if type == 'cost':
                await casino.question(ctx=ctx, client=client, desc=F'Kostet es etwas um sich zu bewerben? (Falls nein gebe `0` an)')
                msg = await client.wait_for('message', check=checkint, timeout=60)
                cost = int(msg.content)
                cur.execute(f"UPDATE cv2.c_jobs SET cost = '{cost}' WHERE tbid = '{tbid}'")
                await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! Es kostet nun {cost}{casino.get_currency(guildid=guildid)} um sich für {utils.escape(jobname)} zu bewerben')
            if type == 'payout':
                await casino.question(ctx=ctx, client=client, desc=F'Wie viel kann man mit dem Job verdienen?')
                msg = await client.wait_for('message', check=checkint, timeout=60)
                payout = int(msg.content)
                cur.execute(f"UPDATE cv2.c_jobs SET earning = '{payout}' WHERE tbid = '{tbid}'")
                await casino.question(ctx=ctx, client=client,
                                      desc=F'Alles Klar! Man kann mit {utils.escape(jobname)} nun {payout}{casino.get_currency(guildid=guildid)} verdienen.')
            if type == 'skill':
                skillname = ''
                skilllevel = 0
                secskillname = ''
                secskilllevel = 0
                await casino.question(ctx=ctx, client=client, desc=F'Wird ein Skill benötigt? (Falls nein gebe `0` an)')
                msg = await client.wait_for('message', check=check, timeout=60)
                skillname = str(msg.content)
                if not casino.is_skill(ctx=ctx, skill=skillname) and skillname != '' and skillname != '0':
                    return await utils.send_error(ctx=ctx, client=client, desc=f'Ich konnte den Skill nicht finden!')

                if str(skillname) != '' and str(skillname) != '0':
                    await casino.question(ctx=ctx, client=client, desc=F'Auf welchem Level?')
                    msg = await client.wait_for('message', check=checkint, timeout=60)
                    skilllevel = int(msg.content)
                    await casino.question(ctx=ctx, client=client, desc=F'Wird ein weiterer Skill benötigt? (Falls nein gebe `0` an)')
                    msg = await client.wait_for('message', check=check, timeout=60)
                    secskillname = str(msg.content)
                    if not casino.is_skill(ctx=ctx, skill=secskillname) and secskillname != '' and secskillname != '0':
                        return await utils.send_error(ctx=ctx, client=client, desc=f'Ich konnte den Skill nicht finden!')
                    if str(secskillname) == '' or str(secskillname) == '0':
                        secskillname = ''
                    else:
                        await casino.question(ctx=ctx, client=client, desc=F'Auf welchem Level?')
                        msg = await client.wait_for('message', check=checkint, timeout=60)
                        secskilllevel = int(msg.content)
                else:
                    skillname = ''
                cur.execute(f"UPDATE cv2.c_jobs SET skillname = '{skillname}' WHERE tbid = '{tbid}'")
                cur.execute(f"UPDATE cv2.c_jobs SET skilllevel = '{skilllevel}' WHERE tbid = '{tbid}'")
                cur.execute(f"UPDATE cv2.c_jobs SET secskillname = '{secskillname}' WHERE tbid = '{tbid}'")
                cur.execute(f"UPDATE cv2.c_jobs SET secskilllevel = '{secskilllevel}' WHERE tbid = '{tbid}'")
                await casino.question(ctx=ctx, client=client,
                                      desc=F'Alles Klar! Ich habe das Skillsystem geupdated.')
        else:
            return await utils.send_error(ctx=ctx, client=client, desc=f'Es exestiert kein ein Job mit diesem Namen!')
    @staticmethod
    async def viewjob(ctx, client):
        def checkmaxstring(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200
        guildid = ctx.guild.id
        await casino.question(ctx=ctx, client=client, desc=F'Welchen Job möchtest du sehen?')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        if casino.is_job(ctx=ctx,name=str(msg.content)):
            embed=discord.Embed(color=utils.embed_color(ctx=ctx,client=client), title=F'Job Info')
            cur.execute(f"SELECT * FROM cv2.c_jobs")
            a = cur.fetchall()
            for x in a:
                if str(x[10]) == f'{guildid}.{str(msg.content).lower()}':
                    embed.add_field(name=F'Name', value=F'{utils.escape(x[0])}')
                    embed.add_field(name=F'Price', value=F'{x[2]}{casino.get_currency(guildid=guildid)}')
                    role = ctx.guild.get_role(int(x[1]))
                    if role:
                        embed.add_field(name=F'Given Role', value=F'{role.mention}')
                    embed.add_field(name=F'Payout', value=F'{x[3]}{casino.get_currency(guildid=guildid)}')
                    if str(x[4]) != '':
                        if casino.is_skill(ctx, str(x[4])):
                            embed.add_field(name=F'Skill - {utils.escape(x[4])}', value=F'Level {x[5]}')
                    if str(x[6]) != '':
                        if casino.is_skill(ctx, str(x[6])):
                            embed.add_field(name=F'Skill - {utils.escape(x[6])}', value=F'Level {x[7]}')
                    embed.add_field(name=F'Visible', value=F'{str(x[8]).replace("0", "False").replace("1", "True")}')
                    await ctx.send(embed=embed)
        else:
            return await utils.send_error(ctx=ctx, client=client, desc=f'Es exestiert kein ein Job mit diesem Namen!')


    @staticmethod
    async def addskill(ctx, client):
        if casino.max_skill(ctx=ctx) == False:
            return await utils.send_error(ctx=ctx, client=client, desc=f'Du bist am Skill Limit angekommen!')
        def checkmaxstring(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200

        def checkint(message):
            return message.author == ctx.author and message.channel == ctx.channel and int(message.content)

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        guildid = ctx.guild.id
        await casino.question(ctx=ctx, client=client, desc=F'Wie soll der Skill heißen? (Maximal 200 Zeichen)')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        skillname = str(msg.content)
        if casino.is_skill(ctx=ctx, skill=skillname):
            return await utils.send_error(ctx=ctx, client=client, desc=f'Es exestiert bereits ein Job mit diesem Namen! Bitte editiere ihn!')


        await casino.question(ctx=ctx, client=client, desc=F'Was kostet es, den Skill zu trainieren?')
        msg = await client.wait_for('message', check=checkint, timeout=60)
        cost = int(msg.content)

        try:
            tbid = f'{guildid}.{skillname.lower()}'
            sql = "INSERT INTO cv2.c_skills (skillname, traincost, guildid, tbid) VALUES (%s, %s, %s, %s)"
            val = (skillname, cost, guildid, tbid)
            cur.execute(sql, val)
            await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! Der Skill wurde erstellt.')
        except Exception as e:
            await utils.send_error(ctx=ctx, client=client, desc=f'Merkwürdig! Irgendetwas ist schief gelaufen.')
            print(e)
            raise e
    @staticmethod
    async def removeskill(ctx, client):
        def checkmaxstring(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200
        guildid = ctx.guild.id
        await casino.question(ctx=ctx, client=client, desc=F'Welchen Skill möchtest du löschen?')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        jobname = str(msg.content)
        if casino.is_skill(ctx=ctx, skill=jobname):
            tbid = f'{guildid}.{jobname.lower()}'
            cur.execute(f"DELETE FROM cv2.c_skills WHERE tbid = '{tbid}'")
            await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! Der Skill wurde gelöscht.')
        else:
            return await utils.send_error(ctx=ctx, client=client, desc=f'Es exestiert kein ein Skill mit diesem Namen!')
    @staticmethod
    async def editskill(ctx, client):

        def checkmaxstring(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200
        def checkint(message):
            return message.author == ctx.author and message.channel == ctx.channel and int(message.content)
        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel
        def checktype(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200 and str(message.content) in ['name', 'cost']
        guildid = ctx.guild.id
        await casino.question(ctx=ctx, client=client, desc=F'Welchen Skill möchtest du bearbeiten?')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        jobname = str(msg.content)
        if casino.is_skill(ctx=ctx, skill=jobname):
            tbid = f'{guildid}.{jobname.lower()}'
            await casino.question(ctx=ctx, client=client, desc=F'Was möchtest du bearbeiten?\r(`name`, `cost`)')
            msg = await client.wait_for('message', check=checktype, timeout=60)
            type = str(msg.content)
            if type == 'name':
                await casino.question(ctx=ctx, client=client, desc=F'Wie soll der Skill heißen?')
                msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
                newjobname = str(msg.content)
                if not casino.is_job(ctx=ctx, name=newjobname):
                    cur.execute(f"UPDATE cv2.c_skills SET jobname = '{newjobname}' WHERE tbid = '{tbid}'")
                    cur.execute(f"UPDATE cv2.c_skills SET tbid = '{guildid}.{newjobname.lower()}' WHERE tbid = '{guildid}.{jobname.lower()}'")
                    await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! der Skill heißt nun {utils.escape(newjobname)}')
                else:
                    return await utils.send_error(ctx=ctx, client=client, desc=f'Es exestiert bereits ein Skill mit diesem Namen!')

            if type == 'cost':
                await casino.question(ctx=ctx, client=client, desc=F'Wie viel kostet es, um den Skill zu trainieren?')
                msg = await client.wait_for('message', check=checkint, timeout=60)
                cost = int(msg.content)
                cur.execute(f"UPDATE cv2.c_skills SET traincost = '{cost}' WHERE tbid = '{tbid}'")
                await casino.question(ctx=ctx, client=client, desc=F'Alles Klar! Es kostet nun {cost}{casino.get_currency(guildid=guildid)} um den Skill {utils.escape(jobname)} zu trainieren.')
        else:
            return await utils.send_error(ctx=ctx, client=client, desc=f'Es exestiert kein ein Skill mit diesem Namen!')
    @staticmethod
    async def skills(ctx, client):
        txt = ''

        def checkmaxstring(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200

        guildid = ctx.guild.id

        cur.execute(f"SELECT * FROM cv2.c_skills")
        a = cur.fetchall()
        for x in a:
            if casino.is_skill(ctx=ctx, skill=str(x[0])):
                txt += f'**• {utils.escape(x[0])}** {x[1]}{casino.get_currency(guildid)}\r'
        if txt == '':
            txt = '*Huch? Offenbar gibt es hier nix.*'
        if len(txt) > 2048:
            txt = txt[:2045] + '...'
        embed = discord.Embed(color=utils.embed_color(ctx=ctx, client=client), title=F'Skill Info', description=f'{txt}')
        await ctx.send(embed=embed)


    @staticmethod
    async def additem(ctx, client):
        if casino.max_items(ctx=ctx) == False:
            return await utils.send_error(ctx=ctx, client=client, desc=f'Du bist am Item Limit angekommen!')

        def checkmaxstring(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200

        def checkint(message):
            return message.author == ctx.author and message.channel == ctx.channel and str(message.content).isdigit()

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        guildid = ctx.guild.id
        await casino.question(ctx=ctx, client=client, desc=F'Wie soll das Item heißen?')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        name = str(msg.content)
        await casino.question(ctx=ctx, client=client, desc=F'Beschreibe dein Item?')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        descr = str(msg.content)
        await casino.question(ctx=ctx, client=client, desc=F'Wie viel soll dein Item kosten?')
        msg = await client.wait_for('message', check=checkint, timeout=60)
        price = int(msg.content)
        await casino.question(ctx=ctx, client=client, desc=F'Welche Rolle soll vergeben werden? (Falls keine gebe `0` an)')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        roleid = int(msg.content.replace('@&', '').replace('<', '').replace('>', ''))
        if str(msg.content) == '0':
            roleid = 0
        else:
            role = ctx.guild.get_role(roleid)
            if not role:
                return await utils.send_error(ctx=ctx, client=client, desc=f'Ich konnte die Rolle nicht finden!')
            else:
                roleid = role.id
        await casino.question(ctx=ctx, client=client, desc=F'Welche Rolle soll entfernt werden? (Falls keine gebe `0` an)')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        roleid2 = int(msg.content.replace('@&', '').replace('<', '').replace('>', ''))
        if str(msg.content) == '0':
            roleid2 = 0
        else:
            role = ctx.guild.get_role(roleid2)
            if not role:
                return await utils.send_error(ctx=ctx, client=client, desc=f'Ich konnte die Rolle nicht finden!')
            else:
                roleid2 = role.id
        await casino.question(ctx=ctx, client=client, desc=F'Welche Rolle soll benötigt werden? (Falls keine gebe `0` an)')
        msg = await client.wait_for('message', check=checkmaxstring, timeout=60)
        roleid3 = int(msg.content.replace('@&', '').replace('<', '').replace('>', ''))
        if str(msg.content) == '0':
            roleid3 = 0
        else:
            role = ctx.guild.get_role(roleid3)
            if not role:
                return await utils.send_error(ctx=ctx, client=client, desc=f'Ich konnte die Rolle nicht finden!')
            else:
                roleid3 = role.id

    @staticmethod
    async def removeitem(ctx, client):
        pass
    @staticmethod
    async def edititem(ctx, client):
        pass
    @staticmethod
    async def viewitem(ctx, client):
        pass

    @staticmethod
    async def setupclans(ctx, client):

        set_price = 0
        user_price = 0
        upgrade_price = 0

        def checkmaxstring(message):
            return message.author == ctx.author and message.channel == ctx.channel and len(str(message.content)) <= 200

        def checkint(message):
            return message.author == ctx.author and message.channel == ctx.channel and int(message.content)

        guildid = ctx.guild.id

        if txt == '':
            txt = '*Huch? Offenbar gibt es hier nix.*'
        if len(txt) > 2048:
            txt = txt[:2045] + '...'
        try:
            sql = "INSERT INTO cv2.c_setup (skillname, traincost, guildid, tbid) VALUES (%s, %s, %s, %s)"
            val = (skillname, cost, guildid, tbid)
            cur.execute(sql, val)
        except:
            cur.execute(f"UPDATE cv2.c_setup SET traincost = '{cost}' WHERE tbid = '{tbid}'")
        embed = discord.Embed(color=utils.embed_color(ctx=ctx, client=client), title=F'Skill Info', description=f'{txt}')
        await ctx.send(embed=embed)

    @staticmethod
    def is_skill(ctx, skill):
        cur.execute(f"SELECT * FROM cv2.c_skills")
        a = cur.fetchall()
        for x in a:
            if x[2] == ctx.guild.id:
                if str(x[0]).lower() == skill.lower():
                    return True
        return False
    @staticmethod
    def is_job(ctx, name):
        cur.execute(f"SELECT * FROM cv2.c_jobs")
        a = cur.fetchall()
        for x in a:
            if x[9] == ctx.guild.id:
                if str(x[0]).lower() == name.lower():
                    return True
        return False
    @staticmethod
    def max_job(ctx):
        count = 0
        cur.execute(f"SELECT * FROM cv2.c_jobs")
        a = cur.fetchall()
        for x in a:
            if x[9] == ctx.guild.id:
                count +=1
        if utils.has_premium_tier3(userid=ctx.author.id):
            if count > 100:
                return False
        elif utils.has_premium_tier2(userid=ctx.author.id):
            if count > 50:
                return False
        elif utils.has_premium_tier1(userid=ctx.author.id):
            if count > 30:
                return False
        else:
            if count > 20:
                return False
        return True

    @staticmethod
    def max_items(ctx):
        count = 0
        cur.execute(f"SELECT * FROM cv2.c_items")
        a = cur.fetchall()
        for x in a:
            if x[11] == ctx.guild.id:
                count += 1
        if utils.has_premium_tier3(userid=ctx.author.id):
            if count > 100:
                return False
        elif utils.has_premium_tier2(userid=ctx.author.id):
            if count > 50:
                return False
        elif utils.has_premium_tier1(userid=ctx.author.id):
            if count > 30:
                return False
        else:
            if count > 20:
                return False
        return True
    @staticmethod
    def max_skill(ctx):
        count = 0
        cur.execute(f"SELECT * FROM cv2.c_skills")
        a = cur.fetchall()
        for x in a:
            if x[2] == ctx.guild.id:
                count += 1
        if utils.has_premium_tier3(userid=ctx.author.id):
            if count > 75:
                return False
        elif utils.has_premium_tier2(userid=ctx.author.id):
            if count > 50:
                return False
        elif utils.has_premium_tier1(userid=ctx.author.id):
            if count > 30:
                return False
        else:
            if count > 20:
                return False
        return True
    @staticmethod
    def get_currency(guildid):
        cur.execute(f'SELECT * FROM cv2.c_setup')
        a = cur.fetchall()
        for x in a:
            if x[0] == guildid:
                if x[1] == '' or x[1] == None:
                    return '💸'
                else:
                    return utils.escape(x[1])
        return '💸'
class users():
    def __init__(self):
        self._channels = {}

    @staticmethod
    def get_commands_counter(userid):
        cur.execute(f"SELECT * FROM cv2.topusers")
        a = cur.fetchall()
        for x in a:
            if x[0] == userid:
                return int(x[1])
        return 0

    @staticmethod
    def get_invites(userid, guild, code):
        cur.execute(f"SELECT * FROM cv2.invite WHERE guildid='{guild.id}'")
        a = cur.fetchall()
        for x in a:
            if x[5] == userid:
                if x[0] == guild.id:
                    if str(x[1]) == str(code):
                        return int(x[4])
        return 0

    @staticmethod
    def get_all_invites(userid, guild):
        invites = 0
        cur.execute(f"SELECT * FROM cv2.invite WHERE guildid='{guild.id}'")
        a = cur.fetchall()
        for x in a:
            if x[5] == userid:
                if x[0] == guild.id:
                    invites += int(x[4])
        return invites
    @staticmethod
    def is_invite_member_in_guild(guild, member):
        cur.execute(f"SELECT * FROM cv2.invite WHERE guildid='{guild.id}'")
        a = cur.fetchall()
        for x in a:
            if x[0] == guild.id:
                if x[5] == member.id:
                    return True
        return False

    @staticmethod
    def get_giveaway_messages(guild, member, messageid):
        cur.execute(f"SELECT * FROM cv2.giveawaymessages")
        a = cur.fetchall()
        for x in a:
            if x[3] == F'{guild.id}.{messageid}.{member.id}':
                return x[2]
        return False
class bewerbungen():
    def __init__(self):
        self._channels = {}

    @staticmethod
    def get_questions(guildid):
        cur.execute(f"SELECT * FROM cv2.applyquestions")
        a = cur.fetchall()
        for x in a:
            if x[0] == guildid:
                channel = []
                rolles = x[2]
                if rolles == '':
                    return channel
                for char in rolles:
                    if char in "[]":
                        rolles = rolles.replace(char, '')
                rolles = rolles.split(',;,-, ')
                for srole in rolles:
                    try:
                        if not srole == '':
                            channel.append(srole)
                    except:
                        pass
                return channel
        return False

    @staticmethod
    def get_answers(guildid, memberid):
        cur.execute(f"SELECT * FROM cv2.applys")
        a = cur.fetchall()
        for x in a:
            if x[1] == guildid:
                if x[0] == memberid:
                    questions = []
                    rolles = x[2]
                    if rolles == '':
                        return questions
                    for char in rolles:
                        if char in "[]":
                            rolles = rolles.replace(char, '')
                    rolles = rolles.split(',;,-, ')
                    for srole in rolles:
                        y = str(srole).split('--||--')
                        try:
                            if not y[0].replace(' ', '') == '' and not y[1].replace(' ', '') == '':
                                questions.append([y[0], y[1]])
                        except:
                            pass
                    return questions
        return False

    @staticmethod
    def already(guildid, memberid):
        cur.execute(f"SELECT * FROM cv2.applys")
        a = cur.fetchall()
        for x in a:
            if x[1] == guildid:
                if x[0] == memberid:
                    return True
        return False
    @staticmethod
    def get_channel(guildid):
        cur.execute(f"SELECT * FROM cv2.applyquestions")
        a = cur.fetchall()
        for x in a:
            if x[0] == guildid:
                return int(x[1])
        return False
class partners():
    def __init__(self):
        self._channels = {}

    @staticmethod
    def get_channels(guildid):
        cur.execute(f"SELECT * FROM cv2.partner")
        a = cur.fetchall()
        for x in a:
            if x[0] == guildid:
                channel = []
                rolles = x[1].replace(' ', '')
                if rolles == '':
                    return channel
                for char in rolles:
                    if char in "[]":
                        rolles = rolles.replace(char, '')
                rolles = rolles.split(',')
                for srole in rolles:
                    try:
                        channel.append(int(srole))
                    except:
                        pass
                return channel
        return False

    @staticmethod
    def has_partner(guildid):
        cur.execute(f"SELECT * FROM cv2.partner")
        a = cur.fetchall()
        for x in a:
            if x[0] == guildid:
                return True
        return False

    @staticmethod
    def get_cooldown(guildid):
        cur.execute(f"SELECT * FROM cv2.partner")
        a = cur.fetchall()
        for x in a:
            if x[0] == guildid:
                return int(x[6])
        return False
class games():
    def __init__(self):
        self._channels = {}

    @staticmethod
    def get_sg_speed(userid):
        cur.execute(f"SELECT * FROM cv2.speedgame")
        a = cur.fetchall()
        for x in a:
            if x[0] == userid:
                return float(x[1])
        return False
class permissions():
    def __init__(self):
        self._channels = {}

    @staticmethod
    def has_bot_admin(ctx):
        cur.execute(f"SELECT * FROM cv2.admins")
        a = cur.fetchall()
        for x in a:
            if x[0] == ctx.author.id:
                if x[2] in ['OWNER', 'ADMIN']:
                    return True
        return False
    @staticmethod
    def has_admin(ctx):
        if permissions.has_bot_admin(ctx=ctx):
            return True
        if ctx.author.permissions_in(ctx.channel).administrator:
            return True
        if permissions.has_mod(ctx=ctx) == True:
            return True
        return False

    @staticmethod
    def has_mod(ctx):
        cur.execute(f"SELECT * FROM cv2.permissions")
        a = cur.fetchall()
        for x in a:
            if x[0] == ctx.guild.id:
                if x[1] == ctx.author.id:
                    if str(x[2]) == str(ctx.command.name):
                        return True
                    if str(x[2]) == 'giveaway' and str(ctx.command.name) in ['greroll', 'gstart']:
                        return True
                    if str(x[2]) == 'invite' and str(ctx.command.name) in ['setinvitechannel', 'removeinvitechannel']:
                        return True
                    if str(x[2]) == 'knast' and str(ctx.command.name) in ['ksetup', 'kadd', 'kremove', 'kupdate', 'kcheck']:
                            return True
                    if str(x[2]) == 'moderation' and str(ctx.command.name) in ['ban', 'unban', 'kick', 'clear']:
                            return True
                    if str(x[2]) == 'music' and str(ctx.command.name) in ['radio']:
                            return True
                    if str(x[2]) == 'rr' and str(ctx.command.name) in ['rradd', 'rrremove', 'mradd', 'mrremove', 'aradd', 'arremove', 'arignoreadd', 'arignoreremvoe']:
                            return True
                    if str(x[2]) == 'secure' and str(ctx.command.name) in ['sk', 'bypass']:
                            return True
                    if str(x[2]) == 'voice' and str(ctx.command.name) in ['settempchannel', 'removetempchannel', 'setvoicerole', 'removevoicerole']:
                            return True

                for role in ctx.author.roles:
                    if role.id == x[1]:
                        if str(x[2]) == str(ctx.command.name):
                            return True
                        if str(x[2]) == 'giveaway' and str(ctx.command.name) in ['greroll', 'gstart']:
                            return True
                        if str(x[2]) == 'invite' and str(ctx.command.name) in ['setinvitechannel', 'removeinvitechannel']:
                            return True
                        if str(x[2]) == 'knast' and str(ctx.command.name) in ['ksetup', 'kadd', 'kremove', 'kupdate', 'kcheck']:
                            return True
                        if str(x[2]) == 'moderation' and str(ctx.command.name) in ['ban', 'unban', 'kick', 'clear']:
                            return True
                        if str(x[2]) == 'music' and str(ctx.command.name) in ['radio']:
                            return True
                        if str(x[2]) == 'rr' and str(ctx.command.name) in ['rradd', 'rrremove', 'mradd', 'mrremove', 'aradd', 'arremove', 'arignoreadd', 'arignoreremvoe']:
                            return True
                        if str(x[2]) == 'secure' and str(ctx.command.name) in ['sk', 'bypass']:
                            return True
                        if str(x[2]) == 'voice' and str(ctx.command.name) in ['settempchannel', 'removetempchannel', 'setvoicerole', 'removevoicerole']:
                            return True
        return False

    @staticmethod
    def member_has_admin(member, ctx):
        if member.permissions_in(ctx.channel).administrator:
            return True
        if permissions.member_has_mod(member=member, ctx=ctx) == True:
            return True
        return False
    @staticmethod
    def member_has_mod(member, ctx):
        cur.execute(f"SELECT * FROM cv2.permissions")
        a = cur.fetchall()
        for x in a:
            if x[0] == ctx.guild.id:
                if x[1] == member.id:
                    if str(x[2]) == str(ctx.command.name):
                        return True
                    if str(x[2]) == 'giveaway' and str(ctx.command.name) in ['greroll', 'gstart']:
                        return True
                    if str(x[2]) == 'invite' and str(ctx.command.name) in ['setinvitechannel', 'removeinvitechannel']:
                        return True
                    if str(x[2]) == 'knast' and str(ctx.command.name) in ['ksetup', 'kadd', 'kremove', 'kupdate', 'kcheck']:
                        return True
                    if str(x[2]) == 'moderation' and str(ctx.command.name) in ['ban', 'unban', 'kick', 'clear']:
                        return True
                    if str(x[2]) == 'music' and str(ctx.command.name) in ['radio']:
                        return True
                    if str(x[2]) == 'rr' and str(ctx.command.name) in ['rradd', 'rrremove', 'mradd', 'mrremove', 'aradd', 'arremove', 'arignoreadd', 'arignoreremvoe']:
                        return True
                    if str(x[2]) == 'secure' and str(ctx.command.name) in ['sk', 'bypass']:
                        return True
                    if str(x[2]) == 'voice' and str(ctx.command.name) in ['settempchannel', 'removetempchannel', 'setvoicerole', 'removevoicerole']:
                        return True

                for role in member.roles:
                    if role.id == x[1]:
                        if str(x[2]) == str(ctx.command.name):
                            if str(x[2]) == str(ctx.command.name):
                                return True
                            if str(x[2]) == 'giveaway' and str(ctx.command.name) in ['greroll', 'gstart']:
                                return True
                            if str(x[2]) == 'invite' and str(ctx.command.name) in ['setinvitechannel', 'removeinvitechannel']:
                                return True
                            if str(x[2]) == 'knast' and str(ctx.command.name) in ['ksetup', 'kadd', 'kremove', 'kupdate', 'kcheck']:
                                return True
                            if str(x[2]) == 'moderation' and str(ctx.command.name) in ['ban', 'unban', 'kick', 'clear']:
                                return True
                            if str(x[2]) == 'music' and str(ctx.command.name) in ['radio']:
                                return True
                            if str(x[2]) == 'rr' and str(ctx.command.name) in ['rradd', 'rrremove', 'mradd', 'mrremove', 'aradd', 'arremove', 'arignoreadd', 'arignoreremvoe']:
                                return True
                            if str(x[2]) == 'secure' and str(ctx.command.name) in ['sk', 'bypass']:
                                return True
                            if str(x[2]) == 'voice' and str(ctx.command.name) in ['settempchannel', 'removetempchannel', 'setvoicerole', 'removevoicerole']:
                                return True
        return False

    @staticmethod
    async def no_perms(ctx):
        embed=discord.Embed(title=f'Fehlende Rechte', description=f'Du hast offenbar zu wenig Rechte um diesen Befehl nutzen zu können!', color=discord.Color.from_rgb(255,0,0))
        await ctx.send(embed=embed)
class utils():
    def __init__(self):
        self._channels = {}
    @staticmethod
    def escape(text):
        return discord.utils.escape_markdown(text=text)
    @staticmethod
    def has_premium_guild(guild, userid):
        cur.execute(f"SELECT * FROM cv2.premium")
        a = cur.fetchall()
        for x in a:
            if x[0] == userid:
                if guild.owner_id == userid:
                    return True
        return False

    @staticmethod
    def has_premium_tier1(userid):
        cur.execute(f"SELECT * FROM cv2.premium")
        a = cur.fetchall()
        for x in a:
            if x[0] == userid:
                if int(x[5]) == 1:
                    return True
        if utils.has_premium_tier2(userid=userid):
            return True
        return False

    @staticmethod
    def has_premium_tier2(userid):
        cur.execute(f"SELECT * FROM cv2.premium")
        a = cur.fetchall()
        for x in a:
            if x[0] == userid:
                if int(x[5]) == 2:
                    return True
        if utils.has_premium_tier3(userid=userid):
            return True
        return False

    @staticmethod
    def has_premium_tier3(userid):
        cur.execute(f"SELECT * FROM cv2.premium")
        a = cur.fetchall()
        for x in a:
            if x[0] == userid:
                if int(x[5]) == 3:
                    return True
        return False
    @staticmethod
    async def no_premium(ctx):
        embed = discord.Embed(title=f'Premium', description=f'Du benötigst als Server Owner Premium um dies nutzen zu können!',
                              color=discord.Color.from_rgb(255, 0, 0))
        await ctx.send(embed=embed)
    @staticmethod
    def time_of_string(ctx, zeit):
        try:
            if 'perma' == zeit or zeit == 'permanent':
                itime = 1
            elif 'm' in zeit:
                for char in zeit:
                    if char in "m":
                        rolles = zeit.replace(char, '')
                itime = int(rolles) * 60 + time.time()
            elif 'h' in zeit:
                for char in zeit:
                    if char in "h":
                        rolles = zeit.replace(char, '')
                itime = int(rolles) * 3600 + time.time()
            elif 'd' in zeit:
                for char in zeit:
                    if char in "d":
                        rolles = zeit.replace(char, '')
                itime = int(rolles) * (3600 * 24) + time.time()
            elif 'w' in zeit:
                for char in zeit:
                    if char in "w":
                        rolles = zeit.replace(char, '')
                itime = int(rolles) * (3600 * 24 * 7) + time.time()
            elif 'M' in zeit:
                for char in zeit:
                    if char in "M":
                        rolles = zeit.replace(char, '')
                itime = int(rolles) * (3600 * 24 * 30) + time.time()
            elif 'y' in zeit:
                for char in zeit:
                    if char in "y":
                        rolles = zeit.replace(char, '')
                itime = int(rolles) * (3600 * 24 * 30 * 12) + time.time()  #

            else:
                return False
            return itime
        except:
            return f'x0x'

    @staticmethod
    def rltime_of_string(zeit):
        if 'perma' == zeit or zeit == 'permanent':
            xtime = ' permanent'
        elif 'm' in zeit:
            rolles = zeit.replace('m', '')
            itime = int(rolles)
            if itime > 1:
                xtime = '' + str(itime) + ' Minuten'
            else:
                xtime = '' + str(itime) + ' Minute'
        elif 'h' in zeit:
            rolles = zeit.replace('h', '')
            itime = int(rolles)
            if itime > 1:
                xtime = '' + str(itime) + ' Stunden'
            else:
                xtime = '' + str(itime) + ' Stunde'
        elif 'd' in zeit:
            rolles = zeit.replace('d', '')
            itime = int(rolles)
            if itime > 1:
                xtime = '' + str(itime) + ' Tage'
            else:
                xtime = '' + str(itime) + ' Tag'
        elif 'w' in zeit:
            rolles = zeit.replace('m', '')
            itime = int(rolles)
            if itime > 1:
                xtime = '' + str(itime) + ' Wochen'
            else:
                xtime = '' + str(itime) + ' Woche'
        elif 'M' in zeit:
            rolles = zeit.replace('M', '')
            itime = int(rolles)
            if itime > 1:
                xtime = '' + str(itime) + ' Monate'
            else:
                xtime = '' + str(itime) + ' Monat'
        elif 'y' in zeit:
            rolles = zeit.replace('y', '')
            itime = int(rolles)
            if itime > 1:
                xtime = '' + str(itime) + ' Jahre'
            else:
                xtime = '' + str(itime) + ' Jahr'

        else:
            return 'Ein Fehler ist aufgetreten'
        return xtime
    @staticmethod
    async def send_embed(ctx, title, desc, client):
        if len(desc) > 2048:
            desc= desc[:2040]+'...'
        embed=discord.Embed(title=title, description=desc, color=utils.embed_color(ctx=ctx, client=client))
        msg = await ctx.send(embed=embed)
        return msg

    @staticmethod
    async def send_error(ctx, desc, client):
        embed = discord.Embed(title=f'Ein Fehler ist aufgetreten', description=desc, color=discord.Color.from_rgb(255,0,0))
        await ctx.send(embed=embed)
    @staticmethod
    def get_correct_help_error_response(ctx):
        cur.execute(f"SELECT * FROM public.help")
        a = cur.fetchall()
        for x in a:
            if prefix + ctx.command.name == x[2].split(' ', 1)[0]:
                return [str(x[2]), str(x[3])]
        for x in a:
            if prefix + ctx.command.name in x[2]:
                return [str(x[2]), str(x[3])]
        return None
    @staticmethod
    def embed_color(ctx, client):
        cl = ctx.guild.get_member(client.user.id).top_role.color
        if str(cl) == '#000000':
            cl = 0x2F3136
        return cl

    @staticmethod
    def embed_color_by_guild(guild, client):
        cl = guild.get_member(client.user.id).top_role.color
        if str(cl) == '#000000':
            cl = 0x2F3136
        return cl
    @staticmethod
    def is_banned(id):
        cur.execute(f"SELECT * FROM cv2.banned")
        a = cur.fetchall()
        for x in a:
            if x[0] == id:
                return True
        return False

    @staticmethod
    def is_banned2(ctx):
        cur.execute(f"SELECT * FROM cv2.banned")
        a = cur.fetchall()
        for x in a:
            if x[0] == ctx.guild.id:
                return True
            if x[0] == ctx.guild.owner_id:
                return True
            if x[0] == ctx.author.id:
                return True
        return False

    @staticmethod
    def is_banned3(user, guild):
        cur.execute(f"SELECT * FROM cv2.banned")
        a = cur.fetchall()
        for x in a:
            if x[0] == guild.id:
                return True
            if x[0] == guild.owner_id:
                return True
            if x[0] == user.id:
                return True
        return False
    @staticmethod
    def get_server_prefix(guildid):
        cur.execute(f"SELECT * FROM cv2.setup")
        a = cur.fetchall()
        for x in a:
            if x[0] == guildid:
                return x[2]
        return prefix

    @staticmethod
    def get_server_owner(guildid):
        cur.execute(f"SELECT * FROM cv2.setup")
        a = cur.fetchall()
        for x in a:
            if x[0] == guildid:
                return x[1]
        return False
    @staticmethod
    def banned_reason(id):
        cur.execute(f"SELECT * FROM cv2.banned")
        a = cur.fetchall()
        for x in a:
            if x[0] == id:
                return x[1]
        return False

    @staticmethod
    def banned_author(id):
        cur.execute(f"SELECT * FROM cv2.banned")
        a = cur.fetchall()
        for x in a:
            if x[0] == id:
                return x[2]
        return False

    @staticmethod
    def banned_time(id):
        cur.execute(f"SELECT * FROM cv2.banned")
        a = cur.fetchall()
        for x in a:
            if x[0] == id:
                return x[3]
        return False

    @staticmethod
    def is_afk(userid, guildid):
        cur.execute(f"SELECT * FROM cv2.afk")
        a = cur.fetchall()
        for x in a:
            if x[0] == userid:
                if x[1] == guildid:
                    return True
        return False

    @staticmethod
    def afk_get_time(userid, guildid):
        cur.execute(f"SELECT * FROM cv2.afk")
        a = cur.fetchall()
        for x in a:
            if x[0] == userid:
                if x[1] == guildid:
                    return x[3]
        return False

    @staticmethod
    def afk_get_reason(userid, guildid):
        cur.execute(f"SELECT * FROM cv2.afk")
        a = cur.fetchall()
        for x in a:
            if x[0] == userid:
                if x[1] == guildid:
                    return x[2]
        return 'afk'

    @staticmethod
    def get_knast_role(guild):
        cur.execute(f"SELECT * FROM cv2.knastsetup")
        a = cur.fetchall()
        for x in a:
            if x[0] == guild.id:
                for role in guild.roles:
                    if x[2] == role.id:
                        return role.id

    @staticmethod
    def get_knast_log(guild):
        cur.execute(f"SELECT * FROM cv2.knastsetup")
        a = cur.fetchall()
        for x in a:
            if x[0] == guild.id:
                for channel in guild.channels:
                    if x[1] == channel.id:
                        return channel.id

    @staticmethod
    def get_knast_user(guild, member):
        cur.execute(f"SELECT * FROM cv2.knastusers")
        a = cur.fetchall()
        for x in a:
            if x[0] == member.id:
                if x[2] == guild.id:
                    return True
        return False

prefix = 'CV2'
INVIS = ' ⠀ '