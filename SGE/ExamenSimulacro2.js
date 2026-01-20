/*
1.Traernos las cajitas de los input
2.Traenos los radiobutton
3.Traenos los radiobutton
4.Traenos el boton
*/

function Añadir() {

    let nombre = document.getElementById('nombre').value.trim();
    let apellido = document.getElementById('Apellido').value.trim();
    let email = document.getElementById('Email').value.trim();
    let edad = parseInt(document.getElementById('Edad').value);
    let aficiones = document.getElementById('Aficiones').value.trim();

    // Radios
   
    let relacionPersonal = document.querySelector('input[name="RelacionPersonal"]:checked');

    // Validar que no haya campos vacíos
    if (!nombre || !apellido || !email || !edad) {
        alert("Faltan campos por rellenar");
        return;
    }

    // Validar edad
    if (!(edad >= 16 && edad <= 99)) {
        alert("Tiene edad no comprendida entre 16-99");
        return;
    }

    // Validar email
    if (!email.includes("@") || !email.includes(".")) {
        alert("El email no tiene el formato adecuado");
        return;
    }

    // Si no hay aficiones
    if (aficiones === "") {
        let relacionLaboral = document.querySelector('input[name="Relacionlaboral"]:checked');
        aficiones = "no tiene aficiones :/";
    }

    // Conseguir texto de la relación
    let relacion = "";
    if (relacionLaboral) relacion = relacionLaboral.value;
    else if (relacionPersonal) relacion = relacionPersonal.value;

    // Crear texto final
    let texto = `${nombre} ${apellido} con email ${email} de ${edad} años es ${relacionLaboral} y le gusta ${aficiones}`;

    // Añadir a la lista
    let li = document.createElement("li");
    li.textContent = texto;
    document.getElementById('textoGuapo').appendChild(li);
}
document.getElementById('BotonAñadir').addEventListener('click', Añadir);
