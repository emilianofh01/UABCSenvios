function distance(t, e) {
    var i = Math.PI / 180
      , n = t[0] * i
      , o = e[0] * i
      , s = Math.sin((e[0] - t[0]) * i / 2)
      , e = Math.sin((e[1] - t[1]) * i / 2)
      , t = s * s + Math.cos(n) * Math.cos(o) * e * e
      , i = 2 * Math.atan2(Math.sqrt(t), Math.sqrt(1 - t));
    return 6371e3 * i
}
function distanceKM(t, e) {
    var i = Math.PI / 180
      , n = t[0] * i
      , o = e[0] * i
      , s = Math.sin((e[0] - t[0]) * i / 2)
      , e = Math.sin((e[1] - t[1]) * i / 2)
      , t = s * s + Math.cos(n) * Math.cos(o) * e * e
      , i = 2 * Math.atan2(Math.sqrt(t), Math.sqrt(1 - t));
    return 6371 * i
}

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
            filter = remapKeys(filter, {
                nombre: "nombre__icontains",
                inventario_menor: "inventario__lt",
                peso_maximo_menor: "peso_maximo__lt",
                velocidad_menor: "velocidad__lt",
                inventario_mayor: "inventario__gt",
                peso_maximo_mayor: "peso_maximo__gt",
                velocidad_mayor: "velocidad__gt",
                peso_maximo_mayor_igual: "peso_maximo__gte",
                velocidad_mayor_igual: "velocidad__gte",
                peso_maximo_menor_igual: "peso_maximo__lte",
                velocidad_menor_igual: "velocidad__lte",
            }, true);
            return axios.get("dron/" + window.toQueryParams(filter))
        },
        get(id) {
            return axios.get(`dron/${id}/`);
        }
    };

    drones.getAll({nombre: searchBar.value})
        .then(e => {
            console.log(e.data)
            drone_list.innerHTML = "";
            e.data.forEach(element => {
                drone_list.innerHTML += `
                <div class="dron">
                    <div>
                        <img src="${window.BaseimgDrones + element.icono}" alt="">
                        <div>
                            <h1>${element.nombre}</h1>
                            <p>${element.desc}</p>
                        </div>
                    </div>
                    <div>
                        <p>$${element.precio}MXN</p>
                    </div>
                </div>
                `;
            });
        })
    window.envios = {
        getAll(filter = {}){
            filter = remapKeys(filter, {
            }, true);
            return axios.get("envio/" + window.toQueryParams(filter))
        },
    }

}

function updatePrices(km) {
    
}

window.addEventListener('load', init);