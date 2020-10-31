import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

#コマンドフレームワーク
command_prefix = '/'
#helpコマンド有
bot = commands.Bot(command_prefix=command_prefix)

#helpコマンド無
#bot = commands.Bot(command_prefix=command_prefix,help_command=None)
#bot.remove_command('help')

#スタートアップ時の動作
@bot.event
async def on_ready():
    #Terminal
    print('Login Successful')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

#ボットからのコマンドは無視する
@bot.event
async def from_bot(ctx):
    if ctx.author.bot:
        return

@bot.command(aliases=["t"])
async def test(ctx):
    await ctx.channel.send("hogehoge")
    return

#Startup bot and Connect to Discord Server
bot.run(TOKEN)

