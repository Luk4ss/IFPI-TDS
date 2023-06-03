import 'package:flutter/material.dart';

import '../Controllers/cadastro_controller.dart';

class Cadastro extends StatefulWidget {
  const Cadastro({super.key});

  @override
  State<Cadastro> createState() => _CadastroState();
}

class _CadastroState extends State<Cadastro> {
  
  final TextEditingController _loginController = TextEditingController();
  final TextEditingController _senhaController = TextEditingController();
  final TextEditingController _senhaConfirmaController =
      TextEditingController();

  String _msgLogin = "";
  String _msgSenha = "";
  String _msgSenhaConfirma = "";

  void _limparCampos(){
    setState(() {
      _msgLogin = "";
      _msgSenha = "";
      _msgSenhaConfirma = "";
    });
  }

  Future<bool> _fazerCadastro() async {
    if (_loginController.text.isEmpty) {
      setState(() {
        _msgLogin = "Preencha o campo de login!";
      });
      return false;
    }

    setState(() {
      _msgLogin = "";
    });

    if (_senhaController.text.isEmpty) {
      setState(() {
        _msgSenha = "Preencha sua senha!";
      });
      return false;
    }

    setState(() {
      _msgSenha = "";
    });

    if (_senhaController.text != _senhaConfirmaController.text) {
      setState(() {
        _msgSenhaConfirma = "As senhas são diferentes!";
      });
      return false;
    }

    setState(() {
      _msgSenhaConfirma = "";
    });

    CadastroController cadastroController =
        CadastroController(_loginController.text, _senhaController.text);
    return await cadastroController.cadastraUsuario();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Cadastro')),
      body: SingleChildScrollView(
          child: Column(
        children: <Widget>[
          const SizedBox(
            height: 30.0,
          ),
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: TextField(
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'Entre com o seu login',
                label: Text('Login')
              ),
              controller: _loginController,
            ),
          ),
          Text(
            _msgLogin,
            style: const TextStyle(color: Colors.red),
          ),
          const SizedBox(
            height: 15.0,
          ),
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: TextField(
              controller: _senhaController,
              obscureText: true,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'Digite a sua senha',
                label: Text('Senha')
              ),
            ),
          ),
          Text(
            _msgSenha,
            style: const TextStyle(color: Colors.red),
          ),
          const SizedBox(
            height: 15.0,
          ),
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: TextField(
              controller: _senhaConfirmaController,
              obscureText: true,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'Digite a sua senha novamente',
                label: Text('Confirmação de Senha')
              ),
            ),
          ),
          Text(
            _msgSenhaConfirma,
            style: const TextStyle(color: Colors.red),
          ),
          const SizedBox(
            height: 15.0,
          ),
          ElevatedButton(
              onPressed: () async {
                if (await _fazerCadastro()) {
                  _limparCampos();
                  Navigator.pushNamed(context, "/login");
                }
              },
              child: const Text('Fazer cadastro')),
          TextButton(
              onPressed: () {
                _limparCampos();
                Navigator.pop(context);
              },
              child: const Text(
                'voltar',
                style: TextStyle(decoration: TextDecoration.underline),
              ))
        ],
      )),
    );
  }
}
