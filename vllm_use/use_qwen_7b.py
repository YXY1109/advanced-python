# 调用vLLM大模型接口的OpenAI规范代码
# 需提前安装openai库：pip install openai

from openai import OpenAI

# 配置客户端连接本地vLLM服务
client = OpenAI(
    base_url="http://localhost:8000/v1",  # vLLM服务地址
    api_key="EMPTY"  # vLLM默认不需要认证
)


def simple_completion():
    """基础文本补全示例"""
    try:
        response = client.completions.create(
            model="DeepSeek-R1-Distill-Qwen-7B",  # 需与部署模型名称一致
            prompt="你是什么模型11",
            temperature=0.7

        )
        print("生成结果：\n" + response.choices[0].text)
    except Exception as e:
        print(f"请求失败：{str(e)}")


def chat_completion():
    """对话式交互示例（推荐）"""
    try:
        response = client.chat.completions.create(
            model="DeepSeek-R1-Distill-Qwen-7B",
            messages=[
                {"role": "system", "content": "你是一个AI编程助手"},
                {"role": "user", "content": "请用Python实现归并排序算法，要求添加详细注释"}
            ],
            max_tokens=800,
            temperature=0.8,
            stream=False  # 是否启用流式传输
        )
        print("助手回复：\n" + response.choices[0].message.content)
    except Exception as e:
        print(f"对话请求失败：{str(e)}")


def stream_chat():
    """流式对话示例"""
    try:
        response = client.chat.completions.create(
            model="DeepSeek-R1-Distill-Qwen-7B",
            messages=[
                {"role": "user", "content": "解释Transformer架构的核心思想"}
            ],
            stream=True,
            # max_tokens=1000,
            temperature=0.5
        )

        print("流式响应：")
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"流式请求失败：{str(e)}")


if __name__ == "__main__":
    # print("=== 基础文本补全测试 ===")
    # simple_completion()

    # print("\n=== 对话式交互测试 ===")
    # chat_completion()

    print("\n=== 流式对话测试 ===")
    stream_chat()
