import geoip2.database
import concurrent.futures
from tqdm import tqdm

# Configurare globală
MAX_WORKERS = 50  # Număr optim de thread-uri

# Deschide baza de date GeoLite2
reader = geoip2.database.Reader('GeoLite2-Country_20250204/GeoLite2-Country.mmdb')

def get_country(ip):
    """ Verifică dacă IP-ul este din România folosind GeoLite2. """
    try:
        response = reader.country(ip)
        if response.country.iso_code == "RO":
            return ip
    except Exception:
        return None
    return None

def filter_romanian_ips(file_path, output_path):
    """ Citește fișierul cu IP-uri, verifică locația și salvează IP-urile din România. """
    with open(file_path, "r") as file:
        ips = {line.split(":")[0].strip() for line in file if line.strip()}  # Elimină spații și duplicate

    romanian_ips = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(tqdm(executor.map(get_country, ips), total=len(ips), desc="Processing IPs"))
        romanian_ips = [ip for ip in results if ip]

    with open(output_path, "w") as output_file:
        output_file.write("\n".join(romanian_ips))

if __name__ == "__main__":
    file_path = "affected_ips.txt"  # Schimbă cu calea fișierului tău
    output_path = "romanian_ips.txt"  # Calea fișierului de ieșire
    filter_romanian_ips(file_path, output_path)
    print(f"IP-urile din România au fost salvate în {output_path}")
