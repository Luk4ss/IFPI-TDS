import 'package:flutter/material.dart';

import '../Controllers/cadastro_contato_controller.dart';
import '../Models/contato.dart';

class CadastroContato extends StatefulWidget {
  
  final String id;

  const CadastroContato({super.key, required this.id});

  @override
  State<CadastroContato> createState() => _CadastroContatoState();
}

class _CadastroContatoState extends State<CadastroContato> {
  final TextEditingController _nomeController = TextEditingController();
  final TextEditingController _telefoneController = TextEditingController();
  final TextEditingController _latitudeController = TextEditingController();
  final TextEditingController _longitudeController = TextEditingController();
  String mensagem = "";
  String _msgNome = "";

  Future<bool> _cadastrarNovoContato() async {
    if (_nomeController.text.isEmpty) {
      setState(() {        
        _msgNome = "Preencha o nome do contato!";
      });
      return false;
    }
    setState(() {
      _msgNome = "";
    });

    String nome = _nomeController.text;
    String? telefone = _telefoneController.text;
    double? latitude =  double.tryParse(_latitudeController.text);
    double? longitude = double.tryParse(_longitudeController.text);
    var contato = Contato(nome, telefone: telefone, latitude: latitude, longitude: longitude );
    var controller = ContatoCadastroController(widget.id, contato);
    return await controller.cadastrarNovoContato();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Novo Contato')),
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
                  hintText: 'Nome do contato',
                  label: Text('Nome')),
              controller: _nomeController,
            ),
          ),
          Text(
            _msgNome,
            style: const TextStyle(color: Colors.red),
          ),
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: TextField(
              controller: _telefoneController,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText: 'ex: (86) 94124-5487',
                label: Text('Telefone'),
              ),
            ),
          ),
          const SizedBox(
            height: 15.0,
          ),
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: TextField(
              controller: _latitudeController,
              decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'ex: -2.546714',
                  label: Text('Latitude')),
            ),
          ),
          const SizedBox(
            height: 15.0,
          ),
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: TextField(
              controller: _longitudeController,
              decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  hintText: 'ex: 5.7577531',
                  label: Text('Longitude')),
            ),
          ),
          Text(mensagem, 
          style:const TextStyle(color: Colors.red)),
          const SizedBox(
            height: 15.0,
          ),
          ElevatedButton(
              onPressed: () {
                _cadastrarNovoContato()
                .then(
                    (value) { 
                      if(value) {
                        _msgNome = "";
                        mensagem = "";
                        Navigator.pop(context);
                      }
                      else {
                        setState(() {
                          mensagem = "Contato não cadastrado!";
                        });
                      }
              })
                .catchError((_){
                  setState((){
                    mensagem = "Erro ao Cadastrar o contato";
                  });
                });
              },
              child: const Text('Cadastrar Contato')),
          TextButton(
              onPressed: () {
                _msgNome = "";
                mensagem = "";
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
