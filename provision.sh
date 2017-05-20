#!/usr/bin/env bash

# Helpful instructions:
# https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04
# https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04
# https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04
# https://github.com/craighurley/vagrant-cloud-init
# https://www.digitalocean.com/community/tutorials/how-to-use-cloud-config-for-your-initial-server-setup

# Add the nginx package repo.
#$ cat <<EOF > /etc/apt/sources.list.d/nginx.list
#deb http://nginx.org/packages/ubuntu/ xenial nginx
#deb-src http://nginx.org/packages/ubuntu/ xenial nginx
#EOF

# Install nginx
#apt-get update
#apt-get install -y nginx
#
## Allow nginx through the firewall (port 80).
## When we do HTTPS, we'll want 'Nginx Full' for both 80/443.
#ufw allow 'Nginx HTTP'
#


# This script runs cloud-init, useful as a Vagrant provisioning script.

# Exit on any failure, showing lines as executed.
set -ex

# Do the cloud-init.
cloud-init init
cloud-init modules
