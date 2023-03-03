#Tuple program
tuple_items=()
total_items=int(input("enter the total number of item:"))
for i in range(total_items):
    user_input=int(input("enter a number:"))
    tuple_items +=(user_input,)
    print(f"item added to tuple are{tuple_items}")
    len(tuple_items)
    print(f"length of tuple is:{i}")
    pos=int(input("enter the position to access the tuple value:"))
    print(f"the elements at the postion {pos} is{tuple_items[pop]}")
