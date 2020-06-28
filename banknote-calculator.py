# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 17:56:12 2020

@author: Zartun
"""


"Banknote calculator for Turkish Lira"

ilkbes_toplam = 0
sonbes_toplam = 0
fark = 0



Flag=True

while Flag:
    yuzluk_banknot = 0
    ellilik_banknot = 0
    yirmilik_banknot = 0
    onluk_banknot = 0
    while True:
      cekilecek_para = int(input("Çekmek istediğiniz para miktarını giriniz: "))
      if cekilecek_para%10==0:
         break
    if cekilecek_para > 100:
     yuzluk_banknot = int(cekilecek_para/100)
     cekilecek_para = cekilecek_para-yuzluk_banknot*100
    if cekilecek_para>=50:
        ellilik_banknot = int(cekilecek_para/50)
        cekilecek_para = cekilecek_para-ellilik_banknot*50
    if cekilecek_para>=20:
            yirmilik_banknot=int(cekilecek_para/20)
            cekilecek_para=cekilecek_para-yirmilik_banknot*20
    if cekilecek_para>=10:
                onluk_banknot=int(cekilecek_para/10)
                cekilecek_para=cekilecek_para-onluk_banknot*10
    print("100lük banknot sayısı : ",yuzluk_banknot)
    print("50lik banknot sayısı : ",ellilik_banknot)
    print("20lik banknot sayısı : ",yirmilik_banknot)
    print("10luk banknot sayısı : ",onluk_banknot)
 
    devam_kontrol = input("Devam etmek istiyorsanız 1, istemiyorsanız 0 yazın")
    if int(devam_kontrol)==1:
     Flag = True
    elif int(devam_kontrol)==0:
         print("İyi günler")
         Flag = False
                    
            


    
   
    
    





