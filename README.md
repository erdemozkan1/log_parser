# Yazılım Laboratuvarı 

Bu Repo Yazılım Laboratuvarı için özel olarak oluşturulmuştur.

## 🚀Repo Özellikler
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
├── homework1/
│   └── datasets/           # Analiz edilecek log dosyası
│.  └── src/
│       └── log_parser.py
│       └── version_controller.py
├── homework2/
│   └── events.jsonl      # Ana Python kodumuz
│.  └── week03_regex_json.py
│.  └── readme.md
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


