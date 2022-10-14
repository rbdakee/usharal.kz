


$(".up").click(function(){
    window.scrollTo(0, 0)
})
const list = ["ru", "kz"]
const langAll = document.querySelectorAll(".langSpan")
let hash = 'ru'
langAll.forEach((lang, index) => {
    lang.addEventListener('click', () => {
        
        if(index == 0){
            langAll[1].classList.remove('chosen')
            hash = 'ru'
        }
        else{
            langAll[0].classList.remove('chosen')
            hash = 'kz'
        }
        lang.classList.add('chosen')
        
        changeLang()
    })
});

const changeLang = () => {
    
    for (let key in langArr) {
        let elemAll = document.querySelectorAll('.lng-' + key);
        elemAll.forEach(elem => {
            if (elem) {
                if(elem.tagName == 'INPUT'){
                    elem.setAttribute("placeholder", langArr[key][hash])
                }
                else
                {
                    elem.innerHTML = langArr[key][hash];
                }
            }
        })

    }
}

