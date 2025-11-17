const header = document.querySelector('header');
const target = document.getElementById('red_header');

function changeColor () {
  header.style.color = '#FF0000';
}

target.addEventListener('click', changeColor);

// Alternative approach
// - inline anonymous function
// Produces equivalent behaviour to original implementation
// Good for cases where the handler is short and won't be reused
// target.addEventListener("click", () => { header.style.color = '#FF0000'; });
