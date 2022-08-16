dictionary1={'Google':1,'Facebook':2,'microsoft':3}
dictionary2={'GFG':1,'Microsoft':2,'Youtub':3}
dictionary1.update(dictionary2);
for key,values in dictionary1.items():
    print(key,values)
    
#2
temp=dict()
temp['key1']={'key1':44,'key2':566}
temp['key2']=[1,2,3,4]
for (key,values) in temp.items():
    print(values,end="")
