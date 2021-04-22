'use strict';

// JAVASCRIPT FOR TEMPLATE FILES

// category_events.html

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
        console.log(res);
        for (const event of res) { 
            eventCategories.push(event.event_name);
        } 
        $("#event_results").append(eventCategories.join(", "));
    });
});

// line 20 and 24 for changes with displaying info 



