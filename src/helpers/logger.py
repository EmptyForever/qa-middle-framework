import logging
import sys
from pathlib import Path

# Создаём папку для логов
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

# Настройка корневого логгера
logger = logging.getLogger('qa_framework')
logger.setLevel(logging.DEBUG)

# Формат для всех логов
formatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s - %(name)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Хендлер для записи в файл
file_handler = logging.FileHandler(LOGS_DIR / 'test.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Хендлер для вывода в консоль
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Добавляем хендлеры в логгер
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Отключаем распространение на корневой логгер
logger.propagate = False
