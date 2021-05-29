from userge import userge, Message, filters

@userge.on_filters(filters.channel)
async def course(message: Message):
    print(message.text)
    if not message.chat.id == -1001458635911:
        return
    if message.photo:
        await message.copy(-1001435287965)
    else:
        await message.copy(-1001458635911)
