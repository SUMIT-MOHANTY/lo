#!/bin/bash
set -e

echo "Starting production server with Gunicorn..."
cd /workspace
exec gunicorn --config gunicorn.conf.py "app:create_app()"
