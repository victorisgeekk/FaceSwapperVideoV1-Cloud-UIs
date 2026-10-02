#!/bin/bash
set -e

python -m pip install --upgrade pip
pip install -r /opt/program/requirements.txt

exec uvicorn app:app --host 0.0.0.0 --port 8080
