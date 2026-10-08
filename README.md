# Log Parser - Yazılım Laboratuvarı 1. Hafta

Bu proje, yazılım laboratuvarı dersinin ilk haftası için geliştirilmiş bir Python log ayrıştırma (parsing) programıdır. Sistem loglarını (`auth.log`) okuyarak içerisindeki verileri anlamlı bir yapıya dönüştürür ve çeşitli istatistikler çıkarır.

## 🚀 Özellikler
Program temel olarak şu işlemleri gerçekleştirmektedir:
- `auth.log` dosyasını satır satır okur (boş satırları atlar).
- Her log satırını ayrıştırarak anahtar-değer (key-value) çiftlerinden oluşan bir Python sözlüğüne (`dict`) dönüştürür.
- Loglardaki `SUCCESS` ve `FAILED` durumlarının toplam sayısını hesaplar.
- `FAILED` durumundaki kayıtların kaynak IP (`src_ip`) adreslerini sayar.
- En fazla başarısız giriş denemesi gerçekleştiren IP adresini tespit eder.

## 📂 Klasör Yapısı
Projenin sorunsuz çalışması için `auth.log` dosyasının doğru dizinde olması gerekmektedir. Dosya yapısı aşağıdaki gibi olmalıdır:

```text
proje_klasoru/
│
├── datasets/
│   └── auth.log           # Analiz edilecek log dosyası
│
├── src/
│   └── log_parser.py      # Ana Python kodumuz
│
└── README.md
```
## 🛠️ Kullanım
Projeyi çalıştırmak için bilgisayarınızda Python 3.x kurulu olmalıdır. Ekstra bir kütüphane yüklemenize gerek yoktur.
Terminal veya komut satırından ana proje klasörüne gidin ve aşağıdaki komutu çalıştırın:
```Bash
python src/log_parser.py
```
## 📊 Örnek Çıktı  
```text
Script başarıyla çalıştığında konsolda aşağıdaki gibi bir çıktı üretir:
Plaintext
Status counts: {'SUCCESS': 25, 'FAILED': 12}
Top failed IP: ('192.168.1.25', 6)
```
Bu dosyayı projene ekledikten sonra, GitHub'a göndermek için terminalde sırayla şu komutları kullanabilirsin:
1. `git add README.md`
2. `git commit -m "README dosyası eklendi"`
3. `git push` 


