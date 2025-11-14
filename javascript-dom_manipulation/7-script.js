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

for (i = 0; i < num_movies; i++) {
    movie = movies['results'][i];
    movie_title = movie['title'];
    console.log(movie_title);
}
