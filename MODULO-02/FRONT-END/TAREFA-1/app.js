
const numeroAleatorio = Math.floor(Math.random() * 100 ) + 1;
const detalhes = document.getElementById("mostrarDetalhes");
const btn_enviar = document.getElementById("enviar");
const historico  = document.getElementById("historico");
let qtd_tentativas = 10;

function handleBtnEnviar(){
    const palpite = Number(document.getElementById("palpite").value);
    detalhes.innerText = ""
    historico.innerText += palpite + ", ";
    if (palpite == numeroAleatorio){
        detalhes.innerText = "Parabéns! Você acertou!"
        detalhes.className = "winner"
        btn_enviar.disabled = true;
    }
    else{
        detalhes.innerText =  palpite > numeroAleatorio ? "Você chutou um número muito alto!" : "Você chutou um número muito baixo!"
        detalhes.className = "wrong"
        document.getElementById("palpite").value = "";
        qtd_tentativas -= 1;
    }

    if(qtd_tentativas == 0){
        detalhes.innerText = "Você Perdeu! Você gastou todas as tentativas.";
        detalhes.className = "loser"
        btn_enviar.disabled = true;
    }
     
    
    
}
