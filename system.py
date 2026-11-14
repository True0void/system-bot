import subprocess
import discord
from discord.ext import commands

SALON_AUTORISE_ID = 
UTILISATEUR_AUTORISE_ID = 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)



@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name=""))
@bot.check
async def verifier_acces(ctx):
    return (
        ctx.channel.id == SALON_AUTORISE_ID
        and ctx.author.id == UTILISATEUR_AUTORISE_ID
    )

@bot.command(name="temp")
async def temperature(ctx):
  resultat = subprocess.run(
      ["vcgencmd", "measure_temp"], capture_output=True, text=True
  )
  await ctx.send(f"```{resultat.stdout.strip()}```")
  #await ctx.send(resultat.stdout.strip())
@bot.command(name="docker")
async def docker_ps(ctx):

  resultat = subprocess.run(
      ["docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}'"], shell=True, capture_output=True, text=True
  )
  sortie = resultat.stdout.strip()
  await ctx.send(f"```{sortie}```")

@bot.command(name="status")
async def status_cmd(ctx):
  resultat = subprocess.run(
      ["uptime -p && who"], shell=True, capture_output=True, text=True
  )
  await ctx.send(f"```{resultat.stdout.strip()}```")

@bot.command(name="free")
async def status_cmd(ctx):
  resultat = subprocess.run(
      ["free -h"], shell=True, capture_output=True, text=True
  )
  await ctx.send(f"```{resultat.stdout.strip()}```")
@bot.command(name="find")
async def find_process(ctx, *, nom: str):
    resultat = subprocess.run(
        ["pgrep", "-afi", nom],
        capture_output=True,
        text=True
    )

    if not resultat.stdout.strip():
        await ctx.send(f"Aucun processus trouvé pour `{nom}`.")
        return

    await ctx.send(f"```text\n{resultat.stdout[:1800]}\n```")


bot.run("")
