function initMap() {
    // Latitude and Longitude
    var myLatLng = {lat: 32.651159, lng: 51.770516};
    
    var map = new google.maps.Map(document.getElementById('google-maps'), {
        zoom: 17,
        center: myLatLng
    });

    var marker = new google.maps.Marker({
        position: myLatLng,
        map: map,
        title: 'Isfahan, Iran' // Title Location
    });
}