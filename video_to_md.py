import os

from dotenv import load_dotenv
import whisper
from moviepy import VideoFileClip
from openai import OpenAI
from tqdm import tqdm

load_dotenv()

# whisper_model = "large-v3"
whisper_model = "large-v3-turbo"
# whisper_model = "base"
video_path = r"D:\PycharmProjects\advanced-python\files"


def extract_audio_from_video(video_path, audio_path):
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        audio.close()
        video.close()
        print("音频提取完成")
    except Exception as e:
        print(f"音频提取失败: {e}")


def audio_to_text(audio_path: str):
    try:
        model = whisper.load_model(whisper_model, device="cuda", download_root=r"D:\whisper")
        result = model.transcribe(audio_path)
        text = result["text"]
        print("语音转文本完成")
        return text
    except Exception as e:
        print(f"语音转文本失败: {e}")
        return None


def summarize_text(text):
    try:
        client = OpenAI()
        completion = client.chat.completions.create(
            model="qwen/qwen-2.5-72b-instruct:free",
            messages=[
                {"role": "system", "content": "你是一个专业的总结者，能够将文本内容进行简洁且准确的总结。"},
                {"role": "user", "content": f"请总结以下文本：{text}"}
            ]
        )
        summary = completion.choices[0].message.content
        print("文本总结完成")
        return summary
    except Exception as e:
        print(f"文本总结失败: {e}")
        return None


def save_to_md(summary, md_path):
    try:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(summary)
        print(f"Markdown 文件已保存到 {md_path}")
    except Exception as e:
        print(f"保存 Markdown 文件失败: {e}")


def main(video_path, audio_path, md_path):
    # 提取音频
    extract_audio_from_video(video_path, audio_path)

    # 语音转文本
    text = audio_to_text(audio_path)
    print(f"text:{text}")

    if text:
        # 文本总结
        summary = summarize_text(text)

        if summary:
            # 保存为 Markdown 文件
            save_to_md(summary, md_path)

    # 删除临时音频文件
    if os.path.exists(audio_path):
        os.remove(audio_path)

    if os.path.exists(video_path):
        os.remove(video_path)


if __name__ == "__main__":

    # 读取files目录下所有文件
    files = os.listdir(video_path)
    for file in tqdm(files):
        if file.endswith(".mp4"):
            video_path = os.path.join("files", file)
            audio_path = os.path.join("files", file.replace(".mp4", ".wav"))
            md_path = os.path.join("files", file.replace(".mp4", ".md"))
            main(video_path, audio_path, md_path)
