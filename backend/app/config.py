import os
from dotenv import load_dotenv

load_dotenv()


def _normalize_db_url(url: str) -> str:
    # Some hosts (older Render/Heroku) hand out "postgres://", which SQLAlchemy 2.x rejects.
    if url.startswith("postgres://"):
        return url.replace("postgres://", "postgresql://", 1)
    return url


class Settings:
    DATABASE_URL: str = _normalize_db_url(os.getenv("DATABASE_URL", "sqlite:///./resumeai.db"))
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-this-secret-key-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    CLAUDE_MODEL: str = os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5")

    MAX_FILE_SIZE_MB: int = 10
    ALLOWED_EXTENSIONS = {".pdf", ".docx"}

    # Comma-separated; trailing slashes are stripped because browsers send origins without one.
    CORS_ORIGINS: list = [
        o.strip().rstrip("/")
        for o in os.getenv("CORS_ORIGINS", "*").split(",")
        if o.strip()
    ]


settings = Settings()
