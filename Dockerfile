FROM python:3.9.4-alpine3.13

ENV TOKEN="1090684830:AAGn4UCeqOO1S6ChVJNbklVCzQiIIIb4Qx4"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]