class QAFrameworkError(Exception):
    """Базовое исключение для всего фреймворка"""
    pass

class APIClientError(QAFrameworkError):
    """Ошибка при работе с API-клиентом"""
    pass

class DatabaseError(QAFrameworkError):
    """Ошибка при работе с базой данных"""
    pass

class ValidationError(QAFrameworkError):
    """Ошибка валидации данных (схемы, модели)"""
    pass

class KafkaError(QAFrameworkError):
    """Ошибка при работе с Kafka"""
    pass

class AuthError(QAFrameworkError):
    """Ошибка авторизации (токены, логин)"""
    pass

class ElementNotFoundError(QAFrameworkError):
    """Элемент не найден в UI"""
    pass
