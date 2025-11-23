# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个AI驱动的Python高级编程学习系统，包含14个章节的完整课程体系。项目结合传统教学内容和现代AI技术，提供从Python对象模型到异步编程实战的全面学习材料，并具备自动化视频处理和文档生成能力。

## 常用命令

### Claude Code智能命令
```bash
# 智能Git提交 - 自动分析变更并生成符合规范的提交信息
/commit

# 该命令会：
# - 自动检测变更类型和影响范围
# - 执行质量检查（构建、测试、代码检查）
# - 生成遵循conventional commits标准的提交信息
# - 确保提交的完整性和规范性
```

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

### 整体架构
```
advanced-python/
├── 📂 chapter01-14/              # 14个完整章节学习资料（100+个Markdown文档）
├── 📂 course_code/               # 配套代码示例（300+个代码片段）
├── 📂 vllm_use/                  # 本地LLM部署示例和实战代码
├── 📂 .claude/                   # Claude Code智能配置和自定义命令
├── 📂 files/                     # 视频处理临时目录（自动清理）
├── 🤖 video_to_md.py             # AI自动化文档生成核心脚本
├── 📋 requirements.txt           # 项目依赖管理
├── 🔧 .env.example/.env          # 环境变量配置
└── 📊 python高级编程思维导图.xmind # 课程知识体系图谱
```

### 章节结构
项目按14个章节组织，每个章节包含多个Markdown文档：

- **第1-4章**：Python基础和面向对象编程（对象模型、魔法函数、元类）
- **第5-9章**：数据结构和内存管理（序列、字典、内存、生成器）
- **第10-14章**：网络和并发编程（Socket、多线程、异步编程）

### 核心技术栈
- **Python 3.x**：主要编程语言
- **Whisper**：语音识别（large-v3-turbo模型，支持CUDA加速）
- **MoviePy**：视频音频处理
- **OpenAI API**：通过OpenRouter调用Qwen-2.5-72B模型
- **vLLM**：本地LLM部署（高性能推理服务）
- **Claude Code**：智能化开发环境配置

### AI自动化工作流程
项目使用`video_to_md.py`实现完整的视频内容处理：
```
视频文件 → 音频提取(MoviePy) → 语音转文本(Whisper) → AI总结(OpenAI) → Markdown文档
```

### 智能工具集成
- **Claude Code配置**：自定义命令、用户偏好设置、智能提交
- **Git工作流**：自动化质量检查和规范化提交
- **开发环境**：PyCharm集成配置和虚拟环境管理

## 开发注意事项

### 环境要求
- Python 3.x（推荐3.8+）
- CUDA支持（用于Whisper GPU加速，可选）
- 足够的磁盘空间处理视频文件
- OpenAI API访问权限（通过OpenRouter）
- 虚拟环境（推荐使用venv）

### 关键依赖说明
```txt
numpy==1.26.4            # 数值计算基础库
moviepy==2.1.2           # 视频音频处理
openai==1.72.0           # OpenAI API客户端
openai-whisper==20240930 # 语音识别模型（large-v3-turbo）
python-dotenv            # 环境变量管理
tqdm                     # 进度条显示
```

### 文件组织
- `chapter01-14/`：各章节学习文档（115个Markdown文件）
- `course_code/`：配套代码示例和实战项目
- `vllm_use/`：本地LLM部署示例代码
- `files/`：视频文件处理目录（自动清理）
- `video_to_md.py`：AI自动化处理脚本
- `.claude/`：Claude Code智能配置和自定义命令

### GPU配置和性能优化
Whisper模型默认使用CUDA加速，配置说明：
```python
# 在video_to_md.py中的第31行
model = whisper.load_model(whisper_model, device="cuda", download_root=r"D:\whisper")

# 可选配置：
# device="cuda"  # GPU加速（推荐，需要CUDA支持）
# device="cpu"   # CPU模式（较慢但兼容性好）
# whisper_model = "large-v3-turbo"  # 平衡速度和精度
# whisper_model = "base"           # 快速但精度较低
```

### API配置
确保`.env`文件正确配置：
```env
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_API_KEY=your_api_key_here
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

### AI辅助学习系统
- **自动语音转文本**：Whisper large-v3-turbo高精度识别
- **AI内容总结**：Qwen-2.5-72B模型智能总结和结构化
- **批量处理**：支持多个视频文件批量转换
- **进度显示**：tqdm进度条和详细错误处理
- **自动清理**：处理完成后自动清理临时文件

### LLM实践平台
- 本地模型部署示例（vLLM框架）
- OpenAI兼容API调用
- 流式和非流式对话
- 高并发推理服务配置

## 开发指导和故障排除

### 常见问题解决
1. **Whisper模型下载失败**：
   - 检查网络连接和防火墙设置
   - 手动设置`download_root`路径
   - 考虑使用代理或镜像源

2. **GPU加速不可用**：
   - 验证CUDA安装：`nvidia-smi`
   - 检查PyTorch CUDA支持：`python -c "import torch; print(torch.cuda.is_available())"`
   - 如有问题可切换到CPU模式

3. **OpenAI API调用失败**：
   - 验证API密钥有效性
   - 检查OpenRouter账户余额
   - 确认网络连接和API端点

4. **视频处理失败**：
   - 检查视频文件格式（支持.mp4）
   - 确保足够的磁盘空间
   - 验证音频轨道是否存在

### 性能优化建议
- 使用SSD存储提高视频处理速度
- 确保充足的内存（建议8GB+）
- GPU环境下Whisper处理速度提升5-10倍
- 批量处理时建议并发数不超过CPU核心数

### 开发最佳实践
- 始终在虚拟环境中工作
- 定期备份学习文档和代码笔记
- 使用Git进行版本控制
- 遵循PEP 8代码规范
- 及时更新依赖包版本

## 项目统计和学习成果

### 完成情况统计
- **✅ 已完成章节**：12/14章（第9、10章待完成）
- **📄 总文档数**：115+个Markdown学习文档
- **💻 代码示例**：300+个可运行代码片段
- **🎯 知识覆盖**：Python高级编程全领域

### 章节完成详情
- ✅ **第1章** - 导学与环境配置（3个文档）
- ✅ **第2章** - Python对象模型（4个文档）
- ✅ **第3章** - 魔法函数（5个文档）
- ✅ **第4章** - 面向对象高级编程（14个文档）
- ✅ **第5章** - 序列类型深入（8个文档）
- ✅ **第6章** - 字典与集合（6个文档）
- ✅ **第7章** - 内存管理（5个文档）
- ✅ **第8章** - 元类编程（8个文档）
- ⏳ **第9章** - 迭代器与生成器（待完成）
- ⏳ **第10章** - Socket编程（待完成）
- ✅ **第11章** - 多线程与多进程（12个文档）
- ✅ **第12章** - 异步编程基础（12个文档）
- ✅ **第13章** - AsyncIO实战（12个文档）
- ✅ **第14章** - 课程总结（1个文档）

### 学习成果应用
完成本课程后，您将具备：
- 🔧 **Python底层原理理解**：对象模型、内存管理、GIL机制
- 🚀 **高级编程技术掌握**：元类、装饰器、描述符、上下文管理器
- ⚡ **并发编程实战能力**：多线程、异步编程、高并发应用开发
- 🌐 **网络编程基础**：Socket编程、HTTP协议理解
- 🤖 **AI工具应用能力**：现代化学习工具链使用和配置