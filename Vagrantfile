# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

setup=<<EOF
wget -q -O - https://get.docker.io/gpg | sudo apt-key add -
echo deb http://get.docker.io/ubuntu docker main | sudo dd of=/etc/apt/sources.list.d/docker.list
sudo apt-get -qq update >/dev/null
sudo apt-get -qq install -y lxc-docker
sudo sed -i "s/^DEFAULT_FORWARD_POLICY="DROP"/DEFAULT_FORWARD_POLICY="ACCEPT"/" /etc/default/ufw
sudo ufw reload
sudo ufw allow 4243/tcp
test ! -f winstone-1.0.5-boot.jar && wget -q https://winstone.googlecode.com/files/winstone-1.0.5-boot.jar
for file in helloworld.war servlet-api.jar run Dockerfile; do
  cp /files/${file} .
done
sudo docker stop $(sudo docker ps -q)
sudo docker build -t openjdk-6-jre-headless .
sudo docker run -d -p 8081:8080 -m=1g -c=2048 openjdk-6-jre-headless /var/java/run
sudo docker run -d -p 8082:8080 -m=512m -c=4096 openjdk-6-jre-headless /var/java/run
sudo docker ps -q
EOF


BOX_NAME="raring"
BOX_URL="http://cloud-images.ubuntu.com/vagrant/%s/current/%s-server-cloudimg-amd64-vagrant-disk1.box" % [BOX_NAME, BOX_NAME]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box_url = BOX_URL
  config.vm.define "server", :default => true do |server|
    server.vm.box = BOX_NAME
    server.vm.provision :shell, :inline => setup
    server.vm.synced_folder "files", "/files"
    server.vm.network :private_network, ip: "172.16.0.12"
    server.vm.provider :virtualbox do |virtualbox|
      virtualbox.customize ["modifyvm", :id, "--cpus", "2"]
      virtualbox.customize ["modifyvm", :id, "--memory", "4096"]
    end
  end
  config.vm.define "client", :default => true do |client|
    client.vm.box = BOX_NAME
    client.vm.synced_folder "files", "/files"
    client.vm.network :private_network, ip: "172.16.0.13"
  end
end
