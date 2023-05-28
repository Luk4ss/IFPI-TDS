import 'package:flutter/material.dart';

import '../Controllers/cadastro_controller.dart';

class Cadastro extends StatelessWidget {
  Cadastro({super.key});

  final TextEditingController _loginController = TextEditingController();
  final TextEditingController _senhaController = TextEditingController();
  final TextEditingController _senhaConfirmaController = TextEditingController();

  final String mensagem="";
  final Color? cor = Colors.red;

  Future<bool> _fazerCadastro() async{


    if(_loginController.text.isEmpty || _senhaController.text.isEmpty || _senhaConfirmaController.text.isEmpty){
      return false;
    }

    if(_senhaController.text != _senhaConfirmaController.text){
      return false;
    }

    CadastroController cadastroController = CadastroController(_loginController.text, _senhaController.text );
    return await cadastroController.cadastraUsuario();

  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Cadastro')
      ),
      body: SingleChildScrollView(
        child: Column(
          children: <Widget>[            
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
            const Text('Cofirme a sua senha'),
            Padding(
              padding: const EdgeInsets.all(10.0),
              child: TextField(
                controller: _senhaConfirmaController,
                obscureText: true,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'Digite a sua senha novamente',
                ),),
            ),
            const SizedBox(height: 15.0,),
            Text(
              mensagem, 
              style: TextStyle(color: cor),),
            const SizedBox(height: 15.0,),
            ElevatedButton(
                onPressed: () async {
                    if(await _fazerCadastro()){
                        Navigator.pushNamed(context, "login");
                    }
                }, 
                child: const Text('Fazer cadastro')),
            TextButton(
              onPressed: (){
                Navigator.pop(context);
              }, 
              child: const Text('voltar', 
                              style: TextStyle(decoration: TextDecoration.underline),))
          ],
        )),
    );
  }
}