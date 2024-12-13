FROM python:3.10-slim as builder

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN /opt/venv/bin/pip install pip --upgrade && \
    /opt/venv/bin/pip install -r requirements.txt --no-cache-dir

FROM python:3.10-slim as runner
WORKDIR /opt/crawler
RUN groupadd -g 1001 scrapy \
    && useradd -u 1001 -g scrapy -m -d /opt/crawler scrapy \
    && chown scrapy:scrapy -R /opt/crawler
USER scrapy

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY --chown=scrapy:scrapy . /opt/crawler

CMD ["python3", "run_spiders.py"]
