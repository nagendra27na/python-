def count_characters(filename):


    with open(filename, "r") as file:


        contents = file.read()

        char_count = {}

        for char in contents:

            if char in char_count:
                char_count[char]+=1


            else:
                char_count[char]=1

        return char_count
date=input("enter the date:")

filename = input("enter the filename to save the date:")

with open(filename,"w") as file:
     file.write(date)

print("opening the file'"+filename+" 'for reading...")

result = count_characters(filename)

print("characters frequency in '" +filename+"' is: \n" +str(result))
     
        
