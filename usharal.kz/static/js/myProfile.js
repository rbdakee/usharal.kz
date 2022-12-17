
$(".up").click(function(){
    window.scrollTo(0, 0)
})
const list = ["ru", "kz"]
let hash = 'ru'
const langAll = document.querySelectorAll(".langSpan")


let fileProf;
function showFileProfile(input){
    fileProf = input.files[0]
    input.previousElementSibling.src = URL.createObjectURL(fileProf)
    input.previousElementSibling.style.height = getComputedStyle(input.parentNode).height
    input.previousElementSibling.style.width = getComputedStyle(input.parentNode).width
  }
var forFavBox = 0
function fill(elem){
    elem.classList.toggle("fa-regular")
    elem.classList.toggle("fa")
    var favZone = document.querySelector('.mainPartWithButton .mainPart')
    console.log(favZone);
    var temp = elem.parentNode.parentNode
    if(elem.classList.contains('fa')){
       
        
        var contentBoxFav = temp.cloneNode(true)
        favZone.prepend(contentBoxFav)
    }
    else{
        
        // if(favZone.hasChildNodes(temp)){
        //    console.log(favZone.c);
        //     // favZone.removeChild(elem)
        // //    console.log('favZone.removeChild(elem): ', favZone.removeChild(elem));
        // }
        console.log(favZone.contains(temp));
    }
    
}   
var newPostZone = document.querySelector('.pageForNewPost .mainBody')

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

var liList  = document.querySelectorAll('.ul li')
liList.forEach(each =>{
    each.addEventListener('click', () => {
        outLi(each,true)
    }) 
    each.addEventListener('mouseover', () => {
        outLi(each, false)
    }) 
       
})
var phoneMask = IMask(
    document.querySelector('.profileNum'), {
    
      mask: '+{7} (000) 000-00-00'
    });
var seephoneMask = IMask(
    document.querySelectorAll('.profileNum')[1], {
    
      mask: '+{7} (000) 000-00-00'
    });
document.querySelector('.changeProfile').addEventListener('click', () => {
    $('.prof').removeClass('prof')
    document.querySelectorAll('.myProfileInner')[1].classList.add('prof')
    document.querySelector('.changeProf .spanWithInput.inner input').value = document.querySelector('.nameOfUser').innerHTML.split(' ').join('')
    document.querySelector('.changeProf img').src = document.querySelector('img').src
    if(document.querySelector('img').getAttribute('src') != 'img/Vector.svg'){
        document.querySelector('.changeProf img').style.width = '100px'
        document.querySelector('.changeProf img').style.height = '100px'
     }
    document.querySelectorAll('option').forEach((opt, index) => {
        //opt.setAttribute('selected', 'false')
        if(opt.innerHTML == document.querySelector('.spanWithInput .userAddress').innerHTML){
            opt.setAttribute('selected', 'true')
        }
    })
    // document.querySelectorAll('option')[0].innerHTML = document.querySelector('.spanWithInput .userAddress').innerHTML
    document.querySelector('.changeProf .phoneSpan input').value = document.querySelector('.phoneSpan input').value.split(' ').join('')
    // document.querySelector('.nameOfUser').innerHTML
})
const saveData = () => {
    if(document.querySelector('.changeProf .spanWithInput input').value.length >= 4){
        document.querySelector('.changeProf .spanWithInput input').classList.remove('validation_error')
        if(document.querySelector('.changeProf .phoneSpan input').value.split(' ').join('').length == 16){
            document.querySelector('.changeProf .phoneSpan input').classList.remove('validation_error')
            $('.prof').removeClass('prof')
            document.querySelectorAll('.myProfileInner')[0].classList.add('prof')
            document.querySelector('.nameOfUser').innerHTML = document.querySelector('.changeProf .spanWithInput.inner input').value
            document.querySelector('img').src = document.querySelector('.changeProf img').src 
            if(document.querySelector('img').getAttribute('src') != 'img/Vector.svg'){
                document.querySelector('img').style.width = '100px'
                document.querySelector('img').style.height = '100px'
            }
            var selindex = document.querySelector("#select").selectedIndex
            
            document.querySelector('.spanWithInput .userAddress').innerHTML =document.querySelectorAll('option')[selindex].innerHTML
            document.querySelector('.phoneSpan input').value = document.querySelector('.changeProf .phoneSpan input').value.split(' ').join('')
        }
        else{
            document.querySelector('.changeProf .phoneSpan input').classList.add('validation_error')
            window.scrollTo(150, 200)
        }
    }
    else{
        document.querySelector('.changeProf .spanWithInput input').classList.add('validation_error')
        window.scrollTo(0, 0)
    }
}
document.querySelector('.confirmButtonLine button').addEventListener('click', saveData)
