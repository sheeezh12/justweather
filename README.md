# justweather
Aplikasi web berbasis Python Flask yang memungkinkan pengguna untuk melihat prakiraan cuaca harian berdasarkan nama kota. Data lokasi diambil dari Nominatim (OpenStreetMap), dan data cuaca diperoleh melalui API Open-Meteo. Dirancang untuk antarmuka yang sederhana, aman, dan mudah dikembangkan.

Fitur

- Validasi dan geolokasi nama kota menggunakan Nominatim
- Prakiraan cuaca harian (suhu maksimum, minimum, curah hujan, dan kondisi cuaca)
- Pemetaan kode cuaca ke deskripsi yang mudah dipahami
- Responsif dan dapat dijalankan secara lokal menggunakan Flask
- Penanganan kesalahan, API timeout, dan fallback jika kota tidak ditemukan

Teknologi

- Backend: Python 3.11, Flask, requests
- Frontend: HTML, CSS, Jinja2
- API: Open-Meteo Forecast API, Nominatim Geocoding API


Lisensi

Kode sumber dari proyek ini dilisensikan di bawah MIT License. Silakan lihat file LICENSE untuk detail selengkapnya.

Lisensi dan Atribusi Pihak Ketiga

- **Open-Meteo**  
  Data cuaca berasal dari [Open-Meteo](https://open-meteo.com/). Lisensi: Creative Commons Attribution 4.0 (CC BY 4.0).  
  Atribusi disertakan di halaman aplikasi.

- **Nominatim (OpenStreetMap)**  
  Layanan pencarian kota menggunakan [Nominatim](https://nominatim.org/) milik OpenStreetMap. Data dilindungi oleh Open Database License (ODbL).  
  Atribusi disertakan di halaman aplikasi dan mengikuti ketentuan OSM.

- **Bootstrap**  
  Jika digunakan, Bootstrap dirilis di bawah MIT License dan tidak mewajibkan atribusi secara visual. Komponen disertakan untuk pengembangan UI.  

Hak cipta pihak ketiga tetap menjadi milik masing-masing pemilik. Proyek ini menggunakan data pihak ketiga hanya untuk tujuan demonstrasi pribadi/non-komersial.

Pengembang

Aplikasi ini dikembangkan sebagai bagian dari eksplorasi backend, API integration, dan validasi data.  
Tujuan utama: efisiensi, keamanan, dan pengalaman pengguna yang bersih.



