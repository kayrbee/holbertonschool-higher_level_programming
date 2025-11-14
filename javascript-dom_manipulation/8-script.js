#!/usr/bin/node

async function getTranslation () {
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const translation = await response.json();
    return (translation);
  } catch (error) {
    console.error(error.message);
  }
}

const translation = await getTranslation();
const hello = document.getElementById('hello');
hello.innerHTML = translation.hello;
