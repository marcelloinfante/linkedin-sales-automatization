import win32com.client

outlook = win32com.client.Dispatch('outlook.application')
mail = outlook.CreateItem(0)

mail.To = 'marcelloinfantee@gmail.com'
mail.Subject = 'Sample Email'
mail.Body = "This is the normal body"
mail.HTMLBody = '<h3>This is HTML Body</h3>'

mail.Send()