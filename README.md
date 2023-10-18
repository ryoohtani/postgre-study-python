## For learning PostgreSQL operations and sql in Python
## PythonでPostgreSQLの操作及びsqlの学習用

<sub> Learning Python to practice sql operations and develop functions for data extraction and table joins. </sub>

<sub> Pythonの学習でsqlの操作練習やデータ抽出やテーブル結合の機能の開発。 </sub>

**環境構築**

*dockerコマンド*

* ビルドコマンド
```
docker compose build
```
* 環境の立ち上げ
```
docker compose up -d
```
* Pythonのコンテナにアクセス
```
docker exec -it sql-python bash
```

* PostgreSQLのコンテナにアクセス
```
docker exec -it postgres-db bash  
```

* pgadmin4のコンテナにアクセス
```
docker exec -it pgadmin4-db bash  
```

*Pythonのコマンド*

* set.py(Pythonのパッケージをビルド、インストール、配布する際の必要情報記載)
```
python setup.py sdist
```

*gitコマンド*

* ローカルリポジトリの新規作成
```
git init
```

* ファイルの追跡(変更分全て)
```
git add .
```

* コミット
```
git commit
```

* ローカルリポジトリにリモートリポジトリのURLを貼り付ける
```
git remote add source URLを貼り付ける
```

* リモートリポジトリへプッシュ
```
git push -u source main
```

* リモートリポジトリからローカルに反映
```
git fetch
```

* ブランチの移動
```
git checkout main
```

* マージ
```
git merge source/main
```

---

**Pythonコードスタイルガイド**
* pep8
```
pep8 対象ファイル
```

* flake8
```
flake8 対象ファイル
```

* pylint
```
pylint 対象ファイル
```
---
*アプリ実行前のDB*
* PGAdmin4とPostgreSQLを使用(ソースコード配置場所は以下)\
/core/backend/py/models

![実行前のDB](https://github.com/ryoohtani/postgre-study-python/assets/139527783/e2b5465e-2097-46b1-94e4-73f9507852b4)

*アプリ実行後のDB*
* learning_table

![lt](https://github.com/ryoohtani/postgre-study-python/assets/139527783/c4ca9b52-698e-4fc8-8e9d-1f9f31e137bf)

* subid_table

![st](https://github.com/ryoohtani/postgre-study-python/assets/139527783/8c154999-3309-4164-978f-4785cccbaf0e)

*アプリ実行後のCLI*

<img width="419" alt="アプリ実行後のcli" src="https://github.com/ryoohtani/postgre-study-python/assets/139527783/947bd175-e69e-435a-a90e-4122e5e59032">

*テーブル結合*

<img width="595" alt="join" src="https://github.com/ryoohtani/postgre-study-python/assets/139527783/3181ce67-a5f8-473a-93bf-65a5a5a34350">

---
**sqlalchemyのCRUDアプリ(通常のSQL文と比較用)**

*sqlalchemyのソースコード配置場所\
/core/backend/py/sqlalc/models*

*動画でのCRUDアプリ動作検証*

*creat実施*

https://github.com/ryoohtani/postgre-study-python/assets/139527783/38fa86ad-979f-42f4-ac36-da180904a979

*insert実施*

https://github.com/ryoohtani/postgre-study-python/assets/139527783/0f6e4978-c972-459f-825e-d166e8f71539

*update実施*

https://github.com/ryoohtani/postgre-study-python/assets/139527783/2f94a578-95ac-4804-b7f7-0f2ab5cad707

*delete実施*

https://github.com/ryoohtani/postgre-study-python/assets/139527783/2687ce75-d45e-44c9-926e-03977bdd15bc

*selectとjoin実施*

https://github.com/ryoohtani/postgre-study-python/assets/139527783/b05b6d6e-847a-4d3d-b8c7-abaddae18ee4
