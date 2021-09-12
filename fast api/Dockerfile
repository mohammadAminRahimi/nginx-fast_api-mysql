FROM python:3.8


RUN apt-get update
RUN apt-get install -y --no-install-recommends default-mysql-client
#RUN apt-get install python3-dev default-libmysqlclient-dev build-essential

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY  . .


WORKDIR /usr/src/app/
ENTRYPOINT ["sh", "entrypoint.sh"]

