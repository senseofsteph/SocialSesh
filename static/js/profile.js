'use strict';


// JAVASCRIPT FOR TEMPLATE FILES


// profile.html

// document.querySelector('#logout-button').addEventListener('click', (evt) => {
//   const loginBtn = evt.target;
//   console.log(evt.target);

//   if (loginBtn.innerHTML === 'Log Out') {
//     loginBtn.innerHTML = 'Log In';
//   } else {
//     loginBtn.innerHTML = 'Log Out';
//   }
// }); 


// form.html

$(document).ready(function($) {
        
  $("#register-form").validate({
          rules: {
              name: "required",                    
              password: {
                  required: true,
                  minlength: 6
              },
             city: "required",
            gender: "required"
           
          },
          messages: {
              fname: "Please enter your first name",
              lname: "Please enter your last name",
              email: "Please enter a valid email",                   
              password: {
                  required: "Please provide a password",
                  minlength: "Your password must be at least 6 characters long"
              },
            gender: "This field is required"
          },
           errorPlacement: function(error, element) 
  {
      if ( element.is(":radio") ) 
      {
          error.appendTo( element.parents('.form-group') );
      }
      else 
      { // This is the default behavior 
          error.insertAfter( element );
      }
   },
          submitHandler: function(form) {
              form.submit();
          }
          
      });
});

// $(function(){
//   $("#createprofile").validate({
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