
function imprimir(){

    const dataOp = document.getElementById("Data").value;

    const valorUnitario = Number(document.getElementById("ValorU").value);

    const codigoAcao = document.getElementById("codigo").value;

    const quantidade = Number(document.getElementById("QntdA").value);

    const taxa_corretagem = Number(document.getElementById("taxa").value);

    const taxaB3 = (valorUnitario *  quantidade) *0.0003;

    const tipoOp = document.getElementById("tipoOperacao").value;

    let totalOperacao = 0;

    /* Para o caso de compra */
    if(tipoOp == "COMPRA"){
        totalOperacao = (quantidade * valorUnitario) + taxaB3 + taxa_corretagem;
    }
    else{
        totalOperacao = (quantidade * valorUnitario) - taxaB3 - taxa_corretagem;
    }

   

    console.log(totalOperacao)

    var mostrar = document.getElementById("detalhes");

    mostrar.innerText = `VALOR DA OPERAÇÃO: R$ ${totalOperacao.toFixed(2)}\n
                         CÓDIGO: ${codigoAcao}\n                         
                         QUANTIDADE: ${quantidade}\n
                         VALOR UNITÁRIO: R$ ${valorUnitario.toFixed(2)}\n
                         TAXA B3: R$ ${taxaB3.toFixed(2)}\n
                         TAXA CORRETAGEM: R$ ${taxa_corretagem.toFixed(2)}\n
                         OPERAÇÃO: ${tipoOp}\n
                         DATA DA OPERAÇÃO: ${dataOp}`;


}

