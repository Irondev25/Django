var button = document.querySelectorAll("td");
var resetButton = document.querySelector(".btn")

button[0].addEventListener('click', function(){ button[0].textContent = "X" });
button[0].addEventListener('contextmenu', function(){ button[0].textContent = "O" });

button[1].addEventListener('click', function(){ button[1].textContent = "X" });
button[1].addEventListener('dblclick', function(){ button[1].textContent = "O" });

button[2].addEventListener('click', function(){ button[2].textContent = "X" });
button[2].addEventListener('dblclick', function(){ button[2].textContent = "O" });

button[3].addEventListener('click', function(){ button[3].textContent = "X" });
button[3].addEventListener('dblclick', function(){ button[3].textContent = "O" });

button[4].addEventListener('click', function(){ button[4].textContent = "X" });
button[4].addEventListener('dblclick', function(){ button[4].textContent = "O" });

button[5].addEventListener('click', function(){ button[5].textContent = "X" });
button[5].addEventListener('dblclick', function(){ button[5].textContent = "O" });

button[6].addEventListener('click', function(){ button[6].textContent = "X" });
button[6].addEventListener('dblclick', function(){ button[6].textContent = "O" });

button[7].addEventListener('click', function(){ button[7].textContent = "X" });
button[7].addEventListener('dblclick', function(){ button[7].textContent = "O" });

button[8].addEventListener('click', function(){ button[8].textContent = "X" });
button[8].addEventListener('dblclick', function(){ button[8].textContent = "O" });


resetButton.addEventListener('click',function(){
  button[0].textContent = " ";
  button[1].textContent = " ";
  button[2].textContent = " ";
  button[3].textContent = " ";
  button[4].textContent = " ";
  button[5].textContent = " ";
  button[6].textContent = " ";
  button[7].textContent = " ";
  button[8].textContent = " ";
})
