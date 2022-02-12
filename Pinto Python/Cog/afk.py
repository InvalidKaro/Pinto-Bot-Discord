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
from xml.etree import cElementTree
from packages.all import * 
from packages.p_mysql import *

class DISBOARD(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def help_afk(self, ctx):
        embed=discord.Embed(title="Help Menu - <a:loading:818229971201818644>AFK")
        embed.add_field(name="p!afk", value="Setze dein afk")
        message = await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command()
    async def afk(self, ctx, *, arg:str="afk"):
        await asyncio.sleep(1)
        sql = "INSERT INTO Pinto.afk(userid, guildid, reason, time, tbid) VALUES(%s, %s, %s, %s, %s)"
        val = (f"{ctx.author.id}", f"{ctx.guild.id}", f"{arg}", f"{time.time()}", f"{ctx.guild.id}.{ctx.author.id}")
        cur.execute(sql, val)
        await utils.send_embed(ctx=ctx, client=self.client, title="Dein AFK wurde gesetzt", desc=f"*{utils.escape(arg)}*")

    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if isinstance(message.channel, discord.DMChannel):
            return
        prefixes = ["p!", f"<@!{self.client.user.id}>"]
        if not message.content.split(" ")[0]in prefixes:
            if utils.is_afk(userid=message.author.id, guildid=message.guild.id):
                cur.execute(f"DELETE FROM pinto.afk WHERE tbid='{message.guild.id}.{message.author.id}'")
                embed=discord.Embed(title="Willkommen zurück", description=f"Dein afk wurde entfernt", color=utils.embed_color(ctx=message, client=self.client))
                await message.channel.send(embed=embed)
                embed=discord.Embed(title=f'Es sind einige Dinge in deiner Abwesenheit geschehen.', description=f'Hier folgen alle Nachrichten von {message.guild}, während du abwesend warst.')
                count = 0
                cur.execute(f"SELECT * FROM Pinto.afkmessages ORDER BY time DESC")
                a = cur.fetchall()
                for x in a:
                    if x[0] == message.author.id:
                        if x[1] == message.guild.id:
                            count+=1
                            memberx=message.guild.get_member(int(x[3]))
                            text = str(x[2])
                            if len(text) >1000:
                                text=text[:+1000]+'...'
                            if count <= 25:
                                embed.add_field(name=f'Von `{memberx}`\r\n{time.strftime("%c", time.localtime(x[4]))}', value=f'[Jump to Message](https://discord.com/channels/{message.guild.id}/{x[6]}/{x[7]})\r```{x[2]}```')
                            cur.execute(f"DELETE FROM Pinto.afkmessages WHERE tbid = '{x[5]}'")
                if count == 0:
                    embed=discord.Embed(title=f'In deiner Abwesenheit auf {message.guild} gab es keine wichtigen Informationen für dich.')
                try:
                    await message.author.create_dm()
                    await message.author.dm_channel.send(embed=embed)
                except:
                    pass
            for member in message.mentions:
                if utils.is_afk(userid=member.id, guildid=message.guild.id):
                    embed = discord.Embed(description=f'{member.mention} ist AFK\r*{discord.utils.escape_markdown(utils.afk_get_reason(userid=member.id, guildid=message.guild.id))}*', color=utils.embed_color(ctx=message, client=self.client))
                    await message.channel.send(embed=embed)
                    sql = "INSERT INTO Pinto.afkmessages (userid, guildid, text, author, time, tbid, channelid, messageid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    xtime = int(time.time())
                    val = (f"{member.id}", f"{message.guild.id}", f'{str(message.content)}', f'{message.author.id}', f'{xtime}', f'{message.guild.id}.{member.id}.{xtime}', f'{message.channel.id}', f'{message.id}')
                    cur.execute(sql, val)
                
     


def setup(client):
    client.add_cog(DISBOARD(client))