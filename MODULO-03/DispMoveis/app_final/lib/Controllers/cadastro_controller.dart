import '../Data/banco.dart';

class CadastroController{

  String login;
  String senha;

  CadastroController(this.login, this.senha);
  

  Future<bool> cadastraUsuario() async{    

    final usuario  =  await Banco.db().child(login).get();
    
    if(usuario.exists){
      return false;
    }

    final newRef = Banco.db().child(login);

    return await newRef.set({      
      "login": login,
      "senha": senha,
      "latidude": 0.0,
      "longitude": 0.0      
    })
    .then((_) => true)
    .catchError((_) => false);


  }

}