FROM python:3.12.7-alpine

WORKDIR /code

RUN apk add --no-cache curl

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/app

CMD ["fastapi", "run", "/code/app/main.py", "--port", "8080"]
