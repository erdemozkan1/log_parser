from pathlib import Path # Farklı işletim sistemlerinde Python Klasörlerin doğru çalışması için Path kullanıyoruz

LOG = Path(__file__).parents[1] / "datasets" / "auth.log"
"""
LOG adında bir değişken tanımlıyoruz
(__file__) şu an üzerinde çalışmış olduğumuz .py dosyasını temsil eder
.parents[1] 1 üst klasöre çık demek
/"datasets" klasörüne gir ordan da / "auth.log" dosyasına  
"""


def parse_line(line: str) -> dict:
    # Satırın başındaki ve sonundaki boşlukları temizleyip boşluklara göre böleriz.
    parts = line.strip().split()

    # Satır boşsa boş sözlük döndür.
    if not parts:
        return {}

    # İlk parça her zaman timestamp (zaman damgası) alanıdır.
    parsed_data = {"timestamp": parts[0]}

    # Kalan parçalar "anahtar=değer" (key=value) formatındadır, bunları sözlüğe ekleriz.
    for part in parts[1:]:
        if "=" in part:
            # Sadece ilk eşittir işaretinden böleriz (değer içinde '=' olma ihtimaline karşı).
            key, value = part.split("=", 1)
            parsed_data[key] = value

    return parsed_data


def main():
    # Sayım işlemleri için sayaç değişkenleri
    status_counts = {"SUCCESS": 0, "FAILED": 0}
    failed_ips = {}

    try:
        with open(LOG, "r", encoding="utf-8") as file:
            for line in file:
                # Boş satırları atlarız.
                if not line.strip():
                    continue

                # Her satırı parse_line fonksiyonu ile ayrıştırırız.
                log_data = parse_line(line)

                status = log_data.get("status")
                src_ip = log_data.get("src_ip")

                # Duruma göre sayıları güncelleriz.
                if status in status_counts:
                    status_counts[status] += 1

                # Durum FAILED ise kaynağı (IP) failed_ips sözlüğünde sayarız.
                if status == "FAILED" and src_ip:
                    failed_ips[src_ip] = failed_ips.get(src_ip, 0) + 1

    except FileNotFoundError:
        print(f"Hata: Log dosyası bulunamadı, yol kontrol edilmeli: {LOG}")
        return

    # 1. SUCCESS ve FAILED sayılarını ekrana yazdır.
    print(f"Status counts: {{'SUCCESS': {status_counts['SUCCESS']}, 'FAILED': {status_counts['FAILED']}}}")

    # 2. En fazla başarısız denemesi olan IP'yi bul ve yazdır.
    if failed_ips:
        # failed_ips sözlüğündeki en yüksek değere (value) sahip anahtarı (key) bulur.
        top_ip = max(failed_ips, key=failed_ips.get)
        print(f"Top failed IP: ('{top_ip}', {failed_ips[top_ip]})")
    else:
        print("Top failed IP: Bulunamadı (FAILED kaydı yok)")


if __name__ == "__main__":
    main()