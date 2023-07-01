
import 'package:flutter/material.dart';

import '../Models/pessoa.dart';

class Menu extends StatelessWidget {
  
  final Pessoa pessoa;

  const Menu({super.key, required this.pessoa});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Menu'),
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(15.0),
            child: SizedBox(
            height: 320, 
            child: Image.asset(
                      'assets/images/globe.png',
                      height: 1,                   
                      fit: BoxFit.cover,
                    )),
          ),
          Row(
            mainAxisSize: MainAxisSize.max,
            children: [
              Padding(
                padding: const EdgeInsets.all(16.0),
                child: ElevatedButton(
                  onPressed: (){
                    Navigator.pushNamed(context, "/mapa", arguments: pessoa.id);
                  },
                  style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.purple,
                      padding: const EdgeInsets.all(40),
                      fixedSize: const Size(165, 150),
                  ), 
                  child: const FittedBox(fit: BoxFit.cover ,child: Text('MAPA'))
                ),
              ),               
                Padding(
                  padding: const EdgeInsets.all(6.0),
                  child: ElevatedButton(
                  onPressed: (){
                    Navigator.pushNamed(context, "/cadastroContato", arguments: pessoa.id);
                  },
                  style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.purple,
                      padding: const EdgeInsets.all(40),
                      fixedSize: const Size(165, 150),                     
                  ), 
                  child: const FittedBox(fit: BoxFit.cover ,child: Text('CADASTRAR')),  
                  ),
                ),
            ],
          ),
          Row(      
            mainAxisSize: MainAxisSize.max,      
            children: [
              Padding(
                padding: const EdgeInsets.all(16.0),
                child: ElevatedButton(
                  onPressed: (){
                    Navigator.pushNamed(context, "/meusContatos", arguments: pessoa.id);
                  },                   
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.purple,
                    padding: const EdgeInsets.all(40),
                    fixedSize: const Size(165, 150),
                  ),
                  child: const FittedBox(fit: BoxFit.cover ,child: Text('CONTATOS')),               
                  ),
              ),
                
                Padding(
                  padding: const EdgeInsets.all(6.0),
                  child: ElevatedButton(
                  onPressed: (){
                    
                  },                 
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.purple,
                    padding: const EdgeInsets.all(40),
                    fixedSize: const Size(165, 150),
                  ),
                  child: const FittedBox(fit: BoxFit.cover ,child: Text('EXTRA')),                
                  ),
                )
            ],
          )
        ]),
    );
  }
}