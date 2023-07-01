import 'package:app_final/Controllers/login_controller.dart';
import 'package:app_final/Models/pessoa.dart';
import 'package:flutter/material.dart';

class Login extends StatefulWidget {
  const Login({super.key, title});

  @override
  State<Login> createState() => _LoginState();
}

class _LoginState extends State<Login> {
  final TextEditingController _loginController = TextEditingController();
  final TextEditingController _senhaController = TextEditingController();

  String _msgCampoLogin = "";
  String _msgCampoSenha = "";
  String _msgExisteUsuario = "";
  Pessoa? pessoa;

  void _limparCampos() {
    setState(() {   
      _loginController.text = "";
      _senhaController.text = "";
      _msgCampoLogin = "";
      _msgCampoSenha = "";
      _msgExisteUsuario = "";
    });
  }

  Future<bool> _existeUsuarioCadastrado() async {
    if (_loginController.text.isEmpty) {
      setState(() {
        _msgCampoLogin = "Preencha o campo de Login!";
      });
      return false;
    }

    setState(() {
      _msgCampoLogin = "";
    });

    if (_senhaController.text.isEmpty) {
      setState(() {
        _msgCampoSenha = "Preencha sua Senha!";
      });
      return false;
    }

    setState(() {
      _msgCampoSenha = "";
    });

    var loginController =
        LoginController(_loginController.text, _senhaController.text);
    pessoa = await loginController.retornaUsuarioCadastrado();
    const CircularProgressIndicator();
    //Se o pessoa é diferente de nulo, é porque ela existe no banco
    return pessoa != null;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('LOGIN')),
      body: SingleChildScrollView(
          child: Column(
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(50.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                SizedBox(
                    height: 150,
                    child: Image.asset(
                      'assets/images/ifpi-logo2.png',
                      fit: BoxFit.cover,
                    ))
              ],
            ),
          ),
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
          Text(_msgCampoLogin, style: const TextStyle(color: Colors.red)),
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
                label: Text('senha')
              ),
            ),
          ),
          Text(
            _msgCampoSenha,
            style: const TextStyle(color: Colors.red),
          ),
          Text(
            _msgExisteUsuario,
            style: const TextStyle(color: Colors.red),
          ),
          const SizedBox(
            height: 15.0,
          ),
          ElevatedButton(
              onPressed: () async {
                if (await _existeUsuarioCadastrado()) {
                  _limparCampos();
                  Navigator.pushNamed(context, "/menu", arguments: this.pessoa );
                } else if (_msgCampoLogin.isEmpty && _msgCampoSenha.isEmpty) {
                  _msgExisteUsuario = "Usuário ou senha inválidos!";
                }
              },
              child: const Text('Fazer login')),
          TextButton(
              onPressed: () {
                _limparCampos();
                Navigator.pushNamed(context, "/cadastro");
              },
              child: const Text(
                'Não possui conta? Cadastre-se!',
                style: TextStyle(decoration: TextDecoration.underline),
              ))
        ],
      )),
    );
  }
}
