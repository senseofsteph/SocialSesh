'use strict';

// Profile html file

// FIRST
// const profileForm = document.querySelector("#createprofile");

// profileForm.addEventListener("submit", (evt) => {
//   const password = document.querySelector("input[name='password']");

//   if (password.value.length < 7) {
//     evt.preventDefault()
//     alert("make me longer!")
//   }

// })


// SECOND
// $(function(){
//   $("form[id='createprofile']").validate({
//     rules: {
//       fname: "required",
//       lname: "required",
//       email: {
//         required: true,
//         email: true
//       },
//       password: {
//         required: true,
//         minlength: 7
//       },
//       phone: {
//         required: true,
//         minlength: 10
//       }
//     },
//     messages: {
//       fname: "Please enter your firstname",
//       lname: "Please enter your lastname",
//       password: {
//         required: "Please provide a password",
//         minlength: "Your password must be at least 7 characters long"
//       },
//       email: "Please enter a valid email address" 
//     },
//       phone: {
//         required: "Please provide your phone number",
//         minlength: "Your phone number must be 10 digits long"
//       },
//   submitHandler: function(form) {
//     form.submit();
//   }
//  });
// });