const showMoreButtonMainPage = $(".buttonLine button")
const showMoreButtonFavPage = $(".showMoreFav")
const allAdvert = $(".adverLine")
const favAdvert = $(".mainPart")

var allAdvertHeight = allAdvert.height()
var favAdvertHeight = favAdvert.height()
const allMessageLink = document.querySelectorAll('.messageLink')
const allMessagesType = document.querySelectorAll('.messagesType')
const btnSABall = document.querySelectorAll('.btnSAB')
// const checkboxFunc = () => {
//     var chooseAll = document.getElementById("check")
//     if(chooseAll.checked){
//         $('body input:checkbox').prop('checked', true);
//     }
//     else{
//         $('body input:checkbox').prop('checked', false);
//     }
// }

var itForBut = 2
var  itForButFav = 2
showMoreButtonMainPage.click(function(){
    if(itForBut < ($(".adverLine .contentBox").length)/4){
        itForBut++
        allAdvertHeight += 360
        allAdvert.css('height', allAdvertHeight)
        window.scrollBy(0, 360)
    }
})

$(".up").click(function(){
    window.scrollTo(0, 0)
})
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

const postsCateg = document.querySelectorAll(".allStatusOfPosts span")
const catBlocks = document.querySelectorAll(".findWithThat")
postsCateg.forEach((eachCatrg, index) => {
    eachCatrg.addEventListener('click', () => {
        for(var sm = 0; sm < 3;sm++){
            if(catBlocks[sm].classList.contains("mpc") == false){
                catBlocks[sm].classList.add("mpc")
            }
        }
        catBlocks[index].classList.remove("mpc")
    })
}
    )
    


var forFavBox = 0
function fill(elem){
    elem.classList.toggle("fa-regular")
    elem.classList.toggle("fa")
    
    
}   
// var newPostZone = document.querySelector('.pageForNewPost .mainBody')

function myFunction(div) {
    //document.querySelector(`.show`).classList.remove("show");
    document.querySelector(`.${div} #myDropdown`).classList.toggle("show");
    
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
  var ctgArray = [
    "lng-service",
    "lng-gadgets", 
    "lng-personalItems", 
    "lng-child", 
    "lng-business", 
    "lng-animals", 
    "lng-house",
    "lng-job", 
    "lng-hobby", 
    "lng-apartments", 
    "lng-transport"
  ]
  var locationArray = [
        "lng-AlmatyReg",
    "lng-AkmolaReg",
    "lng-AtyReg",
    "lng-AktobeReg",
    "lng-EKReg",
    "lng-ZhambylReg",
    "lng-WKReg",
    "lng-KgReg",
    "lng-KosReg",
    "lng-KzReg",
    "lng-MgReg",
    "lng-PvReg",
    "lng-NKReg",
    "lng-TurkReg",
  ]
  
var categories = document.querySelectorAll('.category')
categories.forEach((category, index) => {
    category.addEventListener('click' , () => {
        document.querySelector('.wholeList-btn').innerHTML = categories[index].children[1].innerHTML + ' <i class="fas fa-angle-down arrow"></i>'  
        if(document.querySelector('.wholeList-btn').classList.contains('lng-allCtg')){
            document.querySelector('.wholeList-btn').classList.remove('lng-allCtg')
        }
        document.querySelector('.wholeList-btn').classList.add(ctgArray[index])

    })
})
var a = document.querySelector('#myDropdown a')
a.addEventListener('click', () => {
    console.log(a.parentElement.previousElementSibling);
    a.parentElement.previousElementSibling.innerHTML = a.innerHTML + ' <i class="fas fa-angle-down arrow"></i>'
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
liList.forEach((each, index) =>{
    each.addEventListener('click', () => {
        outLi(each,true, index)
    }) 
    each.addEventListener('mouseover', () => {
        outLi(each, false, index)
    }) 
       
})
const outLi = (each, boolValue, index) => {
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
                if(document.querySelector('.location-btn').classList.contains('lng-allRegion')){
                    document.querySelector('.location-btn').classList.remove('lng-allRegion')
                }
                document.querySelector('.location-btn').classList.add(locationArray[index])
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
// var chooseCategory = document.querySelector('.chooseCategory div')
// chooseCategory.addEventListener('click', () => {
//     console.log(document.querySelectorAll('.ul')[1]);
//     document.querySelectorAll('.ul')[0].style.display = 'none'
//     document.querySelector('.inputModal input').value = ''
//     var needUl = document.querySelectorAll('.ul')[1]
//     needUl.style.display = 'unset'
//     $('section').css('position', 'fixed')
//     showModal()
// })
