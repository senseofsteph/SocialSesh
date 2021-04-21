'use strict';

// JAVASCRIPT FOR TEMPLATE FILES

// category_events.html


// 1st approach
// const event_id = $().value()?

// 2nd approach

const eventResults = document.querySelector("#event_results");

$("#category").on("submit", (evt) => {
    evt.preventDefault();

    const formData = {
        "types" : $("#types").val()
//  Key values the form
    };

    $.post("/api/category", formData, (res) => {
        const eventCategories = [];
        console.log("**************")
        console.log(typeof res);
        for (const category of res.results) { 
            eventCategories.push(category.name);
        } 

        // for (const category of Object.keys(eventResults)) {
        // }

        $("#category").append(eventCategories.join(", "));
    });
});

// const formValues = $("#category").serialize();

// $.post("/category/event/" + event_id, formValues, resultHandler);
// });
