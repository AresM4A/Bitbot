import discord

import tenorpy
from discord.ext import commands
from dotenv import load_dotenv
from pygelbooru import Gelbooru


load_dotenv()
gelbooru = Gelbooru()

class Cogbooru(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()  # event
    async def on_ready(self):
        print("Module: Gelbooru is ready !")

    @commands.command(name="sfwbooru", aliases=['booru'])  # Commandes
    async def sfwbooru(self, ctx, *,request):
        request1 = request.split(',')
        final_request = list(request1)
        blacklist = ['nude', 'hentai', 'nsfw', 'gangbang', 'creampie', 'yaoi', 'yuri', 'sweatdrop', 'furry', 'ass',
                     'fuck', 'sex', 'cock', 'breast', 'big breast', 'panties', 'loli', 'pussy', 'naked']
        for item in final_request:
            if item in blacklist:
                await ctx.send(f'{ctx.author.name} je ne peux pas répondre à votre requête, en effet, cette dernière contient des mots interdits dans un salon sfw ! Si vous souhaitez utiliser des tags nsfw, veuillez les utiliser la commande: `b!hbooru <tags>`, dans le salon approprié.')
            else:
                result = str(await gelbooru.random_post(tags=request1, exclude_tags=blacklist))
                embed = discord.Embed(colour=ctx.author.colour, timestamp = ctx.message.created_at)
                embed.set_image(url=result)
                embed.set_footer(text="Image provided by Gelbooru.com")
                await ctx.send(embed=embed)


    @sfwbooru.error
    async def sfwbooru_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            blacklist = ['nude', 'hentai', 'nsfw', 'gangbang', 'creampie', 'yaoi', 'yuri', 'sweatdrop', 'furry', 'ass',
                         'fuck', 'sex', 'cock', 'breast', 'big breast', 'panties', 'loli', 'pussy', 'naked']
            result = str(await gelbooru.random_post(tags=["1girl"], exclude_tags=blacklist))
            embed = discord.Embed(colour=ctx.author.colour)
            embed.add_field(name="Il manque un tag !", value=f"Veuillez mettre des tags suivants votre requête.\nExemple d'utilisation: `b![sfwbooru|booru] 1girl, neko`")
            embed.set_image(url=result)
            embed.set_footer(text='Image provided by Gelbooru.com')
            await ctx.send(embed=embed)

    @commands.command(name="nsfwbooru", aliases=['hbooru','hentaibooru'])
    async def nsfwbooru(self, ctx, *,request):
        if ctx.channel.is_nsfw():
            request1 = request.split(',')
            final_request = list(request1)
            blacklist = ['loli', 'furry']

            for item in final_request:
                if item in blacklist:
                    await ctx.send(f"{ctx.author.name} vous utilisez un tag interdit ! Voici la liste de ces derniers: {blacklist}.")
                else:
                    result = str(await gelbooru.random_post(tags=request1, exclude_tags=blacklist))
                    embed = discord.Embed(colour=ctx.author.colour, timestamp = ctx.message.created_at)
                    embed.set_image(url=result)
                    embed.set_footer(text="Image provided by Gelbooru.com")
                    await ctx.send(embed=embed)
        else:
            await ctx.send(f'{ctx.author.name}, vous devez effectuer cette commande dans un salon nsfw !')

    @nsfwbooru.error
    async def nsfwbooru_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            result = str(await gelbooru.random_post(tags=["hentai"], exclude_tags=['loli', 'furry']))
            embed = discord.Embed(colour=ctx.author.colour)
            embed.add_field(name="Il manque un tag !", value=f"Veuillez mettre des tags suivants votre requête.\nExemple d'utilisation: `b![nsfwbooru|hbooru|hentaibooru] 1girl, hentai`")
            embed.set_image(url=result)
            embed.set_footer(text='Image provided by Gelbooru.com')
            await ctx.send(embed=embed)

    @commands.command(name="ricardo", aliases=["bg"])
    async def ricardo(self, ctx):
        t = tenorpy.Tenor()
        gif = t.random("ricardo")
        embed = discord.Embed(colour=ctx.author.colour)
        embed.set_image(url=gif)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Cogbooru(client))