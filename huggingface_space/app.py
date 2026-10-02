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
  output_path = "output_cloud.mp4"

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
      "4",
      "--color-matching",
      "seamless",
      "--target-face-index",
      str(int(target_face_index)),  # Auto Detect & Face Lock Index
  ]

  if enhancer != "none":
    cmd.extend(
        ["--face-enhancer", enhancer, "--codeformer-fidelity", str(fidelity)]
    )

  subprocess.run(cmd)
  return output_path


# Gradio Web UI Layout
with gr.Blocks(title="FaceSwapper Cloud UI") as demo:
  gr.Markdown("## 🎭 FaceSwapper (Multi-Face Target Selection & Lock)")
  with gr.Row():
    with gr.Column():
      src_input = gr.Image(type="filepath", label="1. Source Face Image")
      tgt_input = gr.Video(label="2. Target Video")

      gr.Markdown("---")
      face_index = gr.Number(
          value=0,
          precision=0,
          label="Target Face Index (0 = First detected face, 1 = Second face,"
          " etc.)",
          info="ဗီဒီယိုထဲတွင် လူအများပါက မည်သည့်မျက်နှာကို လဲမည်နည်း (0, 1, 2..."
          " ရွေးပေးပါ)",
      )

      enhancer_opt = gr.Radio(
          ["none", "codeformer", "gfpgan"],
          value="codeformer",
          label="Face Enhancer Quality",
      )
      fidelity_slider = gr.Slider(
          0.1, 1.0, value=0.8, label="CodeFormer Fidelity"
      )
      btn = gr.Button("🚀 Lock Face & Start Swap", variant="primary")
    with gr.Column():
      video_output = gr.Video(label="Output Result")

  btn.click(
      run_faceswap,
      inputs=[
          src_input,
          tgt_input,
          face_index,
          enhancer_opt,
          fidelity_slider,
      ],
      outputs=video_output,
  )

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 7860))

  # Cloudflare Tunnel Auto Launch
  try:
    tunnel_url = Tunnel.start(port=port)
    pub_url = tunnel_url.get_url()
    print(
        "\n" + "=" * 60 + f"\n🚀 PUBLIC URL: {pub_url}\n" + "=" * 60 + "\n"
    )
    qr = qrcode.QRCode()
    qr.add_data(pub_url)
    qr.print_ascii(invert=True)
  except Exception as e:
    print(f"Tunnel Notice: {e}")

  # Gradio Web UI Auto Launch
  demo.launch(server_name="0.0.0.0", server_port=port)
   
