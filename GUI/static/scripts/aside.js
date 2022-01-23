const aside = document.querySelector('aside')
const overlay = document.querySelector('.overlay')
let asideHidden = true;

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