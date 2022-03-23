#lex_auth_0127382193364008961449

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    #Write the logic to find and return the number of passengers traveling to the specified destination
    count=0
    for ticket in ticket_list:
        string_list=ticket.split(":")
        if(string_list[2]==destination):
            count+=1
    return count

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    list_of_airline_names=[]
    count_list=[]
    for ticket in ticket_list:
    	flight=ticket.split(":")
    	if flight[0] not in list_of_airline_names:
    		list_of_airline_names.append(flight[0])
    		count_list.append(1)
    	else:
    		for index in range(len(list_of_airline_names)):
    			if(flight[0]==list_of_airline_names[index]):
    				count_list[index]+=1
    				break
    no_of_passengers_per_flight=[]
    for index in range(len(list_of_airline_names)):
    	no_of_passengers_per_flight.append(list_of_airline_names[index]+":"+str(count_list[index]))
    return no_of_passengers_per_flight

def sort_passenger_list():
    #Write the logic to sort the list returned from find_passengers_per_flight() function in the descending order of number of passengers
    passenger_details=find_passengers_per_flight()
    print(passenger_details)
    sorted_passenger_list=[passenger_details[0]]
    for index1 in range(1,len(passenger_details)):
    	flight_list=passenger_details[index1].split(":")
    	for index in range(len(sorted_passenger_list)):
    		ticket_list=sorted_passenger_list[index].split(":")
    		if ticket_list[1]<flight_list[1]:
    			sorted_passenger_list.insert(index,passenger_details[index1])
    			break
    		elif index==len(sorted_passenger_list)-1:
    			sorted_passenger_list.append(passenger_details[index1])
    return sorted_passenger_list

#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())
