// A script that fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', data => {
  $.each(data.results, (i, film) => {
    $('UL#list_movies').append(`<li>${film.title}</li>`);
  });
});
