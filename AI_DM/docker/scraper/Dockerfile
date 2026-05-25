FROM python:3.11-slim
RUN pip install --no-cache-dir requests
WORKDIR /app
COPY scraper.sh /app/scraper.sh
RUN chmod +x /app/scraper.sh
VOLUME /data/intel
CMD ["/app/scraper.sh"]
