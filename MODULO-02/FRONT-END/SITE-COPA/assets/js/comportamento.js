//alert("HI JS!");


function app(){

    const nome = document.getElementById("input_nome");

    const botao = document.getElementById("btn_saudacao");

    //alert('SEJA BEM-VINDO, ' + nome.value);

    botao.addEventListener('click', ()=>{
     //   alert("Hello, " + nome.value)

        const paragraph = document.querySelector("h2");

       // paragraph.innerHTML = nome.value;
        paragraph.innerText = nome.value;
        
    });
};

app()