# gm-discord-bot

This is a simple setup that allows for a bot that interacts with both Discord and GroupMe. The structure is very specific to a specific Discord with my friends.

The Flask API is used to accept post requests from GroupMe. If the message starts with "@discord", this sends a message "!ping" to a channel in discord, which then sends a message back to GroupMe with a list of active users in voice channels and what they are currently playing. Note that users can manually trigger the bot themselves from Discord.

Also included is few line script that I run in a crontab to send a daily status to our GroupMe.

The following environment variables are used:

discord_webhook
groupme_id
afk_channel
discord_client

