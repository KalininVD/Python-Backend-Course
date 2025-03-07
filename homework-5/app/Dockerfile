FROM python:3.11

ENV PYTHONUNBUFFERED=1
WORKDIR /app

RUN python -m venv /venv
RUN /venv/bin/pip install --upgrade pip

COPY . /app/

RUN /venv/bin/pip install -r requirements.txt
ENV PATH="/venv/bin:$PATH"

CMD ["sh", "start.sh"]