//alert("Estoy usando un archivo de javaScrtip")

//Tipado dinamico de variables 
//let nombre="Axel"
//let edad = 21

//4 formas de pintar sobre la consola 
//console.log(nombre)
//console.warn("Esto es una advertencia")
//console.error("EROR!!!!!!!!!!!")
//console.table(nombre)

//De esta forma pedimos informacion al usuario
//let sabor =prompt("Cual es tu sabor de helado preferido")
//console.log(sabor)


//Vamos a pedir al usuario un de la semana y ver si es viernes o no


//let numero = prompt("Introduzca el dia de la semana").toLowerCase();

//if(numero =="Viernes")
   // console.log("Es viernes")
//else
  //  console.log("No es viernes :(")



//Le pedimos al usuario su nombre y su edad y lo pintamoos por consola



//let nombre  = prompt("Introduzca su nombre")
//let edad = parseInt (prompt("Introduzca su edad"))
//console.log(`Me llamo ${nombre} y tengo ${edad+5} años `)

//let edad = prompt("Introduzca su edad")

//if(edad<=17)
{
//    console.log("No puede entrar, eres menor el diablo")
}//else if(edad > 18 && edad < 67)
   // console.log("Eres un trabajador")
//else if(edad >=67)
//console.log("Jubilao")

/*
//let numero = prompt("Introduce un numero")

//if(numero%2==0)
{
//    console.log("Es par ")
}
//else
  //  console.log("Es impar")

*/



/*
confirm("estas seguro?")?document.writeln("Has pulsado aceptar") : document.writeln("Has pulsado cancelar")
*/
/*
let dia = parseInt(prompt("Introduzca el numero del dia de la semana "))

switch(dia)
{
    case "lunes":
    case "martes":
    case "miercoles": 
    case "jueves":
    case "viernes":
    console.log("Se trabaja")
        break;

    case "sabado":
    case "domingo":
        console.log("Es domingo se duerme")
    break;

    default:
        console.log("El numero que se ha introducido es invalido y eres invalido")
}

//let nombre 


*/


/*let frutas =["pera","naranja","limon"]
console.table(frutas)
frutas.push("manzana")
console.table(frutas)
//El pop sirve para quitar el ultimo objecto del array
console.log(frutas.pop)
console.log("Sandia")

console.table(frutas)
//Ordenar alfabameticamente el array
console.table(frutas.sort())
*/




/*
if(confirm("Estas seguro?"))
  document.writeln("Ha pulsadp en acpetar ")
else 
  document.writeln("has pulsado en cancelar")
*/


//let muebles = ['silla','mesas','puerta','ventana','Ordenador','televisor']
//console.log(muebles)
//console.log(muebles[2])
/*
//por el final 
muebles.push('papelera')
console.log(muebles)
console.log(muebles.pop())
console.log(muebles)

//Por el principio
muebles.unshift('proyectar')
console.log(muebles)
console.log(muebles.shift())
console.log(muebles)
*/


//muebles.splice(3,2,'altavoz','telefono')
/*let ultimos =muebles.slice(3,5)
console.log(muebles)
console.log(ultimos)
*/

//Recorrer un array
/*for(let valor of Semana)
*/  
//let semana  = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']

/*
for ( i=0 ;i < Semana.length; i ++)  
{ 
  if(dia ===Semana[i])
  {
    bandera=true
    break
  }  
} 
*/
   
//semana.includes(dia)?alert("el dia existe"):alert("el dia no existe")


//Hacemos un programa que primero nos pida un dia que nos inventemos de la semana y luego nos diga el dia que nos sustituiremos por ese dia 

//dia = prompt("Inventate un dia de la semana").toLowerCase()
//console.log(semana.indexOf(dia))
     
/*    
let laborales  = ['lunes','martes','miercoles','jueves','viernes']
let festivos = ['sabado','domingo']

let semana = festivos.concat(laborales)
*/



//Estos son objetos 
const vehiculo = {
  marca :'Peugeot',
  modelo :206,
  enVenta:false,
  consumo : 5.6,
  colores:['rojo','verde','azul']

}


console.log(vehiculo)
console.log(vehiculo['marca'])
console.log(vehiculo.modelo)


//Vamos a pintar el azul




console.log(vehiculo.colores[2])

vehiculo.precio=20000

console.log(vehiculo)

//Esto sirve para elimiar el precio en su totalida
delete vehiculo.precio


//Sacar los todos los colores


for( i =0;i<vehiculo.colores.length;i++)
{
  console.log(vehiculo.colores[i])
}