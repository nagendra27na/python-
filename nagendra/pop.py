print("program to demonstrate List functions")
list_1=[]
tot_item=int(input("Enter total number of list items:"))
for i in range(tot_item):
    item=input("enter list item")
    list_1.append(item)
    print(f"list items are{list_1}")
    print("1:insert 2:remove 3:append 4:len 5:pop 6:clear")
    choice=int(input("enter the choice:"))
    while choice<7:
        if choice==1:
          print("use of insert() function in list")
          ind=int(input("enter the position to insert the value:"))
          new_item=input("enter the new item to insert:")
          list_1.insert(ind,new_item)
          print("new list after insertion",list_1)
          break
        elif choice==2:
          print("use of remove() function in list")
          item=input("enter the item to remove element from list")
          if item not in list_1:
             print("item not in the list")
          else:
                list_1.remove(item)
                print("updated list after remove is:",list_1)
                break
        elif choice==3:
                item=input("enter the new item to append:")
                list_1.append(item)
                print("list after append",list_1)
                break
        elif choice==4:
                print("use of len() function in list")
                length=len(list_1)
                print(f"length of the list is :{length}")
                break
        elif choice==5:
                print("pop()fuction removes as elements specified postion using index value")
                if ind>len(list_1):
                    print("index out of range,enter the correction index value")
                else:
                        list_1.pop(ind)
                        print("updated list is",list_1)
                break
        elif choice==6:
                print("clear() functions renove all items from the list.")
                newlist=list_1.clear()
                print("after clear function",newlist)
                break

        else:
                print("enter the correction choice")
                break
