$(document).ready(() => {
  $('INPUT#btn_translate').click((event) => {
    const lang = $('INPUT#language_code').val();
    $.getJSON(`https://fourtonfish.com/hellosalut/?lang=${lang}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
