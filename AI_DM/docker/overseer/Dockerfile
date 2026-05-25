FROM python:3.11-slim
RUN pip install --no-cache-dir playwright==1.51.0 requests==2.32.2 beautifulsoup4==4.12.3 schedule==1.2.1 psutil==5.9.8 flask==3.0.3 lxml==5.2.1 markdown==3.6 Pillow==10.3.0
RUN playwright install chromium --with-deps 2>/dev/null || true
WORKDIR /overseer
COPY main.py /overseer/main.py
ENV PYTHONUNBUFFERED=1
CMD ["python3", "main.py"]
