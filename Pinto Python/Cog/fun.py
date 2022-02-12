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

client = commands.Bot(command_prefix = ["p!",'P!', '<@809824051773177917>'])

class FUN(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help_fun(self, ctx):
        embed=discord.Embed(title="Help Menu - 🤡Fun🤡", 
                            color=utils.embed_color(ctx=ctx, client=self.client))
        embed.add_field(name="p!poll <message>", 
                        value="Starte eine Umfrage")
        embed.add_field(name="p!say <message>", 
                        value="Ich wiederhole deine Aussage")
        embed.add_field(name="p!flip", 
                        value="Werfe eine Münze")
        embed.add_field(name="p!hug <member>", 
                        value="Zeit für eine Umarmung!")
        embed.add_field(name="p!pat <member>", 
                        value="Mache jemandem zu deinem Pet")
        embed.add_field(name="p!kiss <member>", 
                        value="Zeige deine Liebe")
        embed.add_field(name="p!slap <member>", 
                        value="Verpasse jemandem eine Ohrfeige")
        embed.add_field(name="p!punch <member>", 
                        value="Verprügel eine Person")
        embed.add_field(name="p!cuddle <member>", 
                        value="Zeige einer Person wie gern du sie hast")
        embed.add_field(name="p!tickle <member>", 
                        value="Kitzel jemanden")
        embed.add_field(name="p!hack <member>", 
                        value="Hacke einen User")
        embed.add_field(name="p!highfive <member>", 
                        value="HIGHFIVE!")
        embed.add_field(name="p!cry", 
                        value="Zeige deine Traurigkeit")
        embed.add_field(name="p!meme", 
                        value="Generiert ein random meme")
        embed.add_field(name="p!dice", 
                        value="Würfel einen Würfel")
        embed.add_field(name="p!ask", 
                        value="Lasse dir etwas Vorhersagen")
        embed.add_field(name="p!slots", 
                        value="Spiele am Automaten")
        embed.add_field(name="p!howgay", 
                        value="Gay rate in Prozent")
        embed.add_field(name="p!simprate", 
                        value="Simp rate in Prozent")
        message = await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def poll(self, ctx, *, message):
        embed=discord.Embed(title="UMFRAGE", 
                            description=f"{message}", 
                            color=utils.embed_color(ctx=ctx, 
                            client=self.client))
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/812044252044328961/812867687696302080/ViaFix-icon-stemmen-2.png")
        embed.set_footer(text=f"Requested by {ctx.author.name}", 
                        icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp=datetime.utcnow()
        message = await ctx.send(embed=embed)
        await message.add_reaction("<:jup:814310864516546600>")
        await message.add_reaction("<:nop:814311008318259210>")
        await ctx.message.delete()
    @commands.command()
    async def say(self,ctx, *, message, ):
        embed=discord.Embed(title=None, 
                            description=f"{message}", 
                            color=utils.embed_color(ctx=ctx, 
                            client=self.client))
        embed.set_author(name=f"{ctx.author.name}", icon_url=f"{ctx.author.avatar_url}")
        embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/809824051773177917/c1cb4b1dab35f99d7162b69e623e9ea6.png?size=256")
        embed.timestamp=datetime.utcnow()
        await ctx.send(embed=embed)
        await ctx.message.delete()    


        
    @commands.command()
    async def hack(self, ctx, member:discord.Member):
        message = await ctx.send(f"Hacking {member.name}...")
        await asyncio.sleep(3)
        await message.edit(content=f"<a:loading:818229971201818644> getting ip adress...")
        await asyncio.sleep(3)
        await message.edit(content=f"<a:loading:818229971201818644> installing virus...")
        await asyncio.sleep(3)
        await message.edit(content=f"<a:loading:818229971201818644> slaping his girl...")
        await asyncio.sleep(3)
        await message.edit(content=f"<a:loading:818229971201818644> order some pizza...")
        await asyncio.sleep(3)
        await message.edit(content=f"<a:loading:818229971201818644> leaking {member.name + '´s'} nudes...")
        await asyncio.sleep(3)
        await message.edit(content=f"<a:loading:818229971201818644> stealing {member.name + '´s'} fortnite account...")
        await asyncio.sleep(3)
        await message.edit(content=f"<a:loading:818229971201818644> wasting his/her robux...")
        await asyncio.sleep(3)
        await message.edit(content=f"hacking done...<a:JQY:802700281087262770>")


    @commands.command()
    async def punch(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        picture = ["https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif", "https://3.bp.blogspot.com/-f2C5CBKw05A/W95nlOPZ4HI/AAAAAAABXVo/eU16NRt_qQIh64c3AvSScDYuRL2H6lAegCKgBGAs/s1600/Omake%2BGif%2BAnime%2B-%2BFairy%2BTail%2BFinal%2BSeason%2B-%2BEpisode%2B282%2B-%2BLucy%2BPunch.gif", "https://media1.tenor.com/images/9fc73d84755865fd0e8a67fe6fad9f0f/tenor.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814939070186258502/tenor_11.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814939070555881472/tenor_12.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814939071255412766/tenor_9.gif"]
        ranpunch = random.choice(picture)
        embed = discord.Embed(description=f"**{ctx.author.name} punches {member.name}**", color=0xffc585)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        await ctx.send(embed=embed) 

    @commands.command()
    async def hug(self, ctx, member:discord.Member):
        if member is None:
            member = ctx.author
        picture = ["https://i.imgur.com/r9aU2xv.gif", "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif", "https://media1.tenor.com/images/506aa95bbb0a71351bcaa753eaa2a45c/tenor.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814935234826207242/0b6bd7ba263b15094cae8450a68ff54b.gif","https://cdn.discordapp.com/attachments/801520852591181855/814935234322628648/934e9111d22518d37b9b5684fa99de79.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814935397557338152/tumblr_mt1cllxlBr1s2tbc6o1_500.gif"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**{ctx.author.name} hugs {member.name} with a lot of love**", color=0xffc585)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        picture = ["https://i.imgur.com/fm49srQ.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814938154997252156/tenor_21.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814938155240128522/tenor_20.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814938155522064434/tenor_19.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814938156113330176/tenor_17.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814938156595281920/tenor_16.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814938156993347584/tenor_15.gif"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**Patsch, Patsch, Patsch! {ctx.author.name} slaps {member.name + '´s'} weak ass**", color=0xffc585)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        picture = ["https://data.whicdn.com/images/247697746/original.gif", "https://cdn.discordapp.com/attachments/801252537553649689/814934405968691250/anime-kiss-icegif-2.gif", "https://cdn.discordapp.com/attachments/801252537553649689/814934404812111902/0WWWvat.gif", "https://cdn.discordapp.com/attachments/801252537553649689/814934370660909086/original.gif","https://cdn.discordapp.com/attachments/801252537553649689/814934369567113247/tenor_8.gif", "https://cdn.discordapp.com/attachments/801252537553649689/814934369876836433/tenor-6.gif"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**{ctx.author.name} kisses {member.name} passionate**", color=0xffc585)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed) 

    @commands.command()
    async def tickle(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        picture = ["https://media1.tenor.com/images/eaef77278673333265da087f65941e48/tenor.gif", "https://i.pinimg.com/originals/d3/85/54/d38554c6e23b86c81f8d4a3764b38912.gif", "https://thumbs.gfycat.com/RealisticNippyFirebelliedtoad-small.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814941108353105920/tenor_23.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814941107476627517/tenor_25.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814941105137254400/tenor_27.gif"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**{ctx.author.name} tickles {member.name}**", color=0xffc585)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)  

    @commands.command()
    async def cuddle(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        picture = ["http://cdn.lowgif.com/medium/6b0a88162a4b836c-.gif", "https://i.pinimg.com/originals/06/dd/8f/06dd8f976b7353d69aec173b44927ef4.gif", "https://thumbs.gfycat.com/ShowyObedientCrane-max-1mb.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814939931734048768/tenor_17.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814939931318419537/tenor_19.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814939930966884362/tenor_18.gif"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**Everybody needs someone! {ctx.author.name} cuddles {member.name}**", color=0xffc585)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)  

    @commands.command()
    async def pat(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        picture = ["https://66.media.tumblr.com/2e3f09020ea634bb89559e3ac01b10dc/tumblr_pr75l9PZId1y0nwq1o2_540.gif", "https://i.pinimg.com/originals/2e/27/d5/2e27d5d124bc2a62ddeb5dc9e7a73dd8.gif", "https://gifimage.net/wp-content/uploads/2017/09/anime-head-pat-gif.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814936890930757632/tenor_10.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814936891401043988/tenor_13.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814936891983134730/tenor_12.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814936891677474836/tenor_14.gif"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**Pat, Pat! {ctx.author.name} pats {member.name}**", color=0xffc585)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)

    @commands.command()
    async def welcome(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        picture = ["https://i.pinimg.com/originals/05/6c/58/056c584d9335fcabf080ca43e583e3c4.gif", "https://media.tenor.com/images/f74374a8d12dbcd33c274dec139a3ff7/tenor.gif", "https://gifimage.net/wp-content/uploads/2017/09/anime-waving-gif-13.gif", "https://i.pinimg.com/originals/1f/41/47/1f41471aeb6ec83e4997211b8899a1dd.gif", "https://i.imgur.com/kSbIc8p.gif", "https://i.imgur.com/kSbIc8p.gif", "https://data.whicdn.com/images/245075010/original.gif", "https://gifimage.net/wp-content/uploads/2018/10/anime-gif-hi-9.gif", "https://i.pinimg.com/originals/eb/29/dd/eb29ddfe83189c61454a7dd074981882.gif", "https://i.pinimg.com/originals/eb/29/dd/eb29ddfe83189c61454a7dd074981882.gif", "https://pa1.narvii.com/6299/457faeaed3eb7f65ca9a1cf037c45a6c6e399c1b_hq.gif", "https://media.tenor.com/images/777d853b8d006cf649408da5d251217c/tenor.gif", "https://media1.tenor.com/images/bb3c7292d3c2e75ba4b51ec15bb9bf3b/tenor.gif", "https://media.tenor.com/images/f74374a8d12dbcd33c274dec139a3ff7/tenor.gif", "https://images3.imgbox.com/ba/35/AYqk4UJk_o.gif", "https://media1.tenor.com/images/ae40603eddb6e4bb1ea56cc6de7d0f6e/tenor.gif", "http://cdn79.picsart.com/184046559000202.gif", "https://media.tenor.com/images/824a5c6fb0eff4de202d0cd4da1e6692/tenor.gif", "https://i.pinimg.com/originals/c2/e2/1a/c2e21a9d8e17c1d335166dbcbe0bd1bf.gif"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**Welcome to {ctx.guild.name}, {member.name}**", color=0xffc585)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        picture = ["https://64.media.tumblr.com/5b4e0848d8080db04dbfedf31a4869e2/tumblr_nq1t6uTqRq1qcsnnso1_540.gif", "https://i.pinimg.com/originals/b4/b1/64/b4b1640525ecadfa1030e6096f3ec842.gif", "http://pa1.narvii.com/5729/7239144f9492a477092d05271e10657b9e1a335b_00.gif", "http://cdn.lowgif.com/full/1d81ac5a37d0b4ef-thanks-page-3-vainglory-community-forums.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814942587990441984/tenor_41.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814942589861888073/tenor_37.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814942590378049576/tenor_35.gif"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**Well {member.name}, you made {ctx.author.name} cry**", color=0x7d76ff)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)

    @commands.command()
    async def highfive(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        picture = ["https://i.imgur.com/gYRdIJy.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814941766674284606/tenor_36.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814941767958528040/tenor_32.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814941769095184424/tenor_28.gif", "https://cdn.discordapp.com/attachments/801520852591181855/814941768545075240/tenor_30.gif"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**{ctx.author.name}, {member.name}... HIGHFIVE!**", color=0x9cff79)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, member:discord.Member, *, reason:str="no reason"):
        if member is None:
            member = ctx.author
        picture = ["punch1", "punch2", "punch3"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**{member.name} you are dead**", color=0xffc585)
        embed.set_image(url="https://i0.wp.com/media2.giphy.com/media/gFYt7JTzRp22k/giphy.gif")
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)

    @commands.command()
    async def av(self, ctx, member:discord.Member =None):
        if member is None:
            member = ctx.author
        embed = discord.Embed(description=f"**{member.name + '´s'} Avatar: **", color=0xffc585)
        embed.set_image(url=f"{member.avatar_url}")
        embed.timestamp=datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def fortnite(self, ctx, member:discord.Member, *, reason:str="no reason", aliases="fn"):
        if member is None:
            member = ctx.author
        picture = ["punch1", "punch2", "punch3"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**{member.name} is gay**", color=0xffc585)
        embed.set_image(url=f"{'https://media.tenor.com/images/5187ae066f8332352ca554484f0bc41f/tenor.gif'}")
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        picture = ["https://memestatic.fjcdn.com/pictures/Press+2+to+see+a+secret+meme_82959a_6424309.jpg", "https://i0.wp.com/memegenerator.net/img/instances/58794075.jpg", "https://media.makeameme.org/created/not-sure-if-z3w2ry.jpg", "https://sfwfun.com/wp-content/uploads/2019/01/best-of-alright-keep-your-secrets-memes-funny-alright-keep-your-secrets-meme-6.jpg", "http://thinkingmeme.com/wp-content/uploads/2019/11/DONT-CLICK-On-These-Top-Secret-Memes-TOP-23-Instagram-Memes-Girls-19.jpg", "https://img.ifunny.co/images/b86e9d6c03ff5048fbd6b1cf6bf6088e212b9725d4016413ca399c451b30990b_1.jpg", "https://ahseeit.com//king-include/uploads/2019/05/59022999_2669054009834712_910993448129094758_n-8262306274.jpg", "https://memeguy.com/photos/images/does-plankton-know-this-secret-311037.png", "https://pbs.twimg.com/media/D9C6B4JXsAIP-sP.jpg", "https://theblackandwhite.net/wp-content/uploads/2020/05/Severin-Snape.png", "https://i.imgflip.com/2/1youob.jpg", "https://i.pinimg.com/originals/f6/28/05/f62805b290c892acc339f11545311a1a.jpg", "https://memegenerator.net/img/instances/64148959/top-secret-classfied.jpg", "https://i.redd.it/c8m27n69vbz21.jpg", "https://pbs.twimg.com/media/D10b4aAXcAAKrJc.jpg", "https://images7.memedroid.com/images/UPLOADED825/5f15d1454436a.jpeg", "https://images7.memedroid.com/images/UPLOADED825/5f15d1454436a.jpeg", "https://i.redd.it/zyz6mdrd54p41.jpg", "https://ih1.redbubble.net/image.704588888.0196/flat,750x,075,f-pad,750x1000,f8f8f8.u5.jpg", "https://i.pinimg.com/originals/cb/83/e7/cb83e77119f134c5b2b5df6cc7c460a1.png", "https://de.meming.world/images/de/thumb/f/fc/Professional_Retard_meme_1.jpg/240px-Professional_Retard_meme_1.jpg", "https://img.buzzfeed.com/buzzfeed-static/static/2018-03/28/12/campaign_images/buzzfeed-prod-web-01/the-newest-spongebob-meme-is-spongebob-naked-and--2-14135-1522254064-8_dblbig.jpg", "https://i.kym-cdn.com/photos/images/newsfeed/001/555/865/166.jpg", "https://i.kym-cdn.com/photos/images/newsfeed/001/555/865/166.jpg", "https://i.redd.it/wwonhh6yypz51.jpg", "https://de.1jux.net/scale_images/697516_b.jpg", "https://de.meming.world/images/de/thumb/7/7d/Mocking_SpongeBob_meme_4.jpg/240px-Mocking_SpongeBob_meme_4.jpg", "https://i.pinimg.com/originals/67/1b/d2/671bd2974f8e23c68af612bc5a4d7d0d.jpg", "https://static.wikia.nocookie.net/spongebob/images/7/7e/SB_at_the_wheel_meme.jpg", "https://i.pinimg.com/564x/af/74/fa/af74fab75dd71e37fadfa06af8d73eb4.jpg", "https://i.pinimg.com/736x/73/94/d8/7394d871dc665b899ed7adab3a847770.jpg", "https://ahseeit.com/german/king-include/uploads/2020/10/thumb_118186279_341796133511217_897759791230183700_n-3778466139.jpg", "https://ahseeit.com/german/king-include/uploads/2020/10/thumb_118186279_341796133511217_897759791230183700_n-3778466139.jpg", "https://memegenerator.net/img/instances/65786053/user-sexylady69-traue-keinem-profilbild-auf-facebook-.jpg", "https://media.makeameme.org/created/dieser-moment-wenn-d9gnqk.jpg", "https://www.todaysparent.com/wp-content/uploads/2017/06/when-your-kid-becomes-a-meme.jpg", "https://images.hindustantimes.com/rf/image_size_630x354/HT/p2/2020/10/26/Pictures/_1b8238d2-1749-11eb-8018-0bdbc3b69c17.jpg", "https://www.echobot.de/sales-blog/wp-content/uploads/Sales-Meme.png", "https://www.bildmachen.net/wp-content/uploads/2019/04/Lehrer-berlin-Meme-800x606.jpg", "https://www.business-punk.com/app/uploads/2019/07/Originalgro%CC%88%C3%9Fe-May-your-days-be-1-2340x1208-c-default.png", "https://ml9j7vuygxxu.i.optimole.com/4P0nY5c-E0MLYNkt/w:auto/h:auto/q:auto/https://www.berkeleypr.com/app/uploads/2018/12/httpswww.pinterest.depin760615824537219158.jpg", "https://static-cdn.arte.tv/cdnp-articles/sites/default/files/styles/gallery_large/public/2018-09/olde-meme-9.png", "https://onlinemarketing.de/wp-content/uploads/2018/07/wlan.jpg", "https://content.umagit.com/sub1/art_img/2019/03/Meme-Monday.jpg", "https://www.bildmachen.net/wp-content/uploads/2019/05/Meme-Creator_1546106420881.jpg", "https://www.br.de/puls/themen/netz/motte-meme-bro-100~_v-img__16__9__m_-4423061158a17f4152aef84861ed0243214ae6e7.jpg", "https://video-images.vice.com/articles/5d9c821120eea30009d69d70/lede/1570541210230-mental-health-memes.png", "https://media1.faz.net/ppmedia/aktuell/3267312477/1.6152307/default/der-erfinder-eines-memes.jpg", "https://irights.info/wp-content/uploads/2016/05/bean-belegfunktion.png", "https://rwrant.co.za/wp-content/uploads/2021/01/2021-Memes-21.jpg", "https://i.imgflip.com/4cg8nv.jpg", "https://media.makeameme.org/created/2020-ends-2021.jpg", "https://i.kym-cdn.com/photos/images/original/001/812/179/a62.jpg", "https://i.dailymail.co.uk/1s/2021/01/08/16/37770406-9126839-People_hve_shared_hilarious_memes_bemoaning_the_start_of_2021_On-a-70_1610122796821.jpg", "https://i.kym-cdn.com/photos/images/original/001/862/341/752.jpg", "https://ahseeit.com//king-include/uploads/2019/05/57186130_577605416068450_1548952475506074216_n-3430992951.jpg", "https://www.albawaba.com/sites/default/files/styles/d08_standard/public/2021-01/ErKWvu5W4AE3sSt_0.jpg", "https://filmdaily.co/wp-content/uploads/2020/07/cleanmeme-lede.jpg", "http://static.demilked.com/wp-content/uploads/2020/06/5ee08c47263e7-funny-jokes-2020-coverimage3.jpg", "https://i.pinimg.com/originals/62/bf/0d/62bf0d6b9ccd73f5e15aad8fa1d6163c.jpg", "https://youngentertainmentmag.com/wp-content/uploads/2018/08/3.png", "https://www.ketovale.com/wp-content/uploads/2017/12/Funny-Keto-memes-1024x536.jpg", "https://2gag5314usvg3k1yhz13gzy4-wpengine.netdna-ssl.com/wp-content/uploads/2019/05/meme3.png", "https://www.everythingmom.com/wp-content/uploads/2020/04/How-Can-You.jpg", "https://st1.latestly.com/wp-content/uploads/2020/01/Funny-memes-on-Valentines-Day.jpg", "https://101blockchains.com/wp-content/uploads/2018/06/the-pressure-bitcoin-funny-meme.jpg", "https://www4.pictures.mabelandmoxie.com/mp/AAqJS-UGtUZl.jpg", "https://img.delicious.com.au/WqbvXLhs/del/2016/06/more-the-merrier-31380-2.jpg", "https://i.pinimg.com/236x/8e/e1/d7/8ee1d7b8d6ee8d10526c736da2d117d2--funny-texts-gag.jpg", "https://media.distractify.com/brand-img/b90yhlA4z/480x252/corona-virus-memes-1583789992354.png", "https://www.nobleromance.com/wp-content/uploads/2019/03/Work-On-Saturday-Memes-3.jpg", "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/screen-shot-2020-04-09-at-12-29-32-pm-1586449781.png", "https://pd-beamliving-cd.beamliving.com/-/media/bu-to-ch/cat-meme-netflix-funny-1000x666.png", "https://taz.de/picture/3968866/948/24754615-1-2-1.jpeg", "https://missy-magazine.de/wp-content/uploads/2020/03/0803-e1585563227901.jpg", "https://missy-magazine.de/wp-content/uploads/2020/03/0803-e1585563227901.jpg", "https://blog.zeta-producer.com/wp-content/uploads/2017/10/hund-meme.jpg", "https://cdn.earlygame.com/uploads/images/_340xAUTO_fit_center-center_none/4878347/cyberpunk-meme-1.jpg", "https://thumbor.forbes.com/thumbor/566x580/https://specials-images.forbesimg.com/imageserve/5e740f3207adf00006db9d14/960x0.jpg", "https://adz.ro/fileadmin/_processed_/5/e/csm_meme1_9e3229f399.jpg", "https://drschwenke.de/wp-content/uploads/2015/09/memes_owner-1.jpg", "https://cdn.discordapp.com/attachments/801252537553649689/815595435049746432/image0.jpg"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**{ctx.author.mention}**",
                                       color=0xffc585)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)

    @commands.command()
    async def gif(self, ctx):
        picture = ["https://media.discordapp.net/attachments/803738637422297108/825323470517829672/image1.gif", "https://media.discordapp.net/attachments/803738637422297108/825323469456801812/image0.gif", "https://media.discordapp.net/attachments/803738637422297108/825117257465331752/image1.gif", "https://media.discordapp.net/attachments/803738637422297108/825117257013264404/image0.gif", "https://media.discordapp.net/attachments/803738637422297108/825117245725474856/image8.gif", "https://media.discordapp.net/attachments/803738637422297108/825117245238673408/image6.gif", "https://media.discordapp.net/attachments/803738637422297108/825117241795805234/image1.gif", "https://media.discordapp.net/attachments/803738637422297108/825117241276235796/image0.gif", "https://media.discordapp.net/attachments/803738637422297108/825067512537677844/image3.gif", "https://media.discordapp.net/attachments/803738637422297108/825067511502209084/image1.gif","https://cdn.discordapp.com/attachments/803738637422297108/807858673200267325/image8.gif", "https://cdn.discordapp.com/attachments/803738637422297108/809118820274929684/a_c88875f761b7f94b1c1c1706698e0918.gif", "https://cdn.discordapp.com/attachments/803738637422297108/809118839589175356/a_48dce7e851aa0344e53eceadfac4d106-1.gif", "https://cdn.discordapp.com/attachments/803738637422297108/809118861253017611/image0-1-1.gif", "https://cdn.discordapp.com/attachments/803738637422297108/809209874747228180/image4.gif", "https://cdn.discordapp.com/attachments/803738637422297108/809209875883098132/image5.gif", "https://media.discordapp.net/attachments/748509258362126377/809794707621150810/a_003bb6cdbc84148fa9fd3f88a66b7abc.gif", "https://media.discordapp.net/attachments/748509258362126377/807698975263948871/Krzst.gif", "https://media.discordapp.net/attachments/748509258362126377/807699000542232596/Krii_1.gif", "https://media.discordapp.net/attachments/748509258362126377/809794752240681030/ezgif-3-70b0a524ac99.gif", "https://media.discordapp.net/attachments/748509258362126377/807698956049580062/image0_7.gif", "https://media.discordapp.net/attachments/748509258362126377/807698929487183892/image0_6.gif", "https://media.discordapp.net/attachments/748509258362126377/806188454941556762/20201205_002234.gif", "https://media.discordapp.net/attachments/748509258362126377/807699023649439764/image2.gif", "https://media.discordapp.net/attachments/788909133000736822/788909266189680690/10.gif", "https://media.discordapp.net/attachments/748509258362126377/793538329076301854/a_fe33256bc762e6f61fc26ec7756ed77a.gif", "https://media.discordapp.net/attachments/608711476219478045/793520865886863380/a_c2b37f0d6d87f0e065a0d6dbb287dac1-1.gif", "https://media.discordapp.net/attachments/748509258362126377/793538554947960852/a_8af28fdd3fecffd2f0cb8539df7cf227.gif", "https://images-ext-2.discordapp.net/external/f-7RLij4YmyZg9fokPQUVjzRRxvQYxEdRzjurDpGxMs/%3Fsize%3D256%26f%3D.gif/https/cdn.discordapp.com/avatars/331483980790497292/a_cfcc96b11bdd5d5b14bfca94ee98b835.gif", "https://cdn.discordapp.com/attachments/803738637422297108/810903253956034600/image0.gif", "https://cdn.discordapp.com/attachments/803738637422297108/810903254635380786/image1.gif", "https://cdn.discordapp.com/attachments/803738637422297108/810903256158175272/image3.gif", "https://cdn.discordapp.com/attachments/803738637422297108/810903256602509332/image4.gif", "https://cdn.discordapp.com/attachments/803738637422297108/810931206279528458/Geantes_Man_106.gif", "https://cdn.discordapp.com/attachments/803738637422297108/810931219595264051/Gif_Trap_3.gif", "https://cdn.discordapp.com/attachments/803738637422297108/810931268673732648/gif609.gif", "https://cdn.discordapp.com/attachments/803738637422297108/810931246313898024/image3.gif", "https://cdn.discordapp.com/attachments/803738637422297108/811010319744892948/image3.gif", "https://cdn.discordapp.com/attachments/803738637422297108/811429275957592104/image0.gif", "https://cdn.discordapp.com/attachments/803738637422297108/811429276943515668/image2.gif", "https://cdn.discordapp.com/attachments/803738637422297108/811429308291219486/image2.gif", "https://cdn.discordapp.com/attachments/803738637422297108/811429310032117810/image7.gif", "https://media.discordapp.net/attachments/748509258362126377/811545296324395039/c6ef2a7a9e4cdb3263fb080d8f9680ad.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812032580542660608/a_55892c7dabbb7e5c5646df6840ad1f86.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118182525272144/image0.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118183435304960/image1.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118183963394069/image2.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118184610103306/image3.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118186035118090/image5.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118186366861322/image6.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118186773577778/image7.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118187076354078/image8.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118312170422282/image1.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118311483080754/image0.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118313291087892/image3.gif", "https://cdn.discordapp.com/attachments/803738637422297108/812118312803893298/image2.gif", "https://cdn.discordapp.com/attachments/803738637422297108/813171787512283158/image0.gif", "https://cdn.discordapp.com/attachments/803738637422297108/813171788162531368/image1.gif", "https://cdn.discordapp.com/attachments/803738637422297108/813619479854317610/image0.gif", "https://cdn.discordapp.com/attachments/803738637422297108/813619480919015524/image4.gif", "https://cdn.discordapp.com/attachments/803738637422297108/813619481708462090/image5.gif", "https://cdn.discordapp.com/attachments/803738637422297108/813619482505117746/image7.gif", "https://cdn.discordapp.com/attachments/803738637422297108/813619482927955998/image8.gif", "https://cdn.discordapp.com/attachments/803738637422297108/813619483322744842/image9.gif", "https://cdn.discordapp.com/attachments/803738637422297108/814418480592977920/image1.gif", "https://cdn.discordapp.com/attachments/803738637422297108/814418482182488074/image3.gif", "https://data.whicdn.com/images/344986513/original.gif", "https://data.whicdn.com/images/346382238/original.gif", "https://data.whicdn.com/images/341347896/original.gif", "https://data.whicdn.com/images/340567277/original.gif", "https://i.pinimg.com/originals/02/36/6f/02366f27a459120b96d033318b743272.gif", "https://i.pinimg.com/originals/f8/48/84/f8488489e9e4c4b3363e7f4728c00f5e.gif", "https://i.pinimg.com/originals/a7/1f/54/a71f54d4d603cf4573c32af851d5a824.gif", "https://data.whicdn.com/images/346479694/original.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423231800508446/image0.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423232366215228/image1.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423232798621746/image2.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423233691746338/image4.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423235049914398/image6.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423235788636180/image8.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423282881757204/image0.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423283846578216/image1.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423284488699924/image2.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423285197406288/image3.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423285775958076/image4.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423286745497620/image5.gif", "https://cdn.discordapp.com/attachments/803738637422297108/815423287319461908/image6.gif", "https://cdn.discordapp.com/attachments/801280640342949899/812040690963841084/39d85cb0ea59d86798aeb83a099ffd39.gif", "https://cdn.discordapp.com/attachments/801280640342949899/812296644481384479/image0.gif", "https://cdn.discordapp.com/attachments/801280640342949899/812598256475439164/4y20cb.gif", "https://cdn.discordapp.com/attachments/801280640342949899/812632277514715166/20210220_150539.gif", "https://cdn.discordapp.com/attachments/801280640342949899/812632278488317962/6tEoAw5175.gif", "https://cdn.discordapp.com/attachments/801280640342949899/812632279544365066/HxkLxzzo6s.gif", "https://cdn.discordapp.com/attachments/801280640342949899/814048688368255025/8f4ad3e8f992ea85c3ba8e977401dd1f.gif", "https://cdn.discordapp.com/attachments/801280640342949899/814048689693130752/original.gif", "https://cdn.discordapp.com/attachments/801280640342949899/814048690389123083/image0-8.gif"]
        ranpunch = random.choice(picture)
        punch1 = embed = discord.Embed(description=f"**{ctx.author.mention}**",
                                       color=0xffc585)
        embed.set_image(url=ranpunch)
        embed.timestamp=datetime.utcnow()
        punch1 = await ctx.send(embed=embed)
    @commands.command()
    async def dice(self, ctx):
        dice = ["Es ist eine 1", "Es ist eine 2", "Es ist eine 3", "Es ist eine 4", "Es ist eine 5", "Es ist eine 6"]
        rannumb = random.choice(dice)
        message = await ctx.send(f'{ctx.author.mention} wirft einen Würfel <a:dice:819039934295834644>')
        await asyncio.sleep(5)
        await message.edit(content=rannumb)
    @commands.command()
    async def ask(self, ctx, message):
        answers = ['Ja', 'Nein', 'Wahrscheinlich', 'Unwahrscheinlich', 'Vielleicht']
        ranans = random.choice(answers)
        message = await ctx.send('Ich versuche deine Frage zu beantworten...')
        await asyncio.sleep(1.2)
        await message.edit(content=f'Die Antwort zu deiner Frage lautet `{ranans}`')

    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, ctx):
        emojis = ("🍎","🍊","🍐","🍋","🍉","🍇","🍓","🍒")
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! :tada:")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! :tada:")
        else:
            await ctx.send(f"{slotmachine} No match, you lost :cry:")
    @commands.command(aliases=['gayrate'])
    async def howgay(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
            percent = range(0, 101)
            rand = random.choice(percent)
            embed = discord.Embed(title='Gay rate', 
                                  description=f'You are {rand}% gay', 
                                  color=0xffc585)
            await ctx.send(embed=embed)
        else:
            percent = range(0, 101)
            rand = random.choice(percent)
            embed = discord.Embed(title='Gay rate', 
                                  description=f'{member.mention} is {rand}% gay', 
                                  color=0xffc585)
            await ctx.send(embed=embed)
    @commands.command()
    async def simprate(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
            percent = range(0, 101)
            rand = random.choice(percent)
            embed = discord.Embed(title='Simp rate', 
                                  description=f'You are {rand}% simp', 
                                  color=0xffc585)
            await ctx.send(embed=embed)
        else:
            percent = range(0, 101)
            rand = random.choice(percent)
            embed = discord.Embed(title='Simp rate', 
                                  description=f'{member.mention} is {rand}% simp', 
                                  color=0xffc585)
            await ctx.send(embed=embed)
    @commands.command()
    async def pp(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
            percent = ['8D', '8=D', '8==D', '8===D', '8====D', '8=====D', '8======D', '8=======D', '8========D', '8=========D', '8==========D', '8===========D', '8============D', '8=============D', '8==============D', '8===============D']
            rand = random.choice(percent)
            embed = discord.Embed(title='pp size', 
                                  description=f'Your pp is:\r\n {rand}', 
                                  color=0xffc585)
            await ctx.send(embed=embed)
        else:
            percent = ['8D', '8=D', '8==D', '8===D', '8====D', '8=====D', '8======D', '8=======D', '8========D', '8=========D', '8==========D', '8===========D', '8============D', '8=============D', '8==============D', '8===============D']
            rand = random.choice(percent)
            embed = discord.Embed(title='pp size', 
                                  description=f'{member.mention}s pp:\r\n {rand}', 
                                  color=0xffc585)
            await ctx.send(embed=embed)









def setup(client):
    client.add_cog(FUN(client))