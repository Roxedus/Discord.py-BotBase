FROM python:3.8-alpine3.12

LABEL maintainer="Roxedus"

COPY / /app

RUN apk add --no-cache --virtual=build-dependencies  --update \
        gcc \
        musl-dev \
        python-dev && \
    python3 -m pip install -r /app/requirements.txt && \
    apk del build-dependencies

WORKDIR /app

VOLUME [ "/data" ]

ENTRYPOINT [ "python3", "/app/launcher.py", "--data-directory", "/data" ]