build:
	docker build -t joanfont/census-bot .
push:
	docker push joanfont/census-bot
release:
	make build push
start:
	docker run --rm joanfont/census-bot