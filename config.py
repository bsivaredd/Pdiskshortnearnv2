# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "25856368"))
API_HASH = os.environ.get("API_HASH", "7a17467cbfa52b50e22df701e25b37b0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5999287074:AAGJ7J3YxYUDrW2Qb0JCzsx_zCHgEGUhR-0")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1265997687")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "pdiskshortearn")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://strange89: strange1234@cluster0.68luwly.mongodb net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1265997687")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001842967271")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "pdiskshortnearn") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'image') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
