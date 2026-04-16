import os
from dotenv import load_dotenv

# 加载.env环境变量
load_dotenv()

class Settings:
    # 智谱GLM API密钥
    API_KEY = os.getenv("API_KEY")
    # GitHub Token（可选，仅用于提交重构后的代码，不用可留空）
    GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")
    # 固定为GLM-4-Flash模型名
    MODEL_NAME = os.getenv("MODEL_NAME", "glm-4-flash")
    # 智谱官方兼容OpenAI格式的接口地址，不要修改
    BASE_URL = os.getenv("BASE_URL", "https://open.bigmodel.cn/api/paas/v4/")