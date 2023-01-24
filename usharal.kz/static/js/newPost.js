
var newPostZone = document.querySelector('.pageForNewPost .mainBody')

function myFunction(div) {
    //document.querySelector(`.show`).classList.remove("show");
    document.querySelector(`.${div} #myDropdown`).classList.toggle("show");
    
}


function deleteAll(){
    document.querySelectorAll('.imageBox img').forEach((each, index) => {
        each.src =  '/static/img/Vector1.svg';
        each.style.width = '50px'
        each.style.height='50px'
        each.style.objectFit = null
        imgArr[index] = '../static/img/Vector1.svg'
     })
     document.querySelector('.imageBox1 input').value = '';
     document.querySelector('.imageBox1 input').disabled = false;
     document.querySelector('.imageBox1 img').setAttribute('src', '/static/img/Vector.svg')
     document.querySelector('.imageBox1 img').setAttribute('style', 'position:absolute; z-index:1')
     document.querySelector('.imageBox1').classList.remove('imageBox')
     document.querySelector('.imageBox1').classList.remove('imageOfUserChoose')
     document.querySelector('.imageBox1').objectFit = null


    
    
}

const deleteFunction = (btn) => {
    var btnParentIndex = +btn.parentNode.parentNode.getAttribute('count')
    imgArr.splice(btnParentIndex, 1)
    imgArr.push('../static/img/Vector1.svg')
    btn.parentNode.previousElementSibling.previousElementSibling.setAttribute('src', '../static/img/Vector1.svg')
    $(`.${btn.parentNode.parentNode.classList[0]} .backColor.active`).removeClass('active')
    $(`.${btn.parentNode.parentNode.classList[0]} div.deleteAnim`).css('animation', 'myAnimOut 0.8s ease 0s 1 normal forwards')
    btn.parentNode.previousElementSibling.previousElementSibling.style.width = '50px'
    btn.parentNode.previousElementSibling.previousElementSibling.style.height = '50px'
    btn.parentNode.previousElementSibling.previousElementSibling.style.objectFit = null
    
    
    // document.querySelector('.absolute').value = ''
    document.querySelectorAll('.imageBox').forEach((each, index) => {
        
        if(imgArr[index] != '../static/img/Vector1.svg'){
            document.querySelector(`.${each.classList[0]} img`).style.width = '100%'
            document.querySelector(`.${each.classList[0]} img`).style.height = '100%'
            document.querySelector(`.${each.classList[0]} img`).style.objectFit = 'cover'
        }
        else{
            document.querySelector(`.${each.classList[0]} img`).style.width = '50px'
            document.querySelector(`.${each.classList[0]} img`).style.height = '50px'
            document.querySelector(`.${each.classList[0]} img`).style.objectFit = null
        }
        document.querySelector(`.${each.classList[0]} img`).setAttribute('src', imgArr[index])
        // document.querySelector('.absolute').value += ` ${imgArr[index]}` + ' '
    })
    
}
const list = ["ru", "kz"]
const langAll = document.querySelectorAll(".langSpan")
let hash = 'ru'


var np = false
const showModal = () => {
    
    $('.shadow').css('display', 'flex')
}
const modal = (str) => {
    showModal()
    // $('section').css('position', 'fixed')
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
            // $('section').css('position', 'sticky')
          
          //console.log();
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
// var a = document.querySelector('#myDropdown a')
// a.addEventListener('click', () => {
//     console.log(a.parentElement.previousElementSibling);
//     a.parentElement.previousElementSibling.innerHTML = a.innerHTML + ' <i class="fas fa-angle-down arrow"></i>'
// })
window.onload = () => {
    let inputSearch = document.querySelector('.inputModal input')
    
    inputSearch.oninput = function(){
        let value = this.value.trim().toLowerCase()
        let list = document.querySelectorAll('.ul li')
        // console.log(list);
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
        outLi(each, false)
    }) 
       
})
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
    "lng-justAstana",
"lng-justAlmaty",
"lng-justShymkent"

  ]
  $(".up").click(function(){
    window.scrollTo(0, 0)
})
const outLi = (each, boolValue,index) => {
    if(boolValue){
        $('.shadow').css('display', 'none')
        if(each.tagName == 'INPUT'){
            var text = each.value
        }
        else{
            var text = each.innerHTML
        }
        if(text.includes('Казахстанская')){
            text = text[0] + 'KO'
        }
        if(document.querySelectorAll('.ul')[0].style.display == 'unset'){
            if(np){
                document.querySelector('.locationInput input').value = text
                if(document.querySelector('.locationInput input').classList.contains('lng-searchByArea')){
                    document.querySelector('.locationInput input').classList.remove('lng-searchByArea')
                }
                document.querySelector('.locationInput input').classList = ''
                document.querySelector('.locationInput input').classList.add(locationArray[index])
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
            if(document.querySelector('.chooseCategory div').classList.contains('lng-catg')){
                document.querySelector('.chooseCategory div').classList.remove('lng-catg')
            }
            console.log(index);
            document.querySelector('.chooseCategory div').classList.add(ctgArray[index-17])
            
        }
        $('section').css('position', 'sticky')
    }
    else{
        var text = each.innerHTML
        document.querySelector('.inputModal input').value = text
    }
    
        
        
}
var reader = []
var chooseCategory = document.querySelector('.chooseCategory div')
chooseCategory.addEventListener('click', () => {
    // console.log(document.querySelectorAll('.ul')[1]);
    document.querySelectorAll('.ul')[0].style.display = 'none'
    document.querySelector('.inputModal input').value = ''
    var needUl = document.querySelectorAll('.ul')[1]
    needUl.style.display = 'unset'
    $('section').css('position', 'fixed')
    showModal()
})
var allBoxAbs 
var imgArr= []

var imgArr = ['../static/img/Vector1.svg', '../static/img/Vector1.svg', '../static/img/Vector1.svg','../static/img/Vector1.svg','../static/img/Vector1.svg','../static/img/Vector1.svg','../static/img/Vector1.svg']
var finalImgArr = []
function showFile(input) {
    input.disabled = true
    if(imgArr[6] == '../static/img/Vector1.svg'){
        var files = input.files || input.currentTarget.files;
        console.log(files)

    reader = [];
    var images = document.querySelectorAll('.imageOfUser');
    var name;
    var bImgClicked = false
    for (var i in files) {
        if (files.hasOwnProperty(i)) {
            // document.querySelector('.absolute').value = '';
            name = 'file' + i;
           
            reader[i] = new FileReader();
            reader[i].readAsDataURL(input.files[i]);
            console.log(reader[i])
            
            reader[i].onload = function (e) {
                // console.log(document.getElementById(name));
                images[i].src = e.target.result;
                imgArr.unshift(e.target.result)
                if(imgArr.length > 8){
                   imgArr.pop()
                }
                console.log(imgArr)
                document.querySelectorAll('.imageOfUser').forEach((each, index) => {
                    if(imgArr[index] != '../static/img/Vector1.svg'){
                                    bImgClicked = true
                                    if(each.classList.contains('imageOfUserChoose')){
                                        each.style.width='115px'
                                        each.style.height='109px'
                                        each.style.borderRadius='10px'
                                    }
                                    else{
                                        each.style.width = '100%'
                                        each.style.height = '100%'
                                        
                                    }
                                    document.querySelectorAll('.imageOfUser')[index].style.objectFit = 'cover'
                                }
                    each.src = imgArr[index]
                    // document.querySelector('.absolute').value += ` ${imgArr[index]}` + ' '
                })
            };
            
        
            
            
            
            
        }
        
            
    }
    }
    
   
        //     allBoxAbs = input.files || input.current
    
    // if(imgArr[6] == '../static/img/Vector1.svg'){
    //     allBoxAbs = input.files || input.currentTarget.files;
    //     file = input.files[0];
    //     imgArr.unshift(URL.createObjectURL(file))
    //     if(imgArr.length > 7){
    //         imgArr.pop()
    //     }
    //     document.querySelectorAll('.imageOfUser').forEach((each, index) => {
    //         if(imgArr[index] != '../static/img/Vector1.svg'){
    //             each.style.width = '100%'
    //             each.style.height = '100%'
    //             document.querySelectorAll('.imageOfUser')[index].style.objectFit = 'cover'
    //         }
    //         each.setAttribute('src',imgArr[index] )
    //     })
    // }
    // else{
    //     alert()
    // }
  }

function btnclck(){
    const socket = new WebSocket('ws://' + location.host + '/post_photo');
    socket.send(imgArr);
}



  var fileProf
  
var currencyMask = IMask(
    document.querySelector('.costBlock input.inner'),
    {
      mask:  '₸ num',
      blocks: {
        num: {
          mask: Number,
          thousandsSeparator: ' '
        }
      }
      
    });
    var phoneMask = IMask(
        document.querySelector('.phoneNumber'), {
        
          mask: '+{7} (000) 000-00-00'
        });
        
    var phoneWhats = IMask(
        document.querySelectorAll('.phoneNumber')[1], {
          mask: '+{7} (000) 000-00-00'
        })
        var obj;
        
    
    var falseIsThere = false
    var checkForValid = []
    var requiredInput = [
        document.querySelector('.newPostHeader input'),
        document.querySelector('.chooseCategory div'),
        document.querySelector('.costBlock input'), 
        document.querySelector('textArea'),
        document.querySelectorAll('.periodOfInputs input')[0],
        document.querySelectorAll('.periodOfInputs input')[1],
        document.querySelectorAll('.periodOfInputs input')[2]
    ]
    var q = 0
    // document.querySelector('.finalButtonDiv button').addEventListener('click', checkInput)
    // document.querySelector('.betaButtonDiv').addEventListener('click', checkInput)
    function checkInput(){
        checkForValid.length = 0
        checkForValid.push(document.querySelector('.newPostHeader input').value.length >= 16)
        checkForValid.push(document.querySelector('.chooseCategory div').innerHTML != 'Выберите категорию')
        checkForValid.push(document.querySelector('.costBlock input').value.length >= 1)
        checkForValid.push(document.querySelector('textArea').value.length >= 80)
        document.querySelectorAll('.periodOfInputs input').forEach((each, index) => {
            
            if(index == 0){
                checkForValid.push(each.value != '')
            }
            else if(index == 1 || index == 2){
                checkForValid.push(each.value.length == 18)
            }
        })
        if(checkForValid.includes(false)){
            
            // console.log(checkForValid);
            var sum = 0
            // checkForValid.forEach((stat, index) => {
            //     console.log(stat);
            //     if(!stat){
            //         q = index
            //         requiredInput[index].classList.add('validation_error')
                    
                    
            //             }
                        
            // })
            for(var i = 0; i < checkForValid.length; i++){
                if(!checkForValid[i]){
                    requiredInput[i].classList.add('validation_error')
                    
                }
                else{
                    requiredInput[i].classList.remove('validation_error')
                }
            }
            for(var j = 0; j < checkForValid.length; j++){
               if(checkForValid[j] == false){
                    let scrollTarget = requiredInput[j];
                    let topOffset = scrollTarget.offsetHeight;
                // const topOffset = 0; // если не нужен отступ сверху
                    let elementPosition = scrollTarget.getBoundingClientRect().top;
                    let offsetPosition = elementPosition - topOffset -200;
                
                    window.scrollBy({
                        top: offsetPosition,
                        behavior: "smooth"
                    });
                    break
               }
            }
        }
        else{
            for(var i = 0; i < checkForValid.length; i++){
                requiredInput[i].classList.remove('validation_error')
                
            }
            alert('success!')
        }
    }
    



const freeField = (el) => {
    if (el.checked){
        document.querySelector('.costBlock .inner.lng-costInTenge').classList.add('hiddenInput')
        
        document.querySelector('.costBlock .inner.lng-costInTenge').value = -1
    }
} 
const field = (el) => {
    if(el.checked){
        document.querySelector('.costBlock .inner.lng-costInTenge').classList.remove('hiddenInput')
        document.querySelector('.costBlock .inner.lng-costInTenge').value = ''
    }
}


const checkForFree = (el) => {
    if (el.value.replace(/\s/g,'')!= '₸' && el.value.replace(/\s/g,'') != '' && el.value.replace(/\s/g,'')!= '₸0'){
        document.querySelector('.withRadio .middleBox input').checked = true
    }
    else if(el.value.replace(/\s/g,'')== '₸' || el.value.replace(/\s/g,'') == '' || el.value.replace(/\s/g,'')== '₸0') {
        
        document.querySelector('.withRadio .freeBox input').checked = true
    }
}
var arrindex = [80,16]
const titleProduct = (el, index) => {
    if(!index){
        
        const textarea = document.querySelector("textarea");
        const count = document.querySelector(".counter .currentValue");
        const text = textarea.value;
        const textlength = textarea.value.length;
        count.innerText = `${textlength}`;
    }
    if (el.value.length < arrindex[index]){
        if(!el.classList.contains('activeInput')){
            el.classList.add('activeInput')
        }
        disableButton(true)
    }
    else{
        el.classList.remove('activeInput')
        disableButton(true)
    }
}
const location1 = (el, index) => {
    if(!index){
        const textarea1 = document.querySelectorAll("textarea")[1];
        const count1 = document.querySelectorAll(".counter .currentValue")[1];
        const text1 = textarea1.value;
        const textlength1= textarea1.value.length;
        count1.innerText = `${textlength1}`;
    }
    
}
const disableButton = (value) => {
    document.querySelectorAll('.finalButtonDiv button').forEach(each => {
        each.disabled = value
    })
}


// ch = document.getElementById('default_phone_number');
// inp = document.getElementById('phone_number_input');
// phone_number = document.getElementById('phone_number').value;
// if (ch.checked){
//     inp.hidden = true;
//     phone_number.hidden = false;
//     inp.value = phone_number;
// }
// else if(ch.checked == false){
//     inp.hidden = false;
//     phone_number.hidden = true;
// }

// if(document.querySelector('.absolute').value == 1){
//     alert()
//     var input = document.querySelector('.bigBoxForImages input')
//     var files = input.files || input.currentTarget.files
//     reader = []
//     var images = document.querySelectorAll('.imageOfUser');
//         var name;
//         for (var i in files) {
//             if (files.hasOwnProperty(i)) {
//                 // document.querySelector('.absolute').value = '';
//                 // name = 'file' + i;
            
//                 reader[i] = new FileReader();
//                 reader[i].readAsDataURL(input.files[i]);
//                 console.log(reader[i])
                
//                 reader[i].onload = function (e) {
//                     images[i].src = e.target.result
//                 }
// }
//         }
//     }

// if(imgArr[6] == '../static/img/Vector1.svg'){
//     var files = input.files || input.currentTarget.files;
//     console.log(files)

// reader = [];
// var images = document.querySelectorAll('.imageOfUser');
// var name;
// for (var i in files) {
//     if (files.hasOwnProperty(i)) {
//         // document.querySelector('.absolute').value = '';
//         name = 'file' + i;
       
//         reader[i] = new FileReader();
//         reader[i].readAsDataURL(input.files[i]);
//         console.log(reader[i])
        
//         reader[i].onload = function (e) {
//             // console.log(document.getElementById(name));
//             images[i].src = e.target.result;
//             imgArr.unshift(e.target.result)
//             if(imgArr.length > 7){
//                imgArr.pop()
//             }
//             console.log(imgArr)
//             document.querySelectorAll('.imageOfUser').forEach((each, index) => {
//                 if(imgArr[index] != '../static/img/Vector1.svg'){
//                                 each.style.width = '100%'
//                                 each.style.height = '100%'
//                                 document.querySelectorAll('.imageOfUser')[index].style.objectFit = 'cover'
//                             }
//                 each.src = imgArr[index]
//                 // document.querySelector('.absolute').value += ` ${imgArr[index]}` + ' '
//             })
//         };
