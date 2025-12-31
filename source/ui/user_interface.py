import flet
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
text_file_path = os.path.join(current_dir, '..', 'text_generate', 'data', 'text.txt')


class SpeedTestUI:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.text = ''

    def __repr__(self):
        return f'{self.__class__.__name__}'


    def get_text(self):
        with open(text_file_path, 'r', encoding='utf-8') as file_with_text:
            self.text = file_with_text.read()
            return self.text
            
    def main(self, page: flet.Page):
        
        self.page = page
        self.page.title = "Speed Test"
        self.page.window_width = self.width
        self.page.window_height = self.height
        
    
        self.page.add(
            flet.Text(self.get_text())
        )
        self.page.update()

