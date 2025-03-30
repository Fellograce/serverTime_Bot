import discord
import asyncio
import datetime
import os
#from dotenv import load_dotenv


#load_dotenv()

# Create a Discord bot instance
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = discord.Client(intents=intents)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = os.getenv('BOT_TOKEN')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

    while True:
        try:
            now = datetime.datetime.utcnow()
            formatted_time = now.strftime('%a %H:%M')  # Format time as HH:MM:SS
            seconds = now.strftime('%S')

            for guild in bot.guilds:
                member = guild.get_member(bot.user.id)

                # Update the bot's nickname with the current time
                await member.edit(nick=formatted_time)

            # Run the loop every hour
            await asyncio.sleep(60 - int(seconds))  # wait till a minute has passed in real time
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(60)

# Run the bot
bot.run(BOT_TOKEN)
