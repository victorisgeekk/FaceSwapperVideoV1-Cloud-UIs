import os
import subprocess
import threading
import time
import gradio as gr
import qrcode
from pycloudflared import Tunnel

# Upstream Repository Clone ပြုလုပ်ခြင်း (မရှိသေးပါက)
if not os.path.exists("cli.py"):
  subprocess.run([
      "git",
      "clone",
      "https://github.com/Deci1337/FaceSwapperVideoV1.git",
      ".",
  ])


def run_faceswap(source_img, target_vid, target_face_index, enhancer, fidelity):
  if not source_img or not target_vid:
    return None
  output_path = "/tmp/sagemaker_output.mp4"

  cmd = [
      "python",
      "cli.py",
      "--source",
      source_img,
      "--target",
      target_vid,
      "--output",
      output_path,
      "--execution-provider",
      "cuda",
      "--execution-threads",
      "8",
      "--color-matching",
      "seamless",
      "--target-face-index",
      str(int(target_face_index)),
  ]

  if enhancer != "none":
    cmd.extend(
        ["--face-enhancer", enhancer, "--codeformer-fidelity", str(fidelity)]
    )

  subprocess.run(cmd)
  return output_path


def launch_ui():
  with gr.Blocks(title="SageMaker FaceSwapper") as demo:
    gr.Markdown("## 🚀 AWS SageMaker FaceSwapper (Multi-Face Target Lock)")
    with gr.Row():
      with gr.Column():
        src = gr.Image(type="filepath", label="1. Source Face Image")
        tgt = gr.Video(label="2. Target Video")
        f_idx = gr.Number(
            value=0, precision=0, label="Target Face Index (0, 1, 2...)"
        )
        enh = gr.Radio(
            ["none", "codeformer", "gfpgan"],
            value="codeformer",
            label="Face Enhancer Quality",
        )
        fid = gr.Slider(0.1, 1.0, value=0.8, label="CodeFormer Fidelity")
        btn = gr.Button("🚀 Lock Face & Start Swap", variant="primary")
      with gr.Column():
        out = gr.Video(label="Output Result")
    btn.click(run_faceswap, inputs=[src, tgt, f_idx, enh, fid], outputs=out)

  demo.launch(
      server_name="0.0.0.0",
      server_port=7860,
      prevent_thread_lock=True,
      quiet=True,
  )


if __name__ == "__main__":
  threading.Thread(target=launch_ui, daemon=True).start()
  time.sleep(3)

  try:
    tunnel_url = Tunnel.start(port=7860)
    pub_url = tunnel_url.get_url()
    print(
        "\n" + "=" * 60 + f"\n🚀 SAGEMAKER PUBLIC URL: {pub_url}\n" + "=" * 60 + "\n"
    )
    qr = qrcode.QRCode()
    qr.add_data(pub_url)
    qr.print_ascii(invert=True)
  except Exception as e:
    print(f"SageMaker Tunnel Error: {e}")

  # Background Server အနေဖြင့် အလုပ်လုပ်စေရန် Loop ပတ်ထားခြင်း
  while True:
    time.sleep(3600)
