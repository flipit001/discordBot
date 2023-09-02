# imports 
from dotenv import load_dotenv
from os import getenv
import discord
from discord.ext import commands

# discord setup
intents = discord.Intents.default()
intents.message_content = True
load_dotenv()
TOKEN = getenv("TOKEN")
client = commands.Bot(command_prefix="?", intents=intents)


@client.command()
async def what(ctx):
    await ctx.send("I know ur confused :)")

@client.command()
async def kick(ctx, usr: discord.Member, *, reason: str="get kicked lmao"):
    if str(usr) == "__redex__":
        await ctx.send("you should be ashamed for trying to kick the god")
        return
    try:
        await usr.kick(reason=reason)
        await ctx.send(f"{usr} has been kicked for: {reason}")
    except:
        await ctx.send("sorry bro, I cant't do it for some reason")

# run bot
client.run(TOKEN)
