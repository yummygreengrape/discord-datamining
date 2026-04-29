FROM python:3.10-alpine

RUN apk add --no-cache git curl nodejs npm \
    && npm install -g js-beautify

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "-u", "main.py"]
