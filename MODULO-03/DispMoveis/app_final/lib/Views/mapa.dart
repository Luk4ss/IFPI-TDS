import 'package:flutter/material.dart';
//import 'package:google_maps_flutter_web/google_maps_flutter_web.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class Mapa extends StatefulWidget {
  const Mapa({super.key});

  @override
  State<Mapa> createState() => _MapaState();
}

class _MapaState extends State<Mapa> {
  Set<Marker> _marcadores = {};

  late GoogleMapController mapController;
  final LatLng _center = const LatLng(-5.08917, -42.80194);

  void _onMapCreated(GoogleMapController controller) {
    mapController = controller;
  }

  void _carregarMarcadores() {
    Set<Marker> marcadorLocal = {};
    Marker markerIfpi = const Marker(
        markerId: MarkerId('IFPI'),
        position: LatLng(-5.0886781966678845, -42.81111159992701),
        infoWindow: InfoWindow(title: 'IFPI CENTRAL'));
    Marker markerIfpiSul = const Marker(
        markerId: MarkerId('IFPI'),
        position: LatLng(-5.101895924224421, -42.81267882725431),
        infoWindow: InfoWindow(title: 'IFPI SUL'));

    Marker markerAlbertao = const Marker(
        markerId: MarkerId("ALBERTAO"),
        position: LatLng(-5.115456967943075, -42.79295743863892),
        infoWindow: InfoWindow(title: 'Albertão'));

    Marker markerSaoJanuario = const Marker(
        markerId: MarkerId("JANUARIO"),
        position: LatLng(-22.890492693770486, -43.22692690115295),
        infoWindow: InfoWindow(title: 'São Januário'));

    Marker markerArenaDaBaixada = const Marker(
        markerId: MarkerId("BAIXADA"),
        position: LatLng(-25.44743656868096, -49.2769866),
        infoWindow: InfoWindow(title: 'Arena Da Baixada'));

    marcadorLocal.add(markerIfpi);
    marcadorLocal.add(markerIfpiSul);
    marcadorLocal.add(markerAlbertao);
    marcadorLocal.add(markerSaoJanuario);
    marcadorLocal.add(markerArenaDaBaixada);

    setState(() {
      _marcadores = marcadorLocal;
    });
  }

  @override
  void initState() {
    super.initState();
    _carregarMarcadores();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(        
        title: const Text("Mapa"),
      ),
      body: GoogleMap(
        onMapCreated: _onMapCreated,
        initialCameraPosition: CameraPosition(target: _center, zoom: 11.0),
        markers: _marcadores,
      ),
    );
  }
}
