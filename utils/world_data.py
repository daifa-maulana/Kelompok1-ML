import json
import requests

"""
Module untuk mengelola dan memproses data dunia (world data).
"""

def fetch_world_data(api_url: str, timeout: int = 10) -> dict:
    """
    Mengambil data dunia dari API eksternal.
    """
    try:
        response = requests.get(api_url, timeout=timeout)
        response.raise_for_status()  # Memicu error jika status code bukan 200
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error saat mengambil data dari API: {e}")
        return {}


def process_country_data(raw_data: dict, country_code: str) -> dict:
    """
    Memfilter dan membersihkan data spesifik untuk negara tertentu.
    """
    # Mengantisipasi jika raw_data kosong atau bukan dictionary
    if not raw_data or not isinstance(raw_data, dict):
        return {}
    
    # Contoh logika filter: mencari data berdasarkan key kode negara
    # Lu bisa sesuaikan struktur key-nya dengan format response API kelompok lu nanti
    country_data = raw_data.get(country_code, {})
    if not country_data:
        # Jika data bertingkat di dalam list (alternatif struktur API umum)
        data_list = raw_data.get("data", [])
        for item in data_list:
            if item.get("country_code") == country_code or item.get("code") == country_code:
                return item
                
    return country_data


def save_to_json(data: dict, file_path: str) -> bool:
    """
    Menyimpan data yang sudah diproses ke dalam file JSON lokal.
    """
    if not data:
        print("Data kosong, batal menyimpan ke file.")
        return False
        
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Data berhasil disimpan ke {file_path}")
        return True
    except IOError as e:
        print(f"Gagal menulis file ke {file_path}: {e}")
        return False