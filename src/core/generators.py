def paginate(items, page_size=10):
    """
    Генератор для постраничного обхода списка.
    
    Args:
        items: Список элементов
        page_size: Размер страницы
    
    Yields:
        Список элементов на странице
    """
    for i in range(0, len(items), page_size):
        yield items[i:i + page_size]

def read_large_csv(filepath, chunk_size=1000):
    """
    Генератор для чтения больших CSV-файлов по кускам.
    Не загружает весь файл в память.
    """
    import csv
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        chunk = []
        for row in reader:
            chunk.append(row)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []
        if chunk:
            yield chunk

def read_large_jsonl(filepath, chunk_size=1000):
    """
    Генератор для чтения больших JSONL-файлов (каждая строка — JSON).
    """
    import json
    with open(filepath, 'r', encoding='utf-8') as f:
        chunk = []
        for line in f:
            if line.strip():
                chunk.append(json.loads(line))
                if len(chunk) >= chunk_size:
                    yield chunk
                    chunk = []
        if chunk:
            yield chunk
