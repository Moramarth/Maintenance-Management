// Google Map Api

async function initMap() {
    const {Map, InfoWindow} = await google.maps.importLibrary("maps");
    const {AdvancedMarkerElement} = await google.maps.importLibrary("marker");

    const _id = 'map';
    const _container = document.getElementById(_id);
    const myLatLng = {
        lat: parseFloat(_container.dataset.lat),
        lng: parseFloat(_container.dataset.lng)
    };

    let _inputLat = document.getElementById( 'js__lat' );
    let _inputLng = document.getElementById( 'js__lng' );

    const map = new Map(document.getElementById(_id), {
        center: {
            lat: myLatLng.lat,
            lng: myLatLng.lng
        },
        mapId: "4504f8b37365c3d0",
        zoom: 7
    });

    const draggableMarker = new AdvancedMarkerElement({
        map,
        position: {
            lat: myLatLng.lat,
            lng: myLatLng.lng,
        },
        gmpDraggable: true,
        title: _container.dataset.title,
    });

    draggableMarker.addListener("dragend", (event) => {
        const position = draggableMarker.position;

        _inputLat.setAttribute( 'value', position.lat );
        _inputLng.setAttribute( 'value', position.lng );
    });
}

initMap();