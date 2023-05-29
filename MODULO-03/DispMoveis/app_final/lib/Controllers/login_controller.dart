import 'package:firebase_database/firebase_database.dart';

import '../Data/banco.dart';
import '../Models/pessoa.dart';

class LoginController{
  String login;
  String senha;

  LoginController(this.login,this.senha);

  Future<Pessoa> retornaUsuarioCadastrado() async{  
    
    if(login.isEmpty || senha.isEmpty){
      return Pessoa();
    }    
    
    final tabelaUsuarios =  await Banco.db().get();

    //Caso não exista usários no banco, então retorna uma pessoa com id vazio
    if(tabelaUsuarios.children.isEmpty){
      return Pessoa();
    }

    bool existeUsuario = false;
    late DataSnapshot user;
    
    //Itera sobre os usuários, e verifica se existe o login digitado
    for(var usuario in tabelaUsuarios.children){
      if(usuario.child('login').value == login){   
        existeUsuario = true;
        user = usuario;
        break;
      }
    }    

    //se não existir o login, então retorna uma pessoa com id vazio
    if(!existeUsuario){
      return Pessoa();
    }   

    //o login existe, mas senha digitada está errada
    if(user.child('senha').value != senha){
      return Pessoa();
    }

    Pessoa pessoa = Pessoa(
      id: user.key as String,
      login: login,
      senha: senha,
    );   

    if(user.child('latitude').exists){
      pessoa.latitude = user.child('latitude').value as double?;
    }
    if(user.child('longitude').exists){
      pessoa.longitude = user.child('longitude').value as double?;
    }
    if(user.child('contatos').exists){
      pessoa.contatos = user.child('contatos').value as List<Pessoa>;
    }

    return pessoa;
  }
}