import 'package:app_final/Models/pessoa.dart';
import 'package:app_final/Views/cadastro.dart';
import 'package:app_final/Views/cadastro_contato.dart';
import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'firebase_options.dart';

import 'Views/login.dart';
import 'Views/menu.dart';

Future<void> main() async {
  
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );
  
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
      home: const Login(title: 'Tela de Login'),
      onGenerateRoute: (settings) {
        if(settings.name == "/menu"){
          final args = settings.arguments as Pessoa; 

          return MaterialPageRoute(
            builder: (context) {
            return Menu(pessoa: args);
          });
        }
        if(settings.name == "/cadastroContato"){
          final args = settings.arguments as String;
          return MaterialPageRoute(
            builder: (context) {
            return CadastroContato(id: args);
          });
        }
      },
      routes: {
        "/login":    (context) => const Login(),
        "/cadastro": (context) => const Cadastro(),
      },
    );
  }
}

