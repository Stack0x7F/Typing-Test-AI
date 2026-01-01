from openai import OpenAI, NotFoundError
from dotenv import load_dotenv
import os
from ..Schemas.Text_valid import Text
from pydantic import ValidationError
from .mock_texts import random_mock_text
load_dotenv()
api_key = os.getenv('api_key')

#Если кончились токены (True)
USE_MOCK_API = False 
MOCK_TEXT = random_mock_text()


#models
deepseek = 'deepseek/deepseek-r1-0528:free'
qwen = 'qwen/qwen3-coder:free'

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key 
)

current_dir = os.path.dirname(os.path.abspath(__file__))
prompt_file_path = os.path.join(current_dir, '..', 'data', 'prompt.txt')

with open(prompt_file_path, 'r', encoding='utf-8') as prompt_file:
    prompt_content = prompt_file.read() 


def generate_mock():
    mock_response_text = MOCK_TEXT

    valid_mock = Text(text=mock_response_text)
    return valid_mock.text


def generate_text():
    
    if USE_MOCK_API:
         return generate_mock()

    else:
        max_retries = 3
        current_model = deepseek 

        for attempt in range(max_retries):
            print(f"Попытка API запроса №{attempt + 1} с моделью {current_model}...")
            
            try:
                response = client.chat.completions.create(
                    model=current_model,
                    messages=[{"role": "user", "content": prompt_content}]
                )
                raw_text = response.choices[0].message.content
                
                try:
                    validated_text_obj = Text(text=raw_text) 
                    return validated_text_obj.text 
                except ValidationError as e:
                    print(f'Текст не прошел валидацию: {e}. Повтор...')
                    continue
                    
                    
            except NotFoundError:
                print(f'Модель {current_model} недоступна. Пробую другую...')
                # некст модель при 404
                current_model = qwen if current_model == deepseek else deepseek
                continue
                
            except Exception as e:
                print(f'Другая ошибка: {e}. Повтор...')
                current_model = qwen if current_model == deepseek else deepseek
                
        # если все плохо
        print("Все попытки исчерпаны. Использую Mock API...")
        return generate_mock()
        

def writing_text_to_file(generated_text_content):
    text_file_path = os.path.join(current_dir, '..', 'data', 'text.txt')
    with open(text_file_path, 'w', encoding='utf-8') as file_for_text:
        file_for_text.write(generated_text_content)
        return 'status: ok'
    