import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7481801715:AAFDx2mtLguQMvYmN4zJBdB-RnC7y2pIR5Y")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "15191874"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "3037d39233c6fad9b80d83bb8a339a07")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5597521952"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Rename_1by1_robot:bve7Z3HNBQEbDM3t@cluster0.r7y7j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")
