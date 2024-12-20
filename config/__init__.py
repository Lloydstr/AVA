from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Workflow Platform"
    API_V1_STR: str = "/api/v1"
    
    # Database settings
    DATABASE_URL: str = "sqlite:///./workflow.db"
    
    # AI Model settings
    MODEL_STORAGE_PATH: str = "./models"
    
    # Security
    SECRET_KEY: str = "your-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    
    class Config:
        case_sensitive = True

settings = Settings() 