import discord
from discord.ext import commands
import os

TOKEN = os.environ['DISCORD_BOT_TOKEN']

#コマンドフレームワーク
command_prefix = '/'
#helpコマンド有
bot = commands.Bot(command_prefix=command_prefix)

#helpコマンド無
#bot = commands.Bot(command_prefix=command_prefix,help_command=None)
#bot.remove_command('help')


# スタートアップ時の動作
@bot.event
async def on_ready():
    #Terminal
    print('Login Successful')
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)

# ボットからのコマンドは無視する
@bot.event
async def from_bot(ctx):
    if ctx.author.bot:
        return

# ガチャの関数，画像の出力まで行う
# 単発のとき
async def gacha_1():
    return

async def gacha_60():
    return

# 使用者はコマンドとガチャの回数を入力する
@bot.command()
async def gacha(ctx, num="Expect_numbers"):
    # 引数numが十進数字であるか判定
    if not num.isdecimal():
        # 引数numが十進数字でないことを知らせる処理
        return 

    # 以下，numが十進数字であるとき
    num = int(num)
    # 単発か60連のみを許す
    if not (num == 1 or num == 60):
        # 単発か60連のみを許してますよと知らせる処理
        return
    
    # 単発のとき
    if num == 1:
        await gacha_1()
    # 60連のとき
    else:
        await gacha_60()

    await ctx.channel.send("ガチャホンバンモ　キタイシテイマスヨ")
    return

#ボットの起動
bot.run(TOKEN)

