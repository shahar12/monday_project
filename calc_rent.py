'''json format: 
'{"floor": float,
 "place": string,
  "state": string,
   "furnished": string,
   "roomsNum": float,
    "storage": bool,
    "garden": bool,
    "parent": bool,
    "elevators": bool,
    "unit": bool,
    "divided": bool,
    "private": bool,
    "private-div": bool,
    "porch": bool,
    "price": float
    }'

'''
import ast
import json
import time


def calculate(json_vals):
    sum = 0
    dic_val = json.loads(json_vals)
    for keys in dic_val.keys():
        print(str(keys) + " : " + str(dic_val[str(keys)]))
    print("calculate data \n")
    time.sleep(2)
    # return result by fourmale
    for keys in dic_val.keys():
        if keys == "roomNum":
            sum += float(dic_val[str(keys)])*750
        if keys == "True":
            sum += 100
        if keys == "floor":
            if int(dic_val[str(keys)]) > 1 :
                sum -= float(dic_val[str(keys)]) * 100
    sum += float(dic_val["price"])
    print("total rent price: " + str(sum))
    return str(sum)
