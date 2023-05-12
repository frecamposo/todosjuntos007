class Persona{
    //atributos
    nombre;
    run;
    fecha_naci;
    telefono;
    correo;
    //mutadores
    setNombre(nombre){
        this.nombre=nombre;
    }
    setRun(run){
        this.run=run;
    }
    //accesadores
    getNombre(){
        return this.nombre;
    }
    getRun(){
        return this.run;
    }
    imprimir(){
        return "Nombre:"+this.getNombre()+" Run:"+this.getRun();
    }
}