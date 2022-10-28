import pandas as pd
import json
import sys

# with open(sys.argv[1], 'r+') as f:
#  	content = f.read()
#  	f.seek(0, 0)
#  	f.write("{\n\t\"data\": " + content + "\n}")
with open(sys.argv[1], "r") as f:
    raw = json.load(f)
    for i in range(len(raw["data"])):
        del(raw["data"][i]["paragraphs"])
        if sys.argv[1] == "train.json" or sys.argv[1] == "valid.json":
            raw["data"][i]["context"] = raw["data"][i]["relevant"]
            del(raw["data"][i]["relevant"])
            raw["data"][i]["answer"]["start"] = [raw["data"][i]["answer"]["start"]]
            raw["data"][i]["answer"]["text"] = [raw["data"][i]["answer"]["text"]]
with open(sys.argv[2], "w") as f:
    json.dump(raw, f, indent=2, ensure_ascii=False)




