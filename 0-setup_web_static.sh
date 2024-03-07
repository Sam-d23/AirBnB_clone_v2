#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static.

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
    apt-get update
    apt-get install -y nginx
fi

# Create necessary directories
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "<html>
  <head></head>
  <body>
    Fake Content to Test Nginx Configuration
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create or recreate symbolic link
rm -f /data/web_static/current
ln -s /data/web_static/releases/test /data/web_static/current

# Give ownership to ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config_block="
server {
    listen 80;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }

    location /redirect_me {
        return 301 https://www.youtube.com;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /usr/share/nginx/html;
        internal;
    }
}
"

# Remove default Nginx configuration and add the custom one
rm -f /etc/nginx/sites-enabled/default
echo "$config_block" > /etc/nginx/sites-available/web_static
ln -s /etc/nginx/sites-available/web_static /etc/nginx/sites-enabled/web_static

# Restart Nginx
service nginx restart

exit 0
