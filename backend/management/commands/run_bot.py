from django.core.management.base import BaseCommand
from backend.bot import dp

import asyncio
import time
class Command(BaseCommand):
    help = 'Run the Aiogram bot'

    def handle(self, *args, **options):
        from aiogram import executor
        executor.start_polling(dp, skip_updates=True)

