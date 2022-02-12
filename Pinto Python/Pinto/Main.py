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




intent = Intents().all()
client = commands.Bot(command_prefix = "!", case_insensitive=True, intents = intent)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"bot ready")


@client.command()
async def help(ctx, arg:str = None):
    if arg == None:
        embed=discord.Embed(title="Help Menu")
        embed.add_field(name="Disboard", value="!help disboard")  #HELP CMDS
        await ctx.send(embed=embed)
    elif arg == "disboard":
        await ctx.invoke(client.get_command("help_disboard"))



for filename in os.listdir('./Cog'):
    if filename.endswith('.py'):
        client.load_extension(f'Cog.{filename[:-3]}')
        print(f"loaded{filename}")






with open("setup.json") as f:
    data = json.load(f)
    _token=data["token"]
client.run(_token)