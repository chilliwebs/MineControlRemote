FROM python:3.10.2-alpine

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /app

ADD streamcraftremote.py /app

EXPOSE 3210

ENTRYPOINT ["python", "/app/streamcraftremote.py"]