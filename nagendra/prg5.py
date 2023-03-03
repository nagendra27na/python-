#Dictionary pogram
dict={}
ele=int(input("enter total number of elements in dictionary "))
for i in range(ele):
    dict_key=input("Enter a string: ")
    dict_val=len(dict_key)
    dict.update({dict_key:dict_val})
print(f"Dictionary is{dict}")    
                 
