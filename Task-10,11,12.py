#rahul=[1,1.3,'abc',True]
#print(rahul)
#print(len(rahul))
# rahul[3]=15
# print(rahul)

#rahul=[12,25,32,65,32,14,89]
#print(rahul[0:8:2])
#print(rahul[-0:-6:2])
#print(rahul[5:0:])
#rahul.append([12,23])
#rahul.extend([12,23,45])
#rahul.clear()
# d=rahul.copy()
# rahul.append(123)
#(rahul.index(12))
# rahul.insert(125,65)
# rahul[0]

# print(rahul)

#print([i**2 for i in [1,2,3]])

#print([i**4 for i in [4,5,6]])

#print(["even" if i%2==0 else "odd" for i in range(0,20)])

#print([num+2 for num in (1,2,3,4,5)])

#program on guess game 

a=[1,2,3,4]
b=int(input("CHOOSE THE CORRECT OPTION:-"))
for a in range(1,2):
    if a==b:
        print("YOU HAVE WON THE GAME")
    elif a==b:
        print("YOU HAVE ONE MORE CHANCE")
    elif a==b:
        print("YOU HAVE LAST CHANCE")
    else:
        print("GAME OVER")







