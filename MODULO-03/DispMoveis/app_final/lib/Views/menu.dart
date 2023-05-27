
import 'package:flutter/material.dart';

class Menu extends StatelessWidget {
  const Menu({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Menu'),
      ),
      body: Column(
        children: [
          const SizedBox(height: 280,),
          Row(
            children: [
              Padding(
                padding: const EdgeInsets.all(6.0),
                child: ElevatedButton(
                  onPressed: (){},
                  style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.purple,
                      padding: const EdgeInsets.all(60),
                      fixedSize: const Size(165, 150),
                  ), 
                  child: const Text('MAPA')),
              ),               
                Padding(
                  padding: const EdgeInsets.all(6.0),
                  child: ElevatedButton(
                  onPressed: (){},
                  style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.purple,
                      padding: const EdgeInsets.all(45),
                      fixedSize: const Size(165, 150),                     
                  ), 
                  child: const Text('CONTATOS')
                  ),
                ),
            ],
          ),
          Padding(            
            padding: const EdgeInsets.all(6.0),
            child: Row(            
              children: [
                ElevatedButton(
                  onPressed: (){},                   
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.purple,
                    padding: const EdgeInsets.all(60),
                    fixedSize: const Size(165, 150),
                  ),
                  child: const Text('EXTRA'),               
                  ),
                  const SizedBox(width: 12,),
                  ElevatedButton(
                  onPressed: (){},                 
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.purple,
                    padding: const EdgeInsets.all(60),
                    fixedSize: const Size(165, 150),
                  ),
                  child: const Text('EXTRA'),                
                  )
              ],
            ),
          )
        ]),
    );
  }
}