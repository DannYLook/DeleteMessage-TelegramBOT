import re
import telebot
import configure


client = telebot.TeleBot(configure.config['token'])


@client.message_handler(content_types = ['text'])
def get_text(message):
    stoca = (message.text)


    stocaf = re.findall('\d+', stoca)
    if len(stocaf) > 0:
        client.delete_message(message.chat.id, message.message_id)

client.polling(none_stop = True, interval = 0)




