"use strict";

function initMap() {
    // takes json string and turns back into JS object
    const professionals = JSON.parse(document.querySelector("#mapResults").getAttribute("data-professionals"));
    
    console.log(professionals);
    console.log("")

    for (const professional of professionals){
        console.log(professional);
    };

    
    // Map options
    const options = {
        zoom:12,
        center: {lat : 37.8046083, lng : -122.2607596}
    };

    // New map
    const map = new google.maps.Map(document.getElementById('map'), options);
    
    //for each business
    for (const professional of professionals){
        //Add marker
        const marker = new google.maps.Marker({
            position:{lat : professional.coordinates.latitude, lng : professional.coordinates.longitude},
            map:map,
            icon: {
                url: 'https://i2.wp.com/catgirlonlineshop.com/wp-content/uploads/2019/12/cropped-depositphotos_263556590-stock-illustration-dog-paw-icon-vector-footprint.png?ssl=1', 
                scaledSize: new google.maps.Size(25, 25)
            },
        })
        //define infoWindow instance
        const infoWindow = new google.maps.InfoWindow();
        //content of the marker's infoWindow
        const businessContent = professional.name;
        //show infoWindow when marker is clicked
        marker.addListener('click', () => {
            infoWindow.close();
            infoWindow.setContent(businessContent)
            infoWindow.open(map, marker);
        });
    };
}
