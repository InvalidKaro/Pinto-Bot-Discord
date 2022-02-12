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
with open('setup.json') as f:
    data = json.load(f)
    _user = data['public_usr']
    _password = data['public_pw']
    _host = data['public_host']
    _database = data['public_DB']
try:
    conn_public = mysql.connector.connect(
        user=_user,
        password=_password,
        host=_host,
        database=_database,
        autocommit=True,
    )
except mysql.connector.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
cur = conn_public.cursor()