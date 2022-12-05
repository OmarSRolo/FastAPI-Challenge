FROM python:3.11

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PYTHONOPTIMIZE=TRUE

COPY . .

RUN pip install --no-cache-dir --upgrade -r requirements/dev.txt

EXPOSE 8000

CMD ["uvicorn", "server:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]



