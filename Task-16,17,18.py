#rahul={10:"shiva","ask":20,1:"AI"}
#print(rahul[10])
# rahul[10]="ravi"
# print(rahul)
#print(rahul.get(10))
#print(rahul.items())
#print(rahul.keys())
#print(rahul.values())
# p=rahul.update({123:'solar'})
# print(p)

# names={1:'rahul',2:'ravi',3:'suresh'}
# user=input("ENTER THE USERNAME:")
# passw=input("ENTER THE PASSWORD:")
# for u,p in names.items():
#     if u==user and p==passw:
#         print("successfull")
#     else:
#         print("invalid")

# rahul=(1,6465,56,15)
# # print(type(rahul))
# # print(len(rahul))
# # print(min(rahul))
# # print(sum(rahul))
# # print(max(rahul))

# rahul1=(45,65,88,9)
# # print(rahul+rahul1)
# print(tuple(zip(rahul+rahul1)))


#Mini Project- Super Market Bill Generation

from datetime import datetime

item={'Bread':40,'Rice':50,'Butter':10,'Sugar':50}
print("-------------------------------------")
print("   ","Welcome To Supermarket","     ")
groceries={'Bread':40,'Rice':50,'Butter':10,'Sugar':50}

customerlist={'Sugar':23,'Rice':45,'Butter':35,'Bread':14}
print('S.no',' ','Item',' ','Quantity',' ','Price')
print('1','    ','Rice','   ','1','       ','50')
print('2','    ','Sugar','  ','1','       ','23')
print('3','    ','Butter',' ','1','       ','35')
print('4','    ','Bread','  ','1','       ','14')
print('-------------------------------------------------')
print("Total",'                  ','122')
print('--------------------------------------------')
print('         ',"THANK YOU",'   ')
print('        ',"VISIT AGAIN",'     ')