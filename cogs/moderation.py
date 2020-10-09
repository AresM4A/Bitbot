import os
import traceback
import sys
import discord
import json
import logging
import asyncio
import time
import datetime
import random
import pickle

from pathlib import Path
from discord.ext import commands
from discord.ext.commands import MissingPermissions, has_permissions
from itertools import cycle

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #event
    async def on_ready(self):
            print('Module: Moderation is ready !')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        # This prevents any commands with local handlers being handled here in on_command_error.
            if hasattr(ctx.command, 'on_error'):
                        return
        
            ignored = (commands.CommandNotFound, commands.UserInputError)
        
        # Allows us to check for original exceptions raised and sent to CommandInvokeError.
        # If nothing is found. We keep the exception passed to on_command_error.
            error = getattr(error, 'original', error)
        
        # Anything in ignored will return and prevent anything happening.
            if isinstance(error, ignored):
                        return

            elif isinstance(error, commands.DisabledCommand):
                        return await ctx.send(f'{ctx.command} a été désactivée.')

            elif isinstance(error, commands.NoPrivateMessage):
                        try:
                                return await ctx.author.send(f'{ctx.command} ne peut pas être utilisée dans les messages privés.')
                        except:
                                pass

        # For this error example we check to see where it came from...
            elif isinstance(error, commands.BadArgument):
                        if ctx.command.qualified_name == 'tag list':  # Check if the command being invoked is 'tag list'
                                return await ctx.send('Je ne trouve pas ce membre dans la liste. Réessayer.')

        # All other Errors not returned come here... And we can just print the default TraceBack.
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
                

    @commands.command(name="kick", pass_context=True) #Commandes
    @has_permissions(kick_members=True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def kick(self, ctx, member : discord.Member, *,reason=None): #il va chercher pour le paramètre "membre" un membre défini par "discord" -> est sur le serveur
            if not member:
                        await ctx.send("Cette personne n'existe pas !")
                        pass

            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} a été kick !')

    @kick.error
    async def kick_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("Veuillez mentionner le membre à kick.\nExemple d'utilisation: b!kick @Example#1234.")

            if isinstance(error, commands.MissingPermissions):
                        await ctx.send(f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !\nPermissions requises: Expulser des membres")

            if isinstance(error, commands.CommandOnCooldown):
                        await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name = "ban", pass_context=True)
    @has_permissions(kick_members=True, ban_members=True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def ban(self, ctx, member : discord.Member, *,reason=None): #il va chercher pour le paramètre "membre" un membre défini par "discord" -> est sur le serveur
            if not member:
                        await ctx.send("Cette personne n'existe pas !")
                        pass

            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} a été banni(e) !')

    @ban.error
    async def ban_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("Veuillez mentionner le membre à bannir.\nExemple d'utilisation: b!ban @Example#1234 Too much warns.")

            if isinstance(error, commands.MissingPermissions):
                        await ctx.send(f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !\nPermissions requises: Expulser des membres et Bannir des membres")

            if isinstance(error, commands.CommandOnCooldown):
                        await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="unban", pass_context=True)
    @has_permissions(kick_members=True, ban_members=True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def unban(self, ctx, *,member):
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')
            #ici, le nom et le num de l'utilisateur vont être séparé en au lvl du # (le # sera suppr)
            if not member:
                        await ctx.send("Cette personne n'existe pas !")
                        pass

            for ban_entry in banned_users:
                user = ban_entry.user
                #on crée un tuple avec les parenthèses '^'
                #rappel: dico = {<key>:<def>}
                #tuple = (<value>)
                #list = [<value>, <value>, ...]
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                        await ctx.guild.unban(user)
                        await ctx.send(f"{user.mention} est désormais débanni !")
                        return

    @unban.error
    async def unban_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("Veuillez spécifier le membre à débannir.\nExemple d'utilisation: b!unban Example#1234.")

            if isinstance(error, commands.MissingPermissions):
                        await ctx.send(f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !\nPermissions requises: Expulser des membres et Bannir des membres")

            if isinstance(error, commands.CommandOnCooldown):
                        await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name="clear", aliases=["purge"], pass_context=True)
    @has_permissions(manage_messages = True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def clear(self, ctx, amount : int):
            amount += 1
            await ctx.channel.purge(limit=amount)
            amount -= 1
            await ctx.send(f"{amount} messages supprimés !")

    @clear.error
    async def clear_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("Veuillez spécifier le nombre de messages à supprimer.\nExemple d'utilisation: b!clear 5")

            if isinstance(error, commands.MissingPermissions):
                        await ctx.send(f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !\nPermissions requises: Gérer les messages")

            if isinstance(error, commands.CommandOnCooldown):
                        await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='warn', aliases=['warning', 'avertir'], pass_context=True)
    @has_permissions(manage_messages = True, kick_members = True)
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def warn(self, ctx, member : discord.Member, *,reason=None):
                member_id = str(member.id)
                pseudo = member
                
                with open("warnings.json", 'r') as file:
                        warned = json.load(file)


                if member_id not in warned:
                        warned[str(member_id)] = 0

                warned[str(member_id)] += 1
                
                with open("warnings.json", "w") as file:
                        json.dump(warned, file, indent=4)
                        
                  
                if reason == None:
                        await ctx.send(f"{member.mention} a été averti par {ctx.author.mention} !")
                else:
                        await ctx.send(f"{member.mention} a été averti par {ctx.author.mention} pour la raison suivante: {reason} !")

                with open("warnings.json", "r") as file:
                        warned = json.load(file)



                if warned[str(member_id)] == 3:
                        reason = "Trop d'avertissements"
                        warned[str(member_id)] = 0
                        await member.kick(reason=reason)
                        await ctx.send(f"{pseudo} a été kick car il avait trop d'avertissements !")
                        warned[str(member_id)] = 0
                
                file.close()


    @warn.error
    async def warn_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("Veuillez spécifier le membre à avertir.\nExemple d'utilisation: b!warn @Example Parce que tu spam")

            if isinstance(error, commands.MissingPermissions):
                        await ctx.send(f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !\nPermissions requises: Gérer les messages et expulser les membres.")

            if isinstance(error, commands.CommandOnCooldown):
                        await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")
                
    @commands.command(name='unwarn', pass_context=True)
    @has_permissions(manage_messages = True, kick_members = True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def unwarn(self, ctx, member : discord.Member):
                member_id = str(member.id)
                
                with open("warnings.json", 'r') as file:
                        warned = json.load(file)


                if member_id not in warned:
                        await ctx.send(f"{member.mention} n'a pas de warn !")

                if warned[str(member_id)] == 0:
                        await ctx.send(f"{member.mention} n'a pas de warn !")

                if warned[str(member_id)] > 0:
                        warned[str(member_id)] -= 1
                        with open("warnings.json", "w") as file:
                                json.dump(warned, file, indent=4)
                        
                
                        await ctx.send(f"{ctx.author.mention} a retiré un avertissement à {member.mention} !")

                        with open("warnings.json", "r") as file:
                                warned = json.load(file)

                file.close()


    @unwarn.error
    async def unwarn_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("Veuillez spécifier la personne à qui vous allez retirer un avertissement.\nExemple d'utilisation: b!unwarn @Example")

            if isinstance(error, commands.MissingPermissions):
                        await ctx.send(f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !\nPermissions requises: Gérer les messages et expulser les membres.")

            if isinstance(error, commands.CommandOnCooldown):
                        await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='clearwarn', pass_context=True)
    @has_permissions(manage_messages = True, kick_members = True)
    @commands.cooldown(rate=1, per=3, type=commands.BucketType.user)
    async def clearwarn(self, ctx, member : discord.Member):
                member_id = str(member.id)
                pseudo = member
                
                with open("warnings.json", 'r') as file:
                        warned = json.load(file)


                if member_id not in warned:
                        await ctx.send(f"{member.mention} n'a pas de warn !")
                        pass

                if warned[str(member_id)] == 0:
                        await ctx.send(f"{member.mention} n'a pas de warn !")
                        pass

                if warned[str(member_id)] > 0:
                        warned[str(member_id)] = 0
                        with open("warnings.json", "w") as file:
                                json.dump(warned, file, indent=4)
                        
                
                        await ctx.send(f"{ctx.author.mention} a vidé le casier judiciaire de {member.mention} !")

                file.close()

    @clearwarn.error
    async def clearwarn_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("Veuillez spécifier le membre qui vera son casier judiciaire vidé.\nExemple d'utilisation: b!clearwarn @Example")

            if isinstance(error, commands.MissingPermissions):
                        await ctx.send(f"Vous n'avez pas les droit suffisant pour utiliser cette commande, {ctx.author.mention} !\nPermissions requises: Gérer les messages et expulser les membres.")

            if isinstance(error, commands.CommandOnCooldown):
                        await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")


def setup(client):
        client.add_cog(Moderation(client))
