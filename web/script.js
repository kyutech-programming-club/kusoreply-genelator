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

  $('#btnsend').on('click', function () {
    $('#result').text('通信中...');
    // Ajax通信を開始
    $.ajax({
      url: '',
      type: 'GET',
      // dataType: 'json',
      // フォーム要素の内容をハッシュ形式に変換
      // data: $('form').serializeArray(),
      timeout: 5000,
    })
      .done(function (data) {
        // 通信成功時の処理を記述
        alert('success!');
        // document.getElementById('js-copy-text').value = data;
        console.log(data);
      })
      .fail(function () {
        // 通信失敗時の処理を記述
        alert('failed');
      });
  })

  // var asyncSend = function () {
  //   $('#result').text('通信中...');
  //   // Ajax通信を開始
  //   $.ajax({
  //     url: 'https://kusoreply-generator.an.r.appspot.com',
  //     type: 'GET',
  //     dataType: 'json',
  //     // フォーム要素の内容をハッシュ形式に変換
  //     data: $('form').serializeArray(),
  //     timeout: 5000,
  //   })
  //     .done(function (data) {
  //       // 通信成功時の処理を記述
  //     })
  //     .fail(function () {
  //       // 通信失敗時の処理を記述
  //       alert('failed');
  //     });
  // }

});
