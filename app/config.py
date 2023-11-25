from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DR_HOST:str
    DR_PORT:int
    DR_USER:str
    DR_PASS:str
    DR_NAME:str 

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DR_USER}:{self.DR_PASS}@{self.DR_HOST}:{self.DR_PORT}/{self.DR_NAME}"


    class Config:
        env_file = '.env'

settings = Settings()

