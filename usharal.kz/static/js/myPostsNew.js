Array.prototype.last = function() {
    return this[this.length - 1];
   }

document.querySelectorAll('.allStatusOfPosts span').forEach((each, index) => {
    each.addEventListener('click', () => {
        var allEl = document.querySelectorAll('.allStatusOfPosts span')
        var needEl = document.querySelector('.allStatusOfPosts span.activeLink')
        var ind = [...allEl].indexOf(needEl)
        
        document.querySelector('.allStatusOfPosts .activeLink').classList.remove('activeLink')
        each.classList.add('activeLink')
        document.querySelectorAll('.findWithThat')[ind].classList.add('mpc')
        document.querySelectorAll('.findWithThat')[index].classList.remove('mpc')
    })
})
var np = false
    var basic = -1
    const showModal = () => {
        
        $('.shadow').css('display', 'flex')
    }
    const modal = (str, num) => {
        
        
        
        showModal()

        $('section').css('overflow', 'hidden')
        document.querySelectorAll('.ul')[1].style.display = 'unset'
        document.querySelectorAll('.ul')[0].style.display = 'none'
        if(str == 'newPost'){
            np = true
            basic = num
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
      function myFunction(div) {
        //document.querySelector(`.show`).classList.remove("show");
        document.querySelector(`.${div} #myDropdown`).classList.toggle("show");
        
    } var a = document.querySelectorAll('#myDropdown a')
    // function insert(randA, ind){
    //     document.querySelectorAll('.sort')[ind].innerHTML = randA.innerHTML
    // }
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
                }
            }
            else{
                if(basic >= 0){
                    document.querySelectorAll('.allCatChild')[basic].innerHTML = text
                    
                  //  document.querySelector(`.${document.querySelectorAll('.chooseCategory')[basic].classList[0]} div`). += '<i class="fa-solid arrow fa-angle-down"></i>'
                }
                //document.querySelector('.chooseCategory div').innerHTML = text
            }
            $('section').css('position', 'sticky')
        }
        else{
            var text = each.innerHTML
            document.querySelector('.inputModal input').value = text 
        }
        
            
            
    }
    $(".up").click(function(){
        window.scrollTo(0, 0)
    })
    const list = ["ru", "kz"]
    let hash = 'ru'
    const langAll = document.querySelectorAll(".langSpan")
    
    window.onload = () => {
        let inputSearch = document.querySelector('.inputModal input')
        
        inputSearch.oninput = function(){
            let value = this.value.trim().toLowerCase()
            let list = document.querySelectorAll('.ul li')
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
//dich?
const transferClick = () => {
    document.querySelectorAll(' .newCreatedButton').forEach(each => {
        // console.log(each);
        each.addEventListener('click', () => {
            
            var parentFind = each.parentNode.parentNode.parentNode.classList[0];
            var tin = document.querySelector(`.${parentFind} .chosenButton`).innerHTML
            document.querySelector(`.${parentFind} .chosenButton`).classList.remove('chosenButton')
            each.classList.add('chosenButton')
            if(+each.innerHTML > +tin ){
                var a = (+each.innerHTML - +tin)*768
                $(`.${parentFind} .allMyContent`).animate({
                    scrollTop: '+=' + a
                },1,'swing')
            }
            else{
                var a = (+tin - +each.innerHTML  )*768
                $(`.${parentFind} .allMyContent`).animate({
                    scrollTop: '-=' + a
                },1,'swing')
            }
        })
    })
};
let input = document.querySelectorAll('.searchPartMy input')
input.forEach((fInput, index) => {
    fInput.oninput = function(){
        let fInputValue = this.value.trim().toLowerCase()
        $(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .allMyContent`).animate({
            scrollTop: 0
        },1,'swing')
        if(fInputValue != ''){
            // console.log(fInputValue)
            document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .nameOfTheProduct`).forEach(name => {
            
                if(name.innerText.toLowerCase().search(fInputValue) == -1){
                    name.parentNode.parentNode.parentNode.parentNode.classList.add('hide')  
                }
                else{
                    name.parentNode.parentNode.parentNode.parentNode.classList.remove('hide')
                }
                
               
            })
            if(document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .myContent`).length == document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .myContent.hide`).length){
                document.querySelector(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .imgThink`).classList.remove('close')
            }
            else{
                document.querySelector(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .imgThink`).classList.add('close')
            }
            button_future_counts = Math.ceil(+(document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .myContent:not(.hide)`).length)/4)
            createButtons(button_future_counts, index)
            transferClick()
            for(var it = 0; it < 3; it++){
                createGhostDiv(it)
            }
            createGhostButtons(button_future_counts , index)

        
        }
        else{
            document.querySelector(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .imgThink`).classList.add('close')
            document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .nameOfTheProduct`).forEach(name => {
            
                name.parentNode.parentNode.parentNode.parentNode.classList.remove('hide')
            })
            button_future_counts = Math.ceil(+(document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .myContent:not(.hide)`).length)/4)
            createButtons(button_future_counts, index)
            createGhostButtons(button_future_counts, index)
            transferClick()
            createGhostDiv(index)
            
        }
    
    }
})
    var chooseAll
    const checkboxFunc = (index) => {
        var prnt = document.querySelectorAll('.findWithThat')[index].classList[0]
        chooseAll = document.querySelector(`.${prnt} #check`)
        if(chooseAll.checked){
          
            
            document.querySelectorAll(`.${prnt} input[type = checkbox]`).forEach(each => {
                if(each.parentNode.parentNode.classList.contains('hide')){

                }
                else{
                    each.checked = true
                    
                }
            })
        }
        else{
            document.querySelectorAll(`.${prnt} input[type = checkbox]`).forEach(each => {
                each.checked = false
            })
            
        }
    }
    var button_future_counts
    const createButtons = (count, index) => {
        document.querySelector(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .lineForNewButtons`).innerHTML = ''

        for(var num = 1; num <= count; num++){
            var newButton = document.createElement('button')
            newButton.classList.add('newCreatedButton')
            if(num == 1){
                newButton.classList.add('chosenButton')
            }
            newButton.innerText = num
            document.querySelector(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .lineForNewButtons`).append(newButton)
        }
        // document.querySelector('.mainMyPostsContent .lineForNewButtons')
        
    }   
    const createGhostDiv = (index) => {
        document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .ghost`).forEach(g => g.remove())
        var count_ghost_div = 4 - document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .myContent:not(.hide)`).length%4
        if(count_ghost_div % 4 != 0){
            for(var coundDiv = 0; coundDiv < count_ghost_div; coundDiv++){
                var ghostDivOrigin = document.createElement('div')
                ghostDivOrigin.classList = 'ghost'
                document.querySelector(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .allMyContent`).append(ghostDivOrigin)
            }
        }

    }
    const createGhostButtons = (arg_count, index) => {
        document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .ghostBtn`).forEach(each => {
            each.remove()
        })
        var actual_count = 6 - arg_count%6
        if(actual_count % 6 != 0){
            for(var it = 0; it < actual_count; it++){
                var ghostBtn = document.createElement('button')
                ghostBtn.classList = 'ghostBtn'
                
                document.querySelector(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .lineForNewButtons`).append(ghostBtn)
            }
        }
    }
    const nextMyButton = document.querySelectorAll('.bottomBut .myContentAngle .fa-angle-right')
    nextMyButton.forEach(n => n.onclick = () => {
        var parentFind = n.parentElement.parentElement.parentElement.classList[0];
        button_future_counts = Math.ceil(+(document.querySelectorAll(`.${parentFind} .myContent:not(.hide)`).length)/4)

        var el = document.querySelectorAll(`.${parentFind} .newCreatedButton`)
        var target =document.querySelector(`.${parentFind} .chosenButton`)
        var index = [...el].indexOf(target)
       
        if(+el[index].innerHTML < button_future_counts){
            $(`.${parentFind} .chosenButton`).removeClass('chosenButton')
            el[index+1].classList.add('chosenButton')
            $(`.${parentFind} .allMyContent`).animate({
                scrollTop: '+=768'
            },1,'swing')
            if(+el[index].innerHTML%6 == 0 && index > 0){
                $(`.${parentFind} .lineForNewButtons`).animate({
                scrollLeft: '+=340'
              }, 300, 'swing');
            }
        }
        else{
    
        }
    
    })
    const prevMyButton = document.querySelectorAll('.bottomBut .myContentAngle .fa-angle-left')
    prevMyButton.forEach(p => p.onclick = () => {
        var parentFind = p.parentElement.parentElement.parentElement.classList[0];
        var el = document.querySelectorAll(`.${parentFind} .newCreatedButton`)
        var target =document.querySelector(`.${parentFind} .chosenButton`)
        
        var index = [...el].indexOf(target)
        
        if(+el[index].innerHTML > 1){
            
            $(`.${parentFind} .chosenButton`).removeClass('chosenButton')
            el[index-1].classList.add('chosenButton')
            $(`.${parentFind} .allMyContent`).animate({
                scrollTop: '-=768'
            },1,'swing')
            if(+el[index].innerHTML%6 == 1 && index > 1){
                $(`.${parentFind} .lineForNewButtons`).animate({
                    scrollLeft: '-=340'
                  }, 300, 'swing')
            }
        }
        else{
    
        }
    })
    
   
    for(var i = 0; i < 2; i++){
        button_future_counts = Math.ceil(+(document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[i].classList[0]} .myContent:not(.hide)`).length)/4)
        createButtons(button_future_counts, i)
        createGhostDiv(i)
        createGhostButtons(button_future_counts, i)
    }
    
    var firstCon = document.querySelectorAll('.firstCon')
    firstCon.forEach((fc, index) => fc.onclick = () => {

        $(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .chosenButton`).removeClass('chosenButton')
        document.querySelector(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .newCreatedButton`).classList.add('chosenButton')
        $(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .allMyContent`).animate({
            scrollTop: 0

        }, 1, 'swing')
        $(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .lineForNewButtons`).animate({
            scrollLeft: 0

        }, 1, 'swing')
    })
    var lastCon = document.querySelectorAll('.lastCon')
    lastCon.forEach((lc, index)=>{
       lc.addEventListener('click', ()=> {
        // alert()
        $(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .chosenButton`).removeClass('chosenButton')
        document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .newCreatedButton`)[document.querySelectorAll(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .newCreatedButton`).length - 1].classList.add('chosenButton')
        $(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .allMyContent`).animate({
            scrollTop: $(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .allMyContent`).get(0).scrollHeight

        }, 1, 'swing')
        $(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .lineForNewButtons`).animate({
            scrollLeft: $(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .lineForNewButtons`).get(0).scrollWidth

        }, 1, 'swing')
       })
        
    })
    
    transferClick()

    
    var ittrash = 0
    var sum = 10000
//    document.querySelectorAll('.mainMyPostsContent .myContent .cost').forEach(each => {
//     sum += 10000
//     each.innerHTML = sum
//    })
   var currencyMask = IMask(
    document.querySelector('.blocks .cost'),
    {
      mask:  '₸ num',
      blocks: {
        num: {
          mask: Number,
          thousandsSeparator: ' '
        }
      }
      
    });
    document.querySelectorAll('.blocks input').forEach((each, index) => {
        
        each.size = each.value.length + 2
        var currencyMask = IMask(
            each,
            {
              mask:  '₸ num',
              blocks: {
                num: {
                  mask: Number,
                  thousandsSeparator: ' '
                }
              }
              
            });
        
    })
    var obj
    var arrValue = [
        [],
        [],
        []
    ]
    // .size = document.querySelector('.blocks input').value.length 
    function insert(randA, ind){
        obj = randA.innerText
        var pf = document.querySelectorAll('.findWithThat')[ind].classList[0]
        // console.log(obj == 'По убыванию ');
        // console.log(obj, pf)
        document.querySelectorAll('.sort')[ind].innerHTML = randA.innerHTML
        document.querySelectorAll(`.${pf} .blocks input`).forEach((cost, index) => {
            arrValue[ind][index] = cost.value
            arrValue[ind][index] = arrValue[ind][index].replaceAll(' ', '')
            arrValue[ind][index] = arrValue[ind][index].replaceAll('₸', '')
        })
        if(obj == 'По убыванию '){
            
            arrValue[ind].sort((a, b) => b - a);
        }
        else if(obj == 'По возростанию '){
            arrValue[ind].sort((a, b) => a-b);
        }
        arrValue[ind].forEach((each, index) => {
            var pf = document.querySelectorAll('.findWithThat')[ind].classList[0]
            str = document.querySelectorAll(`.${pf} .blocks input`)[index].value.replaceAll(' ', '')
            str = str.replaceAll('₸', '')
            console.log(arrValue[ind].indexOf(str));
            // console.log(str)
            document.querySelectorAll(`.${pf} .myContent:not(.hide)`)[index].style.order = arrValue[ind].indexOf(str)
        })
        // document.querySelectorAll(`.${pf} .ghost`).forEach(eachHide => {
        //     eachHide.style.order = arrValue[ind].length++
        // })
        $(`.${pf} .allMyContent`).animate({
            scrollTop: 0

        }, 1, 'swing')
        $(`.${pf} .lineForNewButtons`).animate({
            scrollLeft: 0

        }, 1, 'swing')
        $(`.${pf} .chosenButton`).removeClass('chosenButton')
        document.querySelector(`.${pf} .newCreatedButton`).classList.add('chosenButton')
    }
    // var sum = 10000
    // document.querySelectorAll('.blocks input').forEach(each => {
    //     sum += 10000
    //     each.value = sum
    // })