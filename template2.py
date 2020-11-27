import discord
from discord.ext import commands
import os
import numpy as np

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

def pickup_rare(weight):
    rarities=["R","SR","UR"]
    picked_rarity=np.random.choice(rarities,p=weight)

    if picked_rarity=="UR":
        picked_rarity="".join((picked_rarity,"(",pickup_UR(),")"))

    if picked_rarity=="SR":
        picked_rarity="".join((picked_rarity,"(",pickup_SR(),")"))

    if picked_rarity=="R":
        picked_rarity="".join((picked_rarity,"(",pickup_R(),")"))

    return picked_rarity

def pickup_UR():
    ur=["究極系ノーガード戦法","ぶじゅつかの超速加速","楽団長 ドルケストル","-蒼王宮-恩寵天使 ソーン＝ユーリエフ",
        "対消滅ロングレンジライフルHum-Buster","名門サッカー部 イナズマシュート","魂を司る聖天使 ガブリエル","妖炎参謀 月夜叉",
        "機航師弾 フルーク・ツォイク","荒れ狂う天空王 ぶれいずどらごん","祭りの真打ち！打ち上げ花火","おかあさん だ－いすき",
        "連合宇宙軍 強襲制圧型 装甲多脚戦車","祭りの目玉！ドラゴン花火","どこにでもいけるドア",
        "妖軍一統 ゲネラール","連合宇宙軍 シールドブレイカー","恒星間転送装置 Tele-Pass","反導砲 カノーネ・ファイエル""おとうさん あそんであそんで－","ミナ＆ルナ＆レナのバーゲンセール戦争","ハイカラ盟友忍者 -壬生咲みみみ-","＊絢爛ノ美＊ ボラ＆アルヒコ＆アペイロン","-蒼王宮- 聖歌連隊 ミローディア","【デルミン】デビルミント始龍","合体攻撃！ドリーム☆エンジェルズアロー",
        "学園の王者 生徒会執行部","オールレンジアタック","迅雷の科学者 アバカン","連合宇宙軍 サテライトキャノン","全員集合！魔法少女リリカ☆ルルカ","狂愛の二女 ヴァルヴァラ","紅薔薇の暗殺術 クルエルダー","チーちゃんのウワキオシオキ狙撃","創霊の加護 タイオワ","＊真実ノ美＊ ジョバンニ","【デルミン】デビルミント鬼龍パパミン","絶夢の魔女 リベレーション★ルルカ",
        "とある家庭用メカの反乱","運命の女神 エボリューション☆リリカ","革命の旗","深淵より湧き上がるシャドウ","ドリーム☆マジカルスクエア","全天首都防壁 Hum-Sphere LLIK","銀河防衛ロボ Unidoll-2525","祭りの粋！オトコの手筒花火","モノリス Hum-Unknown","神技官 アンジュ・ソレイユ","独災者 アングリフ・ギフト","忘愛の長女 アレクサンドラ","楽団姫 ディーバ","紅薔薇の副団長 アミスター","-蒼王宮-氷冠女王 イデア=N=ユランブルク","ガルガルのピカピカデコ戦車","雷霊の加護 ワキンヤン","ライバル凶刃忍者 -幽々院ゆらら-","-蒼王宮-終焉禁獣 グラナート","背に負いし亡き妻の加護","#夜光犯罪特区 #きてるちゃんライヴ","#夜光犯罪特区 #終夜の俺様賛美会","エナジー缶 100000ml"]

    return np.random.choice(ur)

def pickup_SR():
    sr=["楽団員 サンバール","一撃必殺 ブラストアッパー","操宴軍馬 ベディ－ネン・パンツァー",
        "焼却ロボ Fladoll-4649","ひめたる力の覚醒","聖女の守り手 黒猫リリィ","楽団員 アルプ","-蒼王宮-白翼騎士 ジェニト","樹霊の加護 イシュティニケ",
        "ゲームバズーカ","聖槍ろんぎぬす","連合宇宙軍 フルアーマー機動兵","おにいちゃん ぎゅーってして","ドスブラック★シスコンブラザー",
        "切り裂き魔 ジャック","祭り行列！ 山車燈籠","あこがれのアイドルからの声援","情愛の四女 クララ","紅薔薇の不壊盾 イノセンテ","デジタル堅牢忍具-不可視金蔵-","*振付ノ美* オルケーシス","-蒼王宮-黒滅導師 アカンティラド","【デルミン】エンジェリック.A.破虎",
        "放火魔 スコーピオン","電撃ロボ Eledoll-115","聖女の前衛 ジル・ド・レ","聖女の後衛 銃士レオン","地獄の番犬 ケルベロス","連合宇宙軍 広域電磁波ジャマ－","帝国機神 ケーニヒ・イェーガー","ゼルっちの横流しフルオートライフル","オンエア部下忍者-アニマルチューバーズ-","*伝説ノ美* プロティバラリナ","【デルミン】デビルミント島","#夜光犯罪特区 #やめるちゃんアゲ","エナジー缶 4000ml",
        "看守長 キャバルリー","全翼飛将 グライフ","魔法少女☆ルルカ","科学部の放課後ジッケンタイム","祭りの華！ だんじりガール","拷問館 パウ・ライヒェ","奏愛の三女 エレオノーラ","紅薔薇の生命線 パレンティア","-蒼王宮-翠光騎士 リョーフキー","#夜光犯罪特区 #メビウス目撃情報","魔法少女 レレカ☆ロロカ",
        "魔法少女☆ララカ","祭り開始！ どでかい和太鼓","呪詛包帯"]
    return np.random.choice(sr)

def pickup_R():
    r=["保健室の救急セット","連合宇宙軍 ステルス迷彩","雨霊の加護 ウィネバ","ドリーム☆ミーティア",
       "初級魔法 ふれいむ","初級魔法 ぶりざーど","銀行強盗 デリンジャー",
       "はらぺこゴースト","聖女の親友 修道女マリー","たんじょうび ぷれぜんと","紅薔薇の聖王剣 セルピエンテ","アイちゃんのオススメ防弾パーカー","*支配ノ美* エレンホス","#夜光犯罪特区 #天馬エイワズ","エナジー缶 1000ml",
       "連合宇宙軍 ジャスティスハンマー","きょうせんしの大剣","爆弾魔 バルカン","爆術死鬼 ツクモ","祭りの終わり！満天提灯","崩愛の爆弾 ジ・エラー","レーザー特注忍具 -双天小烏丸-",
       "はらぺこ吸血バット","死献薬 シュタルク・トート",
       "剣道部エースの五月雨突き","千血妖刀 牛鬼村正","はらぺこメイジ","祭りの思い出！ おじいちゃんの祝砲","【デルミン】オニギリクママン",
       "反政府勢力クラッキング Case-171","かぞく みんなで おしゃしん",]
    return np.random.choice(r)


# ガチャの関数
async def turn_rare(ctx):
    result = []
    s_n = " "
    weight=[0.845,0.135,0.020]
    result.append(pickup_rare(weight))
    s_n="\n".join(result)
    await ctx.channel.send(result[0])

async def turn_60rare(ctx):
    result=[]
    s_n = " "
    weight=[0.845,0.135,0.020]
    for _ in range(0,60):
        result.append(pickup_rare(weight))
        s_n="\n".join(result)
    await ctx.channel.send(s_n)

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
        await turn_rare(ctx)
    # 60連のとき
    else:
        await turn_60rare(ctx)

    await ctx.channel.send("ガチャホンバンモ　キタイシテイマスヨ")
    return

#ボットの起動
bot.run(TOKEN)
