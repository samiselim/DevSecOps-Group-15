
FROM python:3.12-slim

WORKDIR /app

COPY calc.py .

CMD ["python", "-c", "from calc import add; print('2 + 3 =', add(2, 3))"]
