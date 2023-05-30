#!/bin/sh

# Create config.js with the current value of the API_URL environment variable
echo "window.API_URL = '${API_URL:-http://localhost:8000}';" > /usr/share/nginx/html/config.js

# Start Nginx server
nginx -g 'daemon off;'
