#!/usr/bin/node

async function get_movies() {
    try {
        const response = await fetch('https://swapi-api.hbtn.io/api/films/?format=json');
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const movies = await response.json();
        return (movies);
    } catch (error) {
        console.error(error.message);
    }
}

const movies = await get_movies();
const num_movies = movies['count'];


// Fetch the list element only once
const list = document.getElementById('list_movies');

// Loop over movie data to find each movie title & add to a li element
for (i = 0; i < num_movies; i++) {
    let movie = movies['results'][i];
    let movie_title = movie['title'];

    const list_item = document.createElement('li');
    const node = document.createTextNode(movie_title);
    list_item.appendChild(node);

    list.appendChild(list_item);
}
