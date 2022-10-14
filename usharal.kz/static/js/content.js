const list = ["ru", "kz"]
let hash = 'ru'
const langAll = document.querySelectorAll(".langSpan")
langAll.forEach((lang, index) => {
    lang.addEventListener('click', () => {
        
        if(index == 0){
            langAll[1].classList.remove('chosen')
            hash = 'ru'
        }
        else{
            hash = 'kz'
            langAll[0].classList.remove('chosen')
        }
        lang.classList.add('chosen')
        
        changeLang()
    })
});
const changeLang = () => {
   
    for (let key in langArr) {
        console.log(key);
        let elemAll = document.querySelectorAll('.lng-' + key);
        elemAll.forEach(elem => {
            if (elem) {
                if(elem.tagName == 'INPUT' || elem.tagName == 'TEXTAREA'){
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
var np = false
const showModal = () => {
    
    $('.shadow').css('display', 'flex')
}
const modal = (str) => {
    
    showModal()
    $('section').css('position', 'fixed')
    document.querySelectorAll('.ul')[0].style.display = 'unset'
    document.querySelectorAll('.ul')[1].style.display = 'none'
    if(str == 'newPost'){
        np = true
    }
    
}
  var listClassOb = {
    'wholeList-btn':'wholeList-content',
    'location-btn':'location-content'
  }
  window.onclick = function(event) {
    if(event.target.matches('.shadow')){
        if (!event.target.matches('.location-btn')) {
            toggleId(listClassOb['location-btn'])
            $('.shadow').css('display', 'none')
            $('section').css('position', 'sticky')
          
          console.log();
          }
          if (!event.target.matches('.wholeList-btn')) {
            toggleId(listClassOb['wholeList-btn'])
          }
          
    }
  }

  const toggleId = (idClass) => {
    var dropdowns = document.getElementsByClassName(idClass);
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
  }
var categories = document.querySelectorAll('.category')
categories.forEach((category, index) => {
    category.addEventListener('click' , () => {
        document.querySelector('.wholeList-btn').innerHTML = categories[index].children[1].innerHTML + ' <i class="fas fa-angle-down arrow"></i>'  
    })
})

window.onload = () => {
    let inputSearch = document.querySelector('.inputModal input')
    
    inputSearch.oninput = function(){
        let value = this.value.trim().toLowerCase()
        let list = document.querySelectorAll('.ul li')
        console.log(list);
        value
            ?list.forEach(elem => {
                elem.innerText.toLowerCase().search(value) == -1
                    ?elem.classList.add('hide')
                    :
                        elem.classList.remove('hide');
                
            })
            : list.forEach(elem => {
                elem.classList.remove('hide')
            })


    }
    
    
}
var liList  =document.querySelectorAll('.ul li')
liList.forEach(each =>{
    each.addEventListener('click', () => {
        outLi(each,true)
    }) 
    each.addEventListener('mouseover', () => {
        outLi(each, false)
    }) 
       
})
const outLi = (each, boolValue) => {
    if(boolValue){
        $('.shadow').css('display', 'none')
        var text = each.innerHTML
        if(text.includes('Казахстанская')){
            text = text[0] + 'KO'
        }
        if(document.querySelectorAll('.ul')[0].style.display == 'unset'){
            if(np){
                document.querySelector('.locationInput input').value = text
                np = false
            }
            else{
                document.querySelector('.location-btn').innerHTML = text
            }
        }
        else{
            document.querySelector('.chooseCategory div').innerHTML = text
        }
        $('section').css('position', 'sticky')
    }
    else{
        var text = each.innerHTML
        document.querySelector('.inputModal input').value = text
    }
    
        
        
}
var allSize = 0;
var allImg = document.querySelectorAll('.subImages img')
var mainImg = document.querySelector('.mainImgDiv img')
var tempImg = mainImg.src
function plusSlides(n, ist){
    allSize += n;
    if(ist){
        if(allSize > allImg.length){
            allSize = 0
            mainImg.src = tempImg
        }
        else{
            mainImg.src = allImg[allSize-1].src
        }
    }
    else{
        if(allSize == -1){
            
            allSize = allImg.length
            mainImg.src = allImg[allSize-1].src
        }
        else{
            if(allSize == 0){
                mainImg.src = tempImg
            }
            else{
                mainImg.src = allImg[allSize-1].src
            }
        }
    }
    console.log(allSize);
    
}
allImg.forEach((element, index) => {
    element.addEventListener('click', () => {
        mainImg.src = allImg[index].src
        allSize = index+1
    })
});
var a = 0
document.addEventListener('keydown', (event) => {
    if(event.key == 'ArrowRight'){
        document.querySelectorAll('.controlBtn')[1].style.backgroundColor = '#f3f3f3'
        document.querySelectorAll('.controlBtn')[1].style.borderRadius = '0'
        plusSlides(1,1)
    }
    else if(event.key == 'ArrowLeft'){
        document.querySelectorAll('.controlBtn')[0].style.backgroundColor = '#f3f3f3'
        document.querySelectorAll('.controlBtn')[0].style.borderRadius = '0'
        plusSlides(-1,0)
    }
  }, false);
  document.addEventListener('keyup', (event) => {
    if(event.key == 'ArrowRight'){
        document.querySelectorAll('.controlBtn')[1].style.backgroundColor = '#fff'
        document.querySelectorAll('.controlBtn')[1].style.borderRadius = '10px'
        
    }
    else if(event.key == 'ArrowLeft'){
        document.querySelectorAll('.controlBtn')[0].style.backgroundColor = '#fff'
        document.querySelectorAll('.controlBtn')[0].style.borderRadius = '10px'
    }
  }, false);