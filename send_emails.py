import win32com.client
import pygsheets

from datetime import datetime
from decouple import config

from utils import get_leads_data_from_spreadsheets


number_of_emails = int(input('Quantos e-mails você quer enviar: '))

your_name = config('YOUR_NAME')

leads = get_leads_data_from_spreadsheets()

outlook = win32com.client.Dispatch('outlook.application')

def formatFirstName(name):
    formated_name = name.split()[0].capitalize()
    return formated_name

def add_changes_to_spreadsheets(leads):
    gc = pygsheets.authorize(service_file='linkedin-bots-0a9b8a844a62.json')
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1-WfetvgA963wluXNIFxjUDnQcwLqpn7zD2Bu1Z1KRD8/edit#gid=1504590139')
    wks = sh[0]
    wks.set_dataframe(leads, 'A1')

emails_sended = 0
for index, lead in leads.iterrows():
    if emails_sended == number_of_emails:
        break

    if lead.was_email_sended == 'FALSE':
        mail = outlook.CreateItem(0)
        mail.Subject = 'A sua experiência seria muito útil'
        name = formatFirstName(lead['name'])
        mail.HTMLBody = f"""
            Olá {name},
            <br />
            <br />
            Eu peguei o seu contato no Linkedin. Como eu imagino que você é uma pessoa<br />
            muito ocupada e tem muitas mensagens, esse email levará somente 60 segundos<br />
            para ser lido.<br />
            <br />
            Meu nome é Marcello Infante, eu sou Engenheiro de Software na Foremind.<br />
            Lá, a minha função é desenvolver algorítimos e aplicações para democratizar<br />
            o acesso a tecnologias de Inteligência Artificial e Machine Learning<br />
            para pequenas e médias empresas.<br />
            <br />
            Estamos desenvolvendo o nosso produto e estamos em busca de usuários beta<br />
            para testarem a nossa plataforma de forma gratuita. Eu vi no seu perfil que<br />
            com a sua experiência nos poderíamos tirar insights valiosos sobre<br />
            como melhorar nosso produto.<br />
            <br />
            Se eu conseguir um horário na minha agenda, podemos marcar uma call essa semana?<br />
            <br />
            Atenciosamente,<br />
            <br />
            <br />
            {your_name}
            """
        mail.To = lead.email
        mail.Send()
        leads.iloc[index, 3] = True
        leads.iloc[index, 4] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        leads.iloc[index, 5] = your_name
        emails_sended += 1

add_changes_to_spreadsheets(leads)

print(f'Emails enviados: {str(emails_sended)}')
