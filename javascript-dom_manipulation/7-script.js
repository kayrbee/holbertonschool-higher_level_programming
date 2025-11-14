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
movies = await get_movies();
num_movies = movies['count'];
movie_titles = [];

// Create an array of titles
for (i = 0; i < num_movies; i++) {
    movie = movies['results'][i];
    movie_title = movie['title'];
    movie_titles.push(movie_title);
}

// Create new li element for first movie
const list_item = document.createElement('li');
const node = document.createTextNode(movie_titles[0]);
list_item.appendChild(node);

// Find the list element
const list = document.getElementById('list_movies');

// Add movie title to list
list.appendChild(list_item);

// function addMovieTitle() {

// }