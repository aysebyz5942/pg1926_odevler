my_list=[]

al=input("sayilar gir:")
my_list=al
print("GİRİS:",my_list)
index=0 
y=index+1
max=0
while y<len(my_list):   #en buyuk sayıyı bulur
    if my_list[y]>my_list[index]:
        max=my_list[y]
    else :
        pass
    y+=1
print("CIKTI:",max)


