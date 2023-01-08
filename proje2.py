def oyun_alani(boyut, karakter1, karakter2):
    satir = [" " for i in range(boyut)]
    board = [satir.copy() for k in range(boyut)]
    board[0], board[boyut - 1] = ([karakter1 for i in range(boyut)]), ([karakter2 for i in range(boyut)])
    return board


def tabloyu_yazdir(board, boyut):
    """Tabloyu ekrana yazdırmamızı sağlayan fonksiyon."""
    sutun_ad = " ABCDEFGH"
    for sutun in range(boyut + 1):
        print(f"{sutun_ad[sutun]:^4}", end="")
    print("\n   " + "-" * (4 * boyut + 1) + "   ")

    for satir in range(boyut):
        print(f"{satir + 1:^3}", end="|")
        for sutun in range(boyut):
            print(f"{board[satir][sutun]:^3}", end="|")
        print(f"{satir + 1:^3}")
        print("   " + "-" * (boyut * 4 + 1) + "   ")
    for sutun in range(boyut + 1):
        print(f"{sutun_ad[sutun]:^4}", end="")
    print("\n")


def carpisma_kontrol(mevcut_sutun, mevcut_satir, gidilecek_satir, gidilecek_sutun, board):
    """Taşın götürüleceği konum ve güzergah üzerinde farklı bir taş olup olmadığını anlamamızı sağlayan fonksiyon."""

    if gidilecek_satir == mevcut_satir:  # Yatay hareket

        if gidilecek_sutun > mevcut_sutun:  # Sağa gidilecekse
            baslangic_kon = mevcut_sutun
            for i in range(1, abs(gidilecek_sutun - mevcut_sutun)):
                baslangic_index = abs(i - baslangic_kon)
                if board[mevcut_satir][baslangic_index] != " ":
                    return False

        else:  # Sola gidilecekse
            baslangic_kon = gidilecek_sutun
            for i in range(abs(gidilecek_sutun - mevcut_sutun)):
                baslangic_index = abs(i - baslangic_kon)
                if board[mevcut_satir][baslangic_index] != " ":
                    return False

    elif gidilecek_sutun == mevcut_sutun:  # Düşey hareket
        if mevcut_satir > gidilecek_satir:  # Yukarı gidecekse
            baslangic_kon = mevcut_satir
            for i in range(1, abs(gidilecek_satir - mevcut_satir) + 1):
                baslangic_index = abs(i - baslangic_kon)
                if board[baslangic_index][mevcut_sutun] != " ":
                    return False

        else:  # Aşağı gidecekse
            baslangic_kon = gidilecek_satir
            for i in range(abs(gidilecek_satir - mevcut_satir)):
                baslangic_index = abs(i - baslangic_kon)
                if board[baslangic_index][mevcut_sutun] != " ":
                    return False

    else:
        return True


def hareket_et(board, boyut, karakter1, karakter2, sayac):
    """Taşın hareket etmesini sağlayan fonksiyon."""

    def konum_hesapla(konum):
        """mevcut_sutun, mevcut_satir, gidilecek_sutun, gidilecek_satir değişkenlerini sırasıyla döndürür"""
        return (konum_index[konum[0]], konum_index[konum[1]], konum_index[konum[2]], konum_index[konum[3]])

    konum_index = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
                   "1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}
    karakterler = [karakter1, karakter2]

    while True:
        # Kullanıcıdan konum bilgisini alıp hata kontrolü yapar
        konum = list(input(
            f"Oyuncu {karakterler[sayac % 2]}, lütfen hareket ettirmek istediğiniz kendi taşınızın konumunu ve hedef konumu giriniz: ").upper())
        konum.remove(" ")
        if  konum[0] in "ABCDEFGH" and konum[2] in "ABCDEFGH" and konum[1] in "123456789" and konum[3] in "123456789":
            break
        else:
            print("Hatalı veri girişi!")

    while konum[0] == konum[2] and konum[1] == konum[3]:
        konum = list(input(
            f"Oyuncu {karakterler[sayac % 2]}, bulunduğunuz konuma hareket edemezsiniz. Lütfen tekrar giriniz: ").upper())
        konum.remove(" ")

    while not (konum[0] == konum[2] or konum[1] == konum[3]):
        konum = list(input(f"Oyuncu {karakterler[sayac % 2]}, sadece yatay ve dikey şekilde hareket edebilirsiniz, tekrar giriniz: ").upper())
        konum.remove(" ")

    mevcut_sutun, mevcut_satir, gidilecek_sutun, gidilecek_satir = konum_hesapla(konum)
    while karakterler[sayac % 2] != board[mevcut_satir][mevcut_sutun]:
        while True:
            try:
                konum = list(input(
                    f"Oyuncu {karakterler[sayac % 2]}, sadece kendi taşınızı oynatabilirsiniz, lütfen tekrar giriniz: ").upper())
                break
            except:
                print("Hatalı veri girişi!")
        konum.remove(" ")
        mevcut_sutun, mevcut_satir, gidilecek_sutun, gidilecek_satir = konum_hesapla(konum)

    while carpisma_kontrol(mevcut_sutun, mevcut_satir, gidilecek_satir, gidilecek_sutun, board) == False:
        gidilecek_satir, gidilecek_sutun = mevcut_satir, mevcut_sutun
        while True:
            try:
                konum = list(input(
                    f"Oyuncu {karakterler[sayac % 2]}, gitmek istediğiniz yerde veya yolunuzda başka bir taş vardır! Lütfen tekrar giriniz: ").upper())
                break
            except:
                print("Hatalı veri girişi!")
        konum.remove(" ")
        mevcut_sutun, mevcut_satir, gidilecek_sutun, gidilecek_satir = konum_hesapla(konum)

    sembol = board[mevcut_satir][mevcut_sutun]
    board[mevcut_satir][mevcut_sutun] = " "
    board[gidilecek_satir][gidilecek_sutun] = sembol

    return mevcut_sutun, mevcut_satir, gidilecek_satir, gidilecek_sutun, board


def eleme(karakter1, karakter2, gidilecek_satir, gidilecek_sutun, board, sayac, boyut):
    """Taşın oyun kurallarına göre kilitlenip kilitlenmediğini anlayan, bu duruma göre taşı oyun tahtasından çıkaran fonksiyon."""
    dost_kar, rakip_kar = (karakter1, karakter2) if sayac % 2 == 0 else (karakter2, karakter1)

        # Öncesinde taşın köşede olup olmama durumunu kontrol edip, elenme durumunu buna göre kontrol ediyoruz.
    if board[0][0] == rakip_kar:
        if board[1][0] and board[0][1] == dost_kar:
            board[0][0] = " "
    if board[boyut - 1][0] == rakip_kar:
        if board[boyut - 2][0] and board[1][boyut - 1] == dost_kar:
            board[boyut - 1][0] = " "
    if board[0][boyut - 1] == rakip_kar:
        if board[0][boyut - 2] and board[1][boyut - 1] == dost_kar:
            board[0][boyut - 1] = " "
    if board[boyut - 1][boyut - 1] == rakip_kar:
        if board[boyut - 2][boyut - 1] and board[boyut - 1][boyut - 2] == dost_kar:
            board[boyut - 1][boyut - 1] = " "

    try:
        """ Hareket eden taşın etrafında bir taş varsa eğer, o taşın aynı hizadaki bir sonraki index'ini kontrol etmesini
        sağlayan kod parçası."""
        if board[gidilecek_satir - 1][gidilecek_sutun] == rakip_kar:
            if board[gidilecek_satir - 2][gidilecek_sutun] == dost_kar:
                board[gidilecek_satir - 1][gidilecek_sutun] = " "
        if board[gidilecek_satir + 1][gidilecek_sutun] == rakip_kar:
            if board[gidilecek_satir + 2][gidilecek_sutun] == dost_kar:
                board[gidilecek_satir + 1][gidilecek_sutun] = " "
        if board[gidilecek_satir][gidilecek_sutun - 1] == rakip_kar:
            if board[gidilecek_satir][gidilecek_sutun - 2] == dost_kar:
                board[gidilecek_satir][gidilecek_sutun - 1] = " "
        if board[gidilecek_satir][gidilecek_sutun + 1] == rakip_kar:
            if board[gidilecek_satir][gidilecek_sutun + 2] == dost_kar:
                board[gidilecek_satir][gidilecek_sutun + 1] = " "
    except IndexError:
        print(end="")

    tabloyu_yazdir(board, boyut)


def kazanma(board, karakter1, karakter2, kazanan):
    karakter1_say = 0
    karakter2_say = 0
    for i in range(len(board)):
        karakter1_say += board[i].count(karakter1)
        karakter2_say += board[i].count(karakter2)

    if karakter1_say < 2:
        kazanan = karakter2
    elif karakter2_say < 2:
        kazanan = karakter1

    return kazanan


def main():
    devam = "E"
    while devam in "Ee":
        while True:
            try:
                boyut = (input("Lütfen oyun alanının boyutunu giriniz(4x4-8x8): "))
                boyut = int(boyut[0])
                karakter1 = input("Lütfen 1. oyuncuyu temsil edecek karakteri giriniz: ")
                karakter2 = input("Lütfen 2. oyuncuyu temsil edecek karakteri giriniz: ")
                break
            except:
                print("Hatalı veri girişi!")

        board = oyun_alani(boyut, karakter1, karakter2)
        tabloyu_yazdir(board, boyut)
        sayac = 0
        kazanan = " "
        while kazanan == " ":  # Fonksiyonların çalışma amaçlarını öğrenmek için imleci üstüne getirin.
            mevcut_sutun, mevcut_satir, gidilecek_satir, gidilecek_sutun, board = hareket_et(board, boyut, karakter1,
                                                                                             karakter2, sayac)
            carpisma_kontrol(mevcut_sutun, mevcut_satir, gidilecek_satir, gidilecek_sutun, board)
            eleme(karakter1, karakter2, gidilecek_satir, gidilecek_sutun, board, sayac, boyut)
            sayac += 1
            kazanan = kazanma(board, karakter1, karakter2, kazanan)
        print(f"Tebrikler. Kazanan kişi {kazanan}.")
        devam = input("Oynamaya devam etmek ister misiniz? (eEhH): ")

main()
