#lex_auth_012727085763518464103
#Start writing your code here
class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
    	self.__phoneno=phoneno
    	self.__called_no=called_no
    	self.__duration=duration
    	self.__call_type=call_type

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        list_of_calldetail_objects=[]
        for i in range(len(list_of_call_string)):
        	string_list=list_of_call_string[i].split(',')
        	list_of_calldetail_objects.append(CallDetail(string_list[0],string_list[1],string_list[2],string_list[3]))
        self.list_of_call_objects=list_of_calldetail_objects

call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'
list_of_call_string=[call,call2,call3]
Util().parse_customer(list_of_call_string)
