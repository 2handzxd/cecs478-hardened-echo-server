.PHONY: up demo test down bootstrap run

bootstrap:
	docker compose build

up:
	docker compose up -d --build

run:
	docker compose up

demo:
	docker compose exec client sh -c "echo hello secure world"
	docker compose exec client sh -c "echo test message"
	python scripts/export_metrics.py

test:
	pytest tests/ --cov=. --cov-report=term-missing

down:
	docker compose down