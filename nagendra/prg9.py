import datetime

#Get the current date
today= datetime.datetime.now()


#print the current date
print("current date is :",today)


#input number of days to add
days_to_add = int(input("enter the number of days to add: "))


#add the days to current date
new_date = today +datetime.timedelta(days=days_to_add)


#print the new date
print("Date after adding", days_to_add,"days is :",new_date)

