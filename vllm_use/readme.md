## autodl，vllm部署DeepSeek-R1-Distill-Qwen-7B

```命令
租用显卡：https://autodl.com/
租用：4090D 24G现存

pip install vllm
pip install nvitop

下载权重，默认路径：/root/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B：
modelscope download --model deepseek-ai/DeepSeek-R1-Distill-Qwen-7B

启动命令：
python3 -m vllm.entrypoints.openai.api_server --model /root/.cache/modelscope/hub/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B --served-model-name DeepSeek-R1-Distill-Qwen-7B --dtype bfloat16 --tensor-parallel-size 1 --max-model-len 4096 --gpu-memory-utilization 0.8 --trust-remote-code --enable-chunked-prefill
```