# ここはビルド用のコンテナ
FROM python:3.7-slim-buster as builder

WORKDIR /opt/app

COPY pyproject.toml .

RUN pip3 install --no-cache-dir -U pip && \
    pip3 install --no-cache-dir poetry && \
    pip3 install --upgrade pip setuptools wheel

COPY . /opt/app
RUN rm -rf /opt/app/.venv

RUN poetry build
#COPY requirements.lock /opt/app
#RUN pip3 install -r requirements.lock

# ここからは実行用のコンテナ
FROM gcr.io/distroless/python3:debug as runner

#COPY --from=builder /opt/app/dist/my_poetry*.whl /
#RUN pip3 install /*.whl

#COPY --from=builder /usr/local/lib/python3.7/site-packages /root/.local/lib/python3.7/site-packages

COPY src /opt/app/src
#
WORKDIR /opt/app/src
#
#EXPOSE 8000
CMD ["execute_cards.py"]
