import time
from functools import wraps
from src.helpers.logger import logger

def retry(max_attempts=3, delay=1, backoff=2, exceptions=(Exception,)):
    """
    Декоратор для повторного выполнения функции при ошибке.
    
    Args:
        max_attempts: Максимальное количество попыток
        delay: Начальная задержка в секундах
        backoff: Множитель увеличения задержки
        exceptions: Кортеж исключений, которые нужно перехватывать
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            current_delay = delay
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    attempt += 1
                    if attempt == max_attempts:
                        logger.error(f"Retry exhausted for {func.__name__}: {e}")
                        raise
                    logger.warning(f"Retry {attempt}/{max_attempts} for {func.__name__} after {current_delay}s: {e}")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator
