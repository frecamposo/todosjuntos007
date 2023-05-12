function validar() {
    var resp;
    resp=validarContraseña();
    if (resp==false) {
        return false;
    }
    resp=validarEdad();
    if (resp==false) {
        return false;
    }
    rep=validarRut();
    if (resp==false) {
        return false;
    }
    return true;
}
function validarContraseña(){
    let pass1=document.getElementById("pwdPass1").value;
    let pass2=document.getElementById("pwdPass2").value;
    if (pass1==pass2) {
        return true;
    } else {
        //Swal.fire('contraseñas incorrectas');
        alert('contraseñas incorrectas');
        return false;
    }    
}
function validarEdad(){
    var fecha=document.getElementById("datFechaNaci").value;
    var fechaSistema=new Date();
    console.log('Fecha Recuperada:'+fecha);
    console.log('Fecha Sistema:'+fechaSistema);

    var ano=fecha.slice(0,4);
    var mes=fecha.slice(5,7);
    var dia=fecha.slice(8,10);

    console.log('Dia:'+dia);
    console.log('Mes:'+mes);
    console.log('Año:'+ano);

    var nuevaFecha=new Date(ano,(mes-1),dia);
    if (nuevaFecha>fechaSistema) {
        alert('todavia no nace');
        return false;        
    }
    //minimo 18 años
    var unDia=1000 * 60 * 60 * 24; // 1 dia
    console.log('Milisegundo de un Dia:'+unDia);
    var diferencia= (fechaSistema.getTime()-nuevaFecha.getTime());
    console.log('Mili Segundos Diferencia:'+diferencia);
    var dias= diferencia / unDia;
    console.log('Dias de Nacido:'+dias);
    var anoos=Math.trunc( dias/365);
    console.log('Años de Edad:'+anoos);
    if (anoos>=18) {
        return true;
    }else{
        alert('es menor de edad');
        return false;
    }
}
function validarRut() {
    var largo=document.getElementById("txtRut").value.trim().length;
    console.log('Largo Rut:'+largo);
    if (largo==0 || largo>10 || largo<10) {
        alert('rut incorrecto, revisar');
        return false;
    }
    var rut=document.getElementById("txtRut").value;
    var num=3;var suma=0;
    for (let index = 0; index < 8; index++) {
        var caracter= rut.slice(index,index+1);        
        suma=suma+(num*caracter);
        num=num-1;
        if (num==1) {
            num=7;
        }        
    }    
    let residuo= suma % 11;
    let dv= 11-residuo;    
    let el_digito;
    if (dv>9) {
        if (dv==10) {
            el_digito='K';
        } else {
            el_digito=0;
        }
    } else {
        el_digito=dv;
    }
    
    let ultimo= rut.slice(9,10);
    if (ultimo==el_digito) {
       return true;
    } else {
        alert('rut incorrecto');        
        return false;
    }

}
