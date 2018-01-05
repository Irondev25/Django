var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var headThree = document.querySelector("#three");

headOne.addEventListener("mouseover",function(){
  headOne.textContent = "Mouse currently over me!!!";
  headOne.style.color = 'red';
})

headOne.addEventListener("mouseout",function(){
  headOne.textContent = "Mouse Not On Me!!";
  headOne.style.color = 'blue';
})

headTwo.addEventListener("click", function(){
  headTwo.textContent = "Clicked on";
  headTwo.style.color = 'blue';
})

headThree.addEventListener("dblclick",function(){
  headThree.textContent = "Double Clicked!";
  headThree.style.color = 'red';
})
