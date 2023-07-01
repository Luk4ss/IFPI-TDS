import 'package:app_final/Data/banco.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class Mapa extends StatefulWidget {
  const Mapa({super.key, required this.id});  
  final String id;

  @override
  State<Mapa> createState() => _MapaState();
}

class _MapaState extends State<Mapa> {
  Set<Marker> _marcadores = {};
  BitmapDescriptor markerIcon = BitmapDescriptor.defaultMarker;
  

  late GoogleMapController mapController;
  final LatLng _center = const LatLng(-5.08917, -42.80194);

  void _addCustomIcon(){
    BitmapDescriptor.fromAssetImage(const ImageConfiguration(), "assets/images/person.png")
    .then((icon){
      markerIcon = icon;
    });
  }

  void _onMapCreated(GoogleMapController controller) {
      mapController = controller;   
  }

  void _carregaMarcadoresContato() async{
    Set<Marker> marcadorLocal = {}; 
    DataSnapshot contatos = await Banco.recuperaContatosDoUsuario(widget.id);
    int quantidade = contatos.children.length;    

    for(int i = 0; i < quantidade; i++){
      DataSnapshot contato = contatos.child(i.toString());
      if(contato.exists){
        String idMarcador  = contato.child('nome').value as String;
        double? latitude   = contato.child('latitude').exists  ? contato.child('latitude').value as double : null;
        double? longitude  = contato.child('longitude').exists ? contato.child('longitude').value as double : null;
        String telefone    = contato.child('telefone').value as String;
      if(telefone.isEmpty){
        telefone = 'Telefone não cadastrado';
      }
      if(latitude != null && longitude != null){
        marcadorLocal.add(
          Marker(
            markerId: MarkerId(idMarcador),
            position: LatLng(latitude, longitude),
            infoWindow: InfoWindow(title: idMarcador, snippet: telefone),
            icon: markerIcon
          ),        
        );
      }    
      }      
      
      
    }
   
    setState(() {
        _marcadores = marcadorLocal;
    });
      
  }


  @override
  void initState() {
    super.initState();
    _addCustomIcon();
    _carregaMarcadoresContato();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(        
        title: const Text("Mapa"),
      ),
      body: GoogleMap(
        zoomGesturesEnabled: true,
        onMapCreated: _onMapCreated,
        initialCameraPosition: CameraPosition(target: _center, zoom: 7.0),
        markers: _marcadores,

      ),
    );
  }
}
