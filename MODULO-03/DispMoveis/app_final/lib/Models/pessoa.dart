class Pessoa{ 
  String id;
  String login;
  String senha;
  double? latitude;
  double? longitude;
  List<Pessoa> contatos = [];

  Pessoa({this.id = "", this.login="", this.senha = "", this.latitude = 0.0, this.longitude = 0.0});
}