import discord
from discord.ext import commands
from discord import app_commands
import requests
import aiohttp
import subprocess
import os
import asyncio
import shlex
import urllib.parse
from dotenv import load_dotenv
import signal

load_dotenv()
token = os.getenv("token")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash command(s).")
     except Exception as e:
     print(f"Error syncing commands: {e}")
    print(f"Bot is online as {bot.user}")

    async def Welcome(Interaction: discord.interaction):
        await interaction.response.send_message("Hello from MoonSec @ https://github.com/Moon0day/<3")
        
    welcome_command = app_commands.Command(
        name="Welcome message"
        description="gives u a Welcome message"
        callback=welcome    
    )
    welcome_command.default_permission = discord.Permissions(administrator=True)

async def iplookup(interaction: discord.Interaction, ip: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://ip-api.com/json/{ip}") as resp:
            if resp.status != 200:
                await interaction.response.send_message("Failed to fetch IP information.", ephemeral=True)
                return
          data = await resp.json()
            if data['status'] != 'success':
                await interaction.response.send_message("Invalid IP address or API error.", ephemeral=True)
                return
            embed = discord.Embed(title="IP Lookup Result", color=discord.Color.blue())
            embed.add_field(name="IP", value=data.get("query", "N/A"), inline=True)
            embed.add_field(name="Country", value=data.get("country", "N/A"), inline=True)
            embed.add_field(name="Region", value=data.get("regionName", "N/A"), inline=True)
            embed.add_field(name="City", value=data.get("city", "N/A"), inline=True)
            embed.add_field(name="ZIP", value=data.get("zip", "N/A"), inline=True)
            embed.add_field(name="ISP", value=data.get("isp", "N/A"), inline=True)
            embed.add_field(name="Org", value=data.get("org", "N/A"), inline=True)
            embed.add_field(name="ASN", value=data.get("as", "N/A"), inline=True)
            embed.set_footer(text="Data from ip-api.com")
            await interaction.response.send_message(embed=embed)
iplookup_command = app_command.Command(
    name="Iplooooookup"
    description="its in the name gng btw its api based lols"
    callback=iplookup
)
iplookup_command.default_permission = discord.Permission(administartor=True)

async def shdoan(interaction: discord.Interaction, query: str):
    encoded_query = urllib.parse.quote(query)
    shodan_link = f"https://shodan.io/search?query={encoded_query}"

    embed = discord.Embed(
        title="shodan results"
        description=f"[Click here to search for you `{query}`]({shodan_link})",
    )
    await interaction.response.send_message(embed=embed)
    
    shodan_command = app_command.Command(
        name="shodan search"
        description="shodan.io searching lols"
            callback=shodan
    )
    shodan_command.default.permission = discord.Permission(administartor=True)

async def nmap(Interaction: discord.Interaction, target: str):
    process = await asyncio.create_subprocess_exec(
        'nmap', target,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()

    if stderr:
        await Interaction.response.send_message(f"Error:\n```{stderr.decode()}```", ephemeral=True)
    else:
        output = stdout.decode()
        if len(output) > 1900:
            output = output[:1900] + '...'
        await Interaction.response.send_message(f"Scan result:\n```{output}```", ephemeral=True)
nmap_command = app_command.Command(
    name="nmap"
    descripiton="nmap and add your own commands etc"
    callback=nmap
)
nmap_command.default.permission = discord.Permission(adminstrator=True)

bot.tree.add_command(iplookup_command)
bot.tree.add_command(shodan_command)
bot.tree.add_command(nmap_command)

def signal_handler(sig, frame):
    print("Shutting down the bot gracefully...")
    bot.loop.create_task(bot.close())

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

bot.run(token, reconnect=True)
