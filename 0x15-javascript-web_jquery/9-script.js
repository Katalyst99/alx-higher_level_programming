// A script that fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello from that fetch in the HTML tag DIV#hello.
$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', data => {
  $('DIV#hello').text(data.hello);
});
