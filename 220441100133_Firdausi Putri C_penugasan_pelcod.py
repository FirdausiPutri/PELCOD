print("Nama : Firdausi Putri Cahyani")
print("NIM : 220441100133")
print("Menghitung Konversi Suhu")
indeks = {
    "Celcius    ": "c",
    "Kelvin     ": "k",
    "Reamur     ": "r",
    "Fahrenhait ": "f"
}
print("======Indeks Satuan Skala Suhu======")
for i in indeks:
    print("Satuan suhu :", i,"\t Indeks :", indeks[i])
    
suhu = float(input("masukkan suhu :"))
satuan = input("masukkan indeks satuan skala :")

if (satuan == "c"):
    print(suhu, "derajat celcius :" )
    print("Reamur =", (suhu*4/5), "derajat")
    print("Fahrenhait =", (suhu*9/5)+32, "derajat")
    print("Kelvin =", suhu + 273, "derajat")
elif (satuan == "r"):
    print(suhu, "derajat celcius :" )
    print("Celcius =", (suhu*5/4), "derajat")
    print("Fahrenhait =", (suhu*9/4)+32, "derajat")
    print("Kelvin =", (suhu*5/4) + 273, "derajat")
elif (satuan == "f"):
    print(suhu, "derajat celcius :" )
    print("Reamur =", (4/9)*(suhu-32), "derajat")
    print("Celcius =", (5/9)*(suhu-32), "derajat")
    print("Kelvin =", (5/9)*(suhu-32) + 273, "derajat")
elif (satuan == "k"):
    print(suhu, "derajat celcius :" )
    print("Reamur =", (4/5)*(suhu-273), "derajat")
    print("Fahrenhait =", (9/5)*(suhu-273+32), "derajat")
    print("Celcius =", suhu-273, "derajat")