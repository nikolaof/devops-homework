FROM python:3.10-alpine

LABEL author="Nikolaos Fikas"
LABEL description="Kebormed homework challenge."
EXPOSE 5001

WORKDIR /app

COPY app_b.py ./
COPY requirements.txt ./
COPY entrypoint.sh ./
COPY schema.sql ./

RUN mkdir sqlite

RUN chmod +x entrypoint.sh

RUN apk update && apk upgrade

RUN apk add --no-cache sqlite

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "./entrypoint.sh" ]
