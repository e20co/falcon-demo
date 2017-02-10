FROM python:3.5-alpine

MAINTAINER ECG Engineering <techalerts@expansioncapitalgroup.com>

WORKDIR /app

ENV PORT 80

COPY requirements.txt /tmp

RUN apk add --no-cache --virtual .build-deps \
            build-base \
            gcc \
            libc-dev \
            libffi-dev \
            linux-headers \
            musl-dev \
            openssl-dev \
            pcre-dev \
            python3-dev \
    && pip install -r /tmp/requirements.txt \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
            | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
            | sort -u \
            | xargs -r apk info --installed \
            | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

ADD circusd.ini /etc

COPY app /app
EXPOSE $PORT

CMD ["/usr/local/bin/circusd", "/etc/circusd.ini"]
