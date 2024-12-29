FROM python:3.9-slim

WORKDIR /app

COPY server.py .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "server.py" ]