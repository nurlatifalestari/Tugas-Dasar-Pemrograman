#Operator
#Operator Aritmatika
print("\n--- LATIHAN OPERATOR ARITMATIKA ---")
a = 5
b = 3
penjumlahan = a + b
print(f"Hasil Penjumlahan {a} + {b} = {penjumlahan}")
a = 7
b = 3
pengurangan = a - b
print(f"Hasil pengurangan {a} - {b} = {pengurangan}")
a = 45
b = 10
sisabagi = a % b
print(f"Hasil sisa bagi {a} % {b} = {sisabagi}")
a = 80
b = 36
pembagian = a // b
print(f"Hasil pembagian {a} // {b} = {pembagian}")
a = 24
b = 13
perkalian = a * b
print(f"hasil perkalian {a} * {b} = {perkalian}")
a = 5
b = 3
perpangkatan = a ** b
print(f"Hasil perpangkatan {a} ** {b} = {perpangkatan}")
a = 15
b = 2
pembagian_desimal = a / b
print(f"Hasil pembagian desimal {a} / {b} = {pembagian_desimal}")

#Operator Assignment
print("\n--- LATIHAN OPERATOR ASSIGNMENT ---")
c = 10
print(f"Nilai c = {c}")
c += 5  # c = c + 5
print(f"Nilai c setelah c += 5: {c}")
c -= 3  # c = c - 3
print(f"Nilai c setelah c -= 3: {c}")
c *= 2  # c = c * 2
print(f"Nilai c setelah c *= 2: {c}")
c /= 4  # c = c / 4
print(f"Nilai c setelah c /= 4: {c}")

#Operator Perbandingan
print("\n--- LATIHAN OPERATOR PERBANDINGAN ---")
x = 10
y = 5
# 1. Sama dengan (==)
print(f"Apakah {x} == {y} ? {x == y}")
# 2. Tidak sama dengan (!=)
print(f"Apakah {x} != {y} ? {x != y}")
# 3. Lebih besar dari (>)
print(f"Apakah {x} > {y} ? {x > y}")
# 4. Lebih kecil dari (<)
print(f"Apakah {x} < {y} ? {x < y}")
# 5. Lebih besar atau sama dengan (>=)
print(f"Apakah {x} >= {y} ? {x >= y}")
# 6. Lebih kecil atau sama dengan (<=)
print(f"Apakah {x} <= {y} ? {x <= y}")
x = 10
y = 10
print(f"Apakah {x} == {y} ? {x == y}")


#Operator Logika 
print("\n--- LATIHAN OPERATOR LOGIKA ---")
opAnd = a >= b and x <= y and x != y #false
opOr = a >= b or x <= y or x != y #true
opNot = a >= b and not (x <= y) and not (x != y) #false
print(f"Hasil dari {a} >= {b} and {x} <= {y} and {x} != {y} adalah {opAnd}")
print(f"Hasil dari {a} >= {b} or {x} <= {y} or {x} != {y} adalah {opOr}")
print(f"Hasil dari not ({a} >= {b} and {x} <= {y} and {x} != {y}) adalah {opNot}")