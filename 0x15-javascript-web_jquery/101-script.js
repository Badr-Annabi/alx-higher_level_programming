document.addEventListener('DOMContentLoaded', () => {
  $('#add_item').on('click', () => {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('#remove_item').on('click', () => {
    $('ul.my_list li:last-child').remove();
  });
  $('#clear_list').on('click', () => {
    $('ul.my_list').empty();
  });
});
