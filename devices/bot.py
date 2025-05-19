import asyncio
from telegram import Bot




from telegram import Bot

TOKEN = '7829118396:AAHMoNEmBuH6JQ2fKT5uXzobYAHE87InZWM'
CHANNEL_ID = '@testpnx1'
MESSAGE_ID = 55  # شناسه پیام مورد نظر

bot = Bot(token=TOKEN)





async def send_message_and_get_info():
    try:
        # ارسال پیام توسط ربات
        message = await bot.send_message(chat_id=CHANNEL_ID, text="پیامی برای تست")
        print(f"پیام ارسال شد! شناسه پیام: {message.message_id}")
        
        # دریافت اطلاعات پیام ارسال شده
        print(f"متن پیام: {message.text}")
        print(f"ارسال شده توسط: {message.from_user.username}")
        print(f"تاریخ ارسال: {message.date}")
    except Exception as e:
        print(f"خطا در ارسال یا دریافت اطلاعات پیام: {e}")

# اجرای تابع async
if __name__ == "__main__":
    asyncio.run(send_message_and_get_info())




# async def send_messages():
#     """
#     ارسال ۵ بار عدد "6" به کانال
#     """
#     for i in range(5):
#         try:
#             await bot.send_message(chat_id=CHANNEL_ID, text="6")  # استفاده از await
#             print(f"پیام شماره {i + 1} ارسال شد!")
#         except Exception as e:
#             print(f"خطا در ارسال پیام شماره {i + 1}: {e}")
#             break

# # اجرای تابع هم‌زمان
# if __name__ == "__main__":
#     asyncio.run(send_messages())
