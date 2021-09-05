$(function () {
  /*------------------ コピー ------------------*/
  $('#negaposi-copy').on('click', function () {
    var text = document.getElementById('negaposi-reply').value;
    navigator.clipboard.writeText(text);
  });
  $('#combi-copy').on('click', function () {
    var text = document.getElementById('combi-reply').value;
    navigator.clipboard.writeText(text);
  });
  $('#deny-copy').on('click', function () {
    var text = document.getElementById('deny-reply').value;
    navigator.clipboard.writeText(text);
  });

  /*------------------ ajax ------------------*/
  $('#btnsend').on('click', function () {
    var data = document.getElementById('input').value;
    // $('#result').text('通信中...');
    $('#modal-wrapper').show();
    // Ajax通信を開始
    $.ajax({
      url: 'https://kusoreply-generator.an.r.appspot.com',
      type: 'POST',
      contentType: 'application/json; charset=UTF-8',
      data: JSON.stringify({ input: data }),
      timeout: 5000,
    })
      .done(function (data) {
        // 通信成功時の処理を記述
        $('#modal-wrapper').hide();
        document.getElementById('js-copy-text').value = data;
      })
      .fail(function () {
        // 通信失敗時の処理を記述
        $('#modal-wrapper').hide();
        alert('failed');
      });
  })
});
