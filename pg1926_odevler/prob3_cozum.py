my_list=[2,4,1,6,4,0,0]
print("normal liste      :",my_list)  #normal liste 

#my_list.sort()  #siralar
#print(my_list)
index=0
while index < (len(my_list)):
    if my_list[index]==0 and my_list[0]!=0:
        my_list[0],my_list[index]=my_list[index],my_list[0]
    elif  my_list[0]==0:
        my_list[1],my_list[index]=my_list[index],my_list[1]
    else:
        pass
    index+=1
print("0 ları basa aldik :",my_list)  #0 ları başa aldık
my_list.sort()
print("sıralanmıs list   :",my_list) #listeyi sıraladık
