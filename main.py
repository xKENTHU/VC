import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import keep_alive
import os

Verse1 = commands.Bot("v!")
Verse2 = commands.Bot("v!")
Verse3 = commands.Bot("v!")
Verse4 = commands.Bot("v!")
Verse5 = commands.Bot("v!")


class color:
	BOLD = '\033[1m'
	END = '\033[0m'
	UNDERLINE = '\033[4m'

vcid = int(input("1194070630199476394"))
VerseEncrypt1 = os.getenv("MTE4MzY2ODY5NzcxMDIxOTM3NQ.GfNilG.dK0eOgRlPm09BVdhyQP5HdSYhNgKio8EBosvu8")
VerseEncrypt2 = os.getenv("Mzk3ODg0ODk5ODYxOTg3MzI5.GQX2_R.v3nWAcbR6MJ9YClmYZWbZZb77Q9av9ZmVymaxI")
VerseEncrypt3 = os.getenv("ODczMDQyNTg1NTUwMjEzMTkw.GWifNm.-ZUWLA1XVRvCJBlEbER6Vx8u2hIMPO_np2PBd8")
VerseEncrypt4 = os.getenv("MTA5Nzg0OTU5MDA1MDQ3NjA1Mg.GsYCYW.pfAmXoRy_LN04Kb-X6tn4CyoxCSCfjOxPWE5Q8")
VerseEncrypt5 = os.getenv("Token5")

os.system('clear')
print(f"""██╗░░░██╗███████╗██████╗░░██████╗███████╗
██║░░░██║██╔════╝██╔══██╗██╔════╝██╔════╝
╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░█████╗░░
░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██╔══╝░░
░░╚██╔╝░░███████╗██║░░██║██████╔╝███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝

────────────────────────────────────────────────────""")

print(color.BOLD + color.UNDERLINE + "VOICECORD" + color.END)

print("""
Attempting to kill discord
Logging in...
""")


@Verse1.event
async def on_ready():
	channel = Verse1.get_channel(id=vcid)
	await channel.connect()
	print(f"""
[+] {Verse1.user} connected to vc!""")


@Verse2.event
async def on_ready():
	channel = Verse2.get_channel(id=vcid)
	await channel.connect()
	print(f"""
[+] {Verse2.user} connected to vc!""")


@Verse3.event
async def on_ready():
	channel = Verse3.get_channel(id=vcid)
	await channel.connect()
	print(f"""
[+] {Verse3.user} connected to vc!""")


@Verse4.event
async def on_ready():
	channel = Verse4.get_channel(id=vcid)
	await channel.connect()
	print(f"""
[+] {Verse4.user} connected to vc!""")


@Verse5.event
async def on_ready():
	channel = Verse5.get_channel(id=vcid)
	await channel.connect()
	print(f"""
[+] {Verse5.user} connected to vc!""")

keep_alive.keep_alive()

loop = asyncio.get_event_loop()
loop.create_task(Verse1.start(VerseEncrypt1, bot=False))
loop.create_task(Verse2.start(VerseEncrypt2, bot=False))
loop.create_task(Verse3.start(VerseEncrypt3, bot=False))
loop.create_task(Verse4.start(VerseEncrypt4, bot=False))
loop.create_task(Verse5.start(VerseEncrypt5, bot=False))
loop.run_forever()
