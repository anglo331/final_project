
FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN apt-get update -y && apt-get upgrade -y && apt-get install libpq-dev build-essential -y

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD [ "python", "main.py" ]

