// A script that fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', data => {
  $('DIV#character').text(data.name);
});
