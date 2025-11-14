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

// Loop over array of movie titles to add each movie to a li element
for (i = 0; i < num_movies; i++) {
    const list_item = document.createElement('li');
    const node = document.createTextNode(movie_titles[i]);
    list_item.appendChild(node);

    const list = document.getElementById('list_movies');
    list.appendChild(list_item);
}
