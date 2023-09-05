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
THEGOD = getenv("THEGOD")
client = commands.Bot(command_prefix="?", intents=intents)

# commands
@client.command()
async def what(ctx):
    await ctx.send("I know ur confused :)")

@client.command()
async def kick(ctx, usr: discord.Member, *, reason: str="get kicked lmao"):
    if str(usr) == THEGOD:
        await ctx.send("you should be ashamed for trying to kick the god")
        return
    try:
        await usr.kick(reason=reason)
        await ctx.send(f"{usr} has been kicked for: {reason}")
    except commands.errors.CommandInvokeError:
        await ctx.send("sorry bro, I can't do it for some reason")

@client.command()
async def ban(ctx, usr: discord.Member, *, reason: str="get banned lmao"):
    if str(usr) == THEGOD:
        await ctx.send("you should be ashamed for trying to ban the god")
        return
    try:
        await usr.kick(reason=reason)
        await ctx.send(f"{usr} has been banned for: {reason}")
    except commands.errors.CommandInvokeError:
        await ctx.send("sorry bro, I can't do it for some reason")

@client.command()
async def troll_kid(ctx, user: discord.User, *, msg: str):
    # print(ctx.message.author, "__redex__")
    if str(ctx.message.author) == THEGOD:
        await user.send(msg)
        await ctx.message.delete()

    else:
        await ctx.send("hell no")


# run bot
client.run(TOKEN)
