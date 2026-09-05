[README.md](https://github.com/user-attachments/files/31866609/README.md)
# Café & Biscoito — Caixa, Estoque & IA

Aplicativo de gestão que funciona localmente no Windows, sem servidor, compilador ou API obrigatória. Caixa e estoque são salvos automaticamente no computador e a planilha do Excel é atualizada após cada alteração.

## Como abrir

1. Abra a pasta `entrega`.
2. Dê dois cliques em `Cafe-e-Biscoito-1.0.0-Portatil.exe`.
3. O aplicativo abre em uma janela própria; não depende do navegador.

O executável portátil pode ser copiado para outro computador Windows de 64 bits. Os dados permanecem locais em cada computador.

## O que está incluído

- Painel com saldo, entradas, saídas, estoque e alertas.
- Registro de vendas, compras, receitas e despesas.
- Atualização automática do estoque a cada venda ou compra.
- Salvamento local e automático, com gravação atômica para reduzir risco de arquivo incompleto.
- Cadastro e edição de produtos, estoque mínimo, custo e preço de venda.
- Relatório gerencial mensal com resultado, margem e produtos mais vendidos.
- Planilha Excel `.xlsx` automática com Resumo, Produtos, Movimentações, Resumo IA e Controles.
- Assistente inteligente local para resumir caixa, margem e prioridades sem enviar dados para a internet.
- Cópia de segurança e restauração em arquivo JSON.

## Onde os arquivos ficam

- Dados do aplicativo: `%APPDATA%\cafe-e-biscoito\dados-cafe-e-biscoito.json`
- Excel automático: `Documentos\Café & Biscoito\Controle_Cafe_e_Biscoito.xlsx`

O caminho da planilha pode ser alterado em **Configurações**.

## Cuidados

- Gere uma cópia de segurança periodicamente em **Configurações**.
- Feche a planilha no Excel antes de sincronizar novamente, caso o Excel bloqueie o arquivo.
- Os relatórios e resumos são gerenciais e não substituem escrituração fiscal, conciliação bancária ou orientação de um contador.

## Desenvolvimento

```powershell
& 'C:\Program Files\nodejs\npm.cmd' run check
& 'C:\Program Files\nodejs\npm.cmd' run test:xlsx
& 'C:\Program Files\nodejs\npm.cmd' run start
& 'C:\Program Files\nodejs\npm.cmd' run dist:portable
```
