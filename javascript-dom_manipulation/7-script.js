const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const movieList = document.querySelector('#list_movies');

fetch(url)
  .then(response => response.json())
  .then(data => {
    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      movieList.appendChild(listItem);
    });
  })
  .catch(error => console.error('Error fetching movies:', error));