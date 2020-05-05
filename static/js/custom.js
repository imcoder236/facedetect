// function filter1() {
//   var x = document.getElementById("area1").value;
//   alert(x)
//   var url = '/filter1?area111='+x;
//   var req = new XMLHttpRequest();
//     req.onreadystatechange = function(){
//       if(this.readyState == 4 && this.status == 200){
//         alert(req.responseText)
//       }
//     };
//     req.open("GET",url,true);
//     req.send();
// }
// var restURL="http://127.0.0.1:8000/face_app/track/";
//
// $('#area1').click(function(e){
//    e.preventDefault();
//    var nick_name = $(this).val();
//       $.ajax({
//     type: 'GET',
//     url: restURL,
//     data: {"nick_name": nick_name},
//                 success: function (response) {
//                   alert(nick_name);
// });
// $("#area1").onchange(function (e) {
//         e.preventDefault();
//         // get the nickname
//         var nick_name = $(this).val();
//         // GET AJAX request
//         $.ajax({
//             type: 'GET',
//             url: "{% url 'filter1' %}",
//             data: {"nick_name": nick_name},
//             success: function (response) {
//               alert(nick_name);
//         })
//     })
