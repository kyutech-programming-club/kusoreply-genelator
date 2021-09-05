$(function () {
  /*------------------ コピー ------------------*/
  $('#negaposi-copy').on('click', function () {
    var text = document.getElementById('negaposi-reply').value;
    navigator.clipboard.writeText(text);
  });
  $('#comb-copy').on('click', function () {
    var text = document.getElementById('comb-reply').value;
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
        // console.dir(data);
        document.getElementById('negaposi-reply').value = data["negaposi"];
        document.getElementById('comb-reply').value = data["comb"];
        document.getElementById('deny-reply').value = data["deny"];
      })
      .fail(function () {
        // 通信失敗時の処理を記述
        $('#modal-wrapper').hide();
        alert('failed');
      });
  })
});
