import os
import sys
import asyncio
import flet as ft

project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.append(project_root)

from text_generate.generate.ai_service import writing_text_to_file, generate_text, generate_mock
from ui.user_interface import SpeedTestApp

async def start_app(page: ft.Page):
    app = SpeedTestApp()

    async def trigger_generation():
        loop = asyncio.get_running_loop()
        try:
            new_text = await loop.run_in_executor(None, generate_text)

            await loop.run_in_executor(None, lambda: writing_text_to_file(new_text))
            await app.set_text(new_text)
        except Exception as e:
            print(f"Ошибка при генерации: {e}")
            generate_mock()

    app.generate_new_text_callback = trigger_generation

    await app.main(page)

    await trigger_generation()

def main():
    ft.run(start_app)

if __name__ == "__main__":
    main()
