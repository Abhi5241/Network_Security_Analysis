import os
import sys
import json

from dotenv import load_dotenv
load_dotenv()

MongoDbUrl=os.getenv("MONGODB_URL")
print(MongoDbUrl)

import certifi
ca=certifi.where()

import numpy as np
import pandas as pd
