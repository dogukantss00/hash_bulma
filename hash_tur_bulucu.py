import subprocess
import threading
import time
import signal
import os
from tkinter import *

def crack():
    def worker():
        hash1 = ent1.get()
        try:
            # hash-identifier komutunu başlat
            process = subprocess.Popen(["hash-identifier", hash1], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            
            # İşlemi 3 saniye beklet
            time.sleep(1)
            
            # İşlemi sonlandır
            os.kill(process.pid, signal.SIGINT)
            
            # İşlem tamamlandığında çıktıları al
            stdout, stderr = process.communicate(timeout=1)
            
            # Çıktıları işle
            output = stdout.decode('utf-8') if stdout else ""
            errors = stderr.decode('utf-8') if stderr else ""

            # Satırları böl
            satirlar = output.splitlines()

            secili_satir = None

            # 'Possible Hashs:' ile başlayan satırı bul ve bir sonraki satırı al
            for i in range(len(satirlar) - 1):
                if satirlar[i].startswith('Possible Hashs:'):
                    secili_satir = satirlar[i + 1]
                    break

            if secili_satir:
                print("Sonraki satır:", secili_satir.strip())
                lab3.config(text="Hash türünüz:")
                lab2.config(text=secili_satir.strip())
            else:
                lab3.config(text="Hash türü bulunamadı")
                lab2.config(text="")

        except subprocess.TimeoutExpired:
            print("İşlem zaman aşımına uğradı.")
        except Exception as e:
            print("Bir hata oluştu:", e)

    threading.Thread(target=worker).start()

# Create the main window
pencere1 = Tk()
pencere1.title("Hash Öğrenme")
pencere1.geometry("700x400+500+100")

# Create and pack the widgets
label1 = Label(pencere1, text="Hash giriniz")
label1.pack()

ent1 = Entry(pencere1, width=75)
ent1.pack()

buton1 = Button(pencere1, text="ÖĞREN", command=crack)
buton1.pack()

lab3 = Label(pencere1, text="")
lab3.pack()

lab2 = Label(pencere1, text="")
lab2.pack()

# Run the main event loop
pencere1.mainloop()
