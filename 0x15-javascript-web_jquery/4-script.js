const $ = window.$;
$(() => {
  $('#toggle_header').click(() => {
    $('header').toggleClass('red green');
  });
});
