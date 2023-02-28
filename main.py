import discord
from discord.ext import commands
from discord.commands import Option
import config


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





bot.run(config.bot_token)