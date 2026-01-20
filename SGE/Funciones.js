


//1.Acceder al boton
//2.Estar pendiente / escuchar el evento click 
//El evento dispara una funcion
//3. la funcion se ejecuta  
// function saludo()
// {
//   // alert("Estoy saludndo usando el boton") 
//   // console.log(nombre.value)
//    alert(`Hola ${nombre.value}`)
// }



//h2Respuesta.innerHTML = "Esto es una prueba " 

    
    //     let n = document.getElementById('txtNombre').value
    //     switch(n)
    // {
    //     case "lunes":
    //     case "martes":
    //     case "miercoles": 
    //     case "jueves":
    //     case "viernes":
    //     Respuesta.value = "Se trabaja"
    //         break;

    //     case "sabado":
    //     case "domingo":
    //         Respuesta.value="Es domingo se duerme"
    //     break;

    //     default:
    //         console.log("El numero que se ha introducido es invalido y eres invalido")
    // }

const EditorTexto =() =>
{
    

//     //SACAR LA DIRECCION WEB A LA QUE PUNTA EL TERCER ENLACE
//     let enlaces = document.getElementsByTagName('a')
//     let google = document.getElementById('google').value

//     console.log(google)
//     enlaces[2].innerText = google
//     enlaces[2].href = google

//   //console.log(enlaces[2].href)
    if(document.getElementById('texto').value==''){
        //console.log(document.getElementById('Errror').value)
        //alert("El campo de texto a formatear esta vacio")
        document.getElementById('texto').style.bordercolor='red'
    }else 
    {
        document.getElementById("TextoAqui").style=null
        document.getElementById("TextoAqui").textContent=document.getElementById('texto').value
        
    if(document.getElementById("negrita").checked)
        document.getElementById("texto").style.fontWeight = "bold";

    if(document.getElementById("Cursiva").checked)
        document.getElementById("texto").style.fontStyle = "italic";

    if(document.getElementById("Subrallado").checked)
        document.getElementById("texto").style.textDecoration = "underline";


    let color = document.querySelector('input[name="colores"]:checked')
    document.getElementById("TextoAqui").style.color=color.value

    let size  = document.querySelector('input[name="size"]:checked')
    document.getElementById("TextoAqui").style.fontSize=size.value
    }   
}
document.getElementById('btnCambiar').addEventListener('click',EditorTexto)

//let Respuesta = document.getElementById('txtRespuesta')
//let h2Respuesta = document.getElementById('txtRespuesta')


//Crea una funcion que recorra todos los radios y me devuelva el que esta activo


// function Encontrar()
// {
//     let estado = document.getElementByIdName('edad')
//     for( let i;i<estado.length;i++)
//         if(estado[i].checked==true)
//         console.log(estado[i].id)


// }




