FROM python:3.12-alpine as builder

RUN set -eux; \
        apk add --no-cache \
                gcc \
                libc-dev \
                libffi-dev \
                openssl-dev \
                cargo

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY fronius2mqtt .
COPY patches/pyfronius___init__.py /usr/local/lib/python3.12/site-packages/pyfronius/__init__.py

CMD [ "python", "./fronius2mqtt" ]
