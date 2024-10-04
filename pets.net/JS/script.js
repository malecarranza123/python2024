document.addEventListener('DOMContetLoaded', function() {
    const inputBusqueda=document.getElementById('searchInput');//trae el texto del  usuario que agrego en el campo de buscar 
    const botonesVet=document.querySelectorAll('.vet-locations');//selecciona todos los botones que sean de esa clase(.vet-locations) 

    inputBusqueda.addEventListener('input', function(){
        filtroVetLocalidad();
    });

    function filtroVetLocalidad() {
        const texto=inputBusqueda.value.toLowerCase();//convierte todo en minúsculas
        botonesVet.forEach(boton=>{ 
            const localidad=boton.getAtribute('data-localidad').tolowerCase();
            if (localidad.includes(texto)){ 
                boton.style.display='none';
            }else{
                boton.style.display='';
            } //muestra los botones que coinciden con lo que está escribiendo el usuario 
        });
    }
});