# Food Logs

This is a food logging service made up of a Postgres database and a FastAPI backend which are launched with Docker.

## Usage

### Launch the services

```
docker-compose up
```

### Add food logs

```
curl -X POST localhost:8000/logs/ -H "Content-Type: application/json" -d '{"date": "2024-01-01", "name": "Apple", "calories": 90}'
curl -X POST localhost:8000/logs/ -H "Content-Type: application/json" -d '{"date": "2024-01-01", "name": "Apple", "calories": 90}'
curl -X POST localhost:8000/logs/ -H "Content-Type: application/json" -d '{"date": "2024-01-01", "name": "Chicken", "calories": 300}'
curl -X POST localhost:8000/logs/ -H "Content-Type: application/json" -d '{"date": "2024-01-01", "name": "Brocoli", "calories": 120}'
curl -X POST localhost:8000/logs/ -H "Content-Type: application/json" -d '{"date": "2024-01-02", "name": "Apple", "calories": 90}'
curl -X POST localhost:8000/logs/ -H "Content-Type: application/json" -d '{"date": "2024-01-02", "name": "Milk", "calories": 220}'
curl -X POST localhost:8000/logs/ -H "Content-Type: application/json" -d '{"date": "2024-01-03", "name": "Rice", "calories": 400}'
curl -X POST localhost:8000/logs/ -H "Content-Type: application/json" -d '{"date": "2024-01-03", "name": "Banana", "calories": 100}'
curl -X POST localhost:8000/logs/ -H "Content-Type: application/json" -d '{"date": "2024-01-04", "name": "Pizza", "calories": 1000}'
```

### See the food logs

```
curl localhost:8000/logs/
```

### Delete a food log

```
curl -X DELETE localhost:8000/logs/2
```

### See the summary info

```
curl localhost:8000/logs/summary
```

### Search the names of the food logs using regular expressions

```
curl "localhost:8000/logs/search?name_pattern=A.*"
curl "localhost:8000/logs/search?name_pattern=.*n.*n"
```
