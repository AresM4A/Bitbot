import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #event
    async def on_ready(self):
            print('Module: Help is ready !')


    @commands.command(name="_help", aliases=['aide','help', 'h'], pass_context=True)
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def _help(self, ctx):
            author = ctx.message.author

            debut = discord.Embed(colour = discord.Colour.purple(), title = 'Listes des Commandes de bitbot')
            debut.set_author(name = 'Créateur du bot: AresM4A', icon_url='https://images-ext-2.discordapp.net/external/NFEIXIORZ1bqXNTbSqaZRAM-IXJd4aPlXYvz0EWwbkk/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/352369868227739650/8de517064c52c5de6408967d4d7c3641.webp')
            debut.add_field(name = 'Infos', value='Dans toute cette liste, le préfixe utilisé est le préfixe par défaut du bot: "b!". Vous le remplacerez donc selon le préfixe de votre serveur.\nQuand vous voyez un exemple de commande ressemblant à ça: b![test|commande], cela signifie que dans les crochets se trouvent les différents noms pour cette commande.\nLes Cooldowns de chaque commande est fixé à 5 seconde après son utilisation. Les seuls commandes qui échappent à cette règle sont: ban, kick et warn. Ces dernières sont fixées à 1.5 secondes de cooldwons.', inline=False)

            fun = discord.Embed(colour = discord.Colour.blue(), title = 'Fun')
            fun.add_field(name='8ball', value='Posez-moi une question et je vous donnerai mon avis vis-à-vis de celle-ci.\nUtilisation: b!8ball <question>', inline=False)
            fun.add_field(name='roll', value='Je lance un dés pour vous.\nUtilisation: b![roll|dice] <amount>', inline=False)
            fun.add_field(name='avatar', value = "Je vous donne l'avatar du membre que vous voulez. Si vous ne mentionnez personne, je vous donne votre propre avatar.\nUtilisation: b!avatar <mention>", inline = False)
            fun.add_field(name='hug', value="Permet de câliner une personne. Si tu n'as personne à câliner, je peux toujours t'en proposer un !\nUtilisation: b![hug|câlin] <mention>", inline=False)
            fun.add_field(name='kiss', value = "Permet d'embrasser une personne. Si tu n'as personne à embrasser, on pourra toujours s'arranger ~\nUtilisation: b![kiss|bisous] <mention>", inline=False)
            fun.add_field(name='slap', value="Permet de gifler quelqu'un ! Et... tu sais... Si tu n'as personne à gifler... Je me porte volontaire !\nUtilisation: b![slap|gifle] <mention>", inline = False)
            fun.add_field(name='pat', value="Permet de caresser la tête de quelqu'un. Si tu ne peux en donner à personne... Je peux toujours t'en faire !\nUtilisation: b![pat|caresse] <mention>", inline=False)
            fun.add_field(name='sad', value="Permet de montrer aux autres votre dépression.\nUtilisation: b![sad|cry|depression]", inline=False)
            fun.add_field(name='pout', value='Permet de bouder des personnes.\nUtilisation: b![pout|boude] <mention>')
            fun.add_field(name='randomchoose', value='Je décide pour vous entre deux options.\nUtilisation: b![randomchoose|randchoose|rchoose] choix 1|choix 2')

            moderation = discord.Embed(colour = discord.Colour.red(), title='Modération')
            moderation.add_field(name='prefix', value="Vous permet de changer mon préfixe sur ce serveur.\nPermission requise: Gérer le serveur\nUtilisation: b!prefix <nouveau prefix>", inline=False)
            moderation.add_field(name='kick', value="Vous permet d'expulser quelqu'un.\nPermission requise: Expulser des membres\nUtilisation: b!kick {mention} <raison>", inline=False)
            moderation.add_field(name='ban', value="Vous permet de bannir quelqu'un.\nPermissions requises: Expulser des membres et bannir de membres\nUtilisation: b!ban {mention} <raison>", inline=False)
            moderation.add_field(name='unban', value="Vous permet de débannir quelqu'un.\nPermissions requises: Expulser des membres et bannir de membres\nUtilisation: b!unban <mention>", inline=False)
            moderation.add_field(name='clear', value="Vous permet de supprimer un nombre défini de messages.\nPermission requise: Gérer les messages\nUtilisation: b!clear <nombre de messages à supprimer>", inline=False)
            moderation.add_field(name='warn', value="Vous permet d'avertir un membre. Après trois avertissement, le membre est automatiquement expulsé.\nUtilisation: b![warn|warning[avertir] {mention} <raison>", inline=False)
            moderation.add_field(name='unwarn', value="Vous permet de retirer un avertissement à un membre.\nUtilisation: b!unwarn {mention}", inline=False)
            moderation.add_field(name='clearwarn', value="Vous permet de supprimer le casier judiciaire d'un membre.\nUtilisation: b!clearwarn {mention}", inline=False)

            #à faire: commande b!nick (changer le pseudo)
            #finir la parti "Fun"
            #finir la parti NSFW + l'aide de cette partie
            #créer une économie et voir de ce que font les autres bots '^'
            #custom "on join role system"

            diverses = discord.Embed(colour = discord.Colour.orange(), title = 'Diverses')
            diverses.add_field(name = 'help', value = 'Affiche cette aide.\nUtilisation: b![h|help]', inline=False)
            diverses.add_field(name='ping', value ='Je vous renvoie un pong ainsi que ma latence.\nUtilisation: b![ping|latency]', inline=False)
            diverses.add_field(name='members', value='Je vous donne le nombre de membres se trouvant dans le serveur\nUtilisation: b![members|membres]', inline=False)
            diverses.add_field(name='say', value='Dictez-moi ce que je dois dire, maître ~\nPermissions requises: Gérer les messages\nUtilisation: b![say|talk|dire] <chose à me faire dire>', inline=False)
            diverses.add_field(name='github', value= 'Vous donne le lien de mon github.\nUtilisation: b![github|git]', inline = False)
            diverses.add_field(name='issues', value='Si vous rencontrez un ou plusieurs problèmes avec moi, effectuez cette commande !\nUtilisation: b![issues|problème]', inline=False)
            diverses.add_field(name='userinfo', value='Je vous donne toutes les informations concernant un membre du serveur.\nUtilisation: b![userinfo|user]', inline = False)
            diverses.add_field(name='me', value='Donne toute les informations vous concernant.\nUtilisation: b!me', inline = False)


            nsfw = discord.Embed(colour=discord.Colour.magenta(), title="Nsfw")
            nsfw.add_field(name="fuck", value="Cela vous permet de copuler avec un autre membre de votre espèce. Si personne ne veux le pratiquer avec vous, je suis aussi un sex-bot !\nUtilisation: b!fuck <mention>", inline=False)
            nsfw.add_field(name="furry", value="Cela vous envoie une image aléatoire de porn-furry venant de ma base de donnée.\nUtilisation: b!furry", inline=False)
            nsfw.add_field(name='nsfwbooru', value='Cela vous envoie une image aléatoire venant du site Gelbooru.com. Votre commande peut contenir des tags dit "nsfw".\nUtilisation: b![hentaibooru|hbooru] <tag(s)>\nExemple: b!hbooru nude, 1girl', inline=False)

            img = discord.Embed(colour=discord.Colour.green(), title='Images et gifs.')
            img.add_field(name="sfwbooru", value='Cela vous envoie une image aléatoire du site Gelbooru.com. Les tags dit "nsfw" sont desactivés pour cette commande.\nUtilisation: b![sfwbooru|booru] <tag(s)>\nExemple: b!booru 1girl', inline=False)
            img.add_field(name="nsfwbooru", value='Cela vous envoie une image aléatoire du site Gelbooru.com. Les tags dit "nsfw" sont activés pour cette commande.\nUtilisation: b![nsfwbooru|hbooru|hentaibooru] <tag(s)>\nExemple: b!hbooru 1girl, breasts', inline=False)
            
            await author.create_dm()
            await ctx.send(f'Je vous ai envoyé la liste complète de mes commandes en messages privé, {author.mention} !')
            await author.dm_channel.send(embed=debut)
            await author.dm_channel.send(embed=fun)
            await author.dm_channel.send(embed=img)
            await author.dm_channel.send(embed=moderation)
            await author.dm_channel.send(embed=nsfw)
            await author.dm_channel.send(embed=diverses)

    @_help.error
    async def _help_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

                

def setup(client):
        client.add_cog(Help(client))
