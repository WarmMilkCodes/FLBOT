import discord
from discord.ext import commands
from discord.commands import Option
import config
import database as db



intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot} is online!')

@bot.slash_command(description="Assigns FL captain roles")
@commands.has_role('FL League Director')
async def assign_captains(ctx):
    guild = ctx.guild
    members = await guild.fetch_members().flatten()

    with open('captains.txt', 'r') as f:
        for line in f:
            print(f"Processing line: {line}")
            team_name, captain_name = line.strip().split(': ', 1)
            for member in members:
                print(f"Member: {member.display_name}")
                if member.display_name.lower() == captain_name.lower():
                    print(f"Found matching member: {member.display_name}")
                    for role in guild.roles:
                        print(f"Role: {role.name}")
                        if role.name == 'FL Captain':
                            await member.add_roles(role)
                            print(f"Assigned FL Captain role to {captain_name} for team {team_name}")


from config import matches


@bot.slash_command(description="Report a match result")
async def report_match(ctx, team1: str, team2: str, winner: str):
    # Check if the command was called by a captain
    if "FL Captain" not in [role.name for role in ctx.author.roles]:
        await ctx.send("You do not have permission to report a match result.")
        return

    # Check if the teams are valid
    if team1 not in [match["team1"] for match in matches] or team2 not in [match["team2"] for match in matches]:
        await ctx.send("Invalid teams.")
        return

    # Find the match
    for match in matches:
        if match["team1"] == team1 and match["team2"] == team2:
            # Update the winner
            match["winner"] = winner
            await ctx.send(f"Match result reported. {winner} has won the match.")
            return

    # If the match wasn't found, send an error message
    await ctx.send("Match not found.")




bot.run(config.bot_token)