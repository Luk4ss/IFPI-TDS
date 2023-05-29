import '../Data/banco.dart';

class CadastroController{

  String login;
  String senha;

  CadastroController(this.login, this.senha);
  

  Future<bool> cadastraUsuario() async{    
    
    final tabelaUsuarios =  await Banco.db().get();

    //Caso existe usuários cadastrados, verificar se o login já existe para alguém já cadastrado.
    if(tabelaUsuarios.children.isNotEmpty){
      for(var usuario in tabelaUsuarios.children){        
        if(usuario.child('login').value == login){   
          return false;
        }
      }
    }
        
    final newRef = Banco.db().push();

    return await newRef.set({  
      "login": login,
      "senha": senha,   
    })
    .then((_) => true)
    .catchError((_) => false);

  }

}