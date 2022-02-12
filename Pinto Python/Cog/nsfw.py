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

class LEWD(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def help_nsfw(self, ctx):
        embed=discord.Embed(title="Help Menu - LEWD", color=0xff0000)
        embed.add_field(name="p!fuck <member>", 
                        value="ehm yes...", 
                        inline=False)
        embed.add_field(name="p!neko", 
                        value="Meow", 
                        inline=False)
        embed.add_field(name="p!yuri", 
                        value="2 girls", 
                        inline=False)
        embed.add_field(name="p!yaoi", 
                        value="2 dudes", 
                        inline=False)
        embed.add_field(name="p!furry", 
                        value="Hairy stuff", 
                        inline=False)
        embed.add_field(name="p!loli", 
                        value="Are you sure you wanna do this?", 
                        inline=False)
        embed.add_field(name="p!ass", 
                        value="try it yourself...", 
                        inline=False)
        embed.add_field(name="p!tits", 
                        value="try it yourself...", 
                        inline=False)
        embed.add_field(name="p!gay", 
                        value="try it yourself...", 
                        inline=False)
        embed.add_field(name="p!porn", 
                        value="try it yourself...", 
                        inline=False)
        embed.add_field(name="p!bdsm", 
                        value="try it yourself...", 
                        inline=False)
        await ctx.send(embed=embed)
    @commands.command()
    async def fuck(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        embed = discord.Embed(description=f"**{ctx.author.name} does lewd things to {member.name}**", color=0xffc585)
        embed.set_image(url="https://i.imgur.com/8Dq3XYt.gif")
        embed.timestamp=datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command()
    async def neko(self, ctx, *, reason:str="no reason"):
        embed = discord.Embed(description=f"**{ctx.author.name} rawr**", color=0xffc585)
        embed.set_image(url="https://i.pinimg.com/originals/f5/91/1b/f5911b6b69ca9a114372a5cf890807a6.gif")
        embed.timestamp=datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command()
    async def yuri(self, ctx, *, reason:str="no reason"):
        embed = discord.Embed(description=f"**Some yuri stuff for {ctx.author.name}**", color=0xffc585)
        embed.set_image(url="https://cutewallpaper.org/21/yuri-anime-kiss/Anime-Yuri-GIF-Anime-Yuri-Kissing-Discover-and-Share-GIFs.gif")
        embed.timestamp=datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command()
    async def yaoi(self, ctx, *, reason:str="no reason"):
        embed = discord.Embed(description=f"**Some yaoi stuff for {ctx.author.name}**", color=0xffc585)
        embed.set_image(url="https://cdn60.picsart.com/184925822000202.gif")
        embed.timestamp=datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command()
    async def furry(self, ctx, *, reason:str="no reason"):
        embed = discord.Embed(description=f"**{ctx.author.name} is a furry**", color=0xffc585)
        embed.set_image(url="https://i.kym-cdn.com/photos/images/newsfeed/000/803/142/d06.gif")
        embed.timestamp=datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command()
    async def loli(self, ctx, *, reason:str="no reason"):
        embed = discord.Embed(description=f"**Are you sure, {ctx.author.name}?**", color=0xffc585)
        embed.set_image(url="https://i.makeagif.com/media/7-22-2018/xaUFWn.gif")
        embed.timestamp=datetime.utcnow()
        await ctx.send(embed=embed)
    @commands.command()

    async def nudes(self, ctx):
        if ctx.channel.is_nsfw():
            picture = ["https://cdn.boob.bot/ass/4E39.JPG", "https://cdn.boob.bot/ass/4E1B.JPG", "https://cdn.boob.bot/ass/4C65.JPG", "https://cdn.boob.bot/ass/50A0.JPG", "https://cdn.boob.bot/boobs/4CEF.JPG", "https://cdn.boob.bot/boobs/8000CDDB.gif", "https://cdn.boob.bot/boobs/8000231D.gif", "https://cdn.boob.bot/boobs/8000D5BA.gif", "https://cdn.boob.bot/boobs/80004334.gif", "https://cdn.boob.bot/boobs/80004FEB.gif", "https://cdn.boob.bot/boobs/80011BF6.jpg", "https://cdn.boob.bot/boobs/80004771.gif"]
            ranpunch = random.choice(picture)
            punch1 = embed = discord.Embed(description=f"**Here You Go!**", color=0xffc585)
            embed.set_image(url=ranpunch)
            embed.timestamp=datetime.utcnow()
            punch1 = await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="NSFW ONLY", value=f"Bitte benutze diesen Command in einem NSFW Channel", color=0xff0000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/706129830441386074/783737666902294579/oe4iK5i.gif")
            await ctx.send(embed=embed)


    @commands.command()

    async def gay(self, ctx):
        if ctx.channel.is_nsfw():
            picture = ["https://cdn.boob.bot/gay/EBE6.jpg", "https://cdn.boob.bot/gay/844E.jpg", "https://cdn.boob.bot/gay/844E.jpg", "https://cdn.boob.bot/gay/844E.jpg", "https://cdn.boob.bot/gay/201BE.jpeg", "https://cdn.boob.bot/gay/350F6.jpg", "https://cdn.boob.bot/gay/30498.jpg", "https://cdn.boob.bot/gay/2B086.jpg", "https://cdn.boob.bot/gay/1C94C.JPG", "https://cdn.boob.bot/gay/160E8.jpg", "https://cdn.boob.bot/gay/334CE.jpg", "https://cdn.boob.bot/gay/1BB5A.png", "https://cdn.boob.bot/gay/3414A.jpg", "https://cdn.boob.bot/gay/2D2CA.jpg"]
            ranpunch = random.choice(picture)
            punch1 = embed = discord.Embed(description=f"**{ctx.author.mention}, here are your Pics**", color=0xffc585)
            embed.set_image(url=ranpunch)
            embed.timestamp=datetime.utcnow()
            punch1 = await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="NSFW ONLY", value=f"Bitte benutze diesen Command in einem NSFW Channel", color=0xff0000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/706129830441386074/783737666902294579/oe4iK5i.gif")
            await ctx.send(embed=embed)
    @commands.command()

    async def porn(self, ctx):
        if ctx.channel.is_nsfw():
            picture = ["https://cdn.boob.bot/Gifs/15DC.gif", "https://cdn.discordapp.com/attachments/815017955375972362/815020598618226698/22631947.gif", "https://cdn.discordapp.com/attachments/815017955375972362/815020577315880980/01f00a2b8bae7a62431eb6bbe6d74de4.gif", "https://cdn.discordapp.com/attachments/815017955375972362/815020614837862460/aurielee-summers-and-malena-morgan-rimjob.gif", "https://cdn.discordapp.com/attachments/815017955375972362/815020636778135572/unnamed.gif", "https://cdn.discordapp.com/attachments/815017955375972362/815020933626069002/ezgif-4-e45259496796.gif", "https://cdn.discordapp.com/attachments/815017955375972362/815020965733203998/ezgif-7-d9aaa925c435.gif", "https://cdn.boob.bot/Gifs/195D.gif", "https://cdn.boob.bot/Gifs/165A.gif", "https://cdn.boob.bot/Gifs/194F.gif", "https://cdn.boob.bot/Gifs/199F.gif", "https://cdn.boob.bot/Gifs/195A.gif", "https://cdn.boob.bot/Gifs/16ED.gif", "https://cdn.boob.bot/Gifs/17EE.gif", "https://cdn.boob.bot/Gifs/196C.gif", "https://cdn.boob.bot/Gifs/1615.gif", "https://cdn.boob.bot/Gifs/15C0.gif", "https://cdn.boob.bot/Gifs/16F3.gif", "https://cdn.boob.bot/Gifs/15F6.gif", "https://cdn.boob.bot/Gifs/16EA.gif", "https://cdn.boob.bot/Gifs/18D1.gif", "https://cdn.boob.bot/Gifs/176F.gif", "https://cdn.boob.bot/Gifs/16AC.gif", "https://cdn.boob.bot/Gifs/1772.gif", "https://cdn.boob.bot/Gifs/1772.gif", "https://cdn.boob.bot/Gifs/18A4.gif", "https://cdn.boob.bot/Gifs/1982.gif", "https://cdn.boob.bot/Gifs/17E2.gif", "https://cdn.boob.bot/Gifs/17BC.gif", "https://cdn.boob.bot/Gifs/16CD.gif", "https://cdn.boob.bot/Gifs/1866.gif", "https://cdn.boob.bot/Gifs/16A6.gif", "https://cdn.boob.bot/Gifs/1959.gif", "https://cdn.boob.bot/Gifs/16BA.gif", "https://cdn.boob.bot/Gifs/19B4.gif", "https://cdn.boob.bot/Gifs/15F9.gif", "https://cdn.boob.bot/Gifs/15C3.gif", "https://cdn.boob.bot/Gifs/1889.gif", "https://cdn.boob.bot/Gifs/18FB.gif", "https://cdn.boob.bot/Gifs/1849.gif", "https://cdn.boob.bot/Gifs/166D.gif", "https://cdn.boob.bot/Gifs/15F8.gif", "https://cdn.boob.bot/Gifs/17AE.gif", "https://cdn.boob.bot/Gifs/1896.gif", "https://cdn.boob.bot/Gifs/15E6.gif"]
            ranpunch = random.choice(picture)
            punch1 = embed = discord.Embed(description=f"**The usual shit**", color=0xffc585)
            embed.set_image(url=ranpunch)
            embed.timestamp=datetime.utcnow()
            punch1 = await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="NSFW ONLY", value=f"Bitte benutze diesen Command in einem NSFW Channel", color=0xff0000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/706129830441386074/783737666902294579/oe4iK5i.gif")
            await ctx.send(embed=embed)
    @commands.command()
    async def bdsm(self, ctx):
        if ctx.channel.is_nsfw():
            picture = ["https://cdn.boob.bot/Gifs/160F.gif", "https://cdn.boob.bot/bdsm/8EAD.jpg", "https://cdn.boob.bot/bdsm/4542.JPG", "https://cdn.boob.bot/bdsm/5D2F.jpg", "https://cdn.boob.bot/bdsm/BEAA.gif", "https://cdn.boob.bot/bdsm/8CA0.png", "https://cdn.boob.bot/bdsm/D4AD.jpg", "https://cdn.boob.bot/bdsm/45CE.jpg", "https://cdn.boob.bot/bdsm/9BAA.jpg", "https://cdn.boob.bot/bdsm/9BAA.jpg", "https://cdn.boob.bot/bdsm/78CD.gif", "https://cdn.boob.bot/bdsm/CF35.jpg", "https://cdn.boob.bot/bdsm/7CA1.jpg", "https://cdn.boob.bot/bdsm/4358.JPG", "https://cdn.boob.bot/bdsm/C2E7.jpg", "https://cdn.boob.bot/bdsm/BF36.jpg"]
            ranpunch = random.choice(picture)
            punch1 = embed = discord.Embed(description=f"**{ctx.author.mention} MASTER!!!!**", color=0xffc585)
            embed.set_image(url=ranpunch)
            embed.timestamp=datetime.utcnow()
            punch1 = await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="NSFW ONLY", value="Bitte benutze diesen Command in einem NSFW Channel", color=0xff0000)
            embed.set_image(url="https://cdn.discordapp.com/attachments/706129830441386074/783737666902294579/oe4iK5i.gif")
            await ctx.send(embed=embed)






def setup(client):
    client.add_cog(LEWD(client))
