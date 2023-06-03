import 'package:firebase_database/firebase_database.dart';

class Banco{

  static DatabaseReference db(){
    return FirebaseDatabase.instance.ref("usuarios");
  }

  static Future<DataSnapshot> recuperaContatosDoUsuario(String id) async{
    var tabelaContatos =  await db().get();
    return tabelaContatos.child(id).child('contatos');
  }
}