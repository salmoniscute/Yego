@echo off
docker stop yego_database
docker rm yego_database
docker volume rm yego_mysql
docker run --name yego_database -e MYSQL_USER=admin -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=yego -p 8888:3306 --volume yego_mysql:/var/lib/mysql -d mysql:8.1