import discord
from discord.ext import commands
from discord.commands import Option
import config
from config import milk
import database as db
from teams import teams



intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot} is online!')

@bot.slash_command(description="Report winner")
async def report_match(ctx, round:int, winner: str, loser: str):
    winner = winner.upper()
    loser = loser.upper()
    
    await ctx.respond("Reporting match...", ephemeral=True)
    if winner in teams and loser in teams:
        print("Teams found")
    else:
        await ctx.respond("Could not find one of those teams. Check again.")


    # Save the result to a file
    with open("match_results.txt", "a") as f:
        f.write(f"Round {round}: {winner} defeated {loser}\n")

    # Send a confirmation message to the Discord channel
    await ctx.send(f"<@{milk}> \n Match result recorded: {winner} defeated {loser} in round {round}")





bot.run(config.bot_token)