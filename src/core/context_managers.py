from contextlib import contextmanager
from src.helpers.logger import logger

@contextmanager
def db_transaction(connection):
    """Контекстный менеджер для транзакций БД.
    При ошибке делает ROLLBACK, при успехе — COMMIT.
    """
    try:
        yield connection
        connection.commit()
        logger.debug("Transaction committed")
    except Exception as e:
        connection.rollback()
        logger.error(f"Transaction rolled back: {e}")
        raise

@contextmanager
def safe_file_open(filepath, mode='r'):
    """Контекстный менеджер для безопасной работы с файлами.
    Автоматически закрывает файл даже при ошибке.
    """
    file = None
    try:
        file = open(filepath, mode, encoding='utf-8')
        yield file
    finally:
        if file:
            file.close()
            logger.debug(f"File closed: {filepath}")

@contextmanager
def temp_env_var(key, value):
    """Временно меняет переменную окружения, потом возвращает обратно."""
    import os
    old_value = os.environ.get(key)
    os.environ[key] = value
    logger.debug(f"TEMP ENV: {key}={value}")
    try:
        yield
    finally:
        if old_value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = old_value
        logger.debug(f"Restored ENV: {key}={old_value}")
