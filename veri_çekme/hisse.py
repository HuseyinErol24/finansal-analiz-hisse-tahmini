from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import matplotlib.pyplot
import pandas as pd
import tensorflow


class veri_al():
    def __init__(self) -> None:
        self.tarayici = webdriver.Firefox()
        self.link()
        self.veriler()

    
    def link(self):
        self.tarayici.get("https://www.********.com.tr/tr-tr/analiz/hisse/Sayfalar/Tarihsel-Fiyat-Bilgileri.aspx") # :::: web sitesinin linkin giriniz ::::
        i = 0
        i = int(input("bir sayi giriniz"))
        if(0<i):
            print("devam ediyor")
    
    def veriler(self):
        veri_kümesi = self.tarayici.find_element(By.ID,'HisseTekilBody').find_elements(By.TAG_NAME,"tr")
        time.sleep(5)
        kaydet = []
        dosya = open("merhaba.txt","w",encoding="utf-8")
        for i in veri_kümesi:
                tarih = i.find_element(By.CLASS_NAME,'sorting_1').text
                yazı = i.find_elements(By.CLASS_NAME,'text-right')
                TariH = tarih
                Kapanış = yazı[0].text
                Min = yazı[1].text
                Max = yazı[2].text
                aof = yazı[3].text
                Hacim = yazı[4].text
                Sermaye = yazı[5].text
                usd_try = yazı[6].text
                bist_100 = yazı[7].text
                piyasa_degeri_tl = yazı[8].text
                piyasa_degeri_usd = yazı[9].text
                halka_acık_pd_tl = yazı[10].text
                halka_acık_pd_usd = yazı[11].text
                dizi = []
                dizi.append(TariH)
                dizi.append(Kapanış)
                dizi.append(Min)
                dizi.append(Max)
                dizi.append(aof)
                dizi.append(Hacim)
                dizi.append(Sermaye)
                dizi.append(usd_try)
                dizi.append(bist_100)
                dizi.append(piyasa_degeri_tl)
                dizi.append(piyasa_degeri_usd)
                dizi.append(halka_acık_pd_tl)
                dizi.append(halka_acık_pd_usd)
                kaydet.append(dizi)
        df = pd.DataFrame(data=kaydet, columns=['Tarih', 'Kapanış', 'Min', 'Max', 'aof', 'Hacim', 'Sermaye', 'usd_try','bist_100', 'piyasa_degeri_tl','piyasa_degeri_usd','halka_acık_pd_tl','halka_acık_pd_usd'])
        df.to_excel("veri.xlsx", index=False)




                



t = veri_al()