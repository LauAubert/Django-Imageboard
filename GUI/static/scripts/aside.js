const aside = document.querySelector('aside')
const overlay = document.querySelector('.overlay')
const categoryItem = document.getElementById('categorias')
const categoryBlock = document.querySelector('.categorias')
const newPostForm = document.querySelector('.add-post')

const botonMenu = document.querySelector('.menu')
const botonNewThread = document.getElementById('new-thread')

let asideHidden = true;
let categoryHidden = true;
let newPostHidden = true;

botonMenu.addEventListener('click',()=>{
/*Click en menú despliega la barra lateral */
    if (asideHidden){
        asideHidden = false;
        aside.classList.remove('hidden');
        overlay.classList.remove('hidden');
    }
    else{
        asideHidden = true;
        aside.classList.add('hidden');
        overlay.classList.add('hidden');
    }
})

overlay.addEventListener('click',()=>{
/*Click en overlay esconde los elementos desplegados */
        asideHidden = true;
        categoryHidden = true;
        newPostHidden = true;
        aside.classList.add('hidden');
        overlay.classList.add('hidden');
        newPostForm.classList.add('hidden');


})

categoryItem.addEventListener('click',()=>{
/*Click en el item category esconde / muestra las categorias */
    if (categoryHidden){
        categoryHidden=!categoryHidden;
        categoryBlock.classList.remove('hidden');
        categoryItem.querySelector('.right-aside').classList.add('fa-rotate-180')
    }
    else{
        categoryHidden=!categoryHidden;
        categoryBlock.classList.add('hidden');
        categoryItem.querySelector('.right-aside').classList.remove('fa-rotate-180')
    }
})

botonNewThread.addEventListener('click',e=>{
/*Click en newThread abre el modal de crear hilo */
    console.log('a')
    if (newPostHidden){
        newPostHidden=!newPostHidden;
        overlay.classList.remove('hidden')
        newPostForm.classList.remove('hidden')
    }
    else{
        newPostHidden=!newPostHidden;
        overlay.classList.add('hidden')
        newPostForm.classList.add('hidden')
    }
})