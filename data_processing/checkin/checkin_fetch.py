import json

def preprocess():
    with open("checkin_process.json", "r") as readfile:
        checkintime = json.load(readfile)
    procheckintime = []
    for checkin in checkintime:
        checkID = {}
        if  checkin["business_id"]  in checkID.keys():
            if isinstance((checkID[checkin["business_id"]]), list):
                checkID[checkin["business_id"]].append(checkin)
        else:
            checkID[checkin["business_id"]] = []
            checkID[checkin["business_id"]].append(checkin)
        procheckintime.append(checkID)
    with open("post_checkin_process.json", "w") as writefile:
        json.dump(procheckintime, writefile)

# def checkin(bussinessID):
#     with open("post_checkin_process.json", "r") as readfile:
#         checkintime = json.load(readfile)
#     for checkin in checkintime:
#         # bussinessids = list(checkin.keys())
#         if (checkin.keys()[0] == bussinessID):
#             return checkin

def fetch_write_checkin(city):
    with open("../../data/" + city + ".json", 'r') as readfile:
        restaurants = json.load(readfile)
    checkin_time = []
    with open("post_checkin_process.json", "r") as readfile:
        checkintime = json.load(readfile)
    for restaurant in restaurants:
        for checkin in checkintime:
            # bussinessids = list(checkin.keys())
            if (checkin.keys()[0] == restaurant["business_id"]):
                checkin_time.append(checkin)
            # checkin_time.append(checkin(restaurant["business_id"]))
    with open(city + "_checkin.json", 'w') as writefile:
        json.dump(checkin_time, writefile)

def main():
    preprocess()
    cityName = ["Madison", "Cleveland"]
    for city in cityName:
        fetch_write_checkin(city)

if __name__ == '__main__':
    main()