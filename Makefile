build:
	docker-compose build bot
push:
	docker push joanfont/census-bot
release:
	make build push
start:
	docker-compose run --rm --service-ports bot
clean:
	rm -fr log/*
