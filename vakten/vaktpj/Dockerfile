FROM python:3.8-alpine
MAINTAINER Francisco Fuentes dmusta1ne.pak@gmail.com

# https://blog.bitsacm.in/django-on-docker/
# These two environment variables prevent __pycache__/ files.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Make a new directory to put our code in.
ENV APP_HOME=/code
RUN mkdir $APP_HOME
#; mkdir $APP_HOME/staticfiles

# Change the working directory. 
# Every command after this will be run from the /code directory.
WORKDIR $APP_HOME

# Copy the rest of the code. 
COPY . $APP_HOME

# Upgrade pip
RUN pip install --upgrade pip

# Install the requirements.
RUN apk update; apk add netcat-openbsd; \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev \
 zlib-dev jpeg-dev && \
 python3 -m pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

ENTRYPOINT ["/code/entrypoint.sh"]
