import '../Data/banco.dart';

class LoginController{
  String login;
  String senha;

  LoginController(this.login,this.senha);

  Future<bool> verficaSeExisteUsuario() async{  

    if(login.isEmpty || senha.isEmpty){
      return false;
    }
    
    final usuario  =  await Banco.db().child(login).get();

    if(!usuario.exists){
      return false;
    }

    if(usuario.child('senha').value != senha){
      return false;
    }   

    return true;
  }
}