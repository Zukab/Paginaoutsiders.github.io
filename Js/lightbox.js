// const imagenes = document.querySelectorAll('.img-galeria')
// const imagenesLight = document.querySelector('.agregar-imagen')
// const contenedorLight = document.querySelector('.imagen-light')

// imagenes.forEach(imagen =>{
//     imagen.addEventListener('click', ()=>{
//         aparecerimagen( imagen.getAttribute('src'))
       
//     })
// })

// contenedorLight.addEventListener('click', (e)=>{

//     if(e.target !== imagenesLight){
//         contenedorLight.classList.toggle('show')
//         imagenesLight.classList.toggle('showimage')

//     }

// })

// const aparecerimagen=(imagen)=>{
//     imagenesLight.src = imagen;
//     contenedorLight.classList.toggle('show')
//     imagenesLight.classList.toggle('showimage')
// }

/*  send form */
/*
<input type="text" name="Nombre completo" placeholder="Nombre completo">
<input type="text" name="Correo" placeholder="Correo">
<input type="text" name="Telefono" placeholder="Telefono">
*/

async function sendForm(){
    alert('perra')
    var name = document.getElementById('Nombre completo').value;
    var email = document.getElementById('Correo').value;
    var phone = document.getElementById('Telefono').value;
    var message = document.getElementById('Mensaje').value;

    const data = {
        name,
        email,
        phone,
        message,
    }

    alert(name,email,phone,message)
    const response  = await fetch('http://127.0.0.1:8000/api/contact/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
        
    });
    let result = await response.json();
    alert(result)
}