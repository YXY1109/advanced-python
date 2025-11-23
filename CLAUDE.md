# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个Python高级编程课程的学习资料库，系统涵盖Python高级编程和并发编程核心技术。项目包含14个章节的完整学习材料，从Python对象模型到异步编程实战。

## 常用命令

### 环境配置
```bash
# 安装项目依赖
pip install -r requirements.txt

# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows
```

### 自动化文档生成
```bash
# 处理视频文件并生成学习文档
python video_to_md.py

# 注意：需要先配置环境变量
# .env 文件包含：
# OPENAI_BASE_URL=https://openrouter.ai/api/v1
# OPENAI_API_KEY=your_api_key_here
```

### LLM部署示例
```bash
# 运行本地LLM示例
cd vllm_use
python use_qwen_7b.py
```

## 项目架构

### 章节结构
项目按14个章节组织，每个章节包含多个Markdown文档：

- **第1-4章**：Python基础和面向对象编程（对象模型、魔法函数、元类）
- **第5-9章**：数据结构和内存管理（序列、字典、内存、生成器）
- **第10-14章**：网络和并发编程（Socket、多线程、异步编程）

### 核心技术栈
- **Python 3.x**：主要编程语言
- **Whisper**：语音识别（large-v3-turbo模型）
- **MoviePy**：视频音频处理
- **OpenAI API**：通过OpenRouter调用Qwen模型
- **vLLM**：本地LLM部署（可选）

### 自动化工作流程
项目使用`video_to_md.py`实现完整的视频内容处理：
```
视频文件 → 音频提取(MoviePy) → 语音转文本(Whisper) → AI总结(OpenAI) → Markdown文档
```

## 开发注意事项

### 环境要求
- Python 3.x
- CUDA支持（用于Whisper GPU加速）
- 足够的磁盘空间处理视频文件
- OpenAI API访问权限

### 文件组织
- `chapter01-14/`：各章节学习文档
- `files/`：视频文件处理目录（会被自动清理）
- `vllm_use/`：LLM部署示例代码
- `video_to_md.py`：自动化处理脚本

### GPU配置
Whisper模型默认使用CUDA加速，如需修改：
```python
# 在video_to_md.py中修改
model = whisper.load_model(whisper_model, device="cuda")  # GPU
# 或
model = whisper.load_model(whisper_model, device="cpu")   # CPU
```

## 学习路径

### 建议学习顺序
1. **环境搭建** → chapter01
2. **对象模型** → chapter02-04
3. **数据结构** → chapter05-07
4. **函数式编程** → chapter08-09
5. **网络编程** → chapter10
6. **并发编程** → chapter11-14

### 重点关注
- 异步编程（第12-13章）是课程重点和难点
- 元类编程（第8章）需要深入理解
- 多线程与GIL（第11章）是面试热点

## 代码示例特点

- 每个概念都有实际代码演示
- 注重实用性和工程实践
- 包含大量注释和解释
- 支持直接运行和验证

## 特殊功能

### AI辅助学习
- 自动语音转文本
- AI内容总结和结构化
- 支持批量处理视频文件
- 进度显示和错误处理

### LLM实践
- 本地模型部署示例
- OpenAI兼容API调用
- 流式和非流式对话
- 高并发推理服务