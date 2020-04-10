# MySQL
## enable ipv4 forward
1. edit /etc/sysctl.conf
* net.ipv4.ip_forward=1
2. restart network
* systemctl restart network
## pull docker
* docker pull mysql
## run container
1. 将容器内部/var/lib/mysql目录下的数据存储到docker宿主机的$PROJECT/mysql/data目录下，密码为my-secret-w  
* docker run --name $MYSQL_CONTAINER -v $PROJECT/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql  
## edit container
1. 备份sources.list
* cp /etc/apt/sources.list /root/
2. 更换apt-get的源
```sh
cat > /etc/apt/sources.list <<HERE
deb http://mirrors.ustc.edu.cn/debian buster main
deb http://security.debian.org/debian-security buster/updates main
deb http://mirrors.ustc.edu.cn/debian buster-updates main
HERE
```
3. apt-get update
4. apt-get install vim .....
5. edit /root/.bashrc
```sh
 export LS_OPTIONS='--color=auto'
 alias ls='ls $LS_OPTIONS'
 alias ll='ls $LS_OPTIONS -l'
 alias l='ls $LS_OPTIONS -lA'
 alias rm='rm -i'
 alias cp='cp -i'
 alias mv='mv -i'
```
6. commit container
* docker commit $MYSQL_CONTAINER $NEW_MYSQL_IMAGE:$VERSION
## run new container
1. docker stop $MYSQL_CONTAINER
2. docker rm $MYSQL_CONTAINER
3. docker run
* docker run --name $MYSQL_CONTAINER -v $PROJECT/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d $NEW_MYSQL_IMAGE:$VERSION
4. 查看mysql在容器中的IP  
* docker ps  
* docker inspect $MYSQL_CONTAINER | grep IPAddress  
5. 进入mysql容器查看数据库  
* docker exec -it $MYSQL_CONTAINER /bin/bash  
* mysql -uroot -pmy-secret-pw  
6. 修改mysql密码认证
* alter user 'root'@'%' identified with mysql_native_password by 'my-secret-pw';

## create database
* CREATE DATABASE IF NOT EXISTS iabas DEFAULT CHARSET utf8 COLLATE utf8_general_ci;
