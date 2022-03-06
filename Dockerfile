FROM python:3.10-slim-buster AS base

WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8000

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN mkdir uploads

COPY . .

# CMD [ "python3.10", "main.py", "requirements.txt" ]
CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]