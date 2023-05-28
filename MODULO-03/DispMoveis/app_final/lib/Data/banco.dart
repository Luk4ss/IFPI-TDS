import 'package:firebase_database/firebase_database.dart';

class Banco{

  static DatabaseReference db(){
    return FirebaseDatabase.instance.ref("usuarios");
  }
}