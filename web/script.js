$(function () {
  /*------------------ ajax ------------------*/


  /*------------------ コピー ------------------*/
  $('#js-copy').on('click', function () {
    var text = document.getElementById('js-copy-text').value;
    navigator.clipboard.writeText(text);
    // navigator.clipboard.writeText(text).then(function () {
    //   /* clipboard successfully set */
    //   alert('おめでとう！成功したよ！！！');
    // }, function () {
    //   /* clipboard write failed */
    //   alert('failed');
    // });
  });

});
