# HF Space deployment notes (မြန်မာ)

ကျွန်တော်တို့သည် Hugging Face Space အတွက် demo-mode UI တစ်ခုကို ထုတ်ပေးထားသည်။
ဒီမျိုးသော UI သည် ဖိုင်များ preview ပြသပေးနိုင်သော်လည်း heavy ML pipeline ကို Space အတွင်း run မလုပ်ပါ။

အကြံပြုချက်များ
- Full face-swap runs အတွက် Colab / Kaggle / SageMaker သို့ သွားရန် link များထည့်ထားပါသည်။
- Hugging Face Space ကို production-level GPU အဖြစ် အသုံးပြုချင်ပါက private container image (Docker) ကို prebuild လုပ်၍ ECR သို့ push ပြီး HF Space မှင်ကိုပင် pull လုပ်ရန် (paid plan) အကြံပြုသည်။

