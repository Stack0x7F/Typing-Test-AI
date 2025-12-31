import os
import sys

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from text_generate.generate.ai_service import generate_text, writing_text_to_file


text = generate_text()
writing_text_to_file(text)

from ui.user_interface import SpeedTestUI
import flet

my_app = SpeedTestUI(800, 600)
flet.app(target=my_app.main)