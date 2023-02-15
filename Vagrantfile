Vagrant.configure("2") do |config|
  config.vm.box = "ilionx/ubuntu2204"
  config.vm.hostname = "task"
  config.vm.network "forwarded_port", adapter: 2, guest: 80, host: 8080, host_ip: "0.0.0.0"
  config.vm.network "public_network", adapter: 2, ip: "192.168.0.40", bridge: "enp0s25", hostname: true
  config.vm.provider "virtualbox" do |vb|
	vb.memory = "1024"
  end
end
