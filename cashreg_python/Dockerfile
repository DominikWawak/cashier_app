FROM python:3.8-slim-buster


ARG DB_USERNAME
ARG DB_PASSWORD
ARG MYSQL_DB_URL


ENV DB_USERNAME=${DB_USERNAME}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV MYSQL_DB_URL=${MYSQL_DB_URL}

WORKDIR /cashreg_python

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]