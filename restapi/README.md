# restapi
restapi

# Usage 

## Debug with Python
export FLASK_APP=app.py; flask run  #環境変数でFlaskを起動せよ。
python -m flask run 
python app.py # gunicornなしでapp.pyを動かせ

## install
pip install -r requirements.txt
- install linter and coding tools for PEP8
pip install black flake8 isort mypy

## DB
flask db init
flask db migrate
flask db upgrade

## Run with gunicorn
- 設定ファイルを参考にGunicornを動かせ
gunicorn -c ./gunicorn_setting.py   
- wsgi.pyのエントリポイントappをgunicornで動かせ。wsgiはxx.py
gunicorn --bind 0.0.0.0:8080 wsgi:app 	

## Run with Docker
docker build -t restapi:1.0.1 .
docker run -p 8080:8080 -t restapi:1.0.1

docker login
docker tag restapi:1.7 shige7822/restapi
docker push shige7822/restapi

## Jupyterlab
pip install scikit-learn jupyterlab numpy matplotlib
jupyter lab
```
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.DESCR)
```
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets



## Unit test
- unit test
pytest {folder}
pytest {python script}
pytest {python script}::{function}

- 共通部分は、confest.pyにまとめる

- check coverage
pip install pytestcov
pytest test/test_preparation.py --cov



## Test api
curl localhost:5000/tasks
{"message":{"1":"スーパーで買い物をする","2":"Netflixを見る"}}

curl localhost:5000/tasks/1
{"message":"スーパーで買い物をする"}

curl -X POST -H 'Content-Type:application/json' -d '{"task": "ジムに行く"}' localhost:5000/tasks
{"message":"New task created"}

curl -X DELETE localhost:5000/tasks/2
{"message":"Task 2 deleted"}

curl localhost:5000/tasks
{"message":{"1":"スーパーで買い物をする","3":"ジムに行く"}}

curl -X PUT -H 'Accept:application/json' -H 'Content-Type:application/json' -d '{"task": "映画館に行く"}' localhost:5000/tasks/3
{"message":"Task 3 updated"}

curl localhost:5000/tasks
{"message":{"1":"スーパーで買い物をする","3":"映画館に行く"}}

curl -X POST -H 'Content-Type:application/json' -d '{"id": "1", "name": "ジムに行く", "description": "ジムに行く2"}' localhost:5000/tasks

## Error Case

https://qiita.com/kitarikes/items/9c5d6cbc557ed62bb512