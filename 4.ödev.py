yas = int(input("Yaşınızı giriniz:"))
son_ucret = int(input("Son yıllık ücretinizi giriniz:"))
takim_sira = int(input("Takımınızın normal sezondaki sırasını giriniz:"))
TAKIM_SAYISI = 14
MAC_SAYISI = (TAKIM_SAYISI - 1) * 2

if yas < 22:  # yaşa göre serbest kalma durumunu değerlendirir
    serbest_kalma = "Serbest kalma hakkınız bulunmamaktadır"
    serbest_kalma_m = ""
else:  # yaş 22'den büyükse true döndürür
    serbest_kalma = "Serbest kalma hakkınız bulunmaktadır"
    if yas == 22:
        serbest_kalma_m = son_ucret * 2
    elif yas == 23:
        serbest_kalma_m = son_ucret
    elif yas == 24:
        serbest_kalma_m = son_ucret / 2
    else:
        serbest_kalma_m = 0
    serbest_kalma_m = f", serbest kalma maliyetiniz {serbest_kalma_m:.2f} TL"

if takim_sira > 8:  # takım sırasına göre playoff'a katılıp katılmadığı durumları ele alır
    maliyet = son_ucret / MAC_SAYISI
else:
    po_mac_sayisi = int(input("Takımınızın playoff sezonunda oynadığı maç sayısını giriniz:"))
    maliyet = son_ucret / (MAC_SAYISI + po_mac_sayisi)

print(f"Oynadığınız maç başına takıma maliyetiniz: {maliyet:.2f} TL")
print(f"{serbest_kalma}{serbest_kalma_m}")
