def count_characters(string):
    #create an empty dictionary
    char_count= {}

    #loop through each character in the string
    for char in string:
        #if the character is already in the dictionary , increment its count by 1
        if char in char_count:
            char_count[char]+=1

        #if the character is not in the dictionary, add it and set  its  count by 1
        else:
            char_count[char]= 1

    #Return the dictionary
    return char_count
#Input the string
string = input ("enter a string: ")

#call the function and store the result in a variable
result = count_characters(string)

#print the result
print("character count in' "+string+"' is : \n" +str(result))
