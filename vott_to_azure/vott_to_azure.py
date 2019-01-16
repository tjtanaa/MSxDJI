import os
import json

curr_dir = os.path.dirname(os.path.abspath(__file__))

def vott_to_azure():
    json_struct = {}
    for root, dirs, files in os.walk(curr_dir+"/vott_tagged_file/data/obj"):
        for file in files:
            if file.endswith(".txt"):
                print(os.path.join(root, file))
                data_list = []
                with open(os.path.join(root, file), "r") as f_in:
                    line = f_in.readline().split(" ")
                    while line:
                        data = {}
                        data["id"] = line[0]
                        data["bbox"] = [float(value) for value in line[1:5]]
                        data_list.append(data)
                        line = f_in.readline()
                json_struct[file.replace(".txt","")] = data_list
    print(json_struct)
    with open(curr_dir+'/vott_tagged_file/data/obj/anno.json', 'w+') as outfile:  
        json.dump(json_struct, outfile)

if __name__ == '__main__':
    # print(curr_dir)
    vott_to_azure()


