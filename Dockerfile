FROM library/python:3.5.1-alpine

RUN apk --update add ca-certificates

WORKDIR /code/
ADD requirements.txt /code/

RUN pip3 install -r requirements.txt

ADD . /code/
RUN touch .env

ENTRYPOINT ["python3", "main.py"]