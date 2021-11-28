FROM ubuntu:20.04

RUN apt update && apt install -y \
      python3 python3-pip

COPY requirements.txt app/requirements.txt

WORKDIR /app
RUN pip3 install -r requirements.txt

COPY main.py /app

CMD python3 -u main.py