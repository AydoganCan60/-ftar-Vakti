# 🕌 İftar & Sahur Sayacı

Bu Python uygulaması, İstanbul için iftar (akşam ezanı) ve sahur (imsak) vakitlerini otomatik olarak çekerek geri sayım yapar. Vakit geldiğinde ezan sesi çalar.  

## 🚀 Özellikler
- İstanbul için günlük iftar ve sahur saatlerini otomatik çeker.  
- Geri sayım yaparak kalan süreyi gösterir.  
- Vakit geldiğinde ezan sesi çalar.  
- Tkinter GUI ile basit ve kullanıcı dostu arayüz.  

## 🛠 Gereksinimler
Bu proje **Python 3.8+** ile çalışmaktadır. Gerekli bağımlılıkları yüklemek için aşağıdaki adımları takip edin.

## 📥 Kurulum

### 1️⃣ Gerekli bağımlılıkları yükleyin
Öncelikle, bağımlılıkları yüklemek için şu komutu çalıştırın:  

```sh
pip install -r requirements.txt
```
### 2️⃣ Projeyi Çalıştırın
Daha sonra, bağımlılıkları yükledikten sonra bu komutu çalıştırın:  
```
python main.py
```
Uygulama, https://www.sabah.com.tr/istanbul-namaz-vakitleri adresinden iftar ve sahur vakitlerini çeker.
Eğer ses çalmıyorsa, Ezan.wav dosyasının proje dizininde olduğundan emin olun.
Windows kullanıcıları için pygame ve playsound kütüphaneleri arasında otomatik geçiş yapılmaktadır.
