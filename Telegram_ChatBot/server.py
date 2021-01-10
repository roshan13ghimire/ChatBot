  
from bot import telegram_bot

bot = telegram_bot("config.cfg")


def make_reply(msg,f_name):
    reply = None
    if msg == "":
        reply =  "Hello {}".format(f_name)
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
                f_name=str(item["message"]["from"]["first_name"])
            except:
                message = None
                f_name = None
            from_ = item["message"]["from"]["id"]
    else:
        reply = make_reply(message)
        bot.send_message(reply, from_)