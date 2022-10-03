function enviar(){
    const preco_gasolina = Number(document.getElementById("pgasolina").value) ;
    const preco_alcool = Number(document.getElementById("palcool").value);
    const performance_gasolina = Number(document.getElementById("perfgasolina").value);
    const saldo = Number(document.getElementById("grana").value);
    const distancia_total = Number(document.getElementById("km").value); 
    const destino = document.getElementById("destino").value;

    const performance_alcool = (0.7*performance_gasolina).toFixed(2);

    const total_litros_gasolina = (distancia_total/performance_gasolina).toFixed(2);
    const total_litros_alcool = (distancia_total/performance_alcool).toFixed(2);

    const preco_total_gasolina = (total_litros_gasolina * preco_gasolina).toFixed(2);
    const preco_total_alcool = (total_litros_alcool * preco_alcool).toFixed(2);

    console.log("Total de litros de Gasolina necessários para essa viagem: " + total_litros_gasolina + " L");
    console.log("Total de litros de Álcool necessários para essa viagem: " + total_litros_alcool + " L");

    console.log("Custo total para a Gasolina: R$ " + preco_total_gasolina);
    console.log("Custo total para o Álcool: R$ " + preco_total_alcool);
    let msg = "";

    if(saldo >= preco_total_gasolina && saldo >= preco_total_alcool){
        console.log("O seu saldo é suficiente para cobrir os gastos de ambos os tipos de combustíveis")
        let troco = (saldo - preco_total_gasolina).toFixed(2);
        console.log("Sobra: R$ " + troco + " caso abasteça com Gasolina")
        msg ="O seu saldo é suficiente para cobrir os gastos de ambos os tipos de combustíveis\n" + "Sobra: R$ " + troco + " caso abasteça com Gasolina\n";
        troco = (saldo - preco_total_alcool).toFixed(2);
        console.log("Sobra: R$ " + troco + " caso abasteça com Álcool")
        msg += "Sobra: R$ " + troco + " caso abasteça com Álcool";
    }
    else if(saldo >= preco_total_alcool && saldo < preco_total_gasolina){
        console.log("O seu saldo é suficiente para cobrir os gastos apenas para o álcool")
        const troco = saldo - preco_total_alcool
        console.log("Sobra: R$ " + troco)
        msg = "O seu saldo é suficiente para cobrir os gastos apenas para o álcool\n" + "Sobra: R$ " + troco;
    }
    else if(saldo >=preco_total_gasolina && saldo < preco_total_alcool){
        console.log("O seu saldo é suficiente para cobrir os gastos apenas para a Gasolina")
        const troco = saldo - preco_total_gasolina
        console.log("Sobra: R$ " + troco)
        msg = "O seu saldo é suficiente para cobrir os gastos apenas para a Gasolina\n" + "Sobra: R$ " + troco;
    }
    else{
        const deficit_gasolina = (preco_total_gasolina - saldo).toFixed(2);
        const deficit_alcool = (preco_total_alcool - saldo).toFixed(2);
        console.log("O seu saldo não é suficiente para cobrir os gastos dos combustíveis. Você precisa completar com: ");
        console.log("R$ " + deficit_gasolina+ " para gasolina");
        console.log("R$ " + deficit_alcool + " para o Álcool");
        msg = "O seu saldo não é suficiente para cobrir os gastos dos combustíveis. Você precisa completar com: \n" + "R$ " + deficit_gasolina + " para gasolina\n" + "R$ " + deficit_alcool + " para o Álcool";
    }
    
    const div = document.getElementById("saida");
    div.classList.remove("esconder");
    div.classList.add("saida");

    const info_combustivel = document.getElementById("info_combustivel");
    info_combustivel.innerText = "Total de litros de Gasolina necessários para essa viagem: " + total_litros_gasolina + " L.";
    info_combustivel.innerText += "\nTotal de litros de Álcool necessários para essa viagem: " + total_litros_alcool + " L.";

    const info_precos = document.getElementById("info_precos");
    info_precos.innerText = "Custo total para a Gasolina: R$ " + preco_total_gasolina + "\nCusto total para o Álcool: R$ " + preco_total_alcool;

    const info_saldo = document.getElementById("info_saldo")
    info_saldo.innerText = msg;

}