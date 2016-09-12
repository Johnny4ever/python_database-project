Weekday=["Monday","Tuesday","Wenesday","Thursday","Friday","Saturday","Sunday"
         ,{"1st":"House cleaning","2nd":"eat"}]



def type_processor(param1):
    if isinstance(param1,type([])):
        for each in param1:
            return each
    elif isinstance(param1,type("")):
        return param1
    elif isinstance(param1,type({})):
        for each in param1:
            return param1[each]

var=""
for each in Weekday:
     var+="."+type_processor(each)


print(var[1:])
