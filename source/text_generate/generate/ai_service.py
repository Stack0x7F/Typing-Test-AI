from openai import OpenAI
from dotenv import load_dotenv
import os
from ..Schemas.Text_valid import Text
from pydantic import ValidationError

load_dotenv()
api_key = os.getenv('api_key')

# --- КОНФИГУРАЦИЯ РЕЖИМА РАЗРАБОТКИ (нищий/адекватный) ---
USE_MOCK_API = True 

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key 
)

current_dir = os.path.dirname(os.path.abspath(__file__))
prompt_file_path = os.path.join(current_dir, '..', 'data', 'prompt.txt')

with open(prompt_file_path, 'r', encoding='utf-8') as prompt_file:
    prompt_content = prompt_file.read() 
    
def generate_text():
    
    if USE_MOCK_API:
        print("Используется Mock API")
        mock_response_text = "This is a mocked response that is long enough to pass validation tests locally without hitting the rate limit bebebebebe"

        try:
            Text(text=mock_response_text)
            return mock_response_text
        except ValidationError as e:
            raise Exception(f"mock-текст не прошел валидацию Pydantic: {e}")


    else:
        max_retries = 3
        for attempt in range(max_retries):
            print(f"Попытка реального API запроса №{attempt + 1}...")

            response = client.chat.completions.create(
                model="deepseek/deepseek-chat:free",
                messages=[{"role": "user", "content": prompt_content}]
            )
            raw_text = str(response.choices.message.content)
            
            try:
                # Валидация
                validated_text_obj = Text(text=raw_text) 
                return validated_text_obj.text 
            except ValidationError as e:
                print(f'Текст не прошел валидацию: {e}. Повтор...')
        
        raise Exception('Не удалось сгенерировать валидный текст после 3 попыток.')


def writing_text_to_file(generated_text_content):
    text_file_path = os.path.join(current_dir, '..', 'data', 'text.txt')
    with open(text_file_path, 'w', encoding='utf-8') as file_for_text:
        file_for_text.write(generated_text_content)
        return 'status: ok'
    
writing_text_to_file(generate_text())