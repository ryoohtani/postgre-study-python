## For learning PostgreSQL operations and sql in Python
## PythonでPostgreSQLの操作及びsqlの学習用

<sub> Learning Python to practice sql operations and develop functions for data extraction and table joins. </sub>

<sub> Pythonの学習でsqlの操作練習やデータ抽出やテーブル結合の機能の開発。 </sub>

**環境構築**

*dockerコマンド*

* ビルドコマンド
```
docker-compose build
```
* 環境の立ち上げ
```
docker-compose up -d
```
* Pythonのコンテナにアクセス
```
docker exec -it sql-python /bin/bash
```

* PostgreSQLのコンテナにアクセス
```
docker exec -it postgres-db /bin/bash  
```

* pgadmin4のコンテナにアクセス
```
docker exec -it pgadmin4-db /bin/bash  
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
* PGAdmin4とPostgreSQLを使用

<img width="361" alt="part0" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/1ab55e10-074c-493f-9880-7be1a2e7e936">

*アプリ実行後のDB*
* learning_table

<img width="388" alt="スクリーンショット 2023-08-09 9 03 31" src="https://github.com/ryoohtani/simple-chatbot-python/assets/139527783/f081d7f1-bf26-4909-bd05-7fac3393c67a">

* subid_table

*アプリ実行後のCLI*

*テーブル結合*