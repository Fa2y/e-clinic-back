FROM python:alpine

ENV APP_DIR_NAME .
ENV APP_PATH /opt/e-clinic-back

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev postgresql-dev postgresql mysql-client mariadb-connector-c-dev
#Pillow requirements
RUN apk update \
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
#Fonts
ENV LANG en_US.UTF-8
#Install font software, complete font configuration
RUN apk add --update ttf-dejavu fontconfig && rm -rf /var/cache/apk/*
#installing django
COPY requirements.txt /
RUN pip install --default-timeout=3600 -r requirements.txt
RUN rm requirements.txt

#adding entrypoint scripts
COPY docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]

#adding the django project
RUN mkdir -p $APP_PATH
COPY $APP_DIR_NAME $APP_PATH