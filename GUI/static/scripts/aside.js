const aside = document.querySelector('aside')
const overlay = document.querySelector('.overlay')
const categoryItem = document.getElementById('categorias')
const categoryBlock = document.querySelector('.categorias')
let asideHidden = true;
let categoryHidden = true;


document.querySelector('.menu').addEventListener('click',()=>{
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
        asideHidden = true;
        aside.classList.add('hidden');
        overlay.classList.add('hidden');
})

categoryItem.addEventListener('click',()=>{
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
