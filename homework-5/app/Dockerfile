FROM python:3.11

WORKDIR /app

RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["sh", "start.sh"]