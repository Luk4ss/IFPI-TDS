
import 'package:app_final/Controllers/login_controller.dart';
import 'package:flutter/material.dart';

class Login extends StatelessWidget {
  Login({super.key, title});

  final TextEditingController _loginController = TextEditingController();
  final TextEditingController _senhaController = TextEditingController();

  bool _verificaSeExisteUsuarioCadastro(){
    String login = _loginController.text;
    String senha = _loginController.text;
    return LoginController(login: login, senha: senha).existeUsuario(); 
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('LOGIN')
      ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[
            Row(
              mainAxisAlignment: MainAxisAlignment.center,               
              children: [
                SizedBox(
                  height: 150,
                  child: Image.asset('images\\ifpi-logo.jpeg', fit: BoxFit.cover,))
              ],              
            ),
            const SizedBox(height: 30.0,),
            const Text('Login'),
            Padding(
              padding: const EdgeInsets.all(10.0),
              child: TextField(
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'Entre com o seu login',
                ),
                controller: _loginController,
                ),
            ),
            const SizedBox(height: 15.0,),
            const Text('Senha'),
            Padding(
              padding: const EdgeInsets.all(10.0),
              child: TextField(
                controller: _senhaController,
                obscureText: true,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'Digite a sua senha',
                ),),
            ),
            const SizedBox(height: 15.0,),
            ElevatedButton(
                onPressed: (){                  
                  if(_verificaSeExisteUsuarioCadastro()){
                    Navigator.pushNamed(context, "menu");
                  }                                 
                }, 
                child: const Text('Fazer login')),
            TextButton(
              onPressed: (){
                Navigator.pushNamed(context, "cadastro");
              }, 
              child: const Text('Não possui conta? Cadastre-se!', 
                              style: TextStyle(decoration: TextDecoration.underline),))
          ],
        )),
    );
  }
}