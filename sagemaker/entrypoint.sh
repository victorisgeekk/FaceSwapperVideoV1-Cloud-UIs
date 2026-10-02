#!/bin/bash
set -e

python -m pip install --upgrade pip
if [ -f /opt/program/requirements.txt ]; then
  pip install -r /opt/program/requirements.txt
fi

# Optionally install upstream ML requirements if provided inside image or mounted path
if [ -f /opt/program/FaceSwapperVideoV1/requirements.txt ]; then
  pip install -r /opt/program/FaceSwapperVideoV1/requirements.txt
fi

exec uvicorn app:app --host 0.0.0.0 --port 8080
