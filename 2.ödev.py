takim1_ad = input("İlk takımın adını giriniz:")
takim1_set = int(input("İlk takımın kazandığı set adedini giriniz:"))
takim2_ad = input("İkinci takımın adını giriniz:")
takim2_set = int(input("İkinci takımın kazandığı set adedini giriniz:"))
toplam_set = takim1_set + takim2_set

if takim2_set < takim1_set:
    kazanan_ad = takim1_ad
    kaybeden_ad = takim2_ad
else:
    kazanan_ad = takim2_ad
    kaybeden_ad = takim1_ad

if toplam_set < 5:
    kazanan_puan = 3
    kaybeden_puan = 0

else:
    kazanan_puan = 2
    kaybeden_puan = 1

print(f"Maçı kazanan takımın adı: {kazanan_ad}, kazandığı puan: {kazanan_puan}")
print(f"Maçı kaybeden takımın adı: {kaybeden_ad}, kazandığı puan: {kaybeden_puan}")
