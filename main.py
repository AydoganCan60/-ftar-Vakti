import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import json
import os
import pygame
import tkinter as tk
import threading

URL = 'https://www.sabah.com.tr/istanbul-namaz-vakitleri'
DATA_FILE = "vakitler.json"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EZAN_SESI = os.path.join(BASE_DIR, "Ezan.wav")

# Pygame ses motorunu başlat
pygame.mixer.init()

def fetch_namaz_times():
    try:
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')
        vakitler_div = soup.find('div', class_='vakitler boxShadowSet')
        if vakitler_div:
            vakitler = vakitler_div.find_all('span')
            imsak = vakitler[0].text.strip()
            aksam = vakitler[4].text.strip()
            with open(DATA_FILE, "w") as f:
                json.dump({"imsak": imsak, "aksam": aksam, "tarih": datetime.now().strftime("%Y-%m-%d")}, f)
            return imsak, aksam
    except Exception as e:
        print(f"Hata: {e}")
    return None, None

def load_namaz_times():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            if data.get("tarih") == datetime.now().strftime("%Y-%m-%d"):
                return data["imsak"], data["aksam"]
    return fetch_namaz_times()

def ezan_bildirimi():
    """Ezan sesini çalar (thread içinde çalıştırılır)."""
    if not os.path.exists(EZAN_SESI):
        print("Ezan ses dosyası bulunamadı!")
        return

    try:
        print("🔊 Ezan sesi çalıyor...")
        
        # Pygame ses çalma
        pygame.mixer.music.load(EZAN_SESI)
        pygame.mixer.music.play()

        # Ezan bitene kadar bekle
        while pygame.mixer.music.get_busy():
            continue

    except Exception as e:
        print(f"Pygame ile çalma hatası: {e}, playsound kullanılıyor...")
        try:
            from playsound import playsound
            playsound(EZAN_SESI)
        except Exception as e:
            print(f"Playsound ile de hata oluştu: {e}")

def ezan_calistir():
    """Ezanı farklı bir thread içinde çalıştırarak GUI'nin donmasını önler."""
    threading.Thread(target=ezan_bildirimi, daemon=True).start()

def update_gui():
    global imsak, aksam
    simdi = datetime.now()
    
    imsak_saat = datetime.strptime(imsak, "%H:%M").time()
    aksam_saat = datetime.strptime(aksam, "%H:%M").time()
    
    aksam_vakti = datetime.combine(simdi.date(), aksam_saat)
    imsak_vakti = datetime.combine(simdi.date(), imsak_saat)

    # Eğer vakit geçmişse, bir sonraki gün için hesapla
    if simdi > aksam_vakti:
        aksam_vakti += timedelta(days=1)
    if simdi > imsak_vakti:
        imsak_vakti += timedelta(days=1)

    kalan_sure_aksam = aksam_vakti - simdi
    kalan_sure_imsak = imsak_vakti - simdi

    # Ezan çalma kontrolü (10 saniye içinde çalsın)
    if 0 <= (aksam_vakti - simdi).total_seconds() <= 10:
        ezan_calistir()

    if 0 <= (imsak_vakti - simdi).total_seconds() <= 10:
        ezan_calistir()

    iftar_label.config(text=f"İftara kalan süre: {kalan_sure_aksam.seconds // 3600} saat {kalan_sure_aksam.seconds % 3600 // 60} dakika {kalan_sure_aksam.seconds % 60} saniye")
    sahur_label.config(text=f"Sahura kalan süre: {kalan_sure_imsak.seconds // 3600} saat {kalan_sure_imsak.seconds % 3600 // 60} dakika {kalan_sure_imsak.seconds % 60} saniye")

    root.after(1000, update_gui)

imsak, aksam = load_namaz_times()
root = tk.Tk()
root.title("İftar & Sahur Sayacı")
root.geometry("350x150")

iftar_label = tk.Label(root, text="İftara kalan süre: Hesaplanıyor", font=("Arial", 12))
iftar_label.pack(pady=10)
sahur_label = tk.Label(root, text="Sahura kalan süre: Hesaplanıyor", font=("Arial", 12))
sahur_label.pack(pady=10)

update_gui()
root.mainloop()
