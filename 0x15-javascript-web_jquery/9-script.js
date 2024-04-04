$(() => {
  const $hello = $('DIV#hello');
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: (value) => {
      $hello.append(value.hello);
    }
  });
});
