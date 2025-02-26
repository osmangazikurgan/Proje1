import hesaplamalar.hesapmakinesi
import sekiller.sekilcizdirme
import saglık.saglık
import oyunlar.oyun
import ders.derstakibi
import carpimtablo.carpımtablosu
import yemekler.yemekoneri
import takvim.takvimaylar
import hesaplamalar.hesaplamalar

def anamenu():
    print("╔════════════════════════╗")
    print("║   KONSOL APP           ║")
    print("║1-Hesap Makinesi        ║")
    print("║2-Şekil Çizdirme        ║")
    print("║3-Sağlık                ║")
    print("║4-Oyunlar               ║")
    print("║5-Not Hesaplama         ║")
    print("║6-Ders Takibi           ║")
    print("║7-Çarpım Tablosu        ║")
    print("║8-Takvim                ║")
    print("║9-Yemek Önerileri       ║")
    print("║10-Çıkış (e)            ║")
    print("║ seçiminiz nedir?       ║")
    print("╚════════════════════════╝")
    secim = input("Seçiminiz nedir?")
    if secim == "1":
        hesaplamalar.hesapmakinesi.hmmenu()
    elif secim == "2":
        sekiller.sekilcizdirme.cizimmenu()
    elif secim == "3":
        saglık.saglık.saglıkmenu()
    elif secim == "4":
        oyunlar.oyun.oyunmenu()
    elif secim == "5":
        hesaplamalar.harfnot.harfnotu()
    elif secim == "6":
        ders.derstakibi.dtmenu()
    elif secim == "7":
        carpimtablo.carpımtablosu.ctmenu()
    elif secim == "8":
        takvim.takvimaylar.takvimmenu()
    elif secim == "9":
        yemekler.yemekoneri.menumenu()
    elif secim == "10" or secim.lower() == "e":
        exit()
    else:
        print("Seçim sadece 1,2,3,4,5,6,7,8,9,10, olabilir.")
    
    anamenu()

anamenu()