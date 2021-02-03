class okul():
    def __init__(self,isim,soyisim,pozition,giris_yil):
        self.isim=isim
        self.soyisim=soyisim
        self.pozition=pozition
        self.giris_yil=giris_yil
class yonetici(okul):
    def __init__(self,deneyim,maas):
        self.deneyim=deneyim
        self.maas=maas
class personel(okul):
    def __init__(self,deneyim,maas):
        self.deneyim=deneyim
        self.maas=maas

class ogrenci(okul):
    def __init__(self,ogr_no,basari_sira,topluluk):
        self.ogr_no=ogr_no
        self.basari_sira=basari_sira
        self.topluluk=topluluk
        
class sinif(ogrenci):
    def __init__(self,sinif_isim,sinif_hoca):
        self.sinif_isim=sinif_isim
        self.sinif_hoca=sinif_hoca
        
ahmet=okul("ahmet","yildiz","yonetici",2007)

hoca=personel("konya tek, gazi uni",3000)
print(hoca)

