'use strict';

// JAVASCRIPT FOR TEMPLATE FILES

// category_events.html


// 1st approach
// const event_id = $().value()?

// 2nd approach

const eventResults = document.querySelector('#event_results');

$('#category').on('submit', (evt) => {
    evt.preventDefault();

    const data = {
        'types' : $('#types').val()
//  Key values thr form
    };
    $.post("/api/category", data, (res) => {
        const eventCategories = [];
        console.log(res);
        // for (const category of res.results) { 
        //     eventCategories.push(category.name);
        // }
        // $("#category").append(eventCategories.join(", "));
    });
});

// const formValues = $("#category").serialize();

// $.post("/category/event/" + event_id, formValues, resultHandler);
// });
