$(function () {
  /*------------------ ajax ------------------*/


  /*------------------ コピー ------------------*/
  $('#js-copy').on('click', function () {
    $('#js-copy-text').select();
    document.execCommand('copy');//非推奨
  });
});
