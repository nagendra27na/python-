print("program to filter only even numbers")
list_1=[]
tot_item=int(input("enter total number of list items: "))
for i in range(tot_item):
    item=int(input("enter list item : "))
    list_1.append(item)
print("f list items are {list_1}")
print("\n Even number from the said list:")
even_nums = list(filter(lambda x: x%2 == 0,list_1))
print(even_nums)
