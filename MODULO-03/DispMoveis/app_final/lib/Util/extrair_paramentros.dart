import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';

import '../Models/contato.dart';

class ExtrairParametros extends StatelessWidget {
  final String id;
  final String idContato;
  final Contato contato;

  const ExtrairParametros({super.key, required this.id, required this.idContato, required this.contato});

  @override
  Widget build(BuildContext context) {
    return const Placeholder();
  }
}