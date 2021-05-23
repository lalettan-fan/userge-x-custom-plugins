from userge import userge, Message, filters

@userge.on_filters(filters.channel)
async def find_heroku_bin(message: Message):
    text = message.text or message.caption or ""
    if "heroku" in text.lower():
        await message.copy(-1001127585391)
