print("program to demonstrate List functions")
list_1=[]
tot_item=int(input("Enter total number of list items:"))
for i in range(tot_item):
    item+input("Enter list item")
    list_1.append(item)
print(f"list item are(list_1)")
print("1:insert 2:remove 3:append 4:len 5:pop 6:clear")
choice =int(input("enter the choice:"))
while choice<7:
    if choice==1:
            print("use of insert() function in list")
             int=int(input("enter the positionto insert the value:"))
                 new_item=input("enter the new item to insert:")
                 list_1.insert(ind,new_item)
                print("new list after insertion",list_1)
                 break
                elif choice==2:
                    print("use of remove()function in list")
                    item=input("enter the item to remove element from list")
                    if item not in list_1:
                        print("item not in the list")
                        else:
                            list_1.remove(item)
                            print("update list after removal is:",list_1)
                            break
                        elif choice==3:
                            item=input("enter the new item to append:")
                            list_1.append(item)
                            print("list after append",list_1)
                            break
                        elif choice==4:
                            print("use oflen() function in list")
                            length=len(list_1)
                            print(f"length of the list is:{length}")
                            break
                        elif choice==5:
                            print("pop()function removes an elements specified position using
                            
