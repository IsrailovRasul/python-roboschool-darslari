# -*- coding: utf-8 -*-
"""

Muallif: Rasul Israilov 
Mavzu: If else elif  or end operatorlari bilan tanishamiz 
Created on Wed Feb 22 12:02:33 2023
if-elif-else KETMA-KETLIGI
Dastur davomida bir nechta shartni tekshirish talab qilinishi mumkin. Bunday holatda biz if-elif-else ketma-ketligidan 
foydalanamiz. elif - else va if so'zalrining jamlanmasi bo'lib, "aks holda, agar" deb tarjima qilinadi. Bunday if bilan
 boshlangan ketma-ketlik bir nechta elif lardan iborat bo'lishi mumkin. 
Python avval if shartini tekshiradi, shart bajarilmasa elif ga o'tadi, birinchi elif sharti bajarilmasa keyingi
 elif ga o'tadi va hokazo davom etaveradi.
 Diqqat!if-elif-else ketma-ketlikda biror shart bajarilishi bilan, Python qolgan shartlarni tekshirmaydi.
Keling bir misol ko'ramiz. Hayvonot bo'giga kirish quyidagicha belgilangan:
4 yoshdan kichik bolalarga kirish bepul
4 yoshdan 12 yoshgacha kirish 5000 so'm
12 yoshdan kattalarga 10000 so'm
Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini chiqaruvchi dastur yozamiz.
@author: User
"""
# 

"""   
Kod yozishda yaxshi amaliyotlardan biri, kodlarni qisqa yozish va buyruqlarni qayta-qayta takrorlamaslik.
 Bu kelajakda kodni o'zgartirishda ham juda qo'l keladi.  
 """ 
#  

"""
Avval aytganimizdek,  if-elif-else zanjirida bit nechta elif lar bo'lishi mumkin. Misol uchun, hayvonot bog'i 
qariyalar uchun chegirma e'lon qilsa, kodimizni quyidagicha o'zgartirishimiz mumkin:
    """
yosh = int(input('Yoshingiz nechida? '))
if yosh<=4: # yosh bolalarga bepul
    som = 0
elif yosh<=12: # 4 dan 12 yoshgacha 5000 so'm
    som  = 5000   #kichiklarga narh 10000 so'm

else: # qariyalarga esa 8000 so'm
    som  = 8000
print(f"Sizga kirish {som } so'm")


"""
if-elif-else zanjirida ham else qismi majburiy emas:
    """
    
yosh = int(input('Yoshingiz nechida? '))
if yosh<=4:
    price = 0
elif yosh<=12:
    price = 5000
elif yosh<65:
    price = 10000
elif yosh>=65:
    price = 8000    
print(f"Sizga kirish {price} so'm")


"""
AND, OR OPERATORLARI
Yuqorida aytganimizdek, if-elif-else zanjirida shartlarning biri bajarilishi bilan,
 Python qolgan shartlarni tekshirmaydi va ularni bajarmaydi. Lekin ba'zida biz 2 yoki undan ko'p 
 shartlarni tekshirishni talab qilishimiz mumkin,
 buing uchun AND va OR operatorlaridan foydalanamiz.
OR OPERATORI
OR ingliz tilidan "yoki" deb tarjima qilinadi, va ikki va undan ko'p shartlardan biri bajarilishini 
tekshirishda ishlatiladi. Quyidagi misolni ko'raylik, foydalanuvchidan hafta kunini so'raymiz va 
agar kun shanba yoki yakshanba bo'lsa, 
bugun dam olish kuni degan xabarni chiqaramiz, aks holda bugun ish kuni degan xabarni chiqaramiz:

    """
ism=input("Ismingizni kiriting \n>>> ")    
kun = input("Bugun nima kun?>>>")
if kun.lower()=='shanba' or kun.lower()=='yakshanba':
    print(f" {ism.title()} aka bugun dam olish kuni dam oling ")
else:
    print(f"{ism.title()} Bugun ish kuni, ishga boring !!!")    
"""
AND OPERATORI
AND ingliz tilidan "va" deb tarjima qilinadi, va ikki va undan ko'p shartlarning barchasi bajarilishini 
tekshirishda ishlatiladi. AND operatori bilan yozilgan shartlarning barchasi bajarilgandagina TRUE qiymati qaytadi, 
agar shartlardan biri bajarilmay qolsa ham FALSE qiymati qaytadi.
Quyidagi misolni ko'ramiz:  
    """
kun = input("Bugun nima kun?")
harorat = float(input("Havo harorati qanday?"))
if kun.lower()=='yakshanba' and harorat>=30:
    print("Cho'milgani ketdik!")
elif kun.lower()=='yakshanba' and harorat<=30:
     print("Uyda dam olamiz!" )
# else:  
#       print(" Bugun uyda o\'tiring")
