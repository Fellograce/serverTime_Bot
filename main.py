import discord
import asyncio
import datetime
import os
import requests
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
            #GET request to xiv server
            response = requests.get('https://v2.xivapi.com/api')
            headers = response.headers
            date_string = headers.get('date')
            date_obj = datetime.datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S GMT')

            new_nickname = date_obj.strftime('%a %H:%M')
            seconds = date_obj.second

            for guild in bot.guilds:
                member = guild.get_member(bot.user.id)

                # Update the bot's nickname with the current time
                await member.edit(nick=new_nickname)

            # Run the loop every minute
            await asyncio.sleep(60 - int(seconds))  # wait till a minute has passed in real time
        except Exception as e:
            print(f"An error occurred: {e}")
            await asyncio.sleep(60)

# Run the bot
bot.run(BOT_TOKEN)
