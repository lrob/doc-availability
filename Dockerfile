FROM ubuntu:18.04

RUN apt update && apt install -y \
      python3 python3-pip

COPY requirements.txt app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt

COPY . /app

CMD python3 -u main.py