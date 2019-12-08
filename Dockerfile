FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN pip install -U pip setuptools poetry --no-cache-dir
RUN poetry config settings.virtualenvs.create false

WORKDIR /usr/src/app

COPY pyproject.toml .
COPY poetry.lock .
RUN poetry install

COPY . .

RUN chmod +x ./wait-for-it.sh
RUN chmod +x ./entrypoint.sh
RUN chmod +x ./cmd.sh

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]

CMD ["./cmd.sh"]
