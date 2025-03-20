FROM python:3.8-slim

USER root

RUN   mkdir  /var/flasksite

COPY  .  /var/flasksite/

WORKDIR  /var/flasksite/

RUN  pip3 install -r requirements.txt 

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]