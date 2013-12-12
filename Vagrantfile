# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

BOX_NAME="raring"
BOX_HOST = "cloud-images.ubuntu.com"
BOX_DIR = "vagrant/%s/current" % [BOX_NAME]
BOX_FILE = "%s-ops-cloudimg-amd64-vagrant-disk1.box" % [BOX_NAME]
BOX_URL = "http://%s/%s/%s" % [BOX_HOST, BOX_DIR, BOX_FILE]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box_url = BOX_URL
  config.vm.define "registry", :default => true do |registry|
    registry.vm.box = BOX_NAME
    registry.vm.network :private_network, ip: "172.16.0.12"
    registry.vm.provision :shell do |shell|
      shell.path = "provisioning/shell/setup.sh"
      shell.args = %q(_registry)
    end
    registry.vm.synced_folder "files", "/files"
  end
  config.vm.define "dev" do |dev|
    dev.vm.box = BOX_NAME
    dev.vm.network :private_network, ip: "172.16.0.13"
    dev.vm.provision :shell do |shell|
      shell.path = "provisioning/shell/setup.sh"
      shell.args = %q(_dev)
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
    ops.vm.provision :shell do |shell|
      shell.path = "provisioning/shell/setup.sh"
      shell.args = %q(_ops)
    end
    ops.vm.synced_folder "files", "/files"
  end
end
