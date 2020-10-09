#bot.py

import asyncio
import datetime
import json
import logging
import os
import random
import sys
import time
import traceback
from itertools import cycle
from pathlib import Path
import aiohttp
import discord
import sqlite3

from discord.utils import find
from discord.ext import commands, tasks
from discord.ext.commands import MissingPermissions, has_permissions
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def get_prefix(client, message):
        with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)

        
        return prefixes[str(message.guild.id)]


#client = commands.Bot(command_prefix = "b!")
Client = discord.Client()
client = commands.Bot(command_prefix = get_prefix)
client.version = 'Alpha - 1.0'
client.remove_command('help')

@client.event
async def on_ready():
        await client.change_presence(status=discord.Status.do_not_disturb ,activity=discord.Game(name="b!help | Serving Humans ~"))
        print('Bot has connected to Discord!')

@client.event
async def on_member_join(member):
        embed = discord.Embed(colour=0x95efcc, description = f'Bienvenue {member.name} sur {member.guild} ! Nous sommes désormais {int(member.guild.member_count)} membres !\nFaites `b!help` pour voir la totalité de mes commandes !')
        embed.set_thumbnail(url=f"{member.guild.icon_url}")
        embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
        embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
        embed.timestamp = datetime.datetime.utcnow()

        await member.create_dm()
        await member.dm_channel.send(embed=embed)


@client.event
async def on_guild_join(guild):
        with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)

        
        prefixes[str(guild.id)] = "b!"

        with open("prefixes.json", "w") as f:
                json.dump(prefixes, f, indent=4)

        prefixes.close()

@client.event
async def on_guild_remove(guild):
        with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)

        
        prefixes.pop(str(guild.id))

        with open("prefixes.json", "w") as f:
                json.dump(prefixes, f, indent=4)

        prefixes.close()


#Les commandes par défauts
@client.command(name="prefix")
@has_permissions(manage_guild=True)
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def prefix(ctx, prefix):
        with open('prefixes.json', 'r') as f:
                prefixes = json.load(f)

        
        prefixes[str(ctx.guild.id)] = prefix

        with open("prefixes.json", "w") as f:
                json.dump(prefixes, f, indent=4)

        await ctx.send(f"Mon préfixe sur ce serveur est désormais {prefix} !")

        prefixes.close()


@prefix.error
async def prefix_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send(f"Veuillez spécifier le nouveau préfixe à mettre.\nExemple d'utilisation: b!prefix >.")

        if isinstance(error, commands.MissingPermissions):
                await ctx.send(f"Vous n'avez pas les permissions requises, {ctx.author.mention} !\nPermissions à avoir: Gérer le serveur.")

        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")


@client.command(aliases=["latency"]) #Commandes
@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
async def ping(ctx): #ctx = context, donc: le channel et la rep à l'auteur
        await ctx.send(f"Pong ! Mon ping est de {round(client.latency * 1000)}ms !")
        await asyncio.sleep(5)

@ping.error
async def ping_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")



@client.event
async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
                await ctx.send("Cette commande n'existe pas.\nFaites: b!help pour avoir la liste complète de mes commandes")




for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
