import { Component, OnInit } from '@angular/core';
import { Acao } from '../acao.model';
import {Router} from '@angular/router'
import { AcaoService } from '../acao.service';


@Component({
  selector: 'app-acao-create',
  templateUrl: './acao-create.component.html',
  styleUrls: ['./acao-create.component.css']
})
export class AcaoCreateComponent implements OnInit {

  tipos_operacao = ['COMPRA', 'VENDA']

  acao:Acao = {
    codigo: '',
    valorUnitario: 0.0,
    quantidade: 0,
    taxaCorretagem: 0.0,
    operacao: 'COMPRA',
    data: '01/01/1991'

  }
  constructor(private router:Router, private acaoService: AcaoService) { }

  ngOnInit(): void {
  }

  onSaveAcao():void{
    this.acao.taxaB3 = this.acao.valorUnitario * this.acao.quantidade * 0.0003;
    if(this.acao.operacao == "COMPRA"){
      this.acao.valorTotal = this.acao.valorUnitario * this.acao.quantidade  + this.acao.taxaB3 + this.acao.taxaCorretagem;
    }
    else{
      this.acao.valorTotal = this.acao.valorUnitario * this.acao.quantidade  - this.acao.taxaB3 - this.acao.taxaCorretagem;
    }
    console.log(this.acao)
    this.acaoService.insert(this.acao).subscribe(
      () =>{
        this.navigateToAcoes();
      }
    )
  }


  navigateToAcoes():void{
    this.router.navigate(['/acoes'])
  }

  tpOperacao(entry: string):void{
    this.acao.operacao = entry;
  }

}
