let searchBar = document.querySelector(".searchDrone");
let drone_list = document.querySelector(".drone_list");

searchBar.addEventListener('input', () => {
    drones.getAll({nombre: searchBar.value})
        .then(e => {
            console.log(e.data)

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

    
    drone_list.innerHTML = "";

})
