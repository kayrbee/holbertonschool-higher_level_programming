async function getMovies () {
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

async function main () {
  const movies = await getMovies();

  if (!movies) {
    return (0);
  }

  // const num_movies = movies['count'];
  const numMovies = movies.results.length;

  // Fetch the list element only once
  const list = document.getElementById('list_movies');

  // Loop over movie data to find each movie title & add to a li element
  for (let i = 0; i < numMovies; i++) {
    const movie = movies.results[i];
    const movieTitle = movie.title;

    const listItem = document.createElement('li');
    const node = document.createTextNode(movieTitle);
    listItem.appendChild(node);

    list.appendChild(listItem);
  }
}

main();
