#!/usr/bin/node
const header = document.querySelector('header');
const target = document.getElementById('red_header');

// const click = target.addEventListener(MouseEvent("click"));
const click = target.addEventListener("click", changeColor);

function changeColor() {
    header.style.color = '#FF0000';
}