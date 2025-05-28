FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y \
        netcat-traditional \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt

COPY ./docker/images/flask/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /var/www/app
CMD ["/bin/bash", "/entrypoint.sh"]
