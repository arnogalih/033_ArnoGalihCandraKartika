# PROGRAM KONVERSI CELSIUS KE SATUAN FAHRENHEIT

print("\nPROGRAM KONVERSI FAHRENHEIT\n")

celcius = float(input('masukkan suhu dalam celcius : '))
print("suhu adalah",celcius,"celcius")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit,"fahrenheit")

# PROGRAM KONVERSI FAHRENHEIT KE SATUAN CELCIUS

fahrenheit = float(input('masukkan suhu dalam fahrenheit : '))
print("suhu adalah",fahrenheit,"fahrenheit")

celcius = 5/9 * (fahrenheit - 32)
print("suhu dalam celcius adalah",celcius,"celcius")