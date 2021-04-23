'use strict';

// JAVASCRIPT FOR TEMPLATE FILES

// category_events.html

const eventResults = document.querySelector("#event_results");

$("#category").on("submit", (evt) => {
    evt.preventDefault();
    //  Key and value saved in formData
    const formData = {
        "types" : $("#types").val()
    };

    $.post("/api/category", formData, (res) => {
        const eventCategories = [];
        // console.log("**************")
        // console.log(res);
        for (const event of res) { 
            eventCategories.push("<li><a href=/events/"+ event.event_id +">" + event.event_name +"</a></li>");
        } 
        $("#event_results").html(eventCategories.join(" "))
    });
});



