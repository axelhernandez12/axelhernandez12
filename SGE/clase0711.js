document.getElementById('btnCambiar').addEventListener('click',addTodo)


function addTodo()
{
    let cajita = document.getElementById('elemento')
    let radio = document.querySelector('input[name="radios"]:checked')
    let reso = document.querySelector('input[name="resolucion"]:checked')
  
    let texto = cajita.value
   if(radio.value==='imagen')
   {
   
    let imagen = document.createElement('img')
    imagen.src = texto
    document.body.appendChild(imagen)

   }


   if(radio.value==='enlace')
   {
    let enlaceS = document.createElement('a')
    enlaceS.href = texto
    enlaceS.target ='_blank'
    enlaceS.textContent = texto
    document.body.appendChild(enlaceS)

   }
    
   if(radio.value==='textos')
   {
    let nuevoItem = document.createElement('p')
    nuevoItem.textContent = cajita.value
    document.body.appendChild(nuevoItem)

   } 
}