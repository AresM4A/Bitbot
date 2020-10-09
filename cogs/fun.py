import discord
import asyncio
import datetime
import random


from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener() #event
    async def on_ready(self):
            print('Module: Fun is ready !')

    @commands.command(aliases=['8ball'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def _8ball(self, ctx, *,question):
        responses = ["Essaye plus tard",
                         "Essaye encore",
                         "Pas d'avis ",
                         "C'est ton destin",
                         "Le sort en est jeté",
                         "Une chance sur deux",
                         "Repose ta question",
                         "D'après moi oui",
                         "C'est certain",
                         "Oui absolument",
                         "Tu peux compter dessus",
                         "Sans aucun doute",
                         "Très probable",
                         "Oui",
                         "C'est bien parti",
                         "C'est non",
                         "Peu probable",
                         "Faut pas rêver",
                         "N'y compte pas",
                         "Impossible",]
        await ctx.send(f'La question était: {question}\nMa réponse est: {random.choice(responses)}')

    @_8ball.error
    async def _8ball_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("Veuillez entrer la question à laquelle je dois répondre.\nExemple d'utilisation: b!8ball Suis-je gentil ?")

            if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='roll', aliases=['dice'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def roll(self, ctx, amount : int):
                amount = amount
                jet = random.randint(0, amount)
                await ctx.send(f'Résultat du jet: {jet}')

    @roll.error
    async def roll_error(self, ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send(f"Veuillez spécifier de combien sera le lancer.\nExemple d'utilisation: b!roll 100.")

            if isinstance(error, commands.CommandOnCooldown):
                await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='hug', aliases=["câlin", "calin"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def hug(self, ctx, member : discord.Member):
            hug_gifs = ['https://i.imgur.com/bidVg3w.gif',
                        'https://66.media.tumblr.com/tumblr_lohrpyqMkT1qlh1s6o1_500.gifv',
                        'https://media3.giphy.com/media/vVA8U5NnXpMXK/giphy.gif?cid=ecf05e4730962a4c0700e3f4363b0c90c5c4402642937443&rid=giphy.gif',
                        'https://media0.giphy.com/media/L5f4Z5JoOKARG/giphy.gif?cid=ecf05e473853b230b285fbc3dcaa2e15542cc652d19a9157&rid=giphy.gif',
                        ]
            chosen_gif = random.choice(hug_gifs)
            embed = discord.Embed(description="This gif is provided by Giphy", color=0x9b59b6, timestamp = datetime.datetime.utcnow())
            embed.set_image(url=chosen_gif)
            await ctx.send(f"**{ctx.author.mention} fait un gros câlin à {member.mention} !**", embed=embed)

    @hug.error
    async def hug_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        hug_gifs = ['https://i.imgur.com/bidVg3w.gif',
                        'https://66.media.tumblr.com/tumblr_lohrpyqMkT1qlh1s6o1_500.gifv',
                        'https://media3.giphy.com/media/vVA8U5NnXpMXK/giphy.gif?cid=ecf05e4730962a4c0700e3f4363b0c90c5c4402642937443&rid=giphy.gif',
                        'https://media0.giphy.com/media/L5f4Z5JoOKARG/giphy.gif?cid=ecf05e473853b230b285fbc3dcaa2e15542cc652d19a9157&rid=giphy.gif',
                        'https://media.giphy.com/media/wSY4wcrHnB0CA/giphy.gif',
                        'https://media1.tenor.com/images/7db5f172665f5a64c1a5ebe0fd4cfec8/tenor.gif',
                        'https://media1.tenor.com/images/4db088cfc73a5ee19968fda53be6b446/tenor.gif'
                        ]
                        chosen_hug = random.choice(hug_gifs)
                        embed = discord.Embed(description="This gif is provided by Giphy & Tenor", color=0x9b59b6, timestamp = datetime.datetime.utcnow())
                        embed.set_image(url=chosen_hug)
                        await ctx.send(f"**Bitbot fait un gros câlin à {ctx.author.mention} !**", embed=embed)

                if isinstance(error, commands.CommandOnCooldown):
                    await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='kiss', aliases=["bisous"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def kiss(self, ctx, member : discord.Member):
            kiss_gifs = ['https://media1.tenor.com/images/4b5d5afd747fe053ed79317628aac106/tenor.gif',
                        'https://media1.tenor.com/images/b8d0152fbe9ecc061f9ad7ff74533396/tenor.gif',
                        'https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif',
                        'https://media1.tenor.com/images/1306732d3351afe642c9a7f6d46f548e/tenor.gif',
                        'https://media1.tenor.com/images/a390476cc2773898ae75090429fb1d3b/tenor.gif',
                        'https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif'
                        ]
            chosen_kiss = random.choice(kiss_gifs)
            embed = discord.Embed(description="This gif is provided by Giphy & Tenor", color=0x9b59b6, timestamp = datetime.datetime.utcnow())
            embed.set_image(url=chosen_kiss)
            await ctx.send(f"**{ctx.author.mention} embrasse langoureusement {member.mention} !**", embed=embed)

    @kiss.error
    async def kiss_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        kiss_gifs = ['https://media1.tenor.com/images/4b5d5afd747fe053ed79317628aac106/tenor.gif',
                        'https://media1.tenor.com/images/b8d0152fbe9ecc061f9ad7ff74533396/tenor.gif',
                        'https://media1.tenor.com/images/f5167c56b1cca2814f9eca99c4f4fab8/tenor.gif',
                        'https://media1.tenor.com/images/1306732d3351afe642c9a7f6d46f548e/tenor.gif',
                        'https://media1.tenor.com/images/a390476cc2773898ae75090429fb1d3b/tenor.gif',
                        'https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif'
                        ]
                        chosen_kiss = random.choice(kiss_gifs)
                        embed = discord.Embed(description="This gif is provided by Giphy & Tenor", color=0x9b59b6, timestamp = datetime.datetime.utcnow())
                        embed.set_image(url=chosen_kiss)
                        await ctx.send(f"**Bitbot embrasse langoureusement {ctx.author.mention} !**", embed=embed)

                if isinstance(error, commands.CommandOnCooldown):
                    await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='slap', aliases=["gifle"])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def slap(self, ctx, member : discord.Member):
                slap_gifs = ['https://media1.tenor.com/images/fb17a25b86d80e55ceb5153f08e79385/tenor.gif',
                             'https://media1.tenor.com/images/bc7636b327387414a7eec9be9c3dc59c/tenor.gif',
                             'https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif',
                             'https://media1.tenor.com/images/89309d227081132425e5931fbbd7f59b/tenor.gif',
                             'https://media1.tenor.com/images/53d180f129f51575a46b6d3f0f5eeeea/tenor.gif',
                             'https://media1.tenor.com/images/477821d58203a6786abea01d8cf1030e/tenor.gif'
                             ]
                chosen_slap = random.choice(slap_gifs)
                embed = discord.Embed(description="This gif is provided by Giphy & Tenor", color=0x9b59b6, timestamp = datetime.datetime.utcnow())
                embed.set_image(url=chosen_slap)
                await ctx.send(f"**{ctx.author.mention} gifle {member.mention} !**", embed=embed)

    @slap.error
    async def slap_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        slap_gifs = ['https://media1.tenor.com/images/fb17a25b86d80e55ceb5153f08e79385/tenor.gif',
                                     'https://media1.tenor.com/images/bc7636b327387414a7eec9be9c3dc59c/tenor.gif',
                                     'https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif',
                                     'https://media1.tenor.com/images/89309d227081132425e5931fbbd7f59b/tenor.gif',
                                     'https://media1.tenor.com/images/53d180f129f51575a46b6d3f0f5eeeea/tenor.gif',
                                     'https://media1.tenor.com/images/477821d58203a6786abea01d8cf1030e/tenor.gif'
                                     ]
                        chosen_slap = random.choice(slap_gifs)
                        embed = discord.Embed(description="This gif is provided by Giphy & Tenor", color=0x9b59b6, timestamp = datetime.datetime.utcnow())
                        embed.set_image(url=chosen_slap)
                        await ctx.send(f"**{ctx.author.mention} gifle BitBot !**", embed=embed)

                if isinstance(error, commands.CommandOnCooldown):
                    await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='pat', aliases=['caresse'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def pat(self, ctx, member : discord.Member):
                pat_gifs = ['https://media1.tenor.com/images/93ccdbf8da129c4fdf8a74a73fb34f17/tenor.gif',
                            'https://media1.tenor.com/images/116fe7ede5b7976920fac3bf8067d42b/tenor.gif',
                            'https://media1.tenor.com/images/1a8e560e8873ce2a48b3dfbbaa7805ec/tenor.gif',
                            'https://media1.tenor.com/images/bf646b7164b76efe82502993ee530c78/tenor.gif',
                            'https://media1.tenor.com/images/220babfd5f8b629cc16399497ed9dd96/tenor.gif',
                            'https://media1.tenor.com/images/63924d378cf9dbd6f78c2927dde89107/tenor.gif',
                            'https://media1.tenor.com/images/bb5608910848ba61808c8f28caf6ec7d/tenor.gif'
                            ]
                chosen_pat = random.choice(pat_gifs)
                embed = discord.Embed(description = 'This gif is provided by Giphy & Tenor', colour = discord.Colour.blurple())
                embed.set_image(url = chosen_pat)
                await ctx.send(f"**{ctx.author.mention} caresse {member.mention} !**", embed=embed)

    @pat.error
    async def pat_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        pat_gifs = ['https://media1.tenor.com/images/93ccdbf8da129c4fdf8a74a73fb34f17/tenor.gif',
                            'https://media1.tenor.com/images/116fe7ede5b7976920fac3bf8067d42b/tenor.gif',
                            'https://media1.tenor.com/images/1a8e560e8873ce2a48b3dfbbaa7805ec/tenor.gif',
                            'https://media1.tenor.com/images/bf646b7164b76efe82502993ee530c78/tenor.gif',
                            'https://media1.tenor.com/images/220babfd5f8b629cc16399497ed9dd96/tenor.gif',
                            'https://media1.tenor.com/images/63924d378cf9dbd6f78c2927dde89107/tenor.gif',
                            'https://media1.tenor.com/images/bb5608910848ba61808c8f28caf6ec7d/tenor.gif'
                            ]

                        chosen_pat = random.choice(pat_gifs)
                        embed = discord.Embed(description = 'This gif is provided by Giphy & Tenor', colour = discord.Colour.blurple())
                        embed.set_image(url = chosen_pat)
                        await ctx.send(f"**Bitbot caresse {ctx.author.mention} !**", embed=embed)

                if isinstance(error, commands.CommandOnCooldown):
                    await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='sad', aliases=['cry', 'depression'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def sad(self, ctx):
                sad_gifs = ['https://media1.tenor.com/images/6088fab756706a4bf141e28fe330a2be/tenor.gif',
                            'https://media1.tenor.com/images/9e49b5a5f97d1a91733f38404eff8303/tenor.gif',
                            'https://media1.tenor.com/images/3caea37ad3d608fc57231050f1d52a4c/tenor.gif',
                            'https://media1.tenor.com/images/9cbeebd1e7cc941e6a3f468bae756547/tenor.gif',
                            'https://media1.tenor.com/images/0436bfc9861b4b57ffffda82d3adad6e/tenor.gif',
                            'https://media1.tenor.com/images/da86bb5b78529c31cf95a3faa49d1274/tenor.gif',
                            ]
                chosen_sad = random.choice(sad_gifs)
                embed = discord.Embed(description = 'This gif is provided by Giphy & Tenor', colour = discord.Colour.blurple())
                embed.set_image(url = chosen_sad)
                await ctx.send(f"**{ctx.author.mention} deprime !**", embed=embed)
    @sad.error
    async def sad_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")

    @commands.command(name='pout', aliases=['boude'])
    @commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
    async def pout(self, ctx, member : discord.Member):
                pout_gifs = ['https://media1.tenor.com/images/d52117b1bbec0fa89baa8095e2c0fe87/tenor.gif',
                            'https://media1.tenor.com/images/834176874a04f82c10b6f0ea6180212c/tenor.gif',
                            'https://media1.tenor.com/images/885cdbb1e6950cefdc981db000079c85/tenor.gif',
                            'https://media1.tenor.com/images/271668b1037633d7f7ae63dc1a1c29f2/tenor.gif',
                            'https://media1.tenor.com/images/e15433a7af99094cc98df27802b8948c/tenor.gif',
                            'https://media1.tenor.com/images/8edb176f0430ed576ad2959760a8e98a/tenor.gif',
                            'https://media1.tenor.com/images/d2057a81fb06a382f95cd57a1166ded6/tenor.gif'
                            ]
                chosen_pout = random.choice(pout_gifs)
                embed = discord.Embed(description = 'This gif is provided by Giphy & Tenor', colour = discord.Colour.blurple())
                embed.set_image(url = chosen_pout)
                await ctx.send(f"**{ctx.author.mention} boude {member.mention} !**", embed=embed)

    @pout.error
    async def pout_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        pout_gifs = ['https://media1.tenor.com/images/d52117b1bbec0fa89baa8095e2c0fe87/tenor.gif',
                            'https://media1.tenor.com/images/834176874a04f82c10b6f0ea6180212c/tenor.gif',
                            'https://media1.tenor.com/images/885cdbb1e6950cefdc981db000079c85/tenor.gif',
                            'https://media1.tenor.com/images/271668b1037633d7f7ae63dc1a1c29f2/tenor.gif',
                            'https://media1.tenor.com/images/e15433a7af99094cc98df27802b8948c/tenor.gif',
                            'https://media1.tenor.com/images/8edb176f0430ed576ad2959760a8e98a/tenor.gif',
                            'https://media1.tenor.com/images/d2057a81fb06a382f95cd57a1166ded6/tenor.gif'
                            ]

                        chosen_pout = random.choice(pout_gifs)
                        embed = discord.Embed(description = 'This gif is provided by Giphy & Tenor', colour = discord.Colour.blurple())
                        embed.set_image(url = chosen_pout)
                        await ctx.send(f"**{ctx.author.mention} boude !**", embed=embed)

                if isinstance(error, commands.CommandOnCooldown):
                    await ctx.send(f"{ctx.author.mention}, du calme ! Cette commande est en recharge !")


def setup(client):
    client.add_cog(Fun(client))
