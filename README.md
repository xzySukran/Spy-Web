![---]((https://i.ibb.co.com/qmMSm0T/ca066b6f-2c37-4a70-a366-aadf907359e7.webp](https://i.ibb.co.com/qmMSm0T/ca066b6f-2c37-4a70-a366-aadf907359e7.webp))

## Bahasa indonesia :

# Project Phishing Setup

Proyek ini mencakup skrip `install.sh` untuk mengatur lingkungan Python dan dependensi yang diperlukan untuk menjalankan aplikasi phishing. Selain itu, file `Phising.py` adalah aplikasi Python utama yang akan dijalankan setelah instalasi.

## Langkah Instalasi

1. **Memberikan izin eksekusi pada skrip instalasi**  
   Sebelum menjalankan skrip instalasi, pastikan untuk memberikan izin eksekusi dengan perintah berikut:
   <div>
   <pre><code>chmod +x install.sh</code></pre>
   <button onclick="navigator.clipboard.writeText('chmod +x install.sh')">Copy</button>
   </div>

2. **Menjalankan Skrip Instalasi**  
   Jalankan skrip `install.sh` untuk mengatur lingkungan virtual dan menginstal dependensi yang diperlukan.
   <div>
   <pre><code>./install.sh</code></pre>
   <button onclick="navigator.clipboard.writeText('./install.sh')">Copy</button>
   </div>

3. **Menjalankan Aplikasi Phishing**  
   Setelah instalasi selesai, Anda bisa menjalankan aplikasi dengan:
   <div>
   <pre><code>python3 Phising.py</code></pre>
   <button onclick="navigator.clipboard.writeText('python3 Phising.py')">Copy</button>
   </div>

## Menggunakan Ngrok

1. **Buka Terminal Baru**  
   Di terminal baru, jalankan perintah berikut untuk membuat tunneling melalui Ngrok ke port `4040`:
   <div>
   <pre><code>ngrok http 4040</code></pre>
   <button onclick="navigator.clipboard.writeText('ngrok http 4040')">Copy</button>
   </div>

## Informasi Tambahan

- Aplikasi ini mengandalkan **Flask** dan **requests**, yang akan secara otomatis diinstal oleh `install.sh`.
- Aktifkan lingkungan virtual sebelum menjalankan aplikasi dengan:
  <div>
  <pre><code>source venv/bin/activate</code></pre>
  <button onclick="navigator.clipboard.writeText('source venv/bin/activate')">Copy</button>
  </div>

---

## ENGLISH :

# Project Phishing Setup

This project includes the `install.sh` script to set up the Python environment and required dependencies to run the phishing application. The `Phising.py` file is the main Python application that will be executed after installation.

## Installation Steps

1. **Grant execution permissions to the install script**  
   Before running the install script, make sure to grant execution permissions with the following command:
   <div>
   <pre><code>chmod +x install.sh</code></pre>
   <button onclick="navigator.clipboard.writeText('chmod +x install.sh')">Copy</button>
   </div>

2. **Run the Install Script**  
   Run the `install.sh` script to set up the virtual environment and install the necessary dependencies.
   <div>
   <pre><code>./install.sh</code></pre>
   <button onclick="navigator.clipboard.writeText('./install.sh')">Copy</button>
   </div>

3. **Run the Phishing Application**  
   After the installation is complete, you can run the application with:
   <div>
   <pre><code>python3 Phising.py</code></pre>
   <button onclick="navigator.clipboard.writeText('python3 Phising.py')">Copy</button>
   </div>

## Using Ngrok

1. **Open a New Terminal**  
   In a new terminal, run the following command to create a tunnel through Ngrok to port `4040`:
   <div>
   <pre><code>ngrok http 4040</code></pre>
   <button onclick="navigator.clipboard.writeText('ngrok http 4040')">Copy</button>
   </div>

## Additional Information

- This application depends on **Flask** and **requests**, which will be automatically installed by `install.sh`.
- Activate the virtual environment before running the application with:
  <div>
  <pre><code>source venv/bin/activate</code></pre>
  <button onclick="navigator.clipboard.writeText('source venv/bin/activate')">Copy</button>
  </div>

---
