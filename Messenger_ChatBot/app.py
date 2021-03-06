import os, sys
from flask import Flask, request
from pymessenger import Bot
import Scrap 



app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAMfmNZAprOUBAKHzoxoAaQwdwIL0EWgMfhXtnREHBexZBLd5m7OG2DHLZCJhUpToB9WP99LoZBIvO5sZCwgMbPgvc0cZAUETJLofdLubOtCjtymPjgIJO97MbAuhSe0BguTDtMut5ESPWM1xwboMvNydtFSbQUbkUDuleCXdKCAODmZCZB39lDsD28z7itL60YZD"

bot = Bot(PAGE_ACCESS_TOKEN)





@app.route('/', methods=['GET'])
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "hello":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():

    data = request.get_json()
    log(data)  

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_text = 'no text'
                    if messaging_text.lower() == "help":
                        bot.send_text_message(sender_id, "I can help you to display NEPSE's data, \n\n please enter the tradecompany's symbol ex: ebl for Everest Bank limited " )
                    elif messaging_text[0].lower() == "h" :
                        bot.send_text_message(sender_id, "Hello Roshan")
                    else:
                        response = Scrap.StockPrice(messaging_text)
                        bot.send_text_message(sender_id, response)

    return "ok", 200

def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
	app.run(debug = True, port = 80)