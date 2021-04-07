'use strict';

// Profile html file

$(function(){
  $("form[name='createprofile']").validate({
    rules: {
      fname: "required",
      lname: "required",
      email: {
        required: true,
        email: true
      },
      password: {
      required: true,
      minlength: 7
      }
      phone: 
    },
    messages: {
      fname: "Please enter your firstname",
      lname: "Please enter your lastname",
      password: {
        required: "Please provide a password",
        minlength: "Your password must be at least 7 characters long"
      },
      email: "Please enter a valid email address"
    },
  submitHandler: function(form) {
    form.submit();
  }
 });
});