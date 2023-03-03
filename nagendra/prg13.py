import pandas as pd

df1=pd.DataFrame({'Name':['snigdha','smaya','satvik'],
                  'age':[20,19,18],
                  'Grade':['A','C','A']},
                 index=[1,2,3])
                 

df2=pd.DataFrame({"Name":['mary','Nirmala','shantala'],                
                 'age':[23,30,28],
                  'Grade':['B','C','A']},
                 index=[4,5,6])

result = pd.concat([df1,df2])

print(result)                 

                 
