import pandas as pd
import json
import sys

with open(sys.argv[1], 'r+') as f:
 	content = f.read()
 	f.seek(0, 0)
 	f.write("{\n\t\"data\": " + content + "\n}")
with open(sys.argv[1], "r") as f:
    raw = json.load(f)
    for i in range(len(raw["data"])):
        for j in range(4):
            raw["data"][i]["paragraph_" + str(j)] = raw["data"][i]["paragraphs"][j]
            if sys.argv[1] == "train.json" or sys.argv[1] == "valid.json":
                if raw["data"][i]["paragraphs"][j] == raw["data"][i]["relevant"]:
                    raw["data"][i]["label"] = j
        del(raw["data"][i]["paragraphs"])
        if sys.argv[1] == "train.json" or sys.argv[1] == "valid.json":
            del(raw["data"][i]["answer"])
with open(sys.argv[2], "w") as f:
    json.dump(raw, f, indent=2, ensure_ascii=False)




