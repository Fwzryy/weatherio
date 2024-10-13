import time

def happy_birthday(name):
    # Pesan Happy Birthday
    messages = [
        "H", "A", "P", "P", "Y", " ", 
        "B", "I", "R", "T", "H", "D", "A", "Y", " ", 
        name, "!"
    ]
    
    # Menampilkan setiap huruf dengan jeda waktu
    for char in messages:
        print(char, end='', flush=True)
        time.sleep(0.2)  # Menunggu 0.2 detik setiap huruf
    print("\n\n🎉🎉🎉 Have a Wonderful Day! 🎉🎉🎉")
    
# Memasukkan nama
name = input("Enter the birthday person's name: ")

# Menjalankan fungsi
happy_birthday(name)