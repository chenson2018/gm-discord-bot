#!/usr/bin/python
from discord import Webhook, RequestsWebhookAdapter
import os

webhook = Webhook.from_url(os.environ['discord_webhook'], adapter=RequestsWebhookAdapter())
webhook.send("!pingcron")

