'use strict';

// JAVASCRIPT FOR CALENDAR

// calendar.html

document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');

$.get("api/calendar", (res) => {

  console.log(res);
  const calendar = new FullCalendar.Calendar(calendarEl, res);

  calendar.render();
  });
  
});