FROM python:3.11-slim

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system --deploy

COPY . .

EXPOSE 5000

CMD ["python", "server.py"]