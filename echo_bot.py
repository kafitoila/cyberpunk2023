from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ContentType
from aiogram import F

token: str ='5665289787:AAHVqrTkOvkxMpJuylPtjwy7AXAGEq96r3g'
bot: Bot = Bot(token = token)
dp: Dispatcher = Dispatcher()

async def handle_start_command(message: Message):
    print(message.json(indent=2, exclude_none=True))
    answer: str = 'Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь'
    #await message.answer(answer)
    await bot.send_message(message.chat.id, answer)

async def handle_help_command(message: Message):
    print(message.json(indent=2, exclude_none=True))
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')

async def send_sticker_echo(message: Message):
    print("sticker")
    print(message.json(indent=2, exclude_none=True))
    await message.answer_sticker(message.sticker.file_id)

async def send_photo_echo(message: Message):
    print("photo")
    print(message.json(indent=2, exclude_none=True))
    await message.reply_photo(message.photo[0].file_id)

async def send_video_echo(message: Message):
    print("video")
    print(message.json(indent=2, exclude_none=True))
    await message.answer_video(message.video.file_id)

async def send_video_note_echo(message: Message):
    print("video_note")
    print(message.json(indent=2, exclude_none=True))
    await message.answer_video_note(message.video_note.file_id)

async def send_audio_echo(message: Message):
    print("audio")
    print(message.json(indent=2, exclude_none=True))
    await message.answer_audio(message.audio.file_id)

async def send_voice_echo(message: Message):
    print("voice")
    print(message.json(indent=2, exclude_none=True))
    await message.answer_voice(message.voice.file_id)

async def send_file_echo(message: Message):
    print("files")
    print(message.json(indent=2, exclude_none=True))
    await message.answer_document(message.document.file_id)

async def send_poll_echo(message: Message):
    print("poll")
    print(message.json(indent=2, exclude_none=True))
    await message.answer_poll(message.chat.id, message.poll.question, message.poll.options, message.poll.is_anonymous)

async def send_echo(message: Message):
    print("echo")
    print(message.json(indent=2, exclude_none=True))
    try:
        await message.reply(text=message.text)
    #except TypeError:
    except:
        await message.reply(text='Данный тип сообщений не поддерживается ')

dp.message.register(handle_start_command, Command(commands=["start"]))
dp.message.register(handle_help_command,  Command(commands=['help']))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_video_note_echo, F.video_note)
dp.message.register(send_sticker_echo, F.sticker)
dp.message.register(send_audio_echo, F.audio)
dp.message.register(send_voice_echo, F.voice)
dp.message.register(send_file_echo, F.document)
dp.message.register(send_poll_echo, F.poll)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)