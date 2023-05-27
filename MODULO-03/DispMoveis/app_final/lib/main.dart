import 'package:app_final/Views/cadastro.dart';
import 'package:flutter/material.dart';

import 'Views/login.dart';
import 'Views/menu.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Projeto Final',
      theme: ThemeData(        
        primarySwatch: Colors.blue,
      ),
      home: Login(title: 'Tela de Login'),
      routes: {
        "login":(context) => Login(),
        "cadastro":(context) => Cadastro(),
        "menu":(context) => const Menu()
      },
    );
  }
}

