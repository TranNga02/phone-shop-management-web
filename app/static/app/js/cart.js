var updateBtns = document.getElementsByClassName("update-cart");
// vòng lặp qua từng phaanft tử , với mỗi nút click sẽ thực hiện hàm xử lý
for (i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    // lấy các giá trị dữ liệu từ phần tử dc nhấp vào
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log("productId", productId, "action", action);
    console.log("user", user);
    if (user === "AnonymousUser") {
      console.log("user not loggin");
    } else {
      updateUserOrder(productId, action);
    }
  });
}
function updateUserOrder(productId, action) {
  console.log("user logged in");
  var url = "/update_item/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data", data);
      location.reload();
    });
}
