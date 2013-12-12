from fabric.api import run
from fabric.api import sudo
from fabric.api import put

def web():
  sudo("apt-get -qq update")
  sudo("apt-get install -y nginx")
  put("files/nginx/default", "/etc/nginx/sites-enabled/default", use_sudo=True)
  sudo("service nginx restart")

def docker():
  sudo("wget -q -O - https://get.docker.io/gpg | apt-key add -")
  put("files/docker.list", "/etc/apt/sources.list.d/docker.list", use_sudo=True)
  sudo("apt-get -qq update")
  sudo("apt-get -qq install -y lxc-docker")

def clean():
  sudo("docker ps -q | while read cid;do docker stop $cid;done")
  sudo("docker images | grep helloworld | while read rep tag img rest;do docker rmi $img;done")

def dev():
  docker()
  clean()
  sudo("docker pull ubuntu")
  sudo("docker build -t=helloworld:latest /files/dev")
  sudo("docker run -d -p=8080:8080 helloworld /var/java/run")
  sudo("docker export $(docker ps -q) >/files/helloworld.tar")

def ops():
  docker()
  clean()
  sudo("docker import http://172.16.0.12/helloworld.tar helloworld:latest")
  sudo("docker run -d -p=8081:8080 -m=256m -c=2048 helloworld /var/java/run")
  sudo("docker run -d -p=8082:8080 -m=512m -c=1024 helloworld /var/java/run")
