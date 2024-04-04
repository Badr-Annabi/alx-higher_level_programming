$('document').ready(() => {
  $('INPUT#btn_translate').click(() => {
    translate();
  });
  $('INPUT#language_code').keypress((event) => {
    if (event.which === 13) {
      translate();
    }
  });
  function translate () {
    const url = 'https://hellosalut.stefanbohacek.dev/?';
    $.get(url + $.param({ lang: $('INPUT#language_code').val() }), (data) => {
      $('DIV#hello').html(data.hello);
    });
  }
});
