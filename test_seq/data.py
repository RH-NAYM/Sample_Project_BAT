import json
f = open('result.json')
result = json.load(f)
for i in result.keys():

    if i == "BnH BG-GHW7" or i == "BnH FF-GHW7" or i == "BnH PT-GHW7" or i == "BnH SW-GHW7" or i == "Derby-GHW7" or i == "JPFF-GHW7" or i == "LS FF-GHW7":
        GHW = "GHW = Matched"

    else:
        GHW = "GHW = Missmatched"

print(result)
print(GHW)