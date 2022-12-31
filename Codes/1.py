import json

with open("pos_0.png.json", "r") as in_file:
    data = json.load(in_file)

#print(data["objects"][0]['classTitle'])

ans_dict = []

ans_map = {}

ans_map['dataset_name'] = "pos_0.png.json"
ans_map['image_link'] = ""
ans_map['annotation_type'] = "image"

dobj = data['objects']

ans_map['annotation_attributes'] = {}
ans_map['annotation_objects'] = {}
annotation_attributes = {}
annotation_objects = {}

#print(len(dobj))
#annotation_objects['License Plate']['Precense'] = 0
for i in range(len(dobj)):
    
    if dobj[i]['classTitle'] == 'Vehicle':
        tags = dobj[i]['tags']
        #annotation_attributes = {}
        annotation_attributes['vehicle'] = {}
        annotation_objects['vehicle'] = {}
        for j in range(len(tags)):
            x = tags[j]['name']
            y = tags[j]['value']

            annotation_attributes['vehicle'][x] = y

            for j in range(len(dobj[i]['points']['exterior'])):
                annotation_objects['vehicle']['bbox'] = []
                for k in dobj[i]['points']['exterior']:
                    annotation_objects['vehicle']['bbox'].append(k[0])
                    annotation_objects['vehicle']['bbox'].append(k[1])

        

    elif dobj[i]['classTitle'] == 'License Plate':
        tags = dobj[i]['tags']
        annotation_attributes['License Plate'] = {}
        annotation_objects['License Plate'] = {}
        #annotation_objects['License Plate']['Precense'] = annotation_objects['License Plate']['Precense'] + 1
        for j in range(len(tags)):
            x = tags[j]['name']
            y = tags[j]['value']

            annotation_attributes['License Plate'][x] = y
        
        for j in range(len(dobj[i]['points']['exterior'])):
            annotation_objects['License Plate']['bbox'] = []
            for k in dobj[i]['points']['exterior']:
                annotation_objects['License Plate']['bbox'].append(k[0])
                annotation_objects['License Plate']['bbox'].append(k[1])
            
            #print(annotation_objects['License Plate']['bbox'])
                
                
            
            



        
ans_map['annotation_attributes'] = annotation_attributes
ans_map['annotation_objects'] = annotation_objects

ans_dict.append(ans_map)

with open("Output.json", "w") as outfile:
    json.dump(ans_dict, outfile)

#print(ans_dict)
            
        


