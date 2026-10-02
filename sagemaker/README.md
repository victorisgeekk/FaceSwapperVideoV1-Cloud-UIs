# SageMaker deployment guide (မြန်မာ)

ဒီအောက်ပါအဆင့်များသည် SageMaker သို့ Docker image တင်ပြီး endpoint ဖန်တီးရန် လိုအပ်သည့် အချက်များဖြစ်သည်။

1) Docker image ပြင်ဆင်ခြင်း
- sagemaker/Dockerfile ကို အသုံးပြုပါ။ Upstream repo ကို image ထဲတွင် ထည့်လိုလျှင် `COPY` သို့မဟုတ် `git clone` နည်းလမ်းဖြင့် ထည့်နိုင်သည်။

2) Build & Push to ECR (AWS)
```bash
# AWS CLI and Docker installed
aws ecr create-repository --repository-name faceswapper-video
$(aws ecr get-login --no-include-email --region YOUR_REGION)
docker build -t faceswapper-video:latest -f sagemaker/Dockerfile .
docker tag faceswapper-video:latest <AWS_ACCOUNT_ID>.dkr.ecr.YOUR_REGION.amazonaws.com/faceswapper-video:latest
docker push <AWS_ACCOUNT_ID>.dkr.ecr.YOUR_REGION.amazonaws.com/faceswapper-video:latest
```

3) SageMaker Model & Endpoint ဖန်တီးခြင်း
- SageMaker console သို့သွား၍ Model ဖန်တီးစဉ်တွင် ECR Image URI ထည့်ပါ။
- Endpoint Configuration & Endpoint ဖန်တီးပါ။ GPU instance (ml.g4dn.xlarge သို့မဟုတ် ပိုကြီး) အသုံးပြုရန် ရွေးပါ။

4) Repo placement & dependencies
- Upstream FaceSwapperVideoV1 repo ကို /opt/program/FaceSwapperVideoV1 အောက်တွင် mount လုပ်ပါ၊ ဒါမှမဟုတ် build ဆောင်ရွက်ချိန်တွင် image ထဲသို့ copy လုပ်ပါ။
- Upstream repo ၏ requirements.txt က အလေးအနက်ကြီးသည် — container ထဲတွင် pip install ပြုလုပ်ရာတွင် အချိန်ကြာတတ်သည်။

5) API နမူနာ
- POST /swap endpoint သည် video + source_face file ကို လက်ခံပြီး result.mp4 ကို ပြန်ပေးပါသည်။

6) သတိပေးချက်
- production အတွက် persistent storage (S3) ကို သတ်မှတ်၍ uploaded files နှင့် output တွေကို S3 သို့ သိမ်းဆည်းရန် configure လုပ်ပါ။
- model cache ကို EFS သို့ သိုလှောင်ရန် ပြင်ဆင်ပါ။
