# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

setup=<<EOF
sudo sed -i "s/^DEFAULT_FORWARD_POLICY="DROP"/DEFAULT_FORWARD_POLICY="ACCEPT"/" /etc/default/ufw
sudo ufw reload
sudo ufw allow 4243/tcp
EOF



BOX_NAME="raring"
BOX_URL="http://cloud-images.ubuntu.com/vagrant/%s/current/%s-ops-cloudimg-amd64-vagrant-disk1.box" % [BOX_NAME, BOX_NAME]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box_url = BOX_URL
  config.vm.define "web", :default => true do |web|
    web.vm.box = BOX_NAME
    web.vm.network :private_network, ip: "172.16.0.12"
    web.vm.provision :fabric do |fabric|
      fabric.fabfile_path = "provisioning/setup.py"
      fabric.tasks = ["web"]
    end
    web.vm.synced_folder "files", "/files"
  end
  config.vm.define "dev" do |dev|
    dev.vm.box = BOX_NAME
    dev.vm.network :private_network, ip: "172.16.0.13"
    dev.vm.provision :fabric do |fabric|
      fabric.fabfile_path = "provisioning/setup.py"
      fabric.tasks = ["dev"]
    end
    dev.vm.synced_folder "files", "/files"
    dev.vm.synced_folder "~/Dropbox/Public/docker", "/app"
  end
  config.vm.define "ops" do |ops|
    ops.vm.box = BOX_NAME
    ops.vm.network :private_network, ip: "172.16.0.14"
    ops.vm.provider :virtualbox do |virtualbox|
      virtualbox.customize ["modifyvm", :id, "--cpus", "2"]
      virtualbox.customize ["modifyvm", :id, "--memory", "4096"]
    end
    ops.vm.provision :fabric do |fabric|
      fabric.fabfile_path = "provisioning/setup.py"
      fabric.tasks = ["ops"]
    end
    ops.vm.synced_folder "files", "/files"
  end
end
