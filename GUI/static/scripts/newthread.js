const archivo = document.getElementById('archivo')
const nombreArchivo = document.getElementById('nombre-archivo')
const botonBorrar = document.querySelector('.borrar-archivo')
const defaultText = 'Seleccione una imagen'
nombreArchivo.innerText = defaultText

const titulo = document.getElementById('titulo')
const categoria = document.getElementById('selector-categoria')
const texto = document.getElementById('texto')

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


})