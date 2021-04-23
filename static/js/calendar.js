'use strict';

// JAVASCRIPT FOR CALENDAR

// calendar.html

document.addEventListener('DOMContentLoaded', function() {
  const calendarEl = document.getElementById('calendar');
// make ajax request to pass to events key of unamed obj
// save variable (eventsFromDatabase)

$.post("/api/calendar", Data, (res) => {
  const eventsFromDatabase = [];
  // console.log("**************")
  // console.log(res);
  for (const event of res) { 
      eventsFromDatabase.push(event.event_name, event.event_date, event.event_start_time);
  } 
  // $("#calendar").html(eventsFromDatabase.join(" "))
});

  const calendar = new FullCalendar.Calendar(calendarEl, {
    initialView: 'dayGridMonth',
    initialDate: '2021-04-07',
    headerToolbar: {
      left: 'prev,next today',
      center: 'title',
      right: 'dayGridMonth,timeGridWeek,timeGridDay'
    },
    events: [
      {
        title: 'All Day Event',
        start: '2021-04-01'
      },
      {
        title: 'Long Event',
        start: '2021-04-07',
        end: '2021-04-10'
      },
      {
        title: 'Conference',
        start: '2021-04-11',
        end: '2021-04-13'
      },
      {
        title: 'Meeting',
        start: '2021-04-12T10:30:00',
        end: '2021-04-12T12:30:00'
      },
      {
        title: 'Lunch',
        start: '2021-04-12T12:00:00'
      },
      {
        title: 'Meeting',
        start: '2021-04-12T14:30:00'
      },
      {
        title: 'Birthday Party',
        start: '2021-04-13T07:00:00'
      },
      {
        title: 'Click for Google',
        url: 'http://google.com/',
        start: '2021-04-28'
      }
    ]
  });

  calendar.render();
});