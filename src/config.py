import os

# Database connection settings
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "27017"))
DB_TIMEOUT = int(os.getenv("DB_TIMEOUT", "30"))
DB_NAME = os.getenv("DB_NAME", "petstore")

# Connection pool settings
MAX_POOL_SIZE = int(os.getenv("MAX_POOL_SIZE", "10"))
MIN_POOL_SIZE = int(os.getenv("MIN_POOL_SIZE", "1"))

# Retry settings
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
RETRY_DELAY = int(os.getenv("RETRY_DELAY", "2"))
