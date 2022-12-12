mac_sayisi = int(input("Oynanan maç sayısını giriniz:"))
top_kazanilan_sayi = 0
top_kaybedilen_sayi = 0
top_kazanilan_set = 0
top_kaybedilen_set = 0
top_kazanilan_mac = 0
top_kaybedilen_mac = 0
top_kayipsiz_set = 0
kazanilan_sayi_ort = 0
kaybedilen_sayi_ort = 0
top_sayi_fark = 0

for i in range(mac_sayisi):  # mac sayısını hesaplar
    rakip_ad = input("Rakip takımın adını giriniz:")

    set_kazanilan_sayi = 0
    set_kaybedilen_sayi = 0
    set_kazanilan_set = 0
    set_kaybedilen_set = 0
    set_kazanilan_mac = 0
    set_kaybedilen_mac = 0

    while set_kazanilan_set != 3 and set_kaybedilen_set != 3:  # set sayısını hesaplar
        kazanilan_sayi = int(input("Kazanılan sayi adedini giriniz:"))
        kaybedilen_sayi = int(input("Kaybedilen sayı adedini giriniz:"))
        set_kazanilan_sayi += kazanilan_sayi
        set_kaybedilen_sayi += kaybedilen_sayi

        if kaybedilen_sayi < kazanilan_sayi:
            set_kazanilan_set += 1
        else:
            set_kaybedilen_set += 1
        top_sayi = set_kazanilan_sayi + set_kaybedilen_sayi
        kazanilan_sayi_ort = kazanilan_sayi / top_sayi
        kaybedilen_sayi_ort = kaybedilen_sayi / top_sayi

        if set_kazanilan_set == 3 and set_kaybedilen_set == 0:
            top_kayipsiz_set += 1
        if set_kazanilan_set >= 3:
            set_kazanilan_mac += 1

        elif set_kaybedilen_set > 3:
            set_kaybedilen_mac += 1

    top_kazanilan_sayi += set_kazanilan_sayi
    top_kaybedilen_mac += set_kaybedilen_sayi
    top_kazanilan_set += set_kaybedilen_sayi
    top_kaybedilen_set += set_kaybedilen_set
    top_kazanilan_mac += set_kazanilan_mac
    top_kaybedilen_mac += set_kaybedilen_mac
    top_mac_sayi = top_kazanilan_sayi + top_kaybedilen_sayi
    top_sayi_fark = top_kazanilan_sayi - top_kaybedilen_sayi
    print(f"Rakip takımın adı:{rakip_ad}")
    print(f"Kazanılan toplam sayı:{set_kazanilan_sayi}")
    print(f"Kaybedilen toplam sayı:{set_kaybedilen_sayi}")
    print(f"Kazanılan toplam set: {set_kazanilan_set}")
    print(f"Kaybedilen toplam set: {set_kaybedilen_set}")
    print(f"Set başına kazanılan sayı ortalaması {kazanilan_sayi_ort:.2f}")
    print(f"Set başına kaybedilen sayı ortalaması {kaybedilen_sayi_ort:.2f}")
print(f"Sezon boyunca kazanılan toplam sayı:{top_kazanilan_sayi}")
print(f"Sezon boyunca maç başına kazanılan sayı ortalaması: {top_kazanilan_sayi / mac_sayisi:.2f}")
print(f"Sezon boyunca kazanılan toplam maç adedi:{top_kazanilan_mac}")
print(f"Sezon boyunca kaybedilen toplam maç adedi:{top_kaybedilen_mac}")
print(f"Sezon boyunca set kaybetmeden biten maçların sayısı:{top_kayipsiz_set}")
print(f"Sezon boyunca kazanılan toplam sayı ile kaybedilen toplam sayı arasındaki fark:{top_sayi_fark}")
