document.addEventListener('DOMContentLoaded',function(){
/* 처음 head tag를 읽고나서, 변수가 없어지거나 오류가 생기는 것을 방지하기 위해서 DOMContentLoaded로 먼저 읽어들이게 시킴.*/
var $slideWrap = document.querySelector('.container'),
    $slideContainer = document.querySelector('.slider-container'),
    $slide = document.querySelectorAll('.slide'),
    /*배열로 들어와있어서 index로 접근이 가능하다.*/
    $navPrev = document.getElementById('prev'),
    $navNext = document.getElementById('next'),
    $slideHeight= 600,
    $slideCount = $slide.length,
    $timer = undefined,//이름은 있으나 아직 정의된 것이 없음
    $pagerHTML='',
    $pager=document.querySelector('.pager'), 
    $currentIndex =0;
    //현재 어떤 Index위치의 슬라이드를 보고있는지.
    /*변수를 지정해놓음 JavaScript는 이렇게 class나 id를 가져와 변수로 지정할 수 있음.*/
    /*for(var i=0; i<$slideCount; i++){
        if($slideHeight <$slide[i].offsetHeight){
            $slideHeight = $slide[i].offsetHeight;
        }
    }*/
    /*$slideHeight로 가장 큰 높이를 지정시키고 이것을 부모의 높이로 지정한다.*/

    $slideWrap.style.height= $slideHeight+'px';
    $slideContainer.style.height= $slideHeight+'px';

    for(var a = 0; a < $slideCount; a++){
        $slide[a].style.left = a*100 + "%";
        $pagerHTML += '<span data-ind="' + a + '">' + (a+1)+ '</span>';
        $pager.innerHTML = $pagerHTML;    
    }
    $pagerBtn = document.querySelectorAll('.pager span');
    //가로로 슬라이드들을 옆으로 나열하기

    function goToSlide(idx){
        $slideContainer.classList.add('animated');
        $slideContainer.style.left= -100 * idx+'%';
        //animated 클래스가 걸렸을 때 만 transition이 걸리게 해놨기 때문에 이렇게 classlist를 추가해줘야함.
        $currentIndex = idx;
        for(var y =0 ; y< $pagerBtn.length; y++){
            $pagerBtn[y].classList.remove('active');
        }
        $pagerBtn[idx].classList.add('active');
    }
    goToSlide(0);

    $navPrev.addEventListener('click',function(){
         if($currentIndex==0){
            goToSlide($slideCount-1);
        }
        else{
            goToSlide($currentIndex-1);
        }
    });
    $navNext.addEventListener('click',function(){
        if($currentIndex==$slideCount-1){
            goToSlide(0);
        }
        else{
            goToSlide($currentIndex+1);
        }
    });
    //nav이 대상자에게 Event가 일어나는지 확인.
    //transition은 언제걸리게 해놨는가? : animate클래스가 걸렸을때만 지정해 놨음
    //4초마다 goToSlide 함수에다가 숫자를 넘겨주면 되겠다~
    //javascript는 시간을 주는 요소가 2가지가 있다고한다.
    //setInterval(일,시간);
    function startAutoSlide(){
        $timer = setInterval(function(){
            var nextInd = ($currentIndex + 1)% $slideCount;
            goToSlide(nextInd);
        },2500);
    }
    startAutoSlide();
    $slideWrap.addEventListener('mouseenter',function(){
        clearInterval($timer);
    });
    $slideWrap.addEventListener('mouseleave',function(){
        startAutoSlide();
    });
    //페이저
    for(var x =0;x< $pagerBtn.length; x++){
        $pagerBtn[x].addEventListener('click',function(event){
            var pagerNum = event.target.getAttribute('data-ind');
            goToSlide(pagerNum);
        });
    }
});