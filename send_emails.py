import win32com.client
import pandas as pd
from datetime import datetime

leads = pd.read_csv('./emails.csv')

outlook = win32com.client.Dispatch('outlook.application')

def formatFirstName(name):
    formated_name = name.split()[0].capitalize()
    return formated_name

emails_sended = 0
for index, lead in leads.iterrows():
    if not lead.was_email_sended:
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
            Marcello Infante
            """
        mail.To = lead.email
        mail.Send()
        leads.iloc[index, 3] = True
        leads.iloc[index, 4] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        emails_sended += 1

leads.to_csv("./emails.csv", index=False)

print(f'Emails enviados: {str(emails_sended)}')

