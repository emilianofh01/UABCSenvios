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

    window.toQueryParams = (obj) => {
        return Object.keys(obj).length > 0 ? '?' + Object.keys(obj).map(key => `${key}=${encodeURI(obj[key])}`).join('&') : '';
    };

    remapKeys = window.remapKeys = (obj, keyMap, only = false) =>{
        const r = only ? {} : obj;
        Object.entries(keyMap).forEach(e => {
            if(obj[e[0]]){
                r[e[1]] = obj[e[0]];
                delete obj[e[0]];
            }
        })
        return r;
    }

    window.drones = {
        getAll(filter = {}){
            filter = remapKeys(filter, {nombre: "nombre__icontains"}, true);
            return axios.get("dron/" + window.toQueryParams(filter))
        }
    };



}

window.addEventListener('load', init);