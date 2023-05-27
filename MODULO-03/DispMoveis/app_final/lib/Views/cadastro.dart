import 'package:flutter/material.dart';

class Cadastro extends StatelessWidget {
  Cadastro({super.key});

  final TextEditingController _loginController = TextEditingController();
  final TextEditingController _senhaController = TextEditingController();
  final TextEditingController _senhaConfirmaController = TextEditingController();

  final String mensagem="";
  final Color? cor = Colors.red;


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
                onPressed: (){}, 
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