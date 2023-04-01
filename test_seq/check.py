# Import Lib
import json

# Read Json File
f = open('result.json')
result = json.load(f)

# Check GHW
for i in result.keys():
    if i == "BnH BG-GHW7" or i == "BnH FF-GHW7" or i == "BnH PT-GHW7" or i == "BnH SW-GHW7" or i == "Derby-GHW7" or i == "JPFF-GHW7" or i == "LS FF-GHW7":
        GHW = "GHW = Matched"
    else:
        GHW = "GHW = Missmatched"

# Check Original Sequence
seq = []
sub_list = [1,5,2,3,4]
for i in result.keys():
    if i == "BnH BG-GHW6" or i == "BnH BG-GHW7" or i == "BnH FF-GHW6" or i == "BnH FF-GHW7"or i == "BnH PT-GHW6" or i == "BnH PT-GHW7" or i == "BnH SW-GHW6"or i == "BnH SW-GHW7":
        seq += [1]
    elif i=="JPFF-GHW5" or i=="JPFF-GHW7" or i == "JPSPCL-GHW2" or i=="JPSW-GHW5":
        seq += [2]
    elif i == "LS FF-GHW7":
        seq += [3]
    elif i == "Royals Gold-GHW5" or i =="Royals Next-GHW5":
        seq += [4]
    elif i == "Derby-GHW7":
        seq += [5]
sorted_dict_values = sorted(set(seq))
print(sorted_dict_values)
res = sorted_dict_values == sub_list


print(result)
print(GHW)
print("Are values in order : " + str(res))

# print(result)