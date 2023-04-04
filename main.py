import logging
from checkWord import checkWords
from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_latin,to_cyrillic,transliterate
API_TOKEN = '5874828093:AAEJyJ-XxORYimqXI48-fWLgZsSNGJk0Pjc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu alaykum!\nUzLotinImlo botiga!\nXush kelibsiz.\nDasturchi:\nhttps://t.me/javohir_ergashev30")
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Bu bot orqali\nSiz imlo xatolarengizni tuzatishengiz mumkin\n"
                        "Botni ishlatish so'z yuboring")



@dp.message_handler()
async def echo(message: types.Message):
    word=message.text
    if to_latin(word)==word:
        til='latin'
    elif to_cyrillic(word)==word:
        til='cyrillic'
    print(til)
    wordlist=checkWords(to_cyrillic(word))
    if wordlist['available']:
        response=f"✅{transliterate(message.text,til).capitalize()}"
    else:
        response=f"❌{transliterate(message.text,til)}\n"
        for i in wordlist['matches']:
            response+=f"✅{transliterate(i,til).capitalize()}\n"
    await message.answer(response)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)

