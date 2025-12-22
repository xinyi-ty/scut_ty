try:
    from pydantic_settings import BaseSettings
except Exception:
    # Fallback for environments with pydantic v1 or where pydantic-settings isn't installed
    try:
        from pydantic import BaseSettings
    except Exception:
        raise ImportError("pydantic or pydantic-settings is required for Settings. Install pydantic>=1.10 or pydantic-settings.")


class Settings(BaseSettings):
    API_KEY: str
    GITHUB_API_KEY: str
    MODEL_NAME: str

    # Per-agent token limits (defaults can be overridden via .env)
    DEFAULT_MAX_TOKENS: int = 32000
    REFRACTORING_GENERATOR_MAX_TOKENS: int = 32000
    PLANNER_MAX_TOKENS: int = 32000
    COMPILER_MAX_TOKENS: int = 32000
    TEST_MAX_TOKENS: int = 32000

    class Config:
        env_file = ".env"
