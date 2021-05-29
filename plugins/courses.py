from userge import userge, Message, filters

@userge.on_filters(filters.chat("BursterBins"))
async def find_heroku_bin(message: Message):
    if message.photo:
        await message.copy(-1001435287965)
