.PHONY: install test test-parallel test-api test-ui test-db test-performance coverage report docker-up docker-down docker-kafka-up docker-kafka-down pre-commit

install:
pip install -r requirements.txt
pre-commit install

test:
pytest -v

test-parallel:
pytest -n auto --dist loadscope -v

test-api:
pytest tests/api -v

test-ui:
pytest tests/ui/web -v

test-db:
pytest tests/db -v

test-performance:
pytest tests/performance -v

coverage:
pytest --cov=src --cov-report=html:reports/coverage --cov-report=term-missing --cov-fail-under=85

report:
allure generate reports/allure_results -o reports/allure_report --clean
allure open reports/allure_report

docker-up:
docker-compose -f docker/docker-compose.yml up -d

docker-down:
docker-compose -f docker/docker-compose.yml down -v

docker-kafka-up:
docker-compose -f docker/docker-compose.kafka.yml up -d

docker-kafka-down:
docker-compose -f docker/docker-compose.kafka.yml down -v

pre-commit:
pre-commit run --all-files
