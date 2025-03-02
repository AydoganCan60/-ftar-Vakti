🕌 İftar & Sahur Sayacı

Bu Python uygulaması, İstanbul için iftar (akşam ezanı) ve sahur (imsak) vakitlerini otomatik olarak çekerek geri sayım yapar. Vakit geldiğinde ezan sesi çalar.

🚀 Özellikler

✅ İstanbul için günlük iftar ve sahur saatlerini otomatik çeker.✅ Geri sayım yaparak kalan süreyi gösterir.✅ Vakit geldiğinde ezan sesi çalar.✅ Tkinter GUI ile basit ve kullanıcı dostu bir arayüz sunar.

🛠 Gereksinimler

Python 3.8+

Bir adet Ezan.wav dosyası, main.py ile aynı klasörde bulunmalıdır. Aksi halde ezan sesi çalmaz.

📥 Kurulum

1️⃣ Gerekli bağımlılıkları yükleyin

Öncelikle bağımlılıkları yüklemek için şu komutu çalıştırın:
```
pip install -r req.txt  
```
2️⃣ Uygulamayı Çalıştırın

Bağımlılıkları yükledikten sonra uygulamayı başlatmak için:
```
python main.py  
```
🖥️ Ekran Görüntüsü

![resim](https://github.com/user-attachments/assets/706c0c80-d69b-4f2a-9c46-efc4ebea2056)


🔔 Önemli Notlar

Uygulama, Sabah Namaz Vakitleri sitesinden iftar ve sahur saatlerini çeker.

Eğer ezan sesi çalmıyorsa, Ezan.wav dosyasının proje klasöründe olduğundan emin olun.

Windows kullanıcıları için pygame ve playsound kütüphaneleri arasında otomatik geçiş yapılmaktadır.
