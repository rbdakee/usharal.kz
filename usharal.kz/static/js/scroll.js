$(function() {
  
  function moveLeft() {
    $('.slider').animate({
      scrollLeft: '-=520'
    }, 300, 'swing');
  }
  
  function moveRight() {
    $('.slider').animate({
      scrollLeft: '+=520'
    }, 300, 'swing');
  }
  
  
  $(".next").on("click",function(){
    
    moveRight();
  });
  
  $(".prev").on("click",function(){
    moveLeft();
  });
  
  
});
$(function() {
  
  function moveLeft1() {
    $('.sliderCon').animate({
      scrollLeft: '-=400'
    }, 300, 'swing');
  }
  
  function moveRight1() {
    $('.sliderCon').animate({
      scrollLeft: '+=400'
    }, 300, 'swing');
  }
  
  
  $(".next1").on("click",function(){
    moveRight1();
  });
  
  $(".prev1").on("click",function(){
    moveLeft1();
  });
  
  
});

