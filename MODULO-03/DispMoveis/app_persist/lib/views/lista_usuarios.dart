
import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';
import '../data/data_layer.dart';

class ListaUsuarios extends StatefulWidget {
  const ListaUsuarios({super.key});

  @override
  State<ListaUsuarios> createState() => _ListaUsuariosState();
}

class _ListaUsuariosState extends State<ListaUsuarios> {
  
  List<Map<String, Object?>> usuarios = [
    {"nome": "Lucas"}
  ];

  Future<void> recuperaUsuarios() async{
    Database db = await Banco.getBanco();
    usuarios = await db.query('USERS');
    setState(() {
      usuarios;
    });
  }

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    recuperaUsuarios();
  }


  @override
  Widget build(BuildContext context){
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text("Lista de usuários"),
      ),
      body: Center(
        child: ListView.builder(
          itemCount: usuarios.length,
          itemBuilder: (ctx, i){
              final item = usuarios[i];
              return ListTile(
                  title: Text(item["email"].toString()),
                  subtitle: Text(item["password"].toString()),
                  key: Key(item["id"].toString()),
                  // value: true,
                  // onChanged: (value) {}
                  );
          } ,
        ),
      ),
    );
  }
}