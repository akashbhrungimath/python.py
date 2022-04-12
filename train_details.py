#lex_auth_0127136112798105601178    

train_list=[{'train_no': 23492, 'days_of_run': ['Su', 'Mo', 'We'], 'name': 'Tuticorin Express', 'to': 'TUT', 'ac_fare': 780, 'from': 'MYS', 'sleeper_fare': 450}, {'train_no': 45200, 'days_of_run': ['Mo', 'Fr'], 'name': 'Kaveri Express', 'to': 'CHN', 'ac_fare': 1200, 'from': 'MYS', 'sleeper_fare': 700}, {'train_no': 12093, 'days_of_run': ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa'], 'name': 'Lokmanya Express', 'to': 'LOK', 'ac_fare': 1340, 'from': 'CBE', 'sleeper_fare': 720}, {'train_no': 67234, 'days_of_run': ['Th', 'Fr', 'Sa'], 'name': 'Poorna Express', 'to': 'PUN', 'ac_fare': 2879, 'from': 'ERN', 'sleeper_fare': 987}]

def get_train_name (train_no):
    for train in train_list:
    	if train["train_no"]==train_no:
    		return train
    return "Invalid Train_no"

def get_trains_for_day(day_of_run):
    trains_of_day=[]
    for train in train_list:
    	if day_of_run in train["days_of_run"]:
    		trains_of_day.append(train["train_no"])
    if len(trains_of_day)!=0:
    	return trains_of_day
    return "Invalid day"

def get_total_fare(train_no,passenger_dict):
    total_fare=0
    for train in train_list:
    	if train["train_no"]==train_no:
    		for key1,value1 in passenger_dict.items():	
    			if key1=="sleeper":
    				total_fare+=value1*train["sleeper_fare"]
    			elif key1=="ac":
    				total_fare+=value1*train["ac_fare"]
    			else:
    				print("Invalid seat type")
    return total_fare

#print(get_train_name(25627))
print(get_trains_for_day("We"))
#print(get_total_fare(22642,{"sleeper":5, "ac":1}))
