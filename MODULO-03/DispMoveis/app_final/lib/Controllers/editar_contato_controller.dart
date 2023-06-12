import '../Models/contato.dart';

class EditarContatoController{
  final String id;
  final String idContato;
  final Contato contato;

  const EditarContatoController({required this.id, required this.idContato, required this.contato});

  Future<bool> editarContato() async{
    return false;
  }
  
}