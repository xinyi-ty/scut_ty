from openai import OpenAI
from settings import Settings

class OpenaiLLM:
    def __init__(self):
        self.settings = Settings()
        # 初始化适配智谱GLM的OpenAI客户端
        self.client = OpenAI(
            api_key=self.settings.API_KEY,
            base_url=self.settings.BASE_URL
        )
        # 对话历史内存存储，对齐原仓库逻辑
        self.message_history = []
        # 代码重构场景推荐低温度，保证输出稳定性
        self.temperature = 0.2
        self.max_tokens = 4096

    def chat(self, prompt, system_prompt="你是一名专业的Java代码重构专家，精通软件重构规范，输出可直接编译、无语法错误的标准Java代码。"):
        # 拼接系统提示词与用户指令
        self.message_history.append({"role": "system", "content": system_prompt})
        self.message_history.append({"role": "user", "content": prompt})
        
        # 调用GLM-4-Flash接口
        response = self.client.chat.completions.create(
            model=self.settings.MODEL_NAME,
            messages=self.message_history,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        
        # 提取响应内容，更新对话历史
        reply = response.choices[0].message.content
        self.message_history.append({"role": "assistant", "content": reply})
        return reply