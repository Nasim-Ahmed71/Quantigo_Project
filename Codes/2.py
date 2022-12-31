import json

with open("pos_0.png.json", "r") as file1:
    data1 = json.load(file1)
with open("pos_10010.png.json", "r") as file2:
    data2 = json.load(file2)
with open("pos_10492.png.json", "r") as file3:
    data3 = json.load(file3)



for i in data1["objects"]:
    j = i['classTitle']
    


for i in range(len(data1['objects'])):
    if (data1['objects'][i]['classTitle']) == 'Vehicle':
        data1['objects'][i]['classTitle'] = 'car'
    elif (data1['objects'][i]['classTitle']) == 'License Plate':
        (data1['objects'][i]['classTitle']) = 'number'


for i in range(len(data2['objects'])):
    if (data2['objects'][i]['classTitle']) == 'Vehicle':
        data2['objects'][i]['classTitle'] = 'car'
    elif (data2['objects'][i]['classTitle']) == 'License Plate':
        (data2['objects'][i]['classTitle']) = 'number'


with open("data1.json", "w") as out_f1:
    json.dump(data1, out_f1)


with open("data2.json", "w") as out_f2:
    json.dump(data2, out_f2)
