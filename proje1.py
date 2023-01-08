yeni_kutu = 'E'

while yeni_kutu == 'E' or 'e':
    bilye_sayisi = int(input("Lütfen kutudaki bilye sayısını giriniz:"))
    hatali_bilye = dogru_bilye = 0
    i = bilye1 = bilye2 = 0

    while bilye_sayisi < 10:
        bilye_sayisi = int(input("Bilye sayısı 10 ya da daha büyük bir değer olmalıdır! Lütfen tekrar giriniz:"))
    # for i in range(bilye_sayisi):
    while i < bilye_sayisi and hatali_bilye <= 1:
        bilye_agirligi = int(input("Lütfen bilyenin ağırlığını giriniz:"))
        if i == 0:
            bilye1 = bilye_agirligi
        elif i == 1:
            bilye2 = bilye_agirligi

        if bilye1 != bilye_agirligi :
            hatali_bilye += 1
        else:
                dogru_bilye += 1
        if hatali_bilye > 1:
            print("1'den fazla hatalı bilye bulundu!")
        i += 1

    yeni_kutu = input("Yeni kutu var mı? 'E', 'e', 'H', 'h'")
