import telebot
import config


TOKEN = "5382600166:AAHYSbf3vCvAnuIRhMoa19uP50_PZAbh1EA"

bot = telebot.TeleBot(TOKEN)

keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'юань': 'CNYX',
}


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        values = message.text.split('')

        if len(values) != 3:
            raise Convertion('слишком много параметров.')

        quote, base, amount = values

        if quote == base:
            raise Convertion(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту{quote}')

        try:
            base_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту{base}')


            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
            total_base = json.loads(r.content)[keys[base]]

        return total_base


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате:\n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидить список всех доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

    if len(values) != 3:
        raise ConvertionException('Слишком много параметров.')

    quote, base, amount = values
    total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
    bot.replay_to(message, 'Ошибка пользователя\n{e}')

    except Exception as e:
    bot.reply_to(f'Не удалось обработать команду\n{e}')
else:
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()

