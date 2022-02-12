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
    async def help_disboard(self, ctx):
        embed=discord.Embed(title="Help Menu - Disboard")
        embed.add_field(name="p!disboard enablecounter", 
                        value="Aktiviere den Disboard Bump Counter")
        await ctx.send(embed=embed)
    @commands.command()
    async def disboard(self, ctx, arg:str):
        if arg == "enablecounter":
            sql = "INSERT INTO Pinto.disboardcounter(guildid, userid, count, tbid) VALUES(%s, %s, %s, %s)"
            val = (f"{ctx.guild.id}", f"0", f"0", f"{ctx.guild.id}.0")
            try:
                cur.execute(sql, val)
                await utils.send_embed(ctx=ctx, client=self.client, title="Disboard Counter", desc="✔Der Counter wurde aktiviert")
            except:
                await utils.send_error(ctx=ctx, client=self.client, desc="❌Der Counter ist bereits Aktiv")



def setup(client):
    client.add_cog(DISBOARD(client))