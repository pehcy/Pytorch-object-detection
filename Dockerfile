FROM python:3

WORKDIR /app
ENV STATIC_URL /static

COPY "./requirements.txt" .
RUN pip install -r requirements.txt

CMD ["python", "app.py"]