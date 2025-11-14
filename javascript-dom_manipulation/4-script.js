#!/usr/bin/node

const list = document.querySelector('.my_list');
const target = document.getElementById('add_item');

function addListItem () {
  const listItem = document.createElement('li');
  const node = document.createTextNode('Item');
  listItem.appendChild(node);
  list.appendChild(listItem);
}

target.addEventListener('click', addListItem);
