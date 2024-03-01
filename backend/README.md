# Yego Backend

## Create virtual environment
Run command under `/backend` directory

### For windows user(Powershell)
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

### For MacOS/Linux user
```
python3 -m venv .venv;
source .venv/bin/activate;
pip3 install -r requirements.txt
```

## Startup docker

- docker 啟動資料庫:
```
docker run --name yego_database -e MYSQL_USER=admin -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=yego -p 8888:3306 -d mysql:8.1
```