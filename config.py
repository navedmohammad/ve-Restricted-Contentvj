import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7942365406:AAEhqRL_6PblpO5gXvH9EFvBamDMRsgKe2o")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "20483216"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "2518170d3dd939b3f2893cb0aae805c4")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://navedmohammad053:<db_password>@telegram.9xlun.mongodb.net/?retryWrites=true&w=majority")
