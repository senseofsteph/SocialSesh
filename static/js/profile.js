'use strict';

// JAVASCRIPT FOR TEMPLATE FILES

// category_events.html


// 1st approach
// const event_id = $().value()?

// 2nd approach
$('#category').on('submit', (evt) => {
    evt.preventDefault();

    const data = {
        types : $('#types').value()
//  Key values thr form
    };
    $.post("/api/category", data, (res) => {
        const eventCategories = [];
        for (const category of res.results) { 
            eventCategories.push(category.name);
        }
        $("#category").append(eventCategories.join(", "));
    });
});

// const formValues = $("#category").serialize();

// $.post("/category/event/" + event_id, formValues, resultHandler);
// });
