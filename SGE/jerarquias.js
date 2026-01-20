//1.traernos la lista
//2. traer el valor de la caja de texto
//3.Vamor vcrear un elemento vacio de tipo lista
//4.vamor rellenar con los valores indicados (el texto que viene de la caja)
//5. Aññadir la lista el elemento creado




// let lista = document.getElementById('lista')
// let caja = document.getElementById('mes')
// let cajaP = document.getElementById('parrofo')
 let cajaG = document.getElementById('enlace')


// document.getElementById('boton').addEventListener('click',addElement)
// document.getElementById('botonP').addEventListener('click',addElementP)
document.getElementById('botonG').addEventListener('click',addLink)

// function addElement()
// {
//    // alert("el boton funciona")

//    //Crea un elemento y necesita el tagname que es la etiqueta del html
//    let nuevItem = document.createElement('li')
//    nuevItem.textContent = caja.value
//    lista.appendChild(nuevItem)
//    caja.value=''






// }
// function addElement()
// {
//    // alert("el boton funciona")

//    //Crea un elemento y necesita el tagname que es la etiqueta del html
//    let nuevItem = document.createElement('p')
//    nuevItem.textContent = caja.value
//    document.body.appendChild(nuevItem)
//    cajaP.value=''
// }

function addLink()
{
  let texto = cajaG.value
  let enlace = document.createElement('a')


  enlace.href = texto
  enlace.target = '_blank'
  enlace.textContent=texto

  document.body.appendChild(enlace)
}


let cajita = document.getElementById('imagen')
document.getElementById('botonI').addEventListener('click',addImgaen)

function addImgaen()
{
  
    let texto = cajita.value

    let imagen = document.createElement('img')


    imagen.src = texto
    
    document.body.appendChild(imagen)

}


