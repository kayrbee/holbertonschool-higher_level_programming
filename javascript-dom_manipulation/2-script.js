const header = document.querySelector('header');
const target = document.getElementById('red_header');

function addClass() {
    header.setAttribute("class", "red");
}

target.addEventListener("click", addClass);
