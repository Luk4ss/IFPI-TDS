import '../Data/banco.dart';
import '../Models/contato.dart';

class ContatoCadastroController{
  Contato contato;
  String id;

  ContatoCadastroController(this.id,this.contato);

  Future<bool> cadastrarNovoContato() async{
    final contatos = await Banco.recuperaContatosDoUsuario(id);
    final key = contatos.children.length.toString();
    final newRef = contatos.child(key).ref;

    final novoContato = {
      "nome": contato.nome,
      "telefone": contato.telefone,
      "latitude": contato.latitude,
      "longitude": contato.longitude
    };
    

    return await newRef.set(
       novoContato
    )
    .then((_) => true)
    .catchError((_) => false);
  }
    
}