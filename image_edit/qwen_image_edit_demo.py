"""
Qwen图像编辑演示
使用ModelScope的Qwen-Image-Edit模型进行图像编辑
"""
import json
import os
import time
from io import BytesIO

import requests
from PIL import Image
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# API配置
BASE_URL = 'https://api-inference.modelscope.cn/'
API_KEY = os.environ["MODEL_SCOPE_KEY"]

# 请求头配置
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}


def edit_image(prompt: str, image_url: str, output_filename: str = "result_image.jpg") -> bool:
    """
    编辑图像

    Args:
        prompt: 编辑指令，描述要对图像进行的修改
        image_url: 原始图像的URL
        output_filename: 输出文件名

    Returns:
        bool: 编辑成功返回True，失败返回False
    """
    # 提交图像编辑任务
    response = requests.post(
        f"{BASE_URL}v1/images/generations",
        headers={**HEADERS, "X-ModelScope-Async-Mode": "true"},
        data=json.dumps({
            "model": "Qwen/Qwen-Image-Edit",
            "prompt": prompt,
            "image_url": image_url
        }, ensure_ascii=False).encode('utf-8')
    )

    response.raise_for_status()
    task_id = response.json()["task_id"]
    print(f"任务已提交，任务ID: {task_id}")

    # 轮询任务状态
    while True:
        result = requests.get(
            f"{BASE_URL}v1/tasks/{task_id}",
            headers={**HEADERS, "X-ModelScope-Task-Type": "image_generation"},
        )
        result.raise_for_status()
        data = result.json()

        task_status = data["task_status"]
        print(f"任务状态: {task_status}")

        if task_status == "SUCCEED":
            # 下载并保存生成的图像
            image_url = data["output_images"][0]
            image_response = requests.get(image_url)
            image = Image.open(BytesIO(image_response.content))
            image.save(output_filename)
            print(f"图像编辑完成，结果已保存为: {output_filename}")
            return True

        elif task_status == "FAILED":
            print("图像编辑失败")
            return False

        # 等待5秒后再次查询
        time.sleep(5)


if __name__ == "__main__":
    # 文档：https://modelscope.cn/docs/model-service/API-Inference/intro
    # 示例：将女孩的头发变成蓝色
    prompt = "turn the girl's hair blue"
    image_url = "https://resources.modelscope.cn/aigc/image_edit.png"

    # 示例：图片中眼睛睁大
    # prompt = "Just keep your eyes a bit wider and more natural; don’t change anything else."
    # image_url = "https://thumbnail0.baidupcs.com/thumbnail/00dfb16ebi3f725c356cda57538e5be4?fid=488197452-250528-758737685988322&time=1765980000&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-nSnhic%2F%2Fz2OdEupDr7rmzKQpE7s%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=68610938986884365&dp-callid=0&file_type=0&size=c710_u400&quality=100&vuk=-&ft=video"

    print("开始图像编辑...")
    # 根据image_url生成输出文件名
    original_filename = os.path.basename(image_url)  # 去除URL参数
    name, ext = os.path.splitext(original_filename)
    output_filename = f"{name}_result{ext}"
    success = edit_image(prompt, image_url, output_filename)

    if success:
        print("图像编辑成功完成！")
    else:
        print("图像编辑失败，请检查输入或稍后重试。")
