def kontrol(int ,str):
      sayac_nokta=0
      kontrol2=0
      kontrol1=0
      kontrol3=0
      kontrol4=0
      kullaniciAdi=[]
      
      for ch in str:
           if(ch=='@'): kontrol2=1
           if(ch=='.'):
                  sayac_nokta=sayac_nokta+1
      sayac=sayac_nokta+1 
      if(sayac!=int): kontrol1=1
      for ch in str:
            if(ch!='@'): kullaniciAdi=ch
            if(ch=='@'):break
      for ch in kullaniciAdi:
            if(ch=='-' or ch=='_' or (ch>='a' and ch<='z')or (ch>='A' and ch<='Z') or (ch>='0' or ch<='9')): kontrol3=1

      if( kontrol1==1 and kontrol2==1 and kontrol3==1 and kontrol4==1):
            return True
      else: 
            return False

uzanti_sayisi=input("uzanti sayisini gir: ")
uzunluk=int(uzanti_sayisi)
if(uzunluk<=3):
      mail=input('Mail : ')
else: print("uzanti sayisi en fazla 3 olmalıdır. tekrar dene!")

if(kontrol(uzanti_sayisi,mail)==True):
      print('Mail adresiniz doğru')
else:
      print('Mail adresiniz yanlıs tekrar deneyin')
