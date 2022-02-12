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



class PERMS(commands.Cog):
    def __init__(self, client):
        self.client = client

#⛔ #✅

    @commands.command(aliases=['perms'])
    async def permscheck(self, ctx, member:discord.Member = None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(title=f'Permission Check', 
                              description=f'**{member.name}#{member.discriminator}**',
                              color=0xffc585)

        embed.set_thumbnail(url=f'{member.avatar_url}')
        embed.set_footer(text=f'Requested by {ctx.author.name}')

        embed.add_field(name='`Admin`', 
                        value=str(member.guild_permissions.administrator).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Kick Members`', 
                        value=str(member.guild_permissions.kick_members).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Ban Members`', 
                        value=str(member.guild_permissions.ban_members).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Manage Messages`', 
                        value=str(member.guild_permissions.manage_messages).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Ping Everyone`', 
                        value=str(member.guild_permissions.mention_everyone).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Mute Members`', 
                        value=str(member.guild_permissions.mute_members).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Deafen Members`', 
                        value=str(member.guild_permissions.deafen_members).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Change Nick`', 
                        value=str(member.guild_permissions.change_nickname).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Manage Channels`', 
                        value=str(member.guild_permissions.manage_channels).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Manage Roles`', 
                        value=str(member.guild_permissions.manage_roles).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Manage Server`', 
                        value=str(member.guild_permissions.manage_guild).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        embed.add_field(name='`Manage Perms`', 
                        value=str(member.guild_permissions.manage_permissions).replace('True', '<:check_mark:827958918424428614>').replace('False', '<:nein2:827958960270344263>'),
                        inline=True)
        await ctx.send(embed=embed)

    @commands.command()
    async def has(self,ctx, arg:str = None):
        if arg == None:
            embed=discord.Embed(title="Ich unterstütze folgende Argumente:", description="`admin\r\nkick\r\nban\r\nmessage\r\nping\r\nmute\r\ndeaf\r\nnick\r\nchannel\r\nrole\r\nserver\r\nperms`", color=0xffc585)
            embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
            await ctx.send(embed=embed)
        elif arg == "admin":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Admin", value=str(ctx.author.guild_permissions.administrator).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "kick":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Kick", value=str(ctx.author.guild_permissions.kick_members).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "ban":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Ban", value=str(ctx.author.guild_permissions.ban_members).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "message":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Manage Messages", value=str(ctx.author.guild_permissions.manage_messages).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "ping":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Mention @everyone", value=str(ctx.author.guild_permissions.mention_everyone).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "mute":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Mute", value=str(ctx.author.guild_permissions.mute_members).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "deaf":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Deafen", value=str(ctx.author.guild_permissions.deafen_members).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "nick":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Nick", value=str(ctx.author.guild_permissions.change_nickname).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "channel":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Manage Channels", value=str(ctx.author.guild_permissions.manage_channels).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "role":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Manage Roles", value=str(ctx.author.guild_permissions.manage_roles).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "server":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Manage Server", value=str(ctx.author.guild_permissions.manage_guild).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)
        elif arg == "perms":
            embed = discord.Embed(color=0xffc585)
            embed.add_field(name="Manage Perms", value=str(ctx.author.guild_permissions.manage_permissions).replace('True', '<:check_mark:827958918424428614> Du besitzt diese Berechtigung').replace('False', '<:nein2:827958960270344263> Du besitzt diese Berechtigung nicht'), inline=True)
            await ctx.send(embed=embed)






def setup(client):
    client.add_cog(PERMS(client))