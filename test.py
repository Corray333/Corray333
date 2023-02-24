import keralabot

bot = keralabot.bot('5636709677:AAHwxs4Yarr_Tvh6qY1rrTQRi76sheofE9c')


@bot.message_handler(content_types=['text'])
def replyer(message):
    bot.send_message(message.from_user.id, message.text)

bot.polling(none_stop=True, interval=0)

