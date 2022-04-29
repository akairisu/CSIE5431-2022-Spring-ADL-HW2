import pandas as pd
import json
import sys

with open(sys.argv[1], 'r+') as f:
    with open(sys.argv[2], 'w+') as f2:
        content = f.read()
        f2.seek(0, 0)
        f2.write("{\n\t\"data\": " + content + "\n}")
with open(sys.argv[2], "r") as f:
    raw = json.load(f)
    for i in range(len(raw["data"])):
        for j in range(4):
            raw["data"][i]["paragraph_" + str(j)] = raw["data"][i]["paragraphs"][j]
        del(raw["data"][i]["paragraphs"])
with open(sys.argv[2], "w") as f:
    json.dump(raw, f, indent=2, ensure_ascii=False)




