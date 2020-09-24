const $ = window.$;
$(() => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', data => {
    $('DIV#hello').html(data.hello);
  });
});
