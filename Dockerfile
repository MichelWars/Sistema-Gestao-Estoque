FROM python:3.12-slim

WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8000

# comando CMD não é executado durante o build da imagem somente durante o RUN do container, logo comandos com dependencias só devem ser executados após a conexão com banco de dados
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
