# Python3
## pull docker
* docker pull rackspacedot/python37
## update in container
* mkdir /opt/app 
* docker create -i --name python3_base -v $(pwd):/app -w /app rackspacedot/python37 /bin/bash
* docker start python3_base
* docker exec -it python3_base /bin/bash
  * pip install -i https://mirrors.ustc.edu.cn/pypi/web/simple pip -U
  * pip config set global.index-url https://mirrors.ustc.edu.cn/pypi/web/simple
* exit
## create a new docker image and remove baseline container
* docker commit -m="Comment" -a="Author" python3_base python3_base:$VERSION
* docker kill python3_base
* docker rm python3_base
## create a new container and coding
* docker create -i --name $APPNAME -p 80:8080 -p 81:8081-v $(pwd):/app -w /app python3_base:$VERSION /bin/bash
* docker start $APPNAME
* docker exec -it $APPNAME /bin/bash

## move docker image
* docker commit -m="Comment" -a="Author" $APPNAME $APPNAME:$TAGNAME
* docker save $IMAGENAME $DOCKER_FILE
* docker load < $DOCKER_FILE

## usage
* docker run  -v /usr/src/file:/usr/src/file  -w /usr/src/file rackspacedot/python37 python path.py
* ...
