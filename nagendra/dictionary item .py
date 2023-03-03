def main():
    d={}
    while True:
        print("1 : print dictionry items 2 : access items 3: use get() 4 : change values 5:pop 6 :use len() 7:exit")
        choice=int(input("enter the choice: "))
        if choice==1:
            ele=int(input("enter total numbers of elements in dictionary: "))
            for i in range(ele):


                d_key=input("enter key=")
                d_val=input("enter val=")
                d.update({d_key:d_val})
                print("f dictionary is{d}")

        elif choice==2:
                print("to acess value , use key")
                key=input("enter the key to acess the value=")
                print(d[key])

        elif choice==3:
                 key=input("enter the key to acess the value=")
                 print(f" the value of key {key} is  :")
                 val=d.get(key)
                 print(val)


        elif choice==4:
                 key=input("enter the key to acess the value=")
                 newval=input("enter the new value : ")
                 d.update({key:newval})
                 print(f" after updating the dictionary is :{d}")


        elif choice==5:
                  key=input("enter the key pop:")
                  d.pop(key)
                  print(f"after poping , the dictionary is{d}")

        elif choice==6:
                 print("the size of dic is:")
                 print(len(d))

        elif choice==7:
                 break
        else:
                 print("Enter  the correct choice")
if __name__== "__main__":
      main()
                  
                               
                 





                              
