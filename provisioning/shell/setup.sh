#!/bin/bash

_docker() {
  wget -qO - https://get.docker.io/gpg | apt-key add -
  cp /files/docker.list /etc/apt/sources.list.d
  apt-get -qq update || exit $?
  apt-get -qq install -y lxc-docker
  docker pull ubuntu 
  eval "$@"
}

_registry() {
  _docker
} 
_dev() {
  _docker
}

_ops() {
  _docker
}

eval "$@"
