FROM python:3.8


RUN apt-get update
RUN apt-get install -y --no-install-recommends default-mysql-client
#RUN apt-get install python3-dev default-libmysqlclient-dev build-essential

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt


#RUN pip install django-probes
#RUN python project/manage.py wait_for_database
#RUN python project/manage.py migrate
#RUN pip install mysql-connector-python==8.0.26

COPY  . .
WORKDIR /usr/src/app/project
#EXPOSE 8000
#COPY ./project/entrypoint.sh ./project
ENTRYPOINT ["sh", "../entrypoint.sh"]
#ENTRYPOINT ["python", "manage.py", "migrate"]
