FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

ENV PORT=5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:${PORT}", "app:app"]
