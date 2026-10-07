import json, re
from pathlib import Path
import csv


DATA = Path(__file__).parent / "events.jsonl"
OUTPUT_CSV = Path(__file__).parent / "failed_events.csv"

IP_RE = re.compile(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

def main():
    total_events = 0
    failed_events_list = []
    try:
        with open(DATA, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line: #Boş satırları atlıyoruz.
                    continue
                try:
                    event = json.loads(line)
                except json.JSONDecodeError:

                    # "THIS IS NOT JSON" satırlarını atlıyoruz.
                    print("Geçersiz Json satırı atlandı.")
                    continue
                total_events += 1

                if event.get("status") == "FAILED":
                    src_ip = event.get("src_ip","")

                    if IP_RE.match(src_ip):
                        failed_events_list.append(event)
    except FileNotFoundError:
        print(f"Hata: Veri dosyası bulunamadı: {DATA}")
        return
    print(f"Total events: {total_events}")
    print(f"Failed events: {len(failed_events_list)}")

    if failed_events_list:
        headers = ["timestamp","event_id","src_ip","user","status"]
        with open(OUTPUT_CSV, "w", newline="",encoding="utf-8")as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=headers,extrasaction='ignore')
            writer.writeheader()
            writer.writerows(failed_events_list)
        print(f"CSV oluşturuldu: {OUTPUT_CSV.name}")
if __name__ == "__main__":
    main()
















