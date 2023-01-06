FROM ubuntu:23.04

RUN apt-get clean
RUN apt-get update -y --fix-missing && apt-get install -y python3-pip python3-dev build-essential
RUN pip3 install --upgrade pip

COPY . /app
WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["sh", "run.sh"]
