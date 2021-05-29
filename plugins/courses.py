from userge import userge, Message, filters

@userge.on_filters(filters.chat(-1001458635911))
async def find_heroku_bin(message: Message):
    if message.photo:
        await message.copy(-1001435287965)
    else:
        await message.copy(-1001458635911)
