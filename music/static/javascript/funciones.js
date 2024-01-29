/*const rotated = document.getElementById('logo');
rotated.style.animation.rotated = 'rotate(45deg)';
rotated.style.transform = 'rotate(45deg)';*/
      

    
function burger()
{
  check = document.getElementById('check1').checked;
  if(check == true)
  {
    //alert('true');
    document.getElementById('nav1').style.display = 'table';
  }
  if(check == false)
  {
    //alert('false');
    document.getElementById('nav1').style.display = 'none';
  }
}

function buscador()
{
  if(window.innerWidth < 1001)
  {
    document.getElementById('caja_buscar').style.display = 'none';
    document.getElementById('caja_buscar2').style.display = 'block';
  }
  
}

function validacion() //Funcion para validar datos correctos en el registro
{
  nom= document.getElementById('nombres').value;
  ape= document.getElementById('apellidos').value;
  ed= document.getElementById('edad').value; 
  usu= document.getElementById('usuario').value;
  con= document.getElementById('contraseña').value;
  cel = document.getElementById('celular').value;
  cor = document.getElementById('correo').value;
  reg = document.getElementById('region').selectedIndex;  
  
  if(nom == null || nom.length==0 || /^\s+$/.test(nom))
  { 
    alert('Error.. debe ingresar sus nombres');
    document.datos.nom.focus();
    return false;  
  }
  if(ape == null || ape.length==0 || /^\s+$/.test(ape))
  {
    alert('Error.. debe ingresar sus apellidos');
    document.datos.ape.focus();
    return false;
  }
    
  if(isNaN(ed) || ed.length == 0)
   {
    alert('Error...debe ingresar una edad válida');
    document.datos.ed.focus();
    return false;
  }
  if(usu == null || usu.length==0 || /^\s+$/.test(usu))
  {
    alert('Error.. debe ingresar su nombre de usuario');
    document.datos.usu.focus();
    return false;
  }
  if(con == null || con.length==0 || /^\s+$/.test(con))
  {
    alert('Error.. debe ingresar su contraseña');
    document.datos.con.focus();
    return false;
  }
  if(!(/^\d{9}$/.test(cel)) )
  {
    alert('Error...debe ingresar un teléfono válido');
    document.datos.cel.focus();
    return false;
  }    
    
  if(cor == null || cor.length==0 || /^\s+$/.test(cor))
  {
    alert('Error.. debe ingresar su correo electronico');
    document.datos.cor.focus();
    return false;
  }
  if (reg == null || reg == 0)
  {
    alert('Seleccione una region');
    document.datos.opciones.focus();
    return false;
  }
  else
  {
    return true; 
  }
}

function Ingresar()
{
  var usu;
  var con;
  usu = document.getElementById('usuario').value;
  con = document.getElementById('contraseña').value;
  if(usu==null || usu.length==0)
  {
    alert('Debe ingresar su nombre de usuario ');
  }
  if(con==null || con.length==0)
  {
    alert('Debe ingresar su contraseña ');
  }
  else
  {
    alert('Hola '+ usu + ', Bienvenido a Músicos Chile');
  }
}

function Salir()
{
  alert('Usted ha cerrado la sesion');
}
      
function MensajesRecibidos()
{
  var cantidad1=3;  
  var i=0;
  var usuario1='Sebastian_09';
  var mensaje1='Hola soy Sebastian y necesito un guitarrista para mi banda';
  var fecha1='12/06/2020';

  document.write('Cantidad de Mensajes recibidos: ' + cantidad1);
  document.write('<br>');
  document.write('<hr>');

  for (i=1; i<=cantidad1; i++)
  {
    document.write('Mensaje N°: ' + i); 
    document.write('<br>'); 
    document.write('Usuario: ' + usuario1);
    document.write('<br>');
    document.write('Mensaje: ' + mensaje1);
    document.write('<br>');
    document.write('Fecha: '+ fecha1);
    document.write('<hr>');
  }
}

function MensajesEnviados()
{
  var cantidad2=3; 
  var i=1;  
  var contador2=0;
  var usuario2='Juan_33';
  var mensaje2='Hola soy Felipe necesito banda para poder tocar piano, teclado, o guitara';
  var respuesta2='No respondido aun'
  var fecha2='24/07/2020';

  document.write('Cantidad de Mensajes enviados: ' + cantidad2);
  document.write('<br>');
  document.write('<hr>');

  while(i<=cantidad2)
  {
    document.write('Mensaje N°: ' + i); 
    document.write('<br>'); 
    document.write('Usuario: ' + usuario2);
    document.write('<br>');
    document.write('Mensaje: ' + mensaje2);
    document.write('<br>');
    document.write('Respuesta: ' + respuesta2);
    document.write('<br>');
    document.write('Fecha: '+ fecha2);
    document.write('<hr>');
    i++;
  }
}

function cambiar_tema()
{
  alert('true');
}

function mostrar_chat()
{
  if(window.innerWidth < 1001)
  {
    document.getElementById('cajacontactos').style.display = 'none';
    document.getElementById('cajachat').style.display = 'table';

  }
}

function DebeIniciar()
{
  alert("Debe iniciar sesión")
}

function ContactoExistente()
{
  alert("El contacto ya esta en su lista")
}

function AgrandarImagen2()
{
  //document.getElementById("carousel1").style.display = "block"
}

function Volver2()
{
  //document.getElementById("carousel1").style.display = "none"
}

function filtrarTabla()
    {
      var sexo = document.getElementById("sexo").value;
      var edad = document.getElementById("edad").value;
      var carrera = document.getElementById("carrera").value;
      var region = document.getElementById("region").value;
      var comu = document.getElementById("comu").value;
      var disp = document.getElementById("disp").value;
      var inst = document.getElementById("ins").value;
      var estilo = document.getElementById("estilo").value;
      var artista = document.getElementById("artista").value;
      var tabla = document.getElementById("tabla-musicos");
      var filas = tabla.getElementsByTagName("tr");

      for (var i = 1; i < filas.length; i++)
      {
        var celdaSexo = filas[i].getElementsByTagName("td")[1];
        var celdaEdad = filas[i].getElementsByTagName("td")[2];
        var celdaCarrera = filas[i].getElementsByTagName("td")[3];
        var celdaRegion = filas[i].getElementsByTagName("td")[4];
        var celdaComuna = filas[i].getElementsByTagName("td")[5];
        var celdaDisp = filas[i].getElementsByTagName("td")[6];
        var celdaInst = filas[i].getElementsByTagName("td")[7];
        var celdaEstilo = filas[i].getElementsByTagName("td")[8];
        var celdaArtista = filas[i].getElementsByTagName("td")[9];

        var mostrarFila =
          (sexo === "---" || celdaSexo.innerHTML === sexo) &&
          (edad === "" || celdaEdad.innerHTML === edad) &&
          (carrera === "---" || celdaCarrera.innerHTML === carrera) &&
          (region === "---" || celdaRegion.innerHTML === region) &&
          (comu === "---" || celdaComuna.innerHTML === comu)&&
          (disp === "---" || celdaDisp.innerHTML === disp)&&
          (inst === "---" || celdaInst.innerHTML === inst)&&
          (estilo === "---" || celdaEstilo.innerHTML === estilo)&&
          (artista === "" || celdaArtista.innerHTML === artista);
        

        filas[i].style.display = mostrarFila ? "" : "none";
      }

      if(window.innerWidth < 1001)
      {
        document.getElementById('caja_buscar').style.display = 'none';
        document.getElementById('caja_buscar2').style.display = 'block';
      }
    }
             
