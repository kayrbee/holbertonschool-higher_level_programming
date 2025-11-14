#!/usr/bin/node

async function getCharName () {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const character = await response.json();
    return (character.name);
  } catch (error) {
    console.error(error.message);
  }
}

// Version 2 solution
document.getElementById('character').innerHTML = await getCharName();

// Version 1 solution
// const char_name = await get_char_name();
// const character = document.getElementById('character');
// character.innerHTML = char_name;
