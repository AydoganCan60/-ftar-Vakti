![resim](https://github.com/user-attachments/assets/813b9d44-4ba2-4b5f-8c43-d7b112d9031b)# 🕌 İftar & Sahur Sayacı

Bu Python uygulaması, İstanbul için iftar (akşam ezanı) ve sahur (imsak) vakitlerini otomatik olarak çekerek geri sayım yapar. Vakit geldiğinde ezan sesi çalar.  

## 🚀 Özellikler
- İstanbul için günlük iftar ve sahur saatlerini otomatik çeker.  
- Geri sayım yaparak kalan süreyi gösterir.  
- Vakit geldiğinde ezan sesi çalar.  
- Tkinter GUI ile basit ve kullanıcı dostu arayüz.  

## 🛠 Gereksinimler
Bu proje **Python 3.8+** ile çalışmaktadır. Gerekli bağımlılıkları yüklemek için aşağıdaki adımları takip edin.
Bir adet Ezan.wav dosyası main.py dosyası neredeyse o klasörün içerisinde bulunmalıdır! Yoksa ezan sesi çalmaz.

## 📥 Kurulum

### 1️⃣ Gerekli bağımlılıkları yükleyin
Öncelikle, bağımlılıkları yüklemek için şu komutu çalıştırın:  

```sh
pip install -r req.txt
```
### 2️⃣ Projeyi Çalıştırın
Daha sonra, bağımlılıkları yükledikten sonra bu komutu çalıştırın:  
```
python main.py
```
![resim](https://github.com/user-attachments/assets/f83fa6d5-8302-48ef-bf8e-9b76a7ae7f00)
İşte! zamanı geldiği zaman ezan sesini çalıcak.
Uygulama, https://www.sabah.com.tr/istanbul-namaz-vakitleri adresinden iftar ve sahur vakitlerini çeker.
Eğer ses çalmıyorsa, Ezan.wav dosyasının proje dizininde olduğundan emin olun.
Windows kullanıcıları için pygame ve playsound kütüphaneleri arasında otomatik geçiş yapılmaktadır.
