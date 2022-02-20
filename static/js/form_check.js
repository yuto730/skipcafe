function CheckMail() {
  // 入力値取得
  var input1 = $("#mail01").val();
  var input2 = $("#mail02").val();
  // メールアドレス比較
  if (input1 !== input2) {
      window.alert("メールアドレスが一致しません。");
      return false;
  } else {
      return true;
  }
}

function CheckPassword() {
  // 入力値取得
  var input3 = $("#password01").val();
  var input4 = $("#password02").val();
  // パスワード比較
  if (input3 !== input4) {
      window.alert("パスワードが一致しません。");
      return false;
  } else {
      return true;
  }
}