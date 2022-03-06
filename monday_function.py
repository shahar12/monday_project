from monday import MondayClient
import json
import requests

# monday uniq information of my user
apiKey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE0NzQ2NzA5NywidWlkIjoyNzYwMTUwOCwiaWFkIjoiMjAyMi0wMi0yM1QwOTo0MjoyMS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTEwNzYyOTYsInJnbiI6InVzZTEifQ.uDWh-PSBMqlqQgeGdgVMdelBn08Oip1_yYhq6JIwpGQ"
client = MondayClient(apiKey)
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apiKey}
# create bord_dic <value = bord_name , key = bord_id>
zip_iter = zip(["tools", "request", "events","test"],["2326678952", "2326731714", "2348440107","2348954454"])
dic_bords = dict(zip_iter)

# create new item for bord id = > test check if its ok to replace bord id with static var
def create_new_item(item_name):
    create_item_query = "mutation ($bord_ids : Int! , $myItemName: String!, $columnVals: JSON!) { create_item (board_id:$bord_ids, item_name:$myItemName, column_values:$columnVals) { id } }"
    vars = {"myItemName": item_name}
    data = {"query": create_item_query, "variables": vars}
    r = requests.post(url=apiUrl, json=data, headers=headers) # make request
    if r.status_code != 200:  # throw exception
        print('Status:', r.status_code)
        raise Exception("Add to board failed.")
    else:
        print(json.loads(r))

# {"id": "phone", "text": "", "type": "phone", "value": None}
# function create a new item and update field with the right value
# get = > <item name,string> , <args,class of the uniq bord type filed > , <bord_id , int >
def add_to_bord(item_name,args,bord_id):
    query_chngae_colmun_value = "mutation ($bord_id : Int!,$myItemName: String!, $columnVals: JSON!) { create_item (board_id:$bord_id, item_name:$myItemName, column_values:$columnVals) { id } }"
    data = {"query": query_chngae_colmun_value, "variables": vars}
    r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
    if r.status_code != 200:  # if error throw exception
        print('Status:', r.status_code)
        raise Exception("Add to board failed.")
    else :
        print(json.loads(r))

#crate the query struct to send to monday api
def int_args(args):
    vars = {
        "bord_ids": args.bord_ids,
        "myItemName": args.item_name,
        "columnVals": json.dumps({
            "status": {"label": "Working on it"},
            "date4": {"date": args.date},
            "phone": {"phone": args.phone},
            "location1": args.location,
            # {"email" : { <email name> => "email" : "dipro.b@monday.com", <what will be desply in column><user name> "text" : "email"}} update email column
            "email": {"email": args.Email, "text": "email"},
            # text colum is in this formt  <item_id : <string> >
            "text99": args.pub_name,
            "long_text": args.discreption,
            "long_text_1": args.notes,
            "hour": {"hour": args.time.hour, "minute": args.time.minute}
        })
    }
    return args


def add_new_event_to_bord(args):
    query_chngae_colmun_value = "mutation ($bord_ids : Int! , $myItemName: String!, $columnVals: JSON!) { create_item (board_id:$bord_ids, item_name:$myItemName, column_values:$columnVals) { id } }"
    data = {"query": query_chngae_colmun_value, "variables": args}
    r = requests.post(url=apiUrl, json=data, headers=headers)  # make request
    print(r.json())


#(Utility)# print json with indent
def print_json(json_):
    print(json.dumps(json_, indent=2, sort_keys=True))



# function will fetch data from monday using monday api (see description bellow )
# she convert data from jason to => python object and print it to the screen
def get_data_from_bord_and_print(bord_id):
    res = client.boards.fetch_items_by_board_id(bord_id)
    # convert from json => dic
    print("\n\n\n")
    item_list = list()
    #convert the bord json data to list of list each index contine the fileds of one item
    # item[0] = > list of dic => the id and value of each field
    for item in res["data"]["boards"]:
        for data_item in item["items"]:
            item_list.append(data_item["column_values"])
    # get the value of the fileds
    for item_object in item_list:
        for item_data in item_object:
            print(item_data["id"]+": "+item_data["text"])
        print("\n")



def main():
    # =============================================================================
    # create all the bords info in dict
    # =============================================================================

    # # =============================================================================
    # fatch all the bords and items from monday.com
    # =============================================================================
    res = client.boards.fetch_items_by_board_id(dic_bords["tools"])
    print_json(res)
    # # =============================================================================
    # create a new item in equipment bord on monday.com
    # =============================================================================
    #chngae_colmun_value()
    get_data_from_bord_and_print(dic_bords["tools"])


if __name__ == "__main__":
    main()
