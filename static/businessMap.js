function initMap() {
    const professionalName = document.querySelector("#mapInfo").getAttribute("data-professional-name")
    const businessLat = Number(document.querySelector("#mapInfo").getAttribute("data-business-lat"))
    const businessLng = Number(document.querySelector("#mapInfo").getAttribute("data-business-lng"))
    
    console.log(professionalName)
    console.log("latlng", businessLat, businessLng)
    
    // Map options
    const options = {
        zoom:13,
        center: {lat : businessLat, lng : businessLng}
    };

    // New map
    const map = new google.maps.Map(document.getElementById('map'), options);

    //Add marker
    const marker = new google.maps.Marker({
        position:{lat : businessLat, lng : businessLng},
        map:map,
        icon: {
            url: 'https://i2.wp.com/catgirlonlineshop.com/wp-content/uploads/2019/12/cropped-depositphotos_263556590-stock-illustration-dog-paw-icon-vector-footprint.png?ssl=1', 
            scaledSize: new google.maps.Size(40, 40)
        },
    });

    //define infoWindow instance
    const infoWindow = new google.maps.InfoWindow();

    //content of the marker's infoWindow
    const businessContent = professionalName

    //show infoWindow when marker is clicked
    marker.addListener('click', () => {
        infoWindow.close();
        infoWindow.setContent(businessContent)
        infoWindow.open(map, marker);
    });
}
