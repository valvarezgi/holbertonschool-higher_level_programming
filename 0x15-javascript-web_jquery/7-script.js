const $ = window.$;
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (data, status) => {
  if (status === 'success') {
    $('#character').text(data.name);
  }
});
