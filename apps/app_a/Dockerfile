FROM python:3.10-alpine as base

LABEL author="Nikolaos Fikas"
LABEL description="Kebormed homework challenge."
EXPOSE 5000

WORKDIR /app

COPY app_a.py ./
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

FROM base as test

COPY test.py ./

CMD [ "python", "./test.py" ]

FROM base as production

CMD [ "python", "./app_a.py" ]

