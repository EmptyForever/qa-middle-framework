import pytest
from src.core.config import settings
from src.helpers.logger import logger

# Автоматическая маркировка асинхронных тестов
pytest_plugins = ['pytest_asyncio']

@pytest.fixture(scope="session", autouse=True)
def setup_logging():
    """Фикстура, которая запускается автоматически при старте сессии тестов."""
    logger.info("="*50)
    logger.info(f"Starting test session in ENV: {settings.ENV}")
    logger.info(f"API Base URL: {settings.API_BASE_URL}")
    logger.info(f"PostgreSQL: {settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}")
    logger.info(f"Kafka: {settings.KAFKA_BOOTSTRAP_SERVERS}")
    logger.info("="*50)
    yield
    logger.info("="*50)
    logger.info("Test session finished")
    logger.info("="*50)

@pytest.fixture(scope="function")
def test_data():
    """Фикстура для передачи данных между шагами в тесте."""
    data = {}
    yield data
    # После теста можно почистить данные, если нужно
    logger.debug(f"Test data cleaned: {data}")
