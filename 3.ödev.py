yas = int(input("Yaşınızı giriniz:"))
son_ucret = int(input("Son yıllık ücretinizi giriniz:"))
takim_sira = int(input("Takımınızın normal sezondaki sırasını giriniz:"))

if takim_sira < 8:
    po_mac_sayisi = int(input("Takımınızın playoffta oynadığı maç sayısını giriniz"))
    maliyet = son_ucret / (po_mac_sayisi + 26)
else:
    maliyet = son_ucret / 26

if yas < 22:
    serbest_kalma = "Serbest kalma hakkınız bulunmamaktadır, Serbest kalma maliyetiniz "
else:
    serbest_kalma = "Serbest kalma hakkınız bulunmaktadır"

if yas == 22:
    serbest_kalma_m = son_ucret * 2
elif yas == 23:
    serbest_kalma_m = son_ucret
elif yas == 24:
    serbest_kalma_m = son_ucret / 2
elif yas >= 25:
    serbest_kalma_m = 0

print(f"Oynadığınız maç başına takıma maliyetiniz: {maliyet:.2f} TL")
print(f"{serbest_kalma} {serbest_kalma_m:.2f} TL")