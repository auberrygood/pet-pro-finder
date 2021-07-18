function initMap() {
    
    // Map options
    const options = {
        zoom:13,
        center:coordinates
    };

    // New map
    const map = new google.maps.Map(document.getElementById('map'), options);

    //Add marker
    const marker = new google.maps.Marker({
        position:coordinates,
        map:map,
        icon: {
            url: 'https://i2.wp.com/catgirlonlineshop.com/wp-content/uploads/2019/12/cropped-depositphotos_263556590-stock-illustration-dog-paw-icon-vector-footprint.png?ssl=1', 
            scaledSize: new google.maps.Size(40, 40)
        },
    });

    //define infoWindow instance
    const infoWindow = new google.maps.InfoWindow();

    //content of the marker's infoWindow
    const businessContent = name

    //show infoWindow when marker is clicked
    marker.addListener('click', () => {
        infoWindow.close();
        infoWindow.setContent(businessContent)
        infoWindow.open(map, marker);
    });
}
