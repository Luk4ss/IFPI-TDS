import 'package:flutter/material.dart';
import '../Controllers/editar_contato_controller.dart';
import '../Models/contato.dart';

class EditarContato extends StatefulWidget {
  
  final String id;
  final String idContato;
  final Contato contato;

  const EditarContato({super.key, required this.id, required this.idContato, required this.contato});

  @override
  State<EditarContato> createState() => _EditarContatoState();
}

class _EditarContatoState extends State<EditarContato> {
  final TextEditingController _nomeController = TextEditingController();
  final TextEditingController _telefoneController = TextEditingController();
  final TextEditingController _latitudeController = TextEditingController();
  final TextEditingController _longitudeController = TextEditingController();
  String mensagem = "";
  String _msgNome = "";

  @override
    initState(){
      super.initState();
        _nomeController.text = widget.contato.nome;
        _telefoneController.text = widget.contato.telefone as String;
        if(widget.contato.latitude != null){
          _latitudeController.text = widget.contato.latitude.toString();
        }
        if(widget.contato.longitude != null){
          _longitudeController.text = widget.contato.longitude.toString();
        }
    }

  Future<bool> _editarContato() async {
    if (_nomeController.text.isEmpty) {
      setState(() {        
        _msgNome = "Preencha o nome do contato!";
      });
      return false;
    }
    setState(() {
      _msgNome = "";
    }); 

    Contato contato =  widget.contato;
    contato.nome = _nomeController.text;
    contato.telefone = _telefoneController.text;
    contato.latitude =  double.tryParse(_latitudeController.text);
    contato.longitude = double.tryParse(_longitudeController.text);    
    var controller = EditarContatoController(id: widget.id, idContato:  widget.idContato , contato: contato);
    return await controller.editarContato();
  }

  Future<void> _excluirContato() async {    
    Contato contato =  widget.contato;   
    var controller = EditarContatoController(id: widget.id, idContato:  widget.idContato , contato: contato);
    await controller.excluirContato();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Editar Contato')),
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
                _editarContato()
                .then(
                    (value) { 
                      if(value) {
                        _msgNome = "";
                        mensagem = "";
                        Navigator.pop(context);
                      }
                      else {
                        setState(() {
                          mensagem = "Contato não Editado!";
                        });
                      }
              })
                .catchError((_){
                  setState((){
                    mensagem = "Erro ao editar o contato.";
                  });
                });
              },
              child: const Text('Salvar Alterações')),
          ElevatedButton(
              style: ElevatedButton.styleFrom(backgroundColor: Colors.red),
              onPressed: () {       
                _excluirContato().then((_) => Navigator.pop(context));
                       
              },
              child: const Text('Deletar Contato')),
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
