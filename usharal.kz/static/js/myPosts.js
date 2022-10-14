var chooseAll
    const checkboxFunc = (index) => {
        var prnt = document.querySelectorAll('.findWithThat')[index].classList[0]
        chooseAll = document.querySelector(`.${prnt} #check`)
        if(chooseAll.checked){
          
            
            document.querySelectorAll(`.${prnt} input[type = checkbox]`).forEach(each => {
                each.checked = true
            })
        }
        else{
            document.querySelectorAll(`.${prnt} input[type = checkbox]`).forEach(each => {
                each.checked = false
            })
            
        }
    }
    $(".up").click(function(){
        window.scrollTo(0, 0)
    })
    const list = ["ru", "kz"]
    const langAll = document.querySelectorAll(".langSpan")
    langAll.forEach((lang, index) => {
        lang.addEventListener('click', () => {
            
            if(index == 0){
                langAll[1].classList.remove('chosen')
            }
            else{
                langAll[0].classList.remove('chosen')
            }
            lang.classList.add('chosen')
            changeURLLang(index)
            changeLang()
        })
    });
    const changeURLLang = (index) => {
        let lang = list[index];
        location.href = window.location.pathname + '#' + lang;
    }
    const changeLang = () => {
        let hash = window.location.hash;
        hash = hash.substr(1);
        for (let key in langArr) {
            let elem = document.querySelector('.lng-' + key);
            if (elem) {
                if(elem.classList.contains('lng-placeholder')){
                    elem.setAttribute("placeholder", langArr[key][hash])
                }
                else
                {
                    elem.innerHTML = langArr[key][hash];
                }
            }
    
        }
    }
    var arrCheckbox = [
        [],
        [],
        []
    ]
    const checkObj = {
        "mainMyPostsContent": 0,
        "nonActivePosts": 1,
        "trashMyPostsContent": 2
    }
    const changeStat = (inputChecked) => {
        chooseAll = document.getElementById("check")
        if(!chooseAll.checked){
            var indexCheck = checkObj[inputChecked.parentNode.parentNode.parentNode.parentNode.classList[0] + ""]
           
            if(inputChecked.checked){
            ittrash++
            arrCheckbox[indexCheck].push(inputChecked)
            if(arrCheckbox[indexCheck].length == 5 && arrCheckbox[indexCheck].length != document.querySelectorAll('.myContent #check').length-1){
                arrCheckbox[indexCheck][0].checked = false
                arrCheckbox[indexCheck].shift()
             
            }
            }
            else{
                arrCheckbox[indexCheck] =  arrCheckbox[indexCheck].filter((item) =>item != inputChecked);
            }
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
    const myPosts = document.querySelectorAll(".allStatusOfPosts span")
    const paymentStatus = document.querySelectorAll(".catg")
    
    clickLick(myPosts)
    const allContent = document.querySelectorAll(".mainMyPostsContent .allMyContent")
    var allMyContent = document.querySelectorAll(".mainMyPostsContent .myContent")
    const nextMyButton = document.querySelectorAll('.bottomBut .myContentAngle .fa-angle-right')
    const prevMyButton = document.querySelectorAll('.myContentAngle .fa-angle-left')
    var target =document.querySelector(".mainMyPostsContent .chosenButton")
    var el = document.querySelectorAll(".mainMyPostsContent .newCreatedButton")
    var index = [...el].indexOf(target)
    
    const koefEnd = allContent.length%6
    
    
    
    //fill
    var isNotFull = false
    
    const pagesOfUsersContent = (count, pf) => {
        $(`.${pf} .allMyContent.visible`).removeClass('visible')
        document.querySelectorAll(`.${pf} .allMyContent`)[count].classList.add("visible")
    }
    const doubleLeft = document.querySelectorAll('.myContentAngle .fa-angles-left')
    const doubleRight = document.querySelectorAll('.myContentAngle .fa-angles-right')
    // if(allContent.length <= 6){
    //     doubleLeft.css("display", "none")
    //     doubleRight.css("display", "none")
    // }
    // else{
    //     doubleLeft.css("display", "unset")
    //     doubleRight.css("display", "unset")
    // }
    
    
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
        
    
    function myFunction(div) {
        //document.querySelector(`.show`).classList.remove("show");
        document.querySelector(`.${div} #myDropdown`).classList.toggle("show");
        
    }
    var np = false
    var basic = -1
    const showModal = () => {
        
        $('.shadow').css('display', 'flex')
    }
    const modal = (str, num) => {
        
        
        
        showModal()
        $('section').css('position', 'fixed')
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
                $('section').css('position', 'sticky')
              
              }
              if (!event.target.matches('.wholeList-btn')) {
                
                toggleId(listClassOb['wholeList-btn'])
              }
              
        }
      }
      var a = document.querySelectorAll('#myDropdown a')
    function insert(randA, ind){
        document.querySelectorAll('.sort')[ind].innerHTML = randA.innerHTML
    }
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
    function createButtonsForNewLine(){
        var koefLine = Math.ceil(document.querySelectorAll('.cloneSearch .myContent').length/4)
        var divEl = document.createElement('div')
        divEl.className = 'lineForNewButtons'
        document.querySelector('.mainMyPostsContent .searchButtonLine .previousMyContents').after(divEl)
        for(var k = 0; k <= koefLine; k++){
            var newButtonL = document.createElement('button')
            newButtonL.className = 'newCreatedButton'
            newButtonL.innerHTML = k+1
            divEl.append(newButtonL)
     
        }
    }
    var foundCount = 1
    let fInput = document.querySelector('.mainMyPostsContent .searchPartMy input')
    fInput.oninput = function(){
        
        let fInputValue = this.value.trim().toLowerCase()
        if(fInputValue != ''){
            document.querySelector('.mainMyPostsContent .searchButtonLine .lineForNewButtons').innerHTML = ''
            document.querySelector('.mainMyPostsContent .bottomBut').style.display = 'none'
            document.querySelector('.mainMyPostsContent .searchButtonLine').style.display = 'flex'
            // createButtonsForNewLine()
            document.querySelectorAll('.mainMyPostsContent .nameOfTheProduct').forEach(name => {
            
                if(name.innerText.toLowerCase().search(fInputValue) == -1){
                    name.parentNode.parentNode.parentNode.classList.add('hide')  
                }
                else{
                    name.parentNode.parentNode.parentNode.classList.remove('hide')
                }
               
            })
            if(document.querySelectorAll('.mainMyPostsContent .hide').length == document.querySelectorAll('.mainMyPostsContent .myContent').length){
                document.querySelector(`.mainMyPostsContent .imgThink`).classList.remove('close')
            }
            else{
                document.querySelector(`.mainMyPostsContent .imgThink`).classList.add('close')
            }
            foundCount = Math.ceil((document.querySelectorAll('.mainMyPostsContent .myContent:not(.hide)').length)/4)
            for(var ij = 1; ij <= foundCount; ij++){
                var btnSearch = document.createElement('button')
                btnSearch.className = 'newCreatedButton'
                btnSearch.innerHTML = ij
                if(ij == 1){
                    btnSearch.classList.add('chosenButton')
                }
                document.querySelector('.mainMyPostsContent .searchButtonLine .lineForNewButtons').append(btnSearch)
            }
            var moreBtn = 6  - foundCount%6
            for(var ij = 1; ij <= moreBtn; ij++){
                var btnSearch = document.createElement('button')
                btnSearch.className = 'ghostBtn'
               
                document.querySelector('.mainMyPostsContent .searchButtonLine .lineForNewButtons').append(btnSearch)
            }
        }
        else{
            document.querySelector('.mainMyPostsContent .bottomBut').style.display = 'flex'
            document.querySelector('.mainMyPostsContent .searchButtonLine').style.display = 'none'
            document.querySelectorAll('.mainMyPostsContent .nameOfTheProduct').forEach(name => {
            
                name.parentNode.parentNode.parentNode.classList.remove('hide')
            })
            document.querySelector(`.mainMyPostsContent .imgThink`).classList.add('close')
            document.querySelectorAll('.mainMyPostsContent .searchButtonLine button').forEach(each => {
                each.remove()
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
    function myFunction(div) {
        //document.querySelector(`.show`).classList.remove("show");
        document.querySelector(`.${div} #myDropdown`).classList.toggle("show");
        
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
      const replacement = (parentTrash) => {
       
        
        
        // var lastEl =  document.querySelectorAll(`.${parentTrash} .allMyContent`)[document.querySelectorAll(`.${parentTrash} .allMyContent`).length-1]
        // var lastBtn = document.querySelectorAll(`.${parentTrash} .newCreatedButton`)[document.querySelectorAll(`.${parentTrash} .newCreatedButton`).length-1]
        // if(lastEl.childElementCount == 0){
        //     lastEl.classList.remove('visible')
        //     $(`.${parentTrash} .chosenButton`).removeClass('chosenButton')
        //     lastBtn.remove()
        //      lastEl.remove()
        //      if(document.querySelector(`.${parentTrash} .allMyContent`)){
        //         document.querySelector(`.${parentTrash} .allMyContent`).classList.add('visible')
        //         document.querySelector(`.${parentTrash} .newCreatedButton`).classList.add('chosenButton')
        //         pagesOfUsersContent(0, parentTrash)
        //         $(`.${parentTrash} .lineForNewButtons`).scrollLeft(0)
        //      }
    
        // }
     }
    //  const trash = $(".mainMyPostsContent .absolutelyNotYou")
     const trashAll = document.querySelectorAll('.absolutelyNotYou')
    var ittrash = 0;
    console.log(trashAll);
    trashAll.forEach((trash, index) => {
        var parentTrash;
        trash.addEventListener(('click'), ()=>  {
            parentTrash = document.querySelectorAll('.findWithThat')[index].classList[0]
            // console.log(document.querySelectorAll('.findWithThat')[index].childElementCount);
            var allElem = document.querySelectorAll(`.${parentTrash} #check`)
                allMyContent = document.querySelectorAll(`.${parentTrash} .myContent`)
                for(var i = 1; i < allElem.length; i++){
                    if(allElem[i].checked){
                        // allMyContent[i-1].remove()
                    }
                }
                delAllGhosts()
                itLength = 1;
                addNewGhosts()
                reConsider()
                if(chooseAll.checked){
                
                    
                    document.querySelectorAll(`.${parentTrash} .myContent`).forEach(each => {
                        if(each.classList.contains('hide')){
                            console.log(1);
                        }
                        else{
                            each.remove()
                        }
                        // each.remove()
                    })
                    if(document.querySelectorAll(`.${parentTrash} .myContent:not(.hide)`).length == 0){
                        
                        document.querySelector(`.${parentTrash} #check`).checked = false
                        // document.querySelector(`.${document.querySelectorAll('.findWithThat')[index].classList[0]} .lineForNewButtons`).remove()
                        // // document.querySelectorAll(`.${parentTrash} .imgThink`).classList.remove('close')
                        // $(`.${parentTrash} .imgThink`).css('display', 'none')
                        document.querySelectorAll(`.parentTrash input[type = checkbox]`).forEach(each => {
                            each.checked = false
                        })
                        // document.querySelector('.mainMyPostsContent .searchPartMy input').value = ''
                        // document.querySelectorAll(`.${parentTrash} .myContent`).forEach(each => {
                        //     each.classList.remove('hide')
                        //     // each.remove()
                        // })
                    }
                    else{
                        alert()
                    }
                    
                }
                else{
                    replacement(parentTrash)
                }
            checkForThink(index)
        })
    })
    
    function delAllGhosts(){
        document.querySelectorAll('.mainMyPostsContent .ghost').forEach(each =>{
            each.remove()
        })
    }
    function addNewGhosts(){
        while((itLength*4 - document.querySelectorAll('.mainMyPostsContent .myContent').length) < 0 ){
            itLength++
        }
        for(var i = 0; i < itLength*4 - document.querySelectorAll('.mainMyPostsContent .myContent').length; i++){
            var ghost = document.createElement('div')
            ghost.className = 'ghost'
            document.querySelector('.mainMyPostsContent .allMyContent').append(ghost)
        }
    }
    var current
    function reConsider(){
        var nf = false
        current = +document.querySelector('.mainMyPostsContent .chosenButton').innerHTML
        document.querySelector('.mainMyPostsContent .lineForNewButtons').remove()
        let par = document.querySelector('.mainMyPostsContent .myContentAngle.previousMyContents')
        let newDiv = document.createElement('div')
        newDiv.className = 'lineForNewButtons activeLine'
        par.after(newDiv)
        for(var y = 0; y < itLength; y++){
            var btnNew = document.createElement('button')
            btnNew.classList = 'newCreatedButton'
            btnNew.innerHTML = y+1
            if(+btnNew.innerHTML == current){
                btnNew.classList.add('chosenButton')
                nf = false
            }
            else{
                nf = true
            }
            document.querySelector('.bottomBut .lineForNewButtons').append(btnNew)
        }
        if(nf && current >= 2){
            document.querySelectorAll('.bottomBut .lineForNewButtons button')[current-2].classList.add('chosenButton')
            nf = false
        }
    
    }
    
    function checkForThink(index){
        var el =document.querySelectorAll('.findWithThat')[index] 
        if(el.childElementCount != 4){
            
        }
        else{
            $(`.${el.classList[0]} .imgThink`).css('display', 'flex')
        }
    }
    var chooseCategory = document.querySelector('.chooseCategory div')
        chooseCategory.addEventListener('click', () => {
            document.querySelectorAll('.ul')[0].style.display = 'none'
            document.querySelector('.inputModal input').value = ''
            var needUl = document.querySelectorAll('.ul')[1]
            needUl.style.display = 'unset'
            $('section').css('position', 'fixed')
            showModal()
        })
    var isFirstLine = true
    var lineCount = Math.floor(document.querySelectorAll('.mainMyPostsContent .allMyContent').length/6)+1
    
    
    // checkForCount()
    
    var koef = 0
    var allLine, currentLine, indexLine
   
    nextMyButton.forEach(n => n.onclick = () => {
        
        var parentFind = n.parentElement.parentElement.parentElement.classList[0];
        var el = document.querySelectorAll(`.${parentFind} .newCreatedButton`)
        var target =document.querySelector(`.${parentFind} .chosenButton`)
        var index = [...el].indexOf(target)
        if(+el[index].innerHTML < itLength){
            $(`.${parentFind} .chosenButton`).removeClass('chosenButton')
            el[index+1].classList.add('chosenButton')
            $('.mainMyPostsContent .allMyContent').animate({
                scrollTop: '+=768'
            },1,'swing')
            if(+el[index].innerHTML%6 == 0 && index > 0){
                $(`.mainMyPostsContent .lineForNewButtons`).animate({
                scrollLeft: '+=340'
              }, 300, 'swing');
            }
        }
        else{
    
        }
    
    })
    prevMyButton.forEach(p => p.onclick = () => {
        var parentFind = p.parentElement.parentElement.parentElement.classList[0];
        var el = document.querySelectorAll(`.${parentFind} .newCreatedButton`)
        var target =document.querySelector(`.${parentFind} .chosenButton`)
        var index = [...el].indexOf(target)
        
        if(+el[index].innerHTML > 1){
            
            $(`.${parentFind} .chosenButton`).removeClass('chosenButton')
            el[index-1].classList.add('chosenButton')
            $('.mainMyPostsContent .allMyContent').animate({
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
    doubleLeft.forEach(dl => dl.onclick = () => {
        var parentFind = dl.parentElement.parentElement.parentElement.classList[0];
        $(`.${parentFind} .chosenButton`).removeClass('chosenButton')
        document.querySelectorAll(`.${parentFind} .newCreatedButton`)[0].classList.add('chosenButton')
        pagesOfUsersContent(0, parentFind)
        $(`.${parentFind} .lineForNewButtons`).scrollLeft(0)
    })
    doubleRight.forEach(dr => dr.onclick = () => {
        var parentFind = dr.parentElement.parentElement.parentElement.classList[0];
        $(`.${parentFind} .chosenButton`).removeClass('chosenButton')
        var koefSkip = Math.ceil(document.querySelectorAll(`.${parentFind} .newCreatedButton`).length/6)-1
        $(`.${parentFind} .lineForNewButtons`).scrollLeft(( (document.querySelector(`.${parentFind} .lineForNewButtons`).clientWidth -4)*koefSkip))
        document.querySelectorAll(`.${parentFind} .newCreatedButton`)[document.querySelectorAll(`.${parentFind} .newCreatedButton`).length-1].classList.add('chosenButton')
        pagesOfUsersContent(document.querySelectorAll(`.${parentFind} .allMyContent`).length - 1, parentFind)
    })
    
    var isFirstLine1 = true
        let par1 = document.querySelector('.nonActivePosts .myContentAngle.previousMyContents')
        let newDiv1 = document.createElement('div')
        newDiv1.className = 'lineForNewButtons activeLine'
        par1.after(newDiv1)
        for(var inner = 0; inner < document.querySelectorAll('.nonActivePosts .allMyContent').length; inner++){
            let newButton = document.createElement('button')
            newButton.className = 'newCreatedButton'
            if(isFirstLine1){
                newButton.classList.add('chosenButton')
                isFirstLine1 = false
            }
            newButton.innerHTML = inner+1
            document.querySelector('.nonActivePosts .lineForNewButtons').append(newButton)
        }
        var k = 6 - document.querySelectorAll('.nonActivePosts .newCreatedButton').length%6
        for(var ki = 0; ki < 6; ki++){
            let kiButton = document.createElement('button')
            kiButton.className = 'polter'
            document.querySelector('.nonActivePosts .lineForNewButtons').append(kiButton)
        }
    
    var isFirstLine2 = true
    let par2 = document.querySelector('.trashMyPostsContent .myContentAngle.previousMyContents')
        let newDiv2 = document.createElement('div')
        newDiv2.className = 'lineForNewButtons activeLine'
        par2.after(newDiv2)
        for(var inner = 0; inner < document.querySelectorAll('.trashMyPostsContent .allMyContent').length; inner++){
            let newButton = document.createElement('button')
            newButton.className = 'newCreatedButton'
            if(isFirstLine2){
                newButton.classList.add('chosenButton')
                isFirstLine2 = false
            }
            newButton.innerHTML = inner+1
            document.querySelector('.trashMyPostsContent .lineForNewButtons').append(newButton)
        }
        var k = 6 - document.querySelectorAll('.trashMyPostsContent .newCreatedButton').length%6
        for(var ki = 0; ki < 6; ki++){
            let kiButton = document.createElement('button')
            kiButton.className = 'polter'
            document.querySelector('.trashMyPostsContent .lineForNewButtons').append(kiButton)
        }
    var extitle = document.querySelectorAll('.mainMyPostsContent .nameOfTheProduct')
    var extitle1 = document.querySelectorAll('.nonActivePosts .nameOfTheProduct')
    var extitle2 = document.querySelectorAll('.trashMyPostsContent .nameOfTheProduct')
    // for(var j = 0; j < extitle.length; j++){
    //     extitle[j].innerHTML = '1_'+j
    // }
    for(var j = 0; j < extitle1.length; j++){
        extitle1[j].innerHTML = '2_'+j
    }
    
    for(var j = 0; j < extitle2.length; j++){
        extitle2[j].innerHTML = '3_'+j
    }
    
    var buttonCount = document.querySelectorAll('.mainMyPostsContent .myContent').length
    var itLength = 1
    while((itLength*4 - document.querySelectorAll('.mainMyPostsContent .myContent').length) < 0 ){
        itLength++
    }
    for(var i = 0; i < itLength*4 - document.querySelectorAll('.mainMyPostsContent .myContent').length; i++){
        var ghost = document.createElement('div')
        ghost.className = 'ghost'
        document.querySelector('.mainMyPostsContent .allMyContent').append(ghost)
    }
    let par = document.querySelector('.mainMyPostsContent .myContentAngle.previousMyContents')
    let newDiv = document.createElement('div')
    newDiv.className = 'lineForNewButtons activeLine'
    par.after(newDiv)
    for(var y = 0; y < itLength; y++){
        var btnNew = document.createElement('button')
        btnNew.classList = 'newCreatedButton'
        btnNew.innerHTML = y+1
        if(btnNew.innerHTML == '1'){
            btnNew.classList.add('chosenButton')
        }
        document.querySelector('.bottomBut .lineForNewButtons').append(btnNew)
}
var ghostBtn = 6 - itLength%6
for(var t = 0; t < ghostBtn; t++){
    var btnG = document.createElement('button')
    btnG.classList = 'ghostBtn'
    document.querySelector('.bottomBut .lineForNewButtons').append(btnG)
}
document.querySelector('.searchButtonLine .nextMyContents').addEventListener('click', () => {
    var yellow = document.querySelector('.searchButtonLine .lineForNewButtons .chosenButton')
    var el = document.querySelectorAll('.searchButtonLine .newCreatedButton')
    var index = [...el].indexOf(yellow)
    console.log(index, itLength);
    if(+el[index].innerHTML < el.length){
        $(`.searchButtonLine .chosenButton`).removeClass('chosenButton')
        el[index+1].classList.add('chosenButton')
        $('.mainMyPostsContent .allMyContent').animate({
            scrollTop: '+=768'
        },1,'swing')
    }
    else{

    }
})
document.querySelector('.searchButtonLine .previousMyContents').addEventListener('click', () => {
    var yellow = document.querySelector('.searchButtonLine .lineForNewButtons .chosenButton')
    var el = document.querySelectorAll('.searchButtonLine .newCreatedButton')
    var index = [...el].indexOf(yellow)
    console.log(index, itLength);
    if(+el[index].innerHTML > 1){
        $(`.searchButtonLine .chosenButton`).removeClass('chosenButton')
        el[index-1].classList.add('chosenButton')
        $('.mainMyPostsContent .allMyContent').animate({
            scrollTop: '-=768'
        },1,'swing')
    }
    else{

    }
})