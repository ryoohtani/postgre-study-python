## For learning PostgreSQL operations and sql in Python
## PythonでPostgreSQLの操作及びsqlの学習用

<sub> Learning Python to develop sql manipulation and data extraction functions. </sub>

<sub> Pythonの学習でsqlの操作やデータ抽出機能を開発。 </sub>

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
git remote add origin3 URLを貼り付ける
```

* リモートリポジトリへプッシュ
```
git push -u origin3 main
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
git merge origin3/main
```