FROM python:3.10.5-alpine3.15

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

RUN apk update
RUN python3 -m pip install --no-cache-dir -r requirements.txt

CMD python app