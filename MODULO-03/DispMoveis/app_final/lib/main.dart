import 'package:app_final/Models/pessoa.dart';
import 'package:app_final/Util/extrair_paramentros.dart';
import 'package:app_final/Views/cadastro.dart';
import 'package:app_final/Views/cadastro_contato.dart';
import 'package:app_final/Views/editar_contato.dart';
import 'package:app_final/Views/mapa.dart';
import 'package:app_final/Views/meus_contatos.dart';
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

        if(settings.name == "/mapa"){
          final args = settings.arguments as String;
          return MaterialPageRoute(
            builder: (context) {
            return Mapa(id: args);
          });
        }

         if(settings.name == "/meusContatos"){
          final args = settings.arguments as String;
          return MaterialPageRoute(
            builder: (context) {
            return MeusContatos(id: args);
          });
        }

        if(settings.name == "/editarContato"){
          final args = settings.arguments as ExtrairParametros;
          return MaterialPageRoute(
            builder: (context) {
            return EditarContato(id: args.id, idContato: args.idContato, contato: args.contato,);
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

