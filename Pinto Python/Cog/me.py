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


class DEV(commands.Cog):
    def __init__(self, client):
        self.client = client




def setup(client):
    client.add_cog(DEV(client))








