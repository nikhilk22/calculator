#base image #
FROM python:3.11-slim

#create dir
WORKDIR /app

COPY requirements.txt .
COPY templates/ ./templates/
COPY static/ ./static/

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

# Use exec form for proper signal handling
CMD ["python", "app.py"]
