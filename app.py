from flask import Flask, request
from flask import jsonify
from discord import Webhook, RequestsWebhookAdapter
from waitress import serve
import re
import os

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot_response():
    data = request.get_json()

    if data['name'] != 'discord':
        if re.match(r"^@discord", data['text']):
            webhook = Webhook.from_url(os.environ['discord_webhook'],
                                       adapter=RequestsWebhookAdapter())
            webhook.send("!ping")

    return "1"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port = int(os.environ['gm_flask_port']))
