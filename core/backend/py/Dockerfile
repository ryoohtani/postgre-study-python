FROM python:3.11.4

WORKDIR /core

COPY . /core

# パッケージの更新
RUN apt-get update
# キャッシュクリーンアップと不要なリストの削除
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
# リナックスコマンドのパッケージインストール
RUN apt-get update && apt-get install -y vim less sudo tree
# pip関連
RUN pip install --upgrade pip

RUN pip install --upgrade setuptools

# ポスグレにアクセスをするライブラリ2つ
RUN pip install --upgrade psycopg2
RUN pip install --upgrade sqlalchemy
# mongoにアクセスするためのライブラリ
RUN pip install --upgrade pymongo

# コードスタイルの制約をするライブラリ
RUN pip install --upgrade pep8
RUN pip install --upgrade flake8
RUN pip install --upgrade pylint

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8010