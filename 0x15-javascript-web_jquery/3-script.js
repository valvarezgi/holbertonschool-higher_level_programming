const $ = window.$;
$(() => {
  $('#red_header').click(() => {
    $('header').addClass('red');
  });
});
