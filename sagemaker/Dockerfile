# SageMaker Dockerfile (GPU-capable)
# Uses an official PyTorch image with CUDA 11.8 runtime

FROM pytorch/pytorch:2.2.0-cuda11.8-cudnn8-runtime

WORKDIR /opt/program

# Copy only the minimal runtime requirements for the API service
COPY sagemaker/requirements.txt /opt/program/requirements.txt
RUN pip install --upgrade pip && pip install -r /opt/program/requirements.txt

# Copy the FastAPI app
COPY sagemaker/app.py /opt/program/app.py
COPY sagemaker/entrypoint.sh /opt/program/entrypoint.sh
RUN chmod +x /opt/program/entrypoint.sh

# The upstream FaceSwapperVideoV1 repo is expected to be mounted into /opt/program/FaceSwapperVideoV1
# or added into the image at build time if desired. Large ML deps will be installed from its requirements.txt.

EXPOSE 8080

ENTRYPOINT ["/opt/program/entrypoint.sh"]
