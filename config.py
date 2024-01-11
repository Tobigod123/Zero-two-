import os

TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
BOT_TOKEN = os.environ.get('BOT_TOKEN', '6915492272:AAFPlDwVTVy5UoHhGvOL3K4x5Ts6uNB8Jvw')
API_ID = int(os.environ.get('API_ID', 3847632))
APP_HASH = os.environ.get('APP_HASH', '1a9708f807ddd06b10337f2091c67657')
OWNER_ID = int(os.environ.get('OWNER_ID', 6748415360))
MONGO_DB = os.environ.get('MONGO_DB', 'mongodb+srv://whocarestobi:whocarestobi@cluster0.ayo8gc4.mongodb.net/?retryWrites=true&w=majority')
FILES_CHANNEL = os.environ.get('FILES_CHANNEL', -1002108819224)
BOT_NAME = os.environ.get('BOT_NAME', 'smart encoding')
SESSION_STRING = os.environ.get('SESSION_STRING', 'None')
