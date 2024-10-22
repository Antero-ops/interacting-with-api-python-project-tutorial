import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv

# load the .env file variables

from dotenv import load_dotenv
load_dotenv()

import os

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")