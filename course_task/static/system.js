require(["../../static/test_data.js"], function (response) {
    //data is now loaded.
});
$(function(){
mapboxgl.accessToken = 'pk.eyJ1IjoidGlhbnFpIiwiYSI6ImNqb2JhNTI1dTBhZ24za2w3NWh2bWc3ZW4ifQ.bRqolX5Grt121j46e3CQhw';

var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [118.131624, 24.492368],
    zoom: 11.15
});

var layerList = document.getElementById('menu');
var inputs = layerList.getElementsByTagName('input');
 
function switchLayer(layer) {
var layerId = layer.target.id;
map.setStyle('mapbox://styles/mapbox/' + layerId);
}
 
for (var i = 0; i < inputs.length; i++) {
inputs[i].onclick = switchLayer;
}


// var cood = require("./test_data.js")
var list = [118.131624, 24.492368]
// var list1 = [list[0] + 0.001,list[1] + 0.001]
// var list2 = [list1[0] + 0.01,list1[1] + 0.01]
// var list3 = [list2[0] + 0.01,list2[1] + 0.01]
// var list4 = [list3[0] + 0.01,list3[1] + 0.01]
// var list5 = [list4[0] + 0.01,list4[1] + 0.01]
// var list6 = [list5[0] + 0.01,list5[1] + 0.01]
// var list7 = [list6[0] + 0.01,list6[1] + 0.01]
// var list8 = [list7[0] + 0.01,list7[1] + 0.01]
// var list9 = [list8[0] + 0.01,list8[1] + 0.01]

map.on('load', function () {
    // Add a layer showing the places.
    var cood = k
    map.addLayer({
        "id": "places",
        "type": "symbol",
        "source": {
            "type": "geojson",
            "data": cood
        },
        "layout": {
            "icon-image": "{icon}-15",
            "icon-size" : 1,
            "icon-allow-overlap": true
        }
    });

    map.on('click', 'places', function (e) {
        var coordinates = e.features[0].geometry.coordinates.slice();
        var description = e.features[0].properties.description;

        // Ensure that if the map is zoomed out such that multiple
        // copies of the feature are visible, the popup appears
        // over the copy being pointed to.
        while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
            coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
        }

        new mapboxgl.Popup()
            .setLngLat(coordinates)
            .setHTML(description)
            .addTo(map);
    });

    // Change the cursor to a pointer when the mouse is over the places layer.
    map.on('mouseenter', 'places', function () {
        map.getCanvas().style.cursor = 'pointer';
    });

    // Change it back to a pointer when it leaves.
    map.on('mouseleave', 'places', function () {
        map.getCanvas().style.cursor = '';
    });
});


})