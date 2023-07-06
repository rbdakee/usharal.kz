
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