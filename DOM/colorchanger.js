header = document.querySelector("h1");

function getRandomColor() {
  var letters = "0123456789ABCDEF";
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random()*16)]
  }
  return color;
}


function changeHeaderColor() {
  coloInput = getRandomColor()
  header.style.color = coloInput;
}


setInterval("changeHeaderColor()",500);
