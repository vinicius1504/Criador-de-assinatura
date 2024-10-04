<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Documentação do Aplicativo</title>
</head>
<body>
    <h1>Documentação do Aplicativo de Gerenciamento de Emails</h1>
    
  <h2>Motivo da Criação do Aplicativo</h2>
    <p>
        O aplicativo de gerenciamento de emails foi criado para centralizar, organizar e facilitar o controle de uma grande lista de endereços de email. 
        Em muitas empresas, é comum que a comunicação seja realizada através de vários endereços de email distribuídos entre diversos departamentos e funcionários. 
        Manter esses emails atualizados, verificar sua validade e utilizá-los corretamente pode ser uma tarefa desafiadora e propensa a erros.
    </p>
    <p>
        Este aplicativo tem como objetivo simplificar essa tarefa, fornecendo uma interface fácil de usar para gerenciar os endereços de email, permitindo atualizações 
        em massa, verificações rápidas e uma visão clara de todos os emails da empresa. Além disso, ele pode ser utilizado para testes e desenvolvimento, garantindo 
        que os desenvolvedores tenham um conjunto de dados consistente e realista para trabalhar.
    </p>

   <h2>Estrutura do JSON de Emails</h2>
    <p>
        Abaixo está um exemplo da estrutura JSON usada para armazenar os endereços de email. Esta estrutura é simples e permite fácil manipulação e leitura dos dados.
    </p>
    
   <pre>
{
    "emails": [
        {
            "email": "test1@example.com"
        },
        {
            "email": "test2@example.com"
        },
        {
            "email": "test3@example.com"
        },
        {
            "email": "test4@example.com"
        },
        {
            "email": "test5@example.com"
        },
        {
            "email": "test6@example.com"
        },
        ...
    ]
}
    </pre>

  <h2>Funcionalidades do Aplicativo</h2>
    <ul>
        <li>Visualização de todos os endereços de email cadastrados.</li>
        <li>Busca e filtragem de emails por palavras-chave.</li>
        <li>Adição e remoção de emails da lista.</li>
        <li>Atualização em massa dos endereços de email.</li>
        <li>Verificação da validade dos endereços de email.</li>
    </ul>

  <h2>Como Usar o Aplicativo</h2>
    <p>
        Para usar o aplicativo, siga os passos abaixo:
    </p>
    <ol>
        <li>Acesse a interface do aplicativo através da URL fornecida pela sua empresa.</li>
        <li>Navegue até a seção de gerenciamento de emails.</li>
        <li>Use as opções disponíveis para visualizar, adicionar, remover ou atualizar emails conforme necessário.</li>
        <li>Para atualizações em massa, você pode carregar um arquivo JSON com a estrutura mostrada acima.</li>
        <li>Utilize as ferramentas de verificação para garantir que todos os emails na lista são válidos.</li>
    </ol>
    
   <h2>Benefícios do Aplicativo</h2>
    <p>
        O aplicativo de gerenciamento de emails proporciona diversos benefícios, tais como:
    </p>
    <ul>
        <li>Redução de erros na comunicação interna e externa.</li>
        <li>Maior eficiência na gestão de contatos.</li>
        <li>Facilidade na atualização e manutenção de uma lista de
