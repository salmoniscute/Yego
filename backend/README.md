- docker 啟動資料庫:

    - docker run --name yego_database -e MYSQL_USER=admin -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=yego -p 8888:3306 -d mysql:8.1