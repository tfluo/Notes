# MySQL
## pull docker
* docker pull mysql
## run container
1. 将容器内部/var/lib/mysql目录下的数据存储到docker宿主机的$PROJECT/mysql/data目录下，密码为my-secret-w  
* docker run --name $MYSQL_CONTAINER -v $PROJECT/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql  
2. 查看mysql在容器中的IP  
* docker ps  
* docker inspect $MYSQL_CONTAINER | grep IPAddress  
3. 进入mysql容器查看数据库  
* docker exec -it $MYSQL_CONTAINER /bin/bash  
* mysql -uroot -pmy-secret-pw  
