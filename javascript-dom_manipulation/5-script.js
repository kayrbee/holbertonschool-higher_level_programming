#!/usr/bin/node
const target = document.getElementById('update_header');

function updateHeaderText () {
  document.querySelector('header').innerHTML = 'New Header!!!';
}

target.addEventListener('click', updateHeaderText);
