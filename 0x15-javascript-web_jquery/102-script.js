$('document').ready(() => {
  const url = 'https://hellosalut.stefanbohacek.dev/?';
  $('INPUT#btn_translate').click(() => {
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), (data) => {
      $('DIV#hello').html(data.hello);
    });
  });
});
