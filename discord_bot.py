import discord
from discord.ext import commands

TOKEN = "MTQ1MTU4MjU1ODc4ODc4NDE2OQ.Gdxu10.qGrR3g55x2RgpCEuHJ6I3eG6t4IcKKJY5gPF94"

intents = discord.Intents.default()
intents.message_content = True  # חשוב בשביל לקבל תוכן הודעות

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# דוגמה ליצירת משתמש
@bot.command()
async def create_user(ctx, username, password):
    from database.db import create_user, get_user
    
    if get_user(username):
        await ctx.send(f"❌ המשתמש {username} כבר קיים!")
    else:
        if create_user(username, password):
            await ctx.send(f"✅ המשתמש {username} נוצר בהצלחה!")
        else:
            await ctx.send(f"❌ לא ניתן ליצור את המשתמש.")

bot.run(TOKEN)
