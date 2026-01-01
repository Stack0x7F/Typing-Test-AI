**Установка**

* Клонируйте репозиторий:
  git clone github.com
  cd speed-test-app

* Создайте виртуальное окружение и активируйте его:

  python -m venv venv
  # Для Windows:
  venv\Scripts\activate
  # Для macOS/Linux:
  source venv/bin/activate

* **Установите зависимости:**
  pip install -r requirements.txt

**Настройка окружения**

* Создайте файл .env в корневой директории проекта и добавьте ваш API-ключ с https://openrouter.ai/:

api_key='ваш_ключ_openrouter_здесь'

** Использование **
для использования других моделей:
  в файле ai_service.py:

```python
deepseek = 'deepseek/deepseek-r1-0528:free'
qwen = 'qwen/qwen3-coder:free'
```
заменить/добавить название и ссылку нужной модели (ссылку можно найти на странице модели openrouter)
<img width="1031" height="286" alt="image" src="https://github.com/user-attachments/assets/3deaab78-8e27-46b8-b7c5-e896b200111d" />


** Структура проекта **
📦 WPM_TEST
 ┣ 📂 source
 ┃ ┣ 📂 text_generate
 ┃ ┃ ┣ 📂 data
 ┃ ┃ ┃ ┣ 📜 prompt.txt
 ┃ ┃ ┃ ┗ 📜 text.txt
 ┃ ┃ ┣ 📂 generate
 ┃ ┃ ┃ ┣ 📜 __init__.py
 ┃ ┃ ┃ ┣ 📜 ai_service.py
 ┃ ┃ ┃ ┗ 📜 mock_texts.py
 ┃ ┃ ┗ 📂 Schemas
 ┃ ┃   ┣ 📜 __init__.py
 ┃ ┃   ┗ 📜 Text_valid.py
 ┃ ┣ 📂 ui
 ┃ ┃ ┗ 📜 user_interface.py
 ┃ ┗ 📜 run.py              # Точка входа
 ┣ 📜 .env
 ┗ 📜 requirements.txt

запуск из run.py


python source\run.py
