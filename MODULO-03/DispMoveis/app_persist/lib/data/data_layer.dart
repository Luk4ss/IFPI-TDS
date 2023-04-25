import 'package:sqflite/sqflite.dart';
import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import 'dart:async';

class Banco{

  static Future<Database> getBanco() async{
    var databasePath = await getDatabasesPath();
    String path = join(databasePath, 'banco.db');

    Database db = await (openDatabase(path, version: 1,
                onCreate: (db, versaoRecente) async {
                String sql = "CREATE TABLE USERS(email VARCHAR(30), password VARCHAR(16))";
                await db.execute(sql);
    }));
    return db;
  }

}