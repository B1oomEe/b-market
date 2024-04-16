FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV DEBUG=True
ENV SECRET_KEY="MibJimY9HZCRk56MKgIHcUKhH1"
ENV SESSION_TIME="15552000"
ENV SESSION_COOKIE_HTTPONLY=False
ENV SESSION_TYPE="filesystem"
ENV DB_PORT="5432"
ENV DB_HOST="localhost"
ENV DB_NAME="bmarket"
ENV DB_USER="postgres"
ENV DB_PASSWORD="Rrobocopid12"

#EXPOSE 5000

CMD [ "python3", "source/server.py" ]