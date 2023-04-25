import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import 'dart:async';
import 'lista_usuarios.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final TextEditingController repasswordController = TextEditingController();
  String status = "";
  Color? corErro = Colors.red[500];
  Color? corSucesso = Colors.green[700];
  Color? corResultado;



  Future<Database> _openBanco() async {
    try{
      print('Executando a função openBanco()');
      var databasePath = await getDatabasesPath();
      String path = join(databasePath, 'banco.db');

      Database db = await (openDatabase(path, version: 1,
          onCreate: (db, versaoRecente) async {
        String sql = "CREATE TABLE USERS(email UNIQUE VARCHAR(30), password VARCHAR(16))";
        await db.execute(sql);
      }));
      print('Banco:  ${db.isOpen.toString()}');
      return db;
    }
    catch(ex){
      setState(() {
        status = 'Erro ao cadastrar usuário no banco de dados';
        corResultado = corErro;
      });
      throw Exception();
    }
  }

  bool _validaEmail(String email){
    if(email.isEmpty || email.length > 30 || !email.contains("@")){
      status = "Email é inválido!";
      return false;
    }
    return true;
  }

  bool _validaSenha(String password, String repassword){

    if(password.isEmpty || password.length > 16){
      status = "Senha inválida!";
      return false;
    }
    
    if(repassword != password){
      status = "As senhas digitadas são diferentes!";     
      return false;
    }
    return true;
  }

  void _salvar() async {
    String email = emailController.text;
    String password = passwordController.text;
    String repassword = repasswordController.text;
    if(_validaEmail(email) && _validaSenha(password, repassword)){
      Database db = await _openBanco();
      Map<String, dynamic> dadosUser = {'email': email, 'password' : password};
      int idUser = await db.insert('USERS', dadosUser);
      print('Id retornado: $idUser');
      setState(() {
        status = 'Usuário de ID $idUser cadastrado com sucesso!';
        corResultado = corSucesso;
      });
    }
    else{
      setState(() {
        status;
        corResultado = corErro;
      });
    }
    
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'Email',
              style: TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.bold,
                color: Colors.purple
              ),
            ),
            TextField(
              controller: emailController ,
              keyboardType: TextInputType.emailAddress,
            ),
            const SizedBox(height: 5,),
            const Text(
              "Password",
              style: TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.bold,
                color: Colors.purple
              ),
            ),
            TextField(
              controller: passwordController,
              keyboardType: TextInputType.visiblePassword,
              obscureText: true,
            ),
            const SizedBox(height: 5,),
            const Text('Repita a senha novamente',
             style: TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.bold,
                color: Colors.purple
              )),
            TextField(
              controller: repasswordController,
              keyboardType: TextInputType.visiblePassword,
              obscureText: true,
            ),
            const SizedBox(height: 50,),
            ElevatedButton(
              onPressed: (){
                _salvar();
                Navigator.pushNamed(context, "/listar");
              }, 
              style: ElevatedButton.styleFrom(backgroundColor: Colors.deepPurple),
              child: const Text('Sign Up', style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.bold,
                    color: Colors.white
              ))),
            const SizedBox(height: 8,),
            Text(status, style: TextStyle(
              color: corResultado,
              fontWeight: FontWeight.bold
            ),)
          ],
        ),
      ),
    );
  }
}
