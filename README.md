# restapi
restapi

### Execute
FLASK_APP=restapi.py flask run

### Usage
$ curl localhost:5000/tasks
{"message":{"1":"スーパーで買い物をする","2":"Netflixを見る"}}

$ curl localhost:5000/tasks/1
{"message":"スーパーで買い物をする"}

$ curl -X POST -H 'Content-Type:application/json' -d '{"task": "ジムに行く"}' localhost:5000/tasks
{"message":"New task created"}

$ curl -X DELETE localhost:5000/tasks/2
{"message":"Task 2 deleted"}

$ curl localhost:5000/tasks
{"message":{"1":"スーパーで買い物をする","3":"ジムに行く"}}

$ curl -X PUT -H 'Accept:application/json' -H 'Content-Type:application/json' -d '{"task": "映画館に行く"}' localhost:5000/tasks/3
{"message":"Task 3 updated"}

$ curl localhost:5000/tasks
{"message":{"1":"スーパーで買い物をする","3":"映画館に行く"}}
