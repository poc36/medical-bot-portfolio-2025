import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from bot.handlers import ai_router
from bot.services.mock_api import MockMIS

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    bot_token = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")
    
    if bot_token == "YOUR_BOT_TOKEN_HERE":
        logger.warning("BOT_TOKEN not set. Use .env file.")
    
    bot = Bot(token=bot_token)
    dp = Dispatcher()
    
    mis_service = MockMIS()
    
    dp.include_router(ai_router.router)
    
    @dp.message(Command("start"))
    async def cmd_start(message: types.Message):
        await message.answer(
            "Welcome to Medical AI Assistant!\n"
            "I can help you:\n"
            "Book an appointment\n"
            "Check your booking\n"
            "Cancel appointment\n"
            "Request callback\n"
            "Get information"
        )
    
    logger.info("Bot started successfully!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
