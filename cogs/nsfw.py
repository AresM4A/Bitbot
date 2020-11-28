#Depreciated

import os
import discord
import json
import logging
import asyncio
import time
import datetime
import random

from pathlib import Path
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Nsfw(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Module: Nsfw is ready !')

    @commands.command(name = 'fuck')
    async def fuck(self, ctx, member : discord.Member):
        if ctx.channel.is_nsfw():
            fuck_gifs = ['https://i.imgur.com/IH737EB.gif',
                         'https://thumb-p3.xhcdn.com/a/XuN1zANuNMMCkY_NyWtVUg/000/199/259/043_1000.gif',
                         'http://img1.joyreactor.com/pics/post/nothing-but-porn-xxx-files-fandoms-gif-3602461.gif',
                         'http://porngif.org/wp-content/uploads/2014/01/3583.gif',
                         ]
            chosen_fuck = random.choice(fuck_gifs)
            embed = discord.Embed(color=0xe74c3c, timestamp = datetime.datetime.utcnow())
            embed.set_image(url=chosen_fuck)
            await ctx.send(f"**{ctx.author.mention} baise avec {member.mention} !**", embed = embed)
        else:
            await ctx.send(f'Tu ne peux pas utiliser mes commandes NSFW dans ce salon {ctx.author.mention} !')

    @fuck.error
    async def fuck_error(self, ctx, error):
        if ctx.channel.is_nsfw():
            if isinstance(error, commands.MissingRequiredArgument):
                fuck_gifs = ['https://i.imgur.com/IH737EB.gif',
                             'https://thumb-p3.xhcdn.com/a/XuN1zANuNMMCkY_NyWtVUg/000/199/259/043_1000.gif',
                             'http://img1.joyreactor.com/pics/post/nothing-but-porn-xxx-files-fandoms-gif-3602461.gif',
                             'http://porngif.org/wp-content/uploads/2014/01/3583.gif',
                             ]
                chosen_fuck = random.choice(fuck_gifs)
                embed = discord.Embed(color=0xe74c3c, timestamp = datetime.datetime.utcnow())
                embed.set_image(url=chosen_fuck)
                await ctx.send(f"**Bitbot baise avec {ctx.author.mention} !**", embed = embed)
            
        else:
            await ctx.send(f'Tu ne peux pas utiliser mes commandes NSFW dans ce salon {ctx.author.mention} !')

    @commands.command(name='furry', aliases=["heretic"])
    async def furry(self, ctx):
        if ctx.channel.is_nsfw():
            crusader_gifs = ['https://media1.tenor.com/images/60556e1cc2c9129a61a015e37415e110/tenor.gif',
                         'https://media1.tenor.com/images/9968249f147708559b0be55142cf452b/tenor.gif',
                         'https://media1.tenor.com/images/f53ea229e2108e693091c7ad1108dfe1/tenor.gif',
                         'https://media1.tenor.com/images/b61c80884c6794f54cae202eac24a1ab/tenor.gif',
                         'https://media1.tenor.com/images/9ffafcf364acfe086eb5ab6f69009e07/tenor.gif',
                         'https://media1.tenor.com/images/27306dbb02ac2fc28ef5e9c0075a8cc5/tenor.gif?itemid=17800315',
                         'https://media1.tenor.com/images/3ef771f8f9e3cf599d970339e3a628e0/tenor.gif?itemid=17792300',
                         'https://media1.tenor.com/images/45322ff7861a5edd0598ed4c54ac8f9e/tenor.gif?itemid=16453280',
                         'https://media1.tenor.com/images/763de0265f729533036905536ae55e8a/tenor.gif?itemid=14798873',
                         'https://media1.tenor.com/images/a6476ee3f6dd1e695b0f1d8db8c2257a/tenor.gif?itemid=14822153',
                         'https://media1.tenor.com/images/5535789a8e23da8b8502fe1b4b65932a/tenor.gif?itemid=14927695',
                            ]
            chosen_crusader = random.choice(crusader_gifs)
            embed = discord.Embed(color=0xe74c3c, timestamp = datetime.datetime.utcnow())
            embed.set_image(url=chosen_crusader)
            reason = str(f"{ctx.author} était un hérétique")

            invite = await ctx.channel.create_invite()

            mp = discord.Embed(color=0xe74c3c, timestamp = datetime.datetime.utcnow())
            mp.add_field(name=f"Vous avez été expulsé(e) du server {ctx.author.guild}!", value=f"{ctx.author}, vous avez été expulsé(e) car vous avez fait preuve d'hérésie. Effectivement vous avez voulu voir du porn de furry !", inline=False)
            mp.add_field(name=f"L'invitation:", value=f"{invite}")

            await ctx.author.create_dm()
            await ctx.author.dm_channel.send(embed=mp)
            await ctx.author.kick(reason=reason)
            await ctx.send(f"{ctx.author.mention} a été expulsé pour hérésie !", embed=embed)

        else:
            await ctx.send(f'Tu ne peux pas utiliser mes commandes NSFW dans ce salon {ctx.author.mention} !')

#def setup(client):
    #client.add_cog(Nsfw(client))
