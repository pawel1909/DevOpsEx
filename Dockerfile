FROM python:3.9-slim

WORKDIR /app

COPY server.py .

RUN pip install flask
RUN pip install requests

EXPOSE 5000

CMD [ "python", "server.py" ]