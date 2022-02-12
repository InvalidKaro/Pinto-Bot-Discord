from discord.ext import commands
import logging
import discord
import json
import asyncio
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

log = logging.getLogger(__name__)


def json_open():
    with open('reaction_roles.json', 'r', encoding='utf-8') as f:
        reaction_roles = json.load(f)
        return reaction_roles


class Reactions(commands.Cog):
    """
    This instance handles all reaction role events.
    """

    def __init__(self, client):
        super().__init__()
        self.client = client

    @commands.command()
    async def help_reaction(self, ctx):
        embed=discord.Embed(color=0xffc585)
        embed.add_field(name="Add ReactionRole", value=f"`p!reactionss` <role> <MsgID> <:emote:>", inline=False)
        embed.set_footer(text="Pinto Bot - Developed by Karo")
        embed.timestamp=datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(aliases=["reactionss"])
    async def set_reaction(self, ctx, role: discord.Role = None, msg: discord.Message = None, emoji=None):
        """Set up a reaction role message."""
        reaction_roles = json_open()  # JSFON-Datei wird geöffnet

        try:
            role_dict = reaction_roles[str(msg.id)]
        except:
            role_dict = {}

        if role is None:
            await ctx.send("**Du musst erst eine Rolle definieren**\n Versuche `p!reactionss @role` und mache dann mit dem Rest weiter")
            return

        if msg is None:
            await ctx.send("**Du musst erst eine Msg ID angeben.**\n Versuche `p!reactionss @role` und mache dann mit dem Rest weiter")
            return

        if emoji is None:
            await ctx.send("**Jetzt nurnoch das gewünschte Emoticon (Beachte, dass ich auf dem Ursprungsserver des Emotes sein muss)**\n Versuche `p!reactionss @role messageID :Emote:`.")
            return

        role_dict[emoji] = role.id
        reaction_roles[str(msg.id)] = role_dict

        if role is not None and msg is not None and emoji is not None:
            await msg.add_reaction(emoji)


            with open('reaction_roles.json', 'w', encoding='utf-8') as f:
                json.dump(reaction_roles, f, indent=2, ensure_ascii=False)

            await ctx.channel.send("**Reaction wurde gesetzt**")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.user_id == 809824051773177917:  #Bekommt hier keine Rollen, ist aber nötig
            return
        reaction_roles = json_open()  # Öffnet JSON
        if str(payload.message_id) in list(reaction_roles.keys()):  # Nachricht passt?
            role_dict = reaction_roles[str(payload.message_id)]  # Reaktion passt zur Nachricht?
            if payload.emoji.name in list(role_dict.keys()):
                role_id = role_dict[payload.emoji.name]
                guild = self.client.get_guild(payload.guild_id)
                role = guild.get_role(role_id)
                await guild.get_member(payload.user_id).add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.user_id == 809824051773177917:
            return
        reaction_roles = json_open()
        if str(payload.message_id) in list(reaction_roles.keys()):
            role_dict = reaction_roles[str(payload.message_id)]
            if payload.emoji.name in list(role_dict.keys()):
                role_id = role_dict[payload.emoji.name]
                guild = self.client.get_guild(payload.guild_id)
                role = guild.get_role(role_id)
                await guild.get_member(payload.user_id).remove_roles(role)


def setup(client):
    client.add_cog(Reactions(client))
    log.info("Reactionss loaded.")