first:
	@ echo first

upgrade-ubuntu:
	sudo apt update
	sudo apt -y upgrade

install-python: upgrade-ubuntu
	sudo apt install -y python3-pip

install-openSSL: upgrade-ubuntu
	sudo apt install build-essential checkinstall zlib1g-dev -y

install-cmake: upgrade-ubuntu install-openSSL
	sudo apt install cmake
	sudo apt-get install poppler-utils

.PHONY:
	echo "No command specified"

defualt: .PHONY
