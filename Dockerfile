FROM python:3.8-alpine
WORKDIR /app
COPY src/ /app/
RUN apk add gcc python3-dev libevent-dev libffi-dev build-base py-gevent
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN echo -e "*/15    *       *       *       *       FLASK_APP=/app python3 -m flask cron twitter\n*/15    *       *       *       *       FLASK_APP=/app python3 -m flask cron telegram" >> /etc/crontabs/root
WORKDIR /app
RUN wget -qO /usr/local/bin/wait-for https://raw.githubusercontent.com/eficode/wait-for/master/wait-for \
    && chmod +x /usr/local/bin/wait-for
# RUN apk add waitforit
COPY ./wait.sh /app/wait.sh
RUN chmod +x wait.sh
ENTRYPOINT [ "./wait.sh" ]