
window.onload = () => {
    let inputSearch = document.querySelector('.searchPart input')
    
    inputSearch.oninput = function(){
        let value = this.value.trim().toLowerCase()
        console.log(value);
        let list = document.querySelectorAll('.favouriteSection .contentBox .titleContent')
        if(value){
            list.forEach(name => {
            console.log(name.innerText.toLowerCase().search(value));
                if(name.innerText.toLowerCase().search(value) == -1){
                    name.parentNode.classList.add('hide')  
                }
                else{
                    name.parentNode.classList.remove('hide')
                }
               
            })
        }
        
        else{
            list.forEach(name => {
            
                name.parentNode.classList.remove('hide')
            })
        }
        
        // value
        //     ?list.forEach(elem => {
        //         console.log(elem.innerText);
        //         elem.innerText.toLowerCase().search(value) == -1
        //             ?elem.classList.add('hide')
        //             :
        //                 elem.classList.remove('hide');
                
        //     })
        //     : list.forEach(elem => {
        //         elem.classList.remove('hide')
        //     })


    }
    
    
}
