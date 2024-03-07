# Yego Backend

Run all command under `/backend` directory

## Create/Start virtual environment

### For windows user (Powershell)

1. Create virtual environment
```
python -m venv .venv
```

2. Start virtual environment
```
.\.venv\Scripts\activate
```

3. Install python packages
```
pip install -r requirements.txt
```

### For MacOS/Linux user
1. Create virtual environment
```
python -m venv .venv
```

2. Start virtual environment
```
source .venv/bin/activate;
```

3. Install python packages
```
pip install -r requirements.txt
```

## Startup database by Docker

1.  Pull MySQL image
```
docker pull mysql:8.1
```

2. Run container
```
docker run --name yego_database -e MYSQL_USER=admin -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=yego -p 8888:3306 --volume yego_mysql:/var/lib/mysql -d mysql:8.1
```

## Start uvicorn server
```
python main.py
```
