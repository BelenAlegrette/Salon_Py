/* API */
const URL = "https://s3-us-west-2.amazonaws.com/s.cdpn.io/735173/rpg-2-data.json";
import { Imagen } from "./Imagen.js";
import { Mostrar } from "./Mostrar.js";




fetch(URL, {})
.then((res) => res.json())
.then((data) => {
        console.log(data)
        let galeria = document.getElementById("galeria")
        
        data.gallery.forEach(item => galeria.innerHTML += 
            `<div class="items"><img  src="${item.src}"/></div>` )
        

        // localStorage.setItem("img", JSON.stringify(data.gallery));
    }
)
    .catch((error) => console.log({error}));

// let mans=JSON.parse(localStorage.getItem("img"));

// mans.forEach(items => {
//     const contenedor = new Mostrar("galeria");
//     let id= items.id;
//     let name = items.name;
//     let desc = items.desc;
//     let src = items.src;
//     const img = new Imagen({ id, name, desc, src });
//     contenedor.render(img.src);

// })