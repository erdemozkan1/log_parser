# Homework 2 - JSON, Regex ve CSV İşlemleri

## Ödevin Amacı
Bu ödevin amacı; Python kullanarak JSONL (JSON Lines) formatındaki veri dosyalarını okumak, bozuk/hatalı verileri `try/except` blokları ile programı çökertmeden yönetmek, düzenli ifadeler (Regex) ile veri doğrulaması yapmak ve işlenen verileri CSV formatında dışa aktarmaktır.

## Kullanılan Veri Seti
Ders kapsamında sağlanan `events.jsonl` veri seti kullanılmıştır. Bu dosya, sistem olaylarını ve kullanıcı giriş denemelerini içeren her satırı ayrı bir JSON objesi olan yapıdadır.

## Programın Ne Yaptığı
1. `events.jsonl` dosyasını satır satır okur ve JSON olarak ayrıştırır.
2. Geçersiz JSON formatına sahip satırları hata verip durmak yerine atlar (`JSONDecodeError` yönetimi).
3. Toplam olay (event) sayısını hesaplar.
4. Sadece `status` değeri `FAILED` olan başarısız olayları filtreler.
5. Filtrelenen olayların `src_ip` değerinin geçerli bir IP adresi formatında (Örn: 192.168.1.1) olup olmadığını Regex ile denetler.
6. Tüm doğrulama adımlarından geçen kayıtları `timestamp, event_id, src_ip, user, status` sütun başlıklarıyla `failed_events.csv` dosyasına kaydeder.

## Programın Nasıl Çalıştırılacağı
Terminal veya komut satırında projenin ana dizininden ya da `homework2` klasörünün içinden aşağıdaki komutu çalıştırarak kodları test edebilirsiniz:
```bash
python week03_regex_json.py