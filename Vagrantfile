# -*- mode: ruby -*-
# vi: set ft=ruby :
VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "sonos/trusty64"
  config.vm.box_url = "http://archives.sonos.com/machines/vagrant/trusty64.json"
  config.vm.box_version = "~> 1.1"
  config.vm.provider :virtualbox do |vb|
    # Useful if you need to see what's going on during boot.
    #vb.gui = true
    # Use VBoxManage to customize the VM. For example to change memory:
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "manifests"
    puppet.manifest_file  = "site.pp"
    puppet.module_path  = ["modules", "thirdparty/modules"]
    puppet.options  = "--verbose --debug"
  end
end