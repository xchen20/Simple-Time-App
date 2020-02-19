FROM python:3

MAINTAINER Xiaosong Chen "xc1335@nyu.edu"

COPY . /app

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", "./app.py" ]