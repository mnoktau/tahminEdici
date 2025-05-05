1. Run the program.

2. 1 of the intersections is the answer to a random number or ratio between 1-9.

It's that simple.

Now Let Me Explain The Program:
1. Where the number pi is the first "0", the numbers are created so that the numbers do not repeat from the place where the number is the first "0":
arr = ["0", "2", "8", "84", "1", "9", "7", "16", "93", "99", "3", "75", "10"]
2. A random number is drawn from this sequence, and when "0" comes, the next number is the first value: "birA". When "0" comes again, the previous number is the second value: "birB"
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

3. The numbers are set to be two-digit: this place is a bit tricky; for example, let's say "2" came; since it is "02", the first to create the array instead of "0"
we replace the value "birA" with the ones digit. So "birA", and "2" becomes the new number "22".
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

4. We continued the steps above until we created an array with 9 elements; however, we put it in a loop until our array with "9" elements always consists of different numbers.

5. We collected the entire "9" element array we created and took the percentage formed when we divided the number by this sum; that is, we found the percentages by making a sum of the number division.

and we sorted it from small to large.

7. We also made a percentage in which each number was evenly distributed: Since "9" is a number, each of them was in a percentage of "11.11".

8. We have conditioned the positions of these 2 sequences we have created in the form of intersections.

9. We also have two integer sequences; "1-2-3-4-5-6-7-8-9" and "9-8-7-6-5-4-3-2-1"; We compared them with the positions of numbers with percentages in our main reference sequence.

10. The main and final condition is this: If only "one" number intersects in the integer array and this number is not "5" and at the intersection in our main reference sequence and the equal percentage array, this

If there is a number; the answer is in all intersection numbers!

Example:
// Here we find our first "9" element array.
Kullanıcı girişi (ilk üretilen sayının birler basamağı): 4
Üretilen sayılar: ['84', '43', '48', '42', '44', '75', '47', '16', '93']
// Here we print the percentages of our "9" element array.
Girilen sayıların çıkma yüzdeleri (ilk 9 sayı):
1. sayı (84.0): %17.07
2. sayı (43.0): %8.74
3. sayı (48.0): %9.76
4. sayı (42.0): %8.54
5. sayı (44.0): %8.94
6. sayı (75.0): %15.24
7. sayı (47.0): %9.55
8. sayı (16.0): %3.25
9. sayı (93.0): %18.90
// Here we sort from small to large.
Girilen sayıların çıkma yüzdeleri (küçükten büyüğe):
1. % 3.25 (8. pozisyon, sayı: 16.0)
2. % 8.54 (4. pozisyon, sayı: 42.0)
3. % 8.74 (2. pozisyon, sayı: 43.0)
4. % 8.94 (5. pozisyon, sayı: 44.0)
5. % 9.55 (7. pozisyon, sayı: 47.0)
6. % 9.76 (3. pozisyon, sayı: 48.0)
7. % 15.24 (6. pozisyon, sayı: 75.0)
8. % 17.07 (1. pozisyon, sayı: 84.0)
9. % 18.90 (9. pozisyon, sayı: 93.0)
// Here we make a percentage where the chance of each element coming out is the same.
1. Oran: 1, Yüzde: 11.11% (Sıra: 1)
2. Oran: 1, Yüzde: 11.11% (Sıra: 2)
3. Oran: 1, Yüzde: 11.11% (Sıra: 3)
4. Oran: 1, Yüzde: 11.11% (Sıra: 4)
5. Oran: 1, Yüzde: 11.11% (Sıra: 5)
6. Oran: 1, Yüzde: 11.11% (Sıra: 6)
7. Oran: 1, Yüzde: 11.11% (Sıra: 7)
8. Oran: 1, Yüzde: 11.11% (Sıra: 8)
9. Oran: 1, Yüzde: 11.11% (Sıra: 9)

==================================================
TÜM KOŞULLAR SAĞLANDI - SONUÇLAR
==================================================

//When the conditions are met; we print the formed array, the user input according to the ones digit of the birA, and the intersecting number.
Kullanıcı girişi (ilk üretilen sayının birler basamağı): 4
Üretilen sayılar: ['84', '43', '48', '42', '44', '75', '47', '16', '93']
Kesişen sayı: 9

Girilen sayıların çıkma yüzdeleri (ilk 9 sayı):
1. sayı (84.0): %17.07
2. sayı (43.0): %8.74
3. sayı (48.0): %9.76
4. sayı (42.0): %8.54
5. sayı (44.0): %8.94
6. sayı (75.0): %15.24
7. sayı (47.0): %9.55
8. sayı (16.0): %3.25
9. sayı (93.0): %18.90
// Here for example: When we compare 8-4-2-5-7-3-6-1-9 with "1-2-3-4-5-6-7-8-9" and "9-8-7-6-5-4-3-2-1"; a single "9" matched as a position.
// If it was "5", it wouldn't be, because it would intersect in 2 arrays.
Girilen sayıların çıkma yüzdeleri (küçükten büyüğe):
1. % 3.25 (8. pozisyon, sayı: 16.0)
2. % 8.54 (4. pozisyon, sayı: 42.0)
3. % 8.74 (2. pozisyon, sayı: 43.0)
4. % 8.94 (5. pozisyon, sayı: 44.0)
5. % 9.55 (7. pozisyon, sayı: 47.0)
6. % 9.76 (3. pozisyon, sayı: 48.0)
7. % 15.24 (6. pozisyon, sayı: 75.0)
8. % 17.07 (1. pozisyon, sayı: 84.0)
9. % 18.90 (9. pozisyon, sayı: 93.0)

Sadece Aynı İsimle Ortak Kesişim Değerleri
// Here we take the intersections of our array, which is within the percentage of our 8-4-2-5-7-3-6-6-1-9 array.
Birinci → İkinci Yönünde Aynı İsimle Ortak Kesişimler:
- Kesişim: (11.788617886178862, 20.528455284552848), Birinci: 2 (indeks 2, %8.74), İkinci: 2 (indeks 1, %11.11)
- Kesişim: (55.55555555555556, 64.02439024390245), Birinci: 6 (indeks 6, %15.24), İkinci: 6 (indeks 5, %11.11)
- Kesişim: (88.8888888888889, 100.00000000000001), Birinci: 9 (indeks 8, %18.90), İkinci: 9 (indeks 8, %11.11)

İkinci → Birinci Yönünde Aynı İsimle Ortak Kesişimler:
- Kesişim: (11.788617886178862, 20.528455284552848), Birinci: 2 (indeks 1, %11.11), İkinci: 2 (indeks 2, %8.74)
- Kesişim: (55.55555555555556, 64.02439024390245), Birinci: 6 (indeks 5, %11.11), İkinci: 6 (indeks 6, %15.24)
- Kesişim: (88.8888888888889, 100.00000000000001), Birinci: 9 (indeks 8, %11.11), İkinci: 9 (indeks 8, %18.90)

// As a result, the answer here must be one of "2"-"6"-"9".

Please write if you have a question without hesitation; I promise to explain in detail.
Have a nice day!



