
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


const clickLick = (someArray) => {
    someArray.forEach((each) => {
        each.addEventListener('click', () => {
            links(someArray)
            each.classList.add("activeLink")
        })
    })
}
const links = (smth) => {
    smth.forEach(link => {
        link.classList.remove("activeLink")
    })
}
const paymentStatus = document.querySelectorAll(".catg")

clickLick(paymentStatus)


const myFunction = (number) => {
    document.querySelector(`.${document.querySelectorAll('.paymentSec')[number].classList[0]} .wholeList-content-span`).classList.add('show')
}
window.onclick = function(event) {
    
    if (!event.target.matches('.wholeListSpan button')) {
         document.querySelector('.wholeList-content-span.show').classList.remove('show')
        // toggleId(listClassOb['wholeList-btn'])
      }
  }
const insert = (a, num) => {
    
    //document.querySelectorAll('.wholeListSpan .dateOfOperation')[num].innerHTML = a.innerHTML
}
let inputSearchAll = document.querySelectorAll('.searchPayment input')
var foundCount = 0
let inputSearch = document.querySelector('.searchPayment input')
var found = false

inputSearchAll.forEach((inputSearch, index) => {
    var classInput = inputSearch.getAttribute('paymentType')
    console.log(classInput);
    inputSearch.oninput = function(){
        let value = this.value.trim().toLowerCase()
        if(value != ''){
            let list = document.querySelectorAll(`.${classInput} .operation`)
            let listNum = document.querySelectorAll(`.${classInput} .numberOfOperation`)
            let listSum = document.querySelectorAll(`.${classInput} .sumOfOperation`)
            if(parseInt(value) >= 0){
                listNum.forEach(elem => {
                    if(elem.innerText.toLowerCase().search(value) == -1){
                        elem.parentNode.classList.add('hide');
                    }
                    else{
                        elem.parentNode.classList.remove('hide');
                        
                    }
                })
            }
            else{
                list.forEach(elem => {
                    if(elem.innerText.toLowerCase().search(value) == -1){
                        elem.parentNode.classList.add('hide');
                        
                    }
                    else{
                        elem.parentNode.classList.remove('hide');
                    }
                })
            }
            foundCount = document.querySelectorAll(`.${classInput} .lineForReceipt`).length - document.querySelectorAll(`.${classInput} .hide`).length
            document.querySelector(`.${classInput} .allPossible`).innerHTML = '/' + Math.ceil((foundCount/10))
            itaArray[index] = 1
            document.querySelector(`.${classInput} .current`).innerHTML = 1
            createGhosts(classInput)
        }
        else{
            document.querySelectorAll(`.${classInput} .lineForReceipt`).forEach(each => {
                each.classList.remove('hide')
                foundCount = document.querySelectorAll(`.${classInput} .lineForReceipt`).length
                document.querySelector(`.${classInput} .allPossible`).innerHTML = '/' + Math.ceil((foundCount/10))
            })
        }
    }  
})
document.querySelectorAll('.catg').forEach((catg, index) => {
    catg.addEventListener('click', () => {
        $('.visible').removeClass('visible')
        document.querySelectorAll('.paymentSec')[index].classList.add('visible')
    })
})
var dateArr = []
var date = []
var sortedDate = []
function ascFunc(iClass){
    document.querySelectorAll(`.${iClass} .dateOfOperation`).forEach(eachDate => {
        var temp = eachDate.innerHTML[3] + eachDate.innerHTML[4] + eachDate.innerHTML[2] + eachDate.innerHTML[0] + eachDate.innerHTML[1] + eachDate.innerHTML[5] + eachDate.innerHTML[6] + eachDate.innerHTML[7] + eachDate.innerHTML[8] + eachDate.innerHTML[9]
        var date = new Date(temp)
        dateArr.push(date.toDateString())
    })
    function sortFunction(a,b){  
        var dateA = new Date(a).getTime();
        var dateB = new Date(b).getTime();
        return dateA > dateB ? 1 : -1;  
    }; 

    dateArr.sort(sortFunction);
    
}
function descFunc(){
    document.querySelectorAll('.lineForReceipt .dateOfOperation').forEach(eachDate => {
        var temp = eachDate.innerHTML[3] + eachDate.innerHTML[4] + eachDate.innerHTML[2] + eachDate.innerHTML[0] + eachDate.innerHTML[1] + eachDate.innerHTML[5] + eachDate.innerHTML[6] + eachDate.innerHTML[7] + eachDate.innerHTML[8] + eachDate.innerHTML[9]
        var date = new Date(temp)
        dateArr.push(date.toDateString())
    })
    function sortFunction(a,b){  
        var dateA = new Date(a).getTime();
        var dateB = new Date(b).getTime();
        return dateA < dateB ? 1 : -1;  
    }; 

    dateArr.sort(sortFunction);
}

var changedDate
var ready = []
var block = false
var first = true
var all
var seach
document.querySelectorAll('#myDropdown a').forEach(eachA => {
    eachA.addEventListener('click', () => {
        var iClass = eachA.getAttribute('classInput')
        all = document.querySelectorAll(`.${iClass} .dateOfOperation`)
        console.log(eachA.className);
        if(eachA.className == 'asc'){
            ascFunc(iClass)
            sortedDate = []
            dateArr.forEach((each, index) => {
                var date = new Date(each)
                changedDate = date.toLocaleDateString().replaceAll('.', '/')
                sortedDate.push(changedDate)
            })
            console.log(sortedDate, dateArr);
            all.forEach((each, index) => {
                console.log(each.innerHTML, sortedDate[index]);
                sortedDate.forEach((seach,sindex) => {
                    if(each.innerHTML == seach ){
                        each.parentNode.style.order = sindex
                    }
                })
            })
        }
        else if(eachA.className == 'desc'){
            descFunc(iClass)
            sortedDate = []
            dateArr.forEach((each, index) => {
                var date = new Date(each)
                changedDate = date.toLocaleDateString().replaceAll('.', '/')
                sortedDate.push(changedDate)
            })
            console.log(sortedDate, dateArr);
            all.forEach((each, index) => {
                console.log(each.innerHTML, sortedDate[index]);
                sortedDate.forEach((seach,sindex) => {
                    if(each.innerHTML == seach ){
                        each.parentNode.style.order = sindex
                    }
                })
            })

        }
        
    })
})

inputSearchAll.forEach(each => {
    createGhosts(each.getAttribute('paymentType'))
    document.querySelector(`.${each.getAttribute('paymentType')} .allPossible`).innerHTML = '/' + Math.ceil((document.querySelectorAll(`.${each.getAttribute('paymentType')} .lineForReceipt`).length - document.querySelectorAll('.mainPayment .hide').length)/10)

})
var itaArray = [1, 1, 1]
document.querySelectorAll('.fa-angle-right').forEach((eachArrow, index) => {
    eachArrow.addEventListener('click', () => {
        if(itaArray[index] != Math.ceil((document.querySelectorAll(`.${document.querySelectorAll('.paymentSec')[index].classList[0]} .lineForReceipt`).length - document.querySelectorAll(`.${document.querySelectorAll('.paymentSec')[index].classList[0]} .hide`).length)/10) && document.querySelector(`.${document.querySelectorAll('.paymentSec')[index].classList[0]} .allPossible`).innerHTML != '/0')
        {
            
            $('.boxCon').animate({
                scrollTop: '+=500'
            }, 1, 'swing');
            itaArray[index]++

            document.querySelector(`.${document.querySelectorAll('.paymentSec')[index].classList[0]} .current`).innerHTML = itaArray[index]
            }
    })
})
document.querySelectorAll('.fa-angle-left').forEach((eachArrow,index) => {
    eachArrow.addEventListener('click', function() {
        if(itaArray[index] != 1){
            $('.boxCon').animate({
                scrollTop: '-=500'
           }, 1, 'swing');
           itaArray[index]--
             document.querySelector(`.${document.querySelectorAll('.paymentSec')[index].classList[0]} .current`).innerHTML = itaArray[index]
        }
     })
})
function createGhosts(classInp){
    document.querySelectorAll(`.${classInp} .ghostsDel`).forEach(eachGhost => {
        eachGhost.remove()
    })
    for(var i = 0; i < (10-(document.querySelectorAll(`.${classInp} .lineForReceipt`).length - document.querySelectorAll(`.${classInp} .hide`).length)%10); i++){
        var divEl = document.createElement('div')
        divEl.className = 'ghostDel'
        document.querySelector(`.${classInp} .boxCon`).append(divEl)
    }

}
