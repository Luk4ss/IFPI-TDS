class LoginController{
  String? login;
  String? senha;

  LoginController({login,senha});

  bool existeUsuario(){
    //TODO: VERIFICAR SE O USUÁRIO EXISTE NO BANCO DE DADOS
    return true;
  }
}