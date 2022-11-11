urun_adi = input("urun adini giriniz")
guncel_fiyat = int(input("guncel fiyati giriniz"))
gecen_fiyat = int(input("gecen ayki fiyatı giriniz"))

degisim_miktari = guncel_fiyat - gecen_fiyat
degisim_yuzdesi = (degisim_miktari / gecen_fiyat)*100

print(f"Degisim miktarı: {degisim_miktari}")
print(f"Degisim yuzdesi: % {degisim_yuzdesi:.2f}")