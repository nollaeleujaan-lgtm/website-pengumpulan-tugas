# ====================================
# PROGRAM PERULANGAN PYTHON
# ====================================

# 1. PERULANGAN FOR
print("=== PERULANGAN FOR ===")

for i in range(1, 6):
    print("Perulangan ke-", i)


# 2. PERULANGAN WHILE
print("\n=== PERULANGAN WHILE ===")

i = 1

while i <= 5:
    print("Perulangan ke-", i)
    i += 1


# 3. PERULANGAN DO-WHILE
print("\n=== PERULANGAN DO-WHILE ===")

i = 1

while True:
    print("Perulangan ke-", i)
    i += 1

    if i > 5:
        break


# 4. PERULANGAN BERSARANG (NESTED LOOP)
print("\n=== PERULANGAN BERSARANG (NESTED LOOP) ===")

for baris in range(1, 6):
    for kolom in range(1, 6):
        print("*", end=" ")

    print()