document.getElementById("startButton").addEventListener("click", function () {
  fetch("http://<RaspberryPi-IP>:5000/start-video")
    .then((response) => response.text())
    .then((data) => console.log(data));
});

document.getElementById("stopButton").addEventListener("click", function () {
  fetch("http://<RaspberryPi-IP>:5000/stop-video")
    .then((response) => response.text())
    .then((data) => console.log(data));
});
