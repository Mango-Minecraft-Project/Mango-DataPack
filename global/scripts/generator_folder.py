import json
import os

with open("./data/datapacks.json") as file:
    directory_data = json.load(file)

for directory in directory_data:
    os.makedirs(f"./src/datapacks/{directory}/")
