function deleteAll(){
    console.log('I am Working')
    let photos = document.getElementsByClassName('imageOfUser');
    for(let i = 0; i < photos.length; i++){
        console.log(photos[i])
        photos[i].src = "/static/img/Vector1.svg";
        photos[i].style = 'width:50px'
    }
    imgArr = ['/static/img/Vector1.svg', '/static/img/Vector1.svg', '/static/img/Vector1.svg','/static/img/Vector1.svg','/static/img/Vector1.svg','/static/img/Vector1.svg','/static/img/Vector1.svg','/static/img/Vector1.svg']
    var divElement = document.querySelector('.photo');
                    divElement.removeAttribute('hidden');
                    var elementsWithCount7 = document.querySelectorAll('.photo[count="7"]');
                    elementsWithCount7.forEach(function(element) {
                        element.setAttribute('hidden', true);
                    });
    // document.querySelector("body > div.all > section > form > div.pageForNewPostChild > div.mainBody > div.informationAboutProduct > div.bigBoxForImages > div > div.imageBox2.imageBox > img").src = '/static/img/Vector1.svg';
   
}
var allBoxAbs 
var imgArr= []

var imgArr = ['../static/img/Vector1.svg', '../static/img/Vector1.svg', '../static/img/Vector1.svg','../static/img/Vector1.svg','../static/img/Vector1.svg','../static/img/Vector1.svg','../static/img/Vector1.svg','../static/img/Vector1.svg']
var finalImgArr = []

function showFile(input) {
    deleteAll();

    var images = document.querySelectorAll('.imageOfUser');
    var imgArr = [];

    for (var i = 0; i < images.length; i++) {
        imgArr[i] = '../static/img/Vector1.svg';
    }

    for (var i = 0; i < input.files.length; i++) {
        var reader = new FileReader();
        var name = 'file' + i;

        reader.onload = (function (idx) {
            return function (e) {
                imgArr[idx] = e.target.result;
                if (imgArr.length > 8) {
                    imgArr.pop();
                }
                if (input.length>=8){
                    var elementToHide = document.querySelector('.photo');       
                    elementToHide.setAttribute('hidden', true);
                    var divElement = document.querySelector('.photo[count="7"]');
                    divElement.removeAttribute('hidden');
                    

                }
                updateImages();
            };
        })(i);

        reader.readAsDataURL(input.files[i]);
    }

    function updateImages() {
        document.querySelectorAll('.imageOfUser').forEach((each, index) => {
            if (imgArr[index] != '../static/img/Vector1.svg') {
                each.style.width = '100%';
                each.style.height = '100%';
                each.style.objectFit = 'cover';
            }
            each.src = imgArr[index];
        });
    }

    updateImages();
}

        
    
    var falseIsThere = false
    var checkForValid = []
    var requiredInput = [
        document.querySelector('input.productName'),
        // document.querySelector('.chooseCategory div'),
        document.querySelector('.costBlock input'), 
        document.querySelector('textArea'),
        document.querySelectorAll('textArea')[1],
        document.querySelectorAll('.periodOfInputs input')[0],
        document.querySelectorAll('.periodOfInputs input')[1],
        document.querySelectorAll('.periodOfInputs input')[2]
    ]
    var q = 0
    document.querySelector('.finalBtn').addEventListener('click', checkInput)
    document.querySelector('.previewBtn').addEventListener('click', checkInput)
    function checkInput(){
        checkForValid.length = 0
        checkForValid.push(document.querySelector('input.productName').value.length >= 16)
        // checkForValid.push(document.querySelector('.chooseCategory div').innerHTML != 'Выберите категорию')
        checkForValid.push(document.querySelector('.costBlock input').value.length >= 1)
        checkForValid.push(document.querySelector('textArea').value.length >= 80)
        checkForValid.push(document.querySelectorAll('textArea')[1].value.length >= 5)
        document.querySelectorAll('.periodOfInputs input').forEach((each, index) => {
            
            if(index == 0){
                checkForValid.push(each.value != '')
            }
            else if(index == 1 || index == 2){
                checkForValid.push(each.value.length == 18)
            }
        })
        if(checkForValid.includes(false)){
            var sum = 0
          
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
        }
    }
    



const freeField = (el) => {
    if (el.checked){
        document.querySelector('.costBlock .inner.lng-costInTenge').value = '₸ 0'
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
const disableButton = (value) => {
    document.querySelectorAll('.finalButtonDiv button').forEach(each => {
        each.disabled = value
    })
}

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
        
