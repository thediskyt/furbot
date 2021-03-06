import discord

from discord.ext import commands
bot = commands.Bot(command_prefix='=', description='a simple test bot')

@bot.event
async def on_ready():
    activity = discord.Game(name="with tennis balls | =help", type=2)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print("Toothless is ready ^-^")
    print(f"Toothless is currently in {len(bot.guilds)} guilds")
    print('Bot has started successfully')

@bot.command(name="ping", aliases=["latency"], brief="Shows latency from bot!")
async def greet_back_command(ctx):
   await ctx.send(f'bot ping: **{bot.latency:.2f}**ms')


@bot.command(name="invite", aliases=["inv"], brief="Shows the bot's oauth link")
async def greet_back_command(ctx):
    await ctx.send(f"invite link: __**https://discordapp.com/api/oauth2/authorize?client_id=620990340630970425&permissions=8&scope=bot**__")

@bot.command(name="stats", aliases=["statistics"], brief="shows bot statistics.")
async def greet_back_command(ctx):
	embed=discord.Embed(title="Statistics Toothless:", description="Global Bot Statistics", color=0x00ff00)
	embed.add_field(name="Total Guilds", value=len(bot.guilds), inline=False)
	embed.add_field(name="Total users", value=len(bot.users), inline=False)
	embed.add_field(name="More:", value="Coming soon...", inline=False)
	await ctx.send(embed=embed)

@bot.command(name="av", aliases=["avatar"], brief="shows user avatar.")
async def greet_back_command(ctx):
    await ctx.send(f"User avatar of **{(ctx.message.mentions[0].name)}**:\n{(ctx.message.mentions[0].avatar_url)}")

@bot.command()
async def get_id(ctx, member: discord.Member):
  user_id = member.id
  await ctx.send('The user id is %d.' % user_id)

import config

bot.run(config.token)