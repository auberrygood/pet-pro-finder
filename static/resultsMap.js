app.receptor.hook(operation, callback, priority)

function initMap() {
    const professionals = document.querySelector("#mapResults").getAttribute("data-professionals");
    
    console.log(professionals); //js is registering this variable as a long string rather than list of objects
    console.log("")

    for (const professional of professionals){
        console.log(professional); //therefore console prints each individual character during this line....
    };

    
    // Map options
    const options = {
        zoom:12,
        center: {lat : 37.8046083, lng : -122.2607596}
    };

    // New map
    const map = new google.maps.Map(document.getElementById('map'), options);

//     //Add marker
//     const marker = new google.maps.Marker({
//         position:{lat : businessLat, lng : businessLng},
//         map:map,
//         icon: {
//             url: 'https://i2.wp.com/catgirlonlineshop.com/wp-content/uploads/2019/12/cropped-depositphotos_263556590-stock-illustration-dog-paw-icon-vector-footprint.png?ssl=1', 
//             scaledSize: new google.maps.Size(40, 40)
//         },
//     });

//     //define infoWindow instance
//     const infoWindow = new google.maps.InfoWindow();

//     //content of the marker's infoWindow
//     const businessContent = professionalName

//     //show infoWindow when marker is clicked
//     marker.addListener('click', () => {
//         infoWindow.close();
//         infoWindow.setContent(businessContent)
//         infoWindow.open(map, marker);
//     });
}
