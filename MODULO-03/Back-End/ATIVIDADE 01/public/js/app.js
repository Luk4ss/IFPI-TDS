const salarioInicial = document.getElementById('salarioInicial');
const percentualAplicado = document.getElementById('percentualAplicado');
const valorAumento = document.getElementById('valorAumento');
const novoSalario = document.getElementById('novoSalario');
const resultado = document.getElementById('resultado');
const erros = document.getElementById('erros');
const error = document.getElementById('error');

function reajustar(){
    try{
        limpaCamposDeResposta();
        const salario = parseFloat(document.getElementById('salario').value.replace(",", "."));
        var salarioReajustado = 0;
        var reajuste = 0;0
        var percentual = 0;           
        if(isNaN(salario))      throw "Erro! Você digitou um dado inválido!";
        else if(salario <= 0)   throw "Não existe salários menores ou iguais a zero!";

        else if(salario < 280){
            percentual = 0.20;
            reajuste = salario * percentual;
            salarioReajustado = salario + reajuste;
        }
        else if(salario < 700){
            percentual = 0.15;
            reajuste = salario * percentual;
            salarioReajustado = salario + reajuste;
        }
        else if(salario < 1500){
            percentual = 0.10;
            reajuste = salario * percentual;
            salarioReajustado = salario + reajuste;
        }
        else{   
            percentual = 0.05;
            reajuste = salario * percentual;
            salarioReajustado = salario + reajuste;
        }
        
        resultado.className="mostrar";
        salarioInicial.innerHTML += "<strong> R$ " + salario.toFixed(2).replace(".", ",") + "</strong>.";
        percentualAplicado.innerHTML += "<strong> " + percentual*100 + "%</strong>."; 
        valorAumento.innerHTML += "<strong> R$ " + reajuste.toFixed(2).replace(".", ",") + "</strong>.";
        novoSalario.innerHTML += "<strong> R$ " + salarioReajustado.toFixed(2).replace(".", ",") + "</strong>.";
       
            
        
    }
    catch(err){
        erros.className = "mostrar";
        error.innerHTML =  err;
    }
    
}

function limpaCamposDeResposta(){
    resultado.className ="esconder";
    erros.className = "esconder";
    error.innerHTML = "";
    salarioInicial.innerHTML = "Salário antes do reajuste: ";
    percentualAplicado.innerHTML = "Percentual do aumento aplicado: ";
    valorAumento.innerHTML = "Valor do aumento: ";
    novoSalario.innerHTML = "Novo Salário, após o aumento: ";
}