const archivo = document.getElementById('archivo')
const nombreArchivo = document.getElementById('nombre-archivo')
const botonBorrar = document.querySelector('.borrar-archivo')
const defaultText = 'Seleccione una imagen'
nombreArchivo.innerText = defaultText

const titulo = document.getElementById('titulo')
const categoria = document.getElementById('selector-categoria')
const texto = document.getElementById('texto')


const errorImagen    = document.querySelector('p#error-imagen');
const errorTitulo    = document.querySelector('p#error-titulo');
const errorCategoria = document.querySelector('p#error-categoria');
const errorTexto     = document.querySelector('p#error-texto');

const botonSubir = document.getElementById('submit-post')
archivo.addEventListener('change',e=>{
    nombreArchivo.innerText = archivo.files[0].name
    console.log(archivo.files[0])
})

botonBorrar.addEventListener('click',e=>{
    archivo.value = ''
    nombreArchivo.innerText = defaultText
})

botonSubir.addEventListener('click',e=>{
    e.preventDefault()
    // titulo entre 3 y 60 caracteres
    // categoria válida
    console.log(titulo.value.length)
    console.log(categoria.value)
    console.log(texto.value.length)

    // document.getElementById('form-subir').submit()
    let params = {
        "imagen"    :false,
        "titulo"    :false,
        "categoria" :false,
        "texto"     :false
    }
    // imagen
    if (archivo.value)  {params.imagen = true; }
    else                {params.imagen = false;}
    // titulo
    if (3<titulo.value.length && titulo.value.length<40){params.titulo = true; }
    else                         {params.titulo = false;}
    // categoría
    if (categoria.value){params.categoria = true; }
    else                {params.categoria = false;}
    // texto
    if (texto.value.length>0){params.texto = true; }
    else                     {params.texto = false;}

    // document.getElementById('error-titulo'   ).hidden = params.titulo
    // document.getElementById('error-imagen'   ).hidden = params.imagen
    // document.getElementById('error-categoria').hidden = params.categoria
    // document.getElementById('error-texto'    ).hidden = params.texto
    if(params.imagen)   {errorImagen.classList.add('hidden');}
    else                {errorImagen.classList.remove('hidden');}
    if(params.titulo)   {errorTitulo.classList.add('hidden');}
    else                {errorTitulo.classList.remove('hidden');}
    if(params.categoria){errorCategoria.classList.add('hidden');}
    else                {errorCategoria.classList.remove('hidden');}
    if(params.texto)    {errorTexto.classList.add('hidden');}
    else                {errorTexto.classList.remove('hidden');}

    if (params.imagen && params.titulo && params.categoria && params.texto){
        document.getElementById('form-subir').submit()}


})
