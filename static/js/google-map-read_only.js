// Google Map Api

async function initMap() {
    const {Map, InfoWindow} = await google.maps.importLibrary("maps");

    const _id = 'map';
    const _container = document.getElementById(_id);
    const myLatLng = {
        lat: parseFloat(_container.dataset.lat),
        lng: parseFloat(_container.dataset.lng)
    };

    const map = new Map(document.getElementById(_id), {
        center: {
            lat: myLatLng.lat,
            lng: myLatLng.lng
        },
        mapId: "4504f8b37365c3d0",
        zoom: 12,
    });

    const infowindow = new google.maps.InfoWindow({
        content: _container.dataset.title,
        ariaLabel: "Uluru",
    });

    let marker = new google.maps.Marker({
        position: myLatLng,
        map,
        title: _container.dataset.title,
    });

    marker.addListener("click", () => {
        infowindow.open({
            anchor: marker,
            map,
        });
    });
}

initMap();