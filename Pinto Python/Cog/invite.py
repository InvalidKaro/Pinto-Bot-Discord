import asyncio
from asyncio import sleep as s
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
client = discord.Client


class INVITE(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def help_invite(self, ctx):
        embed=discord.Embed(title="HELP MENU - Invite", color=0xffc585)
        embed.add_field(name="p!invite", 
                        value="Lade den Bot auf deinen Server ein")
        embed.add_field(name="p!vote", 
                        value="Vote für Pinto auf `Matrixbots.xyz`")
        await ctx.send(embed=embed)
    @commands.command()
    async def invite(self, ctx):
        embed=discord.Embed(title="Invite Link", color=0xffc585)
        embed.add_field(name="Pinto", 
                        value=f"[Bot Invite](https://discord.com/api/oauth2/authorize?client_id=809824051773177917&permissions=8&scope=bot\n \r)")
        embed.add_field(name="Support", 
                        value=f"[Support Server](https://discord.gg/kZp6zYA7xz)")
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/809824051773177917/c1cb4b1dab35f99d7162b69e623e9ea6.png?size=256")
        embed.set_footer(text="Pinto Bot - Developed by Karo", 
                        icon_url="https://cdn.discordapp.com/avatars/809824051773177917/c1cb4b1dab35f99d7162b69e623e9ea6.png?size=256")
        await ctx.send(embed=embed)
        await ctx.message.delete() 
    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def reminder(self, ctx, time: int, *, message):
        await ctx.message.add_reaction("<:JQY:802700281087262770>")
        while True:
            await s(time)
            await ctx.send(f"{message}")
    @commands.command()
    async def vote(self, ctx):
        embed=discord.Embed(title="Vote Für Pinto", description=f"[Vote hier](https://www.matrixbots.xyz/bots/vote/809824051773177917) auf `Matrixbots.xyz`", color=0xffc585)
        embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/809824051773177917/c1cb4b1dab35f99d7162b69e623e9ea6.png?size=256")
        embed.set_footer(text="Pinto Bot - Developed by Karo", 
                        icon_url="https://cdn.discordapp.com/avatars/809824051773177917/c1cb4b1dab35f99d7162b69e623e9ea6.png?size=256")
        await ctx.send(embed=embed)
         



 
        

    



def setup(client):
    client.add_cog(INVITE(client))
