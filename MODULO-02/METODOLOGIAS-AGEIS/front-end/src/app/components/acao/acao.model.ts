export interface Acao{
    id?: number
    taxaB3?: number
    valorTotal?: number
    codigo: string,
    valorUnitario: number,
    quantidade: number,
    taxaCorretagem: number,
    operacao: string,
    data: string
}