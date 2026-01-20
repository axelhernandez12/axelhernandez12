

let trabajadores = [
    {
        nombre: "Ana",
        edad: 30,
        puesto: "Desarrolladora",
        experiencia: 5, // en años
        habilidades: [
            "JavaScript",
            "HTML",
            "CSS",
        ],
        enEmpresa: true,
        localizacion: "Madrid"
    },
    {
        nombre: "Luis",
        edad: 25,
        puesto: "Diseñador Gráfico",
        experiencia: 3, // en años
        habilidades: [
            "Photoshop",
            "Illustrator",
            "Figma",
        ],
        enEmpresa: true,
        localizacion: "Barcelona"
    },
    {
        nombre: "Sara",
        edad: 28,
        puesto: "Gerente de Proyectos",
        experiencia: 7, // en años
        habilidades: [
            "Gestión de Proyectos",
            "Comunicación",
            "Liderazgo",
        ],
        enEmpresa: false,
        localizacion: "Valencia"
    },
    {
        nombre: "Javier",
        edad: 35,
        puesto: "Administrador de Sistemas",
        experiencia: 10, // en años
        habilidades: [
            "Linux",
            "Redes",
            "Seguridad Informática",
        ],
        enEmpresa: true,
        localizacion: "Sevilla"
    }
];


/*
Crea una función que imprima en la consola los nombres y 
puestos de todos los trabajadores que están actualmente en la empresa.
*/
/*
for(i =0;i<trabajadores.length;i++)
{
    if(trabajadores[i].enEmpresa==true)
        console.log(`El trabajador: ${trabajadores[i].nombre} trabaja en el puesto :${trabajadores[i].puesto}`)
}
*/

/*
Define una función que calcule y devuelva 
la suma total de la experiencia de todos los trabajadores que están en la empresa.
*/
/*
let contador =0

for(i = 0;i< trabajadores.length;i++)
{
    if(trabajadores[i].enEmpresa==true)
        contador+= trabajadores[i].experiencia
}

console.log("la experiencia es ",contador)
*/

/*
Escribe una función que reciba un nombre de trabajador y devuelva un array con sus habilidades.
*/
/*


nombreTrabajador = prompt("Introduzca el nombre del trabajador").toLowerCase()

for(i =0;i<trabajadores.length;i++)
{
    if(trabajadores[i].nomnbre===nombre)
        console.log(trabajadores[i].nombre)
        console.log(trabajadores[i].habilidades)

}
*/

//Crea una función que reciba un puesto y devuelva un array con los nombres de los trabajadores que ocupan ese puesto.


/*
puesto = prompt("Introduzca el puesto").toLowerCase()
let gente = []

for(i =0;i<trabajadores.length;i++)
{
    if(trabajadores[i].puesto===puesto)
       gente.push(trabajadores[i].nombre)
}

console.log(`El puesto de :${puesto} tiene las personas: ${gente}`)

*/

