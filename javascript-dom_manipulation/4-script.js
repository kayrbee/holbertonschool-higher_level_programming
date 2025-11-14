#!/usr/bin/node

const list = document.querySelector('.my_list')
const target = document.getElementById('add_item');

function addListItem() {
    const list_item = document.createElement("li");
    const node = document.createTextNode("Item")
    list_item.appendChild(node);
    list.appendChild(list_item)
}

target.addEventListener("click", addListItem);
