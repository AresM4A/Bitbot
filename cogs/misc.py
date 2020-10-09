import discord
import json
import asyncio
import random

from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Miscellaneous(commands.Cog):
	
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #event
    async def on_ready(self):
                print('Module: Miscellaneous is ready !')

    @commands.command(name="members", aliases=['membres'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def members(self, ctx):
                guild = ctx.message.guild
                id = guild
                await ctx.send(f"""Il y a {id.member_count} membres sur votre serveur !""")

    @members.error
    async def members_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="say", aliases=['dire','talk'],pass_context=True)
    @has_permissions(manage_messages=True)
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def say(self, ctx, *,content):
                contenu = content
                await ctx.channel.purge(limit=1)
                await ctx.send(f"{contenu}")

    @say.error
    async def say_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("Veuillez spécifier ce que je dois dire.\nExemple d'utilisation: b!say Hello !")

                if isinstance(error, commands.MissingPermissions):
                        await ctx.send("Vous n'avez pas les permissions suffisantes pour me faire dire quelquechose.\nPermissions Requises: Gérer les messages")

                if isinstance(error, commands.CommandOnCooldown):
                    await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='github', aliases = ['git'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def github(self, ctx):
                link = 'https://github.com/AresM4A/Bitbot'
                await ctx.send(f'Voici le lien de mon github: {link}')

    @github.error
    async def github_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='issues', aliases=['problème'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def issues(self, ctx):
                link = 'https://github.com/AresM4A/Bitbot/issues'
                await ctx.send(f"Vous avez rencontré un ou plusieurs problème avec moi ?!\nVite, expliquez nous ce(s) problème(s) à cet adresse: {link}")
    @issues.error
    async def issues_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name = 'avatar')
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def avatar(self, ctx, member : discord.Member):
                avatar_link = member.avatar_url
                embed = discord.Embed(colour = member.color, title = '')
                embed.set_image(url = avatar_link)
                await ctx.send(f"Voici l'avatar de {member.mention}", embed = embed)

    @avatar.error
    async def avatar_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        avatar_link = ctx.author.avatar_url
                        embed = discord.Embed(colour = ctx.author.color, title = '')
                        embed.set_image(url = avatar_link)
                        await ctx.send(f"Voici l'avatar de {ctx.author.mention}", embed = embed)

                if isinstance(error, commands.CommandOnCooldown):
                    await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='userinfo', aliases = ["user"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def userinfo(self, ctx, member : discord.Member):
                member_id = str(member.id)

                with open("warnings.json","r") as file:
                        warned = json.load(file)

                if member_id not in warned:
                        warnings_number = 0

                else:
                        warnings_number = warned[member_id]

                if member.bot == False:
                        lol = "Non, ce n'est pas un bot"
                else:
                        lol = "Oui, c'est un bot"

                if member.nick == None:
                        pseudo = 'Aucun'
                else:
                        pseudo = member.nick

                roles = [role for role in member.roles]
                
                info = discord.Embed(colour = member.color, timestamp = ctx.message.created_at)
                info.set_author(name = f"Informations sur le membre - {member}")
                info.set_thumbnail(url=member.avatar_url)
                info.set_footer(text=f'Demandées par {ctx.author}', icon_url=ctx.author.avatar_url)

                info.add_field(name="Id:", value=member.id, inline=False)
                info.add_field(name="Nom:", value=member.display_name, inline=False)
                info.add_field(name="Pseudo sur le serveur:", value=f"{pseudo}", inline=False)
                info.add_field(name="Nom du Serveur:", value=member.guild, inline=False)
                info.add_field(name="Compte créé le:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
                info.add_field(name="A rejoind le serveur le:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
                info.add_field(name="Rôle principal:", value=member.top_role.mention, inline=False)
                info.add_field(name=f"Roles ({len(roles)})", value=" ".join(role.mention for role in roles), inline=False)
                info.add_field(name=f"Nombre d'avertissement", value=f"{warnings_number}")
                info.add_field(name="Bot ?", value=f"{lol}", inline=False)

                await ctx.send(embed = info)
                file.close()

    @userinfo.error
    async def userinfo_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("Veuillez mentionner la personne dont vous souhaitez voir les informations.\nSi vous souhaitez voir vos propres informations, faites: b!me")

                if isinstance(error, commands.CommandOnCooldown):
                    await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='me')
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def me(self, ctx):
                author = ctx.author

                author_id = str(author.id)

                with open("warnings.json","r") as file:
                        warned = json.load(file)

                if author_id not in warned:
                        warnings_number = 0

                else:
                        warnings_number = warned[author_id]

                if author.bot == False:
                        lol = "Non, je ne suis pas un bot"
                else:
                        lol = "Oui, je suis un bot"

                if author.nick == None:
                        pseudo = 'Aucun'
                else:
                        pseudo = author.nick

                roles = [role for role in author.roles]
                
                info = discord.Embed(colour = author.color, timestamp = ctx.message.created_at)
                info.set_author(name = f"Informations sur le membre - {author}")
                info.set_thumbnail(url=author.avatar_url)
                info.set_footer(text=f'Demandées par {ctx.author}', icon_url=ctx.author.avatar_url)

                info.add_field(name="Id:", value=author.id, inline=False)
                info.add_field(name="Nom:", value=author.name, inline=False)
                info.add_field(name="Pseudo sur le serveur:", value=f"{pseudo}", inline=False)
                info.add_field(name="Nom du Serveur:", value=author.guild, inline=False)
                info.add_field(name="Compte créé le:", value=author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
                info.add_field(name="A rejoind le serveur le:", value=author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=False)
                info.add_field(name="Rôle principal:", value=author.top_role.mention, inline=False)
                info.add_field(name=f"Roles ({len(roles)})", value=" ".join(role.mention for role in roles), inline=False)
                info.add_field(name=f"Nombre d'avertissement", value=f"{warnings_number}")
                info.add_field(name="Bot ?", value=f"{lol}", inline=False)

                await ctx.send(embed = info)
                file.close()

    @me.error
    async def me_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='randomchoose', aliases=["randchoose", "rchoose"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def randomchoose(self, ctx, *,content):
        choose = list(content.split('|'))
        if len(list(choose)) == 1:
            await ctx.send(f"{ctx.author.name}, veuillez me donner deux choses au moins parmis lesquels choisir !\nExemple d'utilisation: `b![randomchoose|randchoose|rchoose] 1|2`")
        else:
            randchoose = random.choice(choose)
            await ctx.send(f"À votre place, je choisirai: {randchoose}.")

    @randomchoose.error
    async def randomchoose_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.name}, vous devez me donner les choses avec lesquels vous hésitez !\nExemple d'utilisation: `b![randomchoose|randchoose|rchoose] 1|2`")
        if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")


def setup(client):
        client.add_cog(Miscellaneous(client))
