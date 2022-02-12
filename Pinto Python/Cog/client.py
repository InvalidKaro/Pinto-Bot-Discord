import asyncio
import discord
from discord.ext import commands
import random
import time
from discord \
    import Member, Guild, User
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
import random
from random import randint

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
client = commands.Bot(command_prefix = ["p!",'P!', '<@809824051773177917>'], 
                      case_insensitive=True, 
                      intents = intent)
client.remove_command("help")


class KEK(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.botname = 'Knast'


@commands.Cog.listener()
async def on_message(self,ctx, message):
    if message.content.startswith('kek'):
        channel = ctx.channel
        await channel.send('<:KEKYou:820473475378577409>')





def setup(client):
    client.add_cog(KEK(client))



