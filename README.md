# Bots do Linkedin
O propósito desse repositório é automatizar processos na ferramenta do Linkedin Sales para a Foremind.

Automações disponíveis:
- Conexão com leads
- Captura de e-mails
- Envio de e-mails

## Como iniciar:
1. Clone o repositório
2. Instale as dependências
`pip install -r requirements.txt`
3. Insira as variáveis de ambiente em um arquivo .env na raiz do projeto
4. Insira o arquivo "linkedin-bots-0a9b8a844a62.json" na raiz do projeto

## Como utilizar a "Conexão de leads"
1. Abra o arquivo "connect.py"
2. Insira a url da lista de leads que quer conectar na variável "leads_urls"
3. Inicie a automação:
`python connect.py`
4. Insira quantas conexões quer enviar e pressione ENTER

 ### Avisos importantes:
 Use a conexão de leads com bom-senso para evitar problemas com o Linkedin.
 Caso esteja tendo problemas para realizar o login, comente a linha "login(driver)" e coloque um "input()" na linha abaixo.
 Em seguida, realize o login e pressione ENTER no terminal.
 
 ## Como utilizar a "Captura de e-mails"
 1. Inicie a automação:
 `python get_emails.py`
 
 **A automação vai pegar todos os e-mails disponíveis dos leads salvos e vai inserir em um Spreedsheets.
 Link do Spreedsheets: https://docs.google.com/spreadsheets/d/1-WfetvgA963wluXNIFxjUDnQcwLqpn7zD2Bu1Z1KRD8/edit#gid=1504590139
 
 ## Como utilizar o "Envio de e-mails":
 ** Ele somente funciona pelo Windows
 
 1. Instale o aplicativo do Outlook
 2. Faça login com a seu conta da Foremind no aplicativo
 3. Inicie a automação:
 `python send_emails.py`
 4. Digite quantos e-mails quer enviar e pressione ENTER
 
 ** A automação vai pegar os e-mails do Spreadsheets, vai enviar os e-mails e vai atualizar a tabela.
