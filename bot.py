import discord
from discord.ext import commands
import requests
import os

def gm_message(bot_id, text):
    params = {"bot_id":bot_id,
              "text":text}

    response = requests.post("https://api.groupme.com/v3/bots/post",
                        headers = {"Content-Type":"application/json"},
                        params  = params)

    return response


intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = commands.Bot(command_prefix='!', intents = intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        ctx = await client.get_context(message)

        voice_channel_list = ctx.guild.voice_channels
        voice_channel_list = [channel for channel in voice_channel_list if channel.id != int(os.environ['afk_channel'])]

        active = []

        try:
            for channel in voice_channel_list:
                for key in channel.voice_states.keys():
                    user = ctx.guild.get_member(key)

                    if user.nick:
                        name = user.nick
                    else:
                        name = user.name

                    try:
                        game = f"playing {user.activities[0].name}"
                    except:
                        game = ""

                    active.append(f"{name} {game}")

            if len(active) > 0:
                active = "\n ".join(active)
                gm_message(os.environ['groupme_id'],
                           f"The following are currently in Discord voice channels:\n\n {active}")
            else:
                if 'cron' not in message.content:
                    gm_message(os.environ['groupme_id'], 
                               f"Nobody is currently in Discord voice channels.")
        except Exception as e:
            print("Exception raised")
            print(e)

client.run(os.environ['discord_client'])
