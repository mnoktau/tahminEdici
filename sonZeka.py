import random
import numpy as np

# Pozisyon kesişim kontrolü için fonksiyon
def check_position_intersection(positions):
    # Referans diziler
    asc_order = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    desc_order = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    # Kesişen sayıları bul
    intersections = []
    for i, pos in enumerate(positions):
        if pos == asc_order[i] or pos == desc_order[i]:
            intersections.append(pos)
    
    # Tek kesişim olmalı ve bu 5 olmamalı
    if len(intersections) == 1 and intersections[0] != 5:
        return intersections[0]  # Tek kesişen sayıyı döndür
    return None

# Birinci Kod: Rastgele sayılar üret ve yüzdeleri hesapla
n = 9

def ana_bulucu():
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    while True:
        random_number = random.choice(arr)
        if random_number == "0":
            return bulucu_ilk_sayi()

def bulucu_ilk_sayi():
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    birA = random.choice(arr)
    return birA, bulucu_ikinci_sayi(birA)

def bulucu_ikinci_sayi(birA):
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    sayar = 0
    ulasici = []
    while True:
        random_number2 = random.choice(arr)
        if random_number2 == "0" and sayar == 0:
            kontrol_sayi = random.choice(arr)
            if kontrol_sayi == "0":
                return "0"
            else:
                sayar += 1
                ulasici.append(kontrol_sayi)
                continue
        elif random_number2 == "0" and sayar != 0:
            birB = ulasici[sayar - 1]
            return birB
        else:
            sayar += 1
            ulasici.append(random_number2)

def transform_number(number, user_input, transformations):
    original = number
    if number == "0":
        result = f"{user_input}{user_input}"
        transformations.append((original, result))
        return result, True
    elif number == "10":
        result = f"{1}{user_input}"
        transformations.append((original, result))
        return result, True
    elif number in ["2", "8", "1", "9", "7", "3"]:
        result = f"{user_input}{number}"
        transformations.append((original, result))
        return result, True
    return number, False

def print_first_n_digits(user_input, n):
    arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
    results = []
    transformations = []
    both_transformed_indices = []
    
    for i in range(n):
        result = ana_bulucu()
        if result:
            birA_transformed, birA_transformed_flag = transform_number(result[0], user_input, transformations)
            birB_transformed, birB_transformed_flag = transform_number(result[1], user_input, transformations)
            results.append((birA_transformed, birB_transformed))
            if birA_transformed_flag and birB_transformed_flag:
                both_transformed_indices.append(i + 1)
    
    flat_results = [item for tup in results for item in tup]
    first_n_elements = flat_results[:n]
    
    return first_n_elements, transformations

# Birinci referansı üret
while True:
    # İlk olarak geçici bir user_input ile sayılar üret
    temp_user_input = random.randint(1, 9)  # Geçici user_input (1-9)
    first_n_elements, _ = print_first_n_digits(temp_user_input, n)
    
    # Üretilen ilk sayının birler basamağını al
    try:
        first_element = first_n_elements[0]
        first_element_int = int(first_element)  # İlk elemanı sayıya çevir
        user_input = first_element_int % 10  # Birler basamağını al
    except (ValueError, IndexError):
        print("İlk eleman geçersiz, yeniden deneniyor...")
        continue
    
    if user_input == 0:  # user_input 0 olmamalı
        print("İlk sayının birler basamağı 0, yeniden deneniyor...")
        continue
    
    # user_input ile nihai sayıları üret
    first_n_elements, transformations = print_first_n_digits(user_input, n)
    
    # Nihai listenin ilk elemanının birler basamağının user_input ile uyumlu olduğunu kontrol et
    try:
        final_first_element = first_n_elements[0]
        final_first_element_int = int(final_first_element)
        final_first_digit = final_first_element_int % 10
        if final_first_digit != user_input:
            print(f"Nihai listenin ilk elemanının birler basamağı ({final_first_digit}) user_input ({user_input}) ile uyumsuz, yeniden deneniyor...")
            continue
    except (ValueError, IndexError):
        print("Nihai listenin ilk elemanı geçersiz, yeniden deneniyor...")
        continue
    
    unique_elements = set(first_n_elements)
    if len(unique_elements) == len(first_n_elements):
        print("\n" + "="*50 + "\n")
        print(f"Kullanıcı girişi (ilk üretilen sayının birler basamağı): {user_input}")
        print(f"Üretilen sayılar: {first_n_elements}")
        
        sayilar = []
        for element in first_n_elements:
            try:
                sayilar.append(float(element))
            except ValueError:
                sayilar.append(float(element[0]))
        
        toplam_agirlik = sum(sayilar)
        yuzdeler1 = [(sayi / toplam_agirlik) * 100 for sayi in sayilar]
        
        transformed_indices = []
        for i, num in enumerate(first_n_elements):
            for original, transformed in transformations:
                if num == transformed and i < n:
                    transformed_indices.append(i)
                    break
        
        sabit_pozisyonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        print(f"\nGirilen sayıların çıkma yüzdeleri (ilk {n} sayı):")
        for i, (pozisyon, sayi, yuzde) in enumerate(zip(sabit_pozisyonlar, sayilar, yuzdeler1)):
            print(f"{pozisyon}. sayı ({sayi}): %{yuzde:.2f}")
        
        yuzde_siralama = sorted(zip(yuzdeler1, sabit_pozisyonlar, sayilar), key=lambda x: x[0])
        print(f"\nGirilen sayıların çıkma yüzdeleri (küçükten büyüğe):")
        referans1_yuzdeler = []
        referans1_isimler = []
        positions = []  # Pozisyonları tutacak liste
        for i, (yuzde, pozisyon, sayi) in enumerate(yuzde_siralama, 1):
            print(f"{i}. % {yuzde:.2f} ({pozisyon}. pozisyon, sayı: {sayi})")
            referans1_yuzdeler.append(yuzde)
            referans1_isimler.append(str(pozisyon))
            positions.append(pozisyon)  # Pozisyonları ekle
        
        # Pozisyon kesişim kontrolü
        intersecting_number = check_position_intersection(positions)
        if intersecting_number is None:
            print("Kesişim koşulu sağlanmadı (ya tek kesişim yok ya da kesişim 5), yeniden deneniyor...")
            continue
        
        rastgele_sayi = random.randint(1, 9)
        print("Rastgele Sayı: ", rastgele_sayi)
        
        # İkinci Kod: Eşit oranlarla yüzdelik dağılım
        def hesapla_yuzde(oranlar):
            ters_oranlar = np.reciprocal(oranlar.astype(float))
            yuzdeler = (ters_oranlar / ters_oranlar.sum()) * 100
            return yuzdeler

        oranlar = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1])
        yuzdeler2 = hesapla_yuzde(oranlar)

        son_deger = 5
        hedef_yuzde = son_deger * 10 - 5

        toplam_yuzde = 0
        secili_index = None

        for i, yuzde in enumerate(yuzdeler2):
            toplam_yuzde += yuzde
            if toplam_yuzde >= hedef_yuzde:
                secili_index = i
                break

        referans2_yuzdeler = []
        referans2_isimler = []
        yuzde_siralama2 = sorted(zip(yuzdeler2, range(1, 10), oranlar), key=lambda x: x[0])
        for i, (yuzde, sira, oran) in enumerate(yuzde_siralama2, 1):
            print(f"{i}. Oran: {oran}, Yüzde: {yuzde:.2f}% (Sıra: {sira})")
            referans2_yuzdeler.append(yuzde)
            referans2_isimler.append(str(sira))

        # Üçüncü Kod: Sadece aynı isimle kesişen aralıkları bul
        def kesisen_araliklari_bul(array1, isimler1, array2, isimler2, yon="Birinci → İkinci"):
            def kumulatif_araliklar(array):
                araliklar = []
                toplam = 0
                for yuzde in array:
                    baslangic = toplam
                    toplam += yuzde
                    araliklar.append((baslangic, toplam))
                return araliklar

            araliklar1 = kumulatif_araliklar(array1)
            araliklar2 = kumulatif_araliklar(array2)
            
            ayni_isim_kesisim_detaylari = []

            print(f"\n{yon} Analizi")
            print(f"Birinci array toplamı: %{sum(array1):.2f}")
            print(f"İkinci array toplamı: %{sum(array2):.2f}")

            for i, (bas1, son1) in enumerate(araliklar1):
                kesisen_indeksler = []
                kesisen_detaylar = []
                ayni_isim_kesisimler = []

                for j, (bas2, son2) in enumerate(araliklar2):
                    baslangic = max(bas1, bas2)
                    bitis = min(son1, son2)
                    if baslangic < bitis:
                        kesisen_indeksler.append(j)
                        detay = {
                            'aralik': (baslangic, bitis),
                            'birinci_indeks': i,
                            'birinci_isim': isimler1[i],
                            'birinci_yuzde': array1[i],
                            'ikinci_indeks': j,
                            'ikinci_isim': isimler2[j],
                            'ikinci_yuzde': array2[j]
                        }
                        kesisen_detaylar.append(detay)
                        if isimler1[i] == isimler2[j]:
                            ayni_isim_kesisimler.append(detay)
                            ayni_isim_kesisim_detaylari.append(detay)

            return ayni_isim_kesisim_detaylari

        # Kesişim analizlerini çalıştır
        birinci_ikinci_ayni_isim_kesisimler = kesisen_araliklari_bul(
            referans1_yuzdeler, referans1_isimler, referans2_yuzdeler, referans2_isimler, yon="Birinci → İkinci"
        )

        ikinci_birinci_ayni_isim_kesisimler = kesisen_araliklari_bul(
            referans2_yuzdeler, referans2_isimler, referans1_yuzdeler, referans1_isimler, yon="İkinci → Birinci"
        )

        # Ortak kesişimleri bul
        ortak_kesisimler_birinci_ikinci = []
        ortak_kesisimler_ikinci_birinci = []

        for b_i in birinci_ikinci_ayni_isim_kesisimler:
            for i_b in ikinci_birinci_ayni_isim_kesisimler:
                if (b_i['aralik'] == i_b['aralik'] and
                    b_i['birinci_isim'] == i_b['ikinci_isim'] and
                    b_i['ikinci_isim'] == i_b['birinci_isim']):
                    ortak_kesisimler_birinci_ikinci.append(b_i)
                    ortak_kesisimler_ikinci_birinci.append(i_b)

        # Kesişimlerin intersecting_number içerdiğini kontrol et
        valid_intersection = False
        for detay in ortak_kesisimler_birinci_ikinci:
            if detay['birinci_isim'] == str(intersecting_number) or detay['ikinci_isim'] == str(intersecting_number):
                valid_intersection = True
                break

        if not valid_intersection:
            print(f"Kesişimler {intersecting_number} sayısını içermiyor, yeniden deneniyor...")
            continue

        # Sonuçları yazdır
        print("\n" + "="*50 + "\nTÜM KOŞULLAR SAĞLANDI - SONUÇLAR\n" + "="*50)
        print(f"Kullanıcı girişi (ilk üretilen sayının birler basamağı): {user_input}")
        print(f"Üretilen sayılar: {first_n_elements}")
        print(f"Kesişen sayı: {intersecting_number}")
        print(f"\nGirilen sayıların çıkma yüzdeleri (ilk {n} sayı):")
        for i, (pozisyon, sayi, yuzde) in enumerate(zip(sabit_pozisyonlar, sayilar, yuzdeler1)):
            print(f"{pozisyon}. sayı ({sayi}): %{yuzde:.2f}")

        print(f"\nGirilen sayıların çıkma yüzdeleri (küçükten büyüğe):")
        for i, (yuzde, pozisyon, sayi) in enumerate(yuzde_siralama, 1):
            print(f"{i}. % {yuzde:.2f} ({pozisyon}. pozisyon, sayı: {sayi})")

        print("\nSadece Aynı İsimle Ortak Kesişim Değerleri")
        print("\nBirinci → İkinci Yönünde Aynı İsimle Ortak Kesişimler:")
        if ortak_kesisimler_birinci_ikinci:
            for detay in ortak_kesisimler_birinci_ikinci:
                print(f"- Kesişim: {detay['aralik']}, "
                      f"Birinci: {detay['birinci_isim']} (indeks {detay['birinci_indeks']}, %{detay['birinci_yuzde']:.2f}), "
                      f"İkinci: {detay['ikinci_isim']} (indeks {detay['ikinci_indeks']}, %{detay['ikinci_yuzde']:.2f})")
        else:
            print("Aynı isimle ortak kesişim bulunamadı.")

        print("\nİkinci → Birinci Yönünde Aynı İsimle Ortak Kesişimler:")
        if ortak_kesisimler_ikinci_birinci:
            for detay in ortak_kesisimler_ikinci_birinci:
                print(f"- Kesişim: {detay['aralik']}, "
                      f"Birinci: {detay['birinci_isim']} (indeks {detay['birinci_indeks']}, %{detay['birinci_yuzde']:.2f}), "
                      f"İkinci: {detay['ikinci_isim']} (indeks {detay['ikinci_indeks']}, %{detay['ikinci_yuzde']:.2f})")
        else:
            print("Aynı isimle ortak kesişim bulunamadı.")

        break
    else:
        print(f"İlk {n} elemanda tekrar eden sayı var, yeniden deneniyor...")
        continue
