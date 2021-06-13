#!/usr/bin/env bash
# Set up web servers for web_static deployment
# Add symbolic link for /web_static page inside my website
# Test by "curl localhost/hbnb_static/index.html"

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo service nginx start

# Add neccessary directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Add temp data to html file for testing purposes
sudo touch /data/web_static/releases/test/index.html
sudo echo "Platypus" | sudo tee /data/web_static/releases/test/index.html

# Add symbolic link "current" that points to "test" folder
# -s is symbolic, -f removes existing destination files so only points to one at a time
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give data folder ownership to ubuntu user/group
# -R is recursive, meaning everything inside also changes ownership
sudo chown -R ubuntu:ubuntu /data

# Add web_static option to config file that searches "current" link
# Link will always point at latest info (index.html in this case) in test folder
find="\tlocation / {"
replace="\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {"
sudo sed -i "s@^${find}@${replace}@" /etc/nginx/sites-available/default

# Restart to apply changes
sudo service nginx restart

# Exit code 0
exit 0