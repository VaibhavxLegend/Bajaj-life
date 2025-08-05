from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # FastAPI Server Configuration
    HOST: str = Field("0.0.0.0", env="HOST")
    PORT: int = Field(8000, env="PORT")
    DEBUG: bool = Field(True, env="DEBUG")

    # Pinecone Configuration
    PINECONE_API_KEY: str = Field(..., env="PINECONE_API_KEY")
    PINECONE_ENV: str = Field(..., env="PINECONE_ENV")
    PINECONE_INDEX: str = Field(..., env="PINECONE_INDEX")

    # OpenAI LLM Configuration
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    EMBEDDING_MODEL: str = Field("text-embedding-ada-002", env="EMBEDDING_MODEL")
    LLM_MODEL: str = Field("gpt-4", env="LLM_MODEL")

    # Document Chunking Parameters
    CHUNK_SIZE: int = Field(500, env="CHUNK_SIZE")
    CHUNK_OVERLAP: int = Field(50, env="CHUNK_OVERLAP")

    # Database URL
    DATABASE_URL: str = Field(..., env="DATABASE_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Global settings instance to be imported throughout the app
settings = Settings()
