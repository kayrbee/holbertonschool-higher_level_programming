#!/usr/bin/node
const list_item = document.createElement("li");
const node = document.createTextNode("Item")
list_item.appendChild(node);

const list = document.querySelector('.my_list')
const target = document.getElementById('add_item');

function addListItem() {
    list.appendChild(list_item)
}

target.addEventListener("click", addListItem);
