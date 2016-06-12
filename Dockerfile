FROM library/python:3.5.1-alpine

RUN apk --update add ca-certificates
RUN pip3 install -U pip

WORKDIR /code/
ADD requirements.txt /code/

RUN pip3 install -r requirements.txt

ADD . /code/

ENTRYPOINT ["python3", "main.py"]