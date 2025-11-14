#!/usr/bin/node
const header = document.querySelector('header');
const target = document.getElementById('toggle_header');

function updateClassValue () {
  if (header.getAttribute('class') === 'red') {
    header.setAttribute('class', 'green');
  } else {
    header.setAttribute('class', 'red');
  }
}

target.addEventListener('click', updateClassValue);
