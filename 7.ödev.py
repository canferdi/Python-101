def istatistik_hesapla(okcu_sayisi, atis_hakki):
    puanlar = []
    top_puanlar = []
    ruzgarlar = {
            'Yıldız':0,
            'Poyraz':0,
            'Gündoğusu':0,
            'Keşişleme':0,
            'Kıble':0,
            'Lodos':0,
            'Günbatısı':0,
            'Karayel':0}
    for atis_turu in range(atis_hakki):   # iç içe liste oluşturup döndürme
        for okcu in range(okcu_sayisi):
            if atis_turu == 0:
                puanlar.append([])   #liste içinde okçu sayısı kadar boş liste oluşturur
            puan = int(input(f"{okcu + 1}. okçunun {atis_turu + 1}. siradaki atışta aldığı puanı giriniz: "))
            if puan == 0:   #ruzgar değerlerini ruzgarlar sözlüğüne atar
                ruzgar = input("Lütfen atış sırasında esen rüzgarın adını giriniz:")
                if ruzgar in ruzgarlar:
                    ruzgarlar[ruzgar] += 1
                else:
                    ruzgarlar[ruzgar] = 1
            puanlar[okcu].append(puan)  # alınan puanı puanlar listesine puanlar listesini de sira_dict sözlüğüne atar
            top_puanlar.append(puan)



    top_puan_say = len(top_puanlar)
    print("Okçu Kayıt No   10P    9P     8P     7P     6P     5P     4P     3P     2P     1P      0P   Toplam Puan")
    print("-------------  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----  -----------")
    for kayit_no in range(okcu_sayisi):
        print(f"{kayit_no + 1:<13}",end='  ')
        print(f"{puanlar[kayit_no].count(10):<5}",end='  ')
        print(f"{puanlar[kayit_no].count(9):<5}",end='  ')
        print(f"{puanlar[kayit_no].count(8):<5}",end='  ')
        print(f"{puanlar[kayit_no].count(7):<5}",end='  ')
        print(f"{puanlar[kayit_no].count(6):<5}",end='  ')
        print(f"{puanlar[kayit_no].count(5):<5}",end='  ')
        print(f"{puanlar[kayit_no].count(4):<5}",end='  ')
        print(f"{puanlar[kayit_no].count(3):<5}",end='  ')
        print(f"{puanlar[kayit_no].count(2):<5}",end='  ')
        print(f"{puanlar[kayit_no].count(1):<5}",end='  ')
        print(f"{puanlar[kayit_no].count(0):<5}",end='  ')
        print(f"{sum(puanlar[kayit_no]):<11}")
    print(f"Tüm Okçular(%)",end=' ')
    print(f"{100*top_puanlar.count(10)/top_puan_say:<5.2f}",end='  ')
    print(f"{100*top_puanlar.count(9)/top_puan_say:<5.2f}",end='  ')
    print(f"{100*top_puanlar.count(8)/top_puan_say:<5.2f}",end='  ')
    print(f"{100*top_puanlar.count(7)/top_puan_say:<5.2f}",end='  ')
    print(f"{100*top_puanlar.count(6)/top_puan_say:<5.2f}",end='  ')
    print(f"{100*top_puanlar.count(5)/top_puan_say:<5.2f}",end='  ')
    print(f"{100*top_puanlar.count(4)/top_puan_say:<5.2f}",end='  ')
    print(f"{100*top_puanlar.count(3)/top_puan_say:<5.2f}",end='  ')
    print(f"{100*top_puanlar.count(2)/top_puan_say:<5.2f}",end='  ')
    print(f"{100*top_puanlar.count(1)/top_puan_say:<5.2f}",end='  ')
    print(f"{100*top_puanlar.count(0)/top_puan_say:<5.2f}\n")
    print("Rüzgar Adı   Iska atış oranı(%)")
    print("----------   ------------------")
    ruzgar_top = tuple(ruzgarlar.values())
    for ruzgar_al in ruzgarlar:
        print(f"{ruzgar_al:<10}",end='   ')
        print(f"{100*ruzgarlar[ruzgar_al]/sum(ruzgar_top):<12.2f}")


def main():
    okcu_sayisi = int(input("Lütfen yarışmaya katılan okçu sayısını giriniz: "))
    atis_hakki = int(input("Lütfen okçulara verilen atış hakkı sayısını giriniz: "))
    istatistik_hesapla(okcu_sayisi, atis_hakki)


main()
