
var botao = document.getElementById("calcular");

botao.addEventListener('click', () => {
   // const _nome = document.getElementById("nome");
    const _peso = Number(document.getElementById("peso").value);
    const _altura = Number(document.getElementById("altura").value);
    const msg  = document.getElementById("mensagem");

    const imc = _peso / (_altura * _altura);
    
    msg.innerText = "Seu IMC é: " + imc


});