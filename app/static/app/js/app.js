function init (){
    let array = [];

    const lat=24.14437;
    const lon=-110.3005;
    const map = L.map('map').setView([lat, lon], 13);

    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
    map.on("click", function (e){
        const {latlng: {
            lat,lng
        }} = e;
        console.log(lat, lng);
        L.marker([lat, lng]).addTo(map).bindPopup("Esto es una marca")

    });

    axios.defaults.withCredentials = true;
    axios.defaults.baseURL = "http://127.0.0.1:8000/api/";
}

window.addEventListener('load', init);