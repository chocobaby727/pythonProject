const currentUrl = location.href;
const validUserUrl = currentUrl + "validate_user_name_ajax/";
const validEmailUrl = currentUrl + "validate_email_ajax/";

console.log(validUserUrl);
console.log(validEmailUrl);

// 名前バリデーション
$("input[name='username']").change(function () {
  const that = this;
  $.ajax({
    type: "get",
    url: validUserUrl,
    // url: "{% url 'accounts:validate_user_name_ajax' %}",
    dataType: "json",
    data: {
      username: $(this).val(),
    },
  })
    .done(function (data) {
      if (!data.success) {
        $(that).addClass("is-invalid");
        $(that).after(
          "<div class='invalid-feedback' style='display: block'>" +
            data.message +
            "</div>"
        );
      } else {
        $(that).removeClass("is-invalid");
        $(that)
          .next()
          .remove(":contains(" + data.message + ")");
      }
    })
    .fail(function (data) {
      alert("通信失敗");
    });
});

// メールアドレスバリデーション
$("input[name='email']").change(function () {
  const that = this;
  $.ajax({
    type: "get",
    url: validEmailUrl,
    // url: "{% url 'accounts:validate_email_ajax' %}",
    dataType: "json",
    data: {
      email: $(this).val(),
    },
  })
    .done(function (data) {
      if (!data.success) {
        $(that).addClass("is-invalid");
        $(that).after(
          "<div class='invalid-feedback' style='display: block'>" +
            data.message +
            "</div>"
        );
      } else {
        $(that).removeClass("is-invalid");
        $(that)
          .next()
          .remove(":contains(" + data.message + ")");
      }
    })
    .fail(function (data) {
      alert("通信失敗");
    });
});
