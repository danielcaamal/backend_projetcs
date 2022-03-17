# pull official base image
FROM python:3.9.6-alpine

# set environment variables (No pycache)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# set work directory
WORKDIR /code/awards

# install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \ 
    pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x entrypoint.sh


# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/code/awards/entrypoint.sh"]