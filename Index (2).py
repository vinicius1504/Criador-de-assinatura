import PySimpleGUI as sg
from PIL import Image, ImageDraw, ImageFont
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import json
import os

def load_email_list():
    if not os.path.exists('emails.json'):
        with open('emails.json', 'w') as file:
            json.dump({'emails': []}, file)
    with open('emails.json', 'r') as file:
        data = json.load(file)
        email_list = [entry['email'] for entry in data['emails']]
    return email_list

def save_email_list(email_list):
    with open('emails.json', 'w') as file:
        json.dump({'emails': [{'email': email} for email in email_list]}, file)

def main():
    email_list = load_email_list()

    layout = [
        [sg.Text('Nome da pessoa:'), sg.InputText(key='-NOME-')],
        [sg.Text('Cargo:'), sg.InputText(key='-CARGO-')],
        [sg.Text('Pesquisar e-mails:'), sg.InputText(key='-SEARCH-', enable_events=True)],
        [sg.Text('Selecione o destinatário do e-mail:')],
        [sg.Listbox(values=email_list, size=(30, 6), key='-LISTBOX-')],
        [sg.Text('Mensagem:')],
        [sg.Multiline(size=(60, 5), key='-MENSAGEM-')],
        [sg.Button('Gerar Assinatura'), sg.Button('Enviar E-mail'), sg.Button('Adicionar E-mail'), sg.Button('Excluir E-mail'), sg.Button('Cancelar')]
    ]

    window = sg.Window('Assinatura e Envio de E-mail', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Cancelar':
            break
        elif event == 'Gerar Assinatura':
            nome = values['-NOME-']
            cargo = values['-CARGO-']
            cor = (26, 48, 82)
            img = Image.open('Assinatura.png')
            I1 = ImageDraw.Draw(img)
            I2 = ImageDraw.Draw(img)
            myFont = ImageFont.truetype('MADE TOMMY Bold_PERSONAL USE.otf', 18)
            myFont2 = ImageFont.truetype('MADE TOMMY Regular_PERSONAL USE.otf', 13)
            I1.text((48, 33), nome, font=myFont, fill=cor)
            I2.text((48, 55), cargo, font=myFont2, fill=cor)
            img.save(f"assinatura_{nome}.png")
            sg.popup(f'Assinatura gerada para {nome}')

        elif event == 'Enviar E-mail':
            recipientes_selecionados = values['-LISTBOX-']
            if not recipientes_selecionados:
                sg.popup('Por favor, selecione pelo menos um destinatário.')
                continue

            mensagem = values['-MENSAGEM-']
            arquivo_assinatura = f"assinatura_{values['-NOME-']}.png"
            arquivo_instrucoes = "passo_a_passo_assinatura.pdf"

            for destinatario in recipientes_selecionados:
                enviar_email(destinatario, arquivo_assinatura, arquivo_instrucoes, mensagem)

            sg.popup('E-mail enviado com sucesso!')

        elif event == 'Adicionar E-mail':
            novo_email = sg.popup_get_text('Digite o novo e-mail:')
            if novo_email and novo_email not in email_list:
                email_list.append(novo_email)
                save_email_list(email_list)
                window['-LISTBOX-'].update(values=email_list)
            elif novo_email:
                sg.popup('O e-mail já existe na lista.')

        elif event == 'Excluir E-mail':
            email_selecionado = values['-LISTBOX-']
            if email_selecionado:
                email_list.remove(email_selecionado[0])
                save_email_list(email_list)
                window['-LISTBOX-'].update(values=email_list)
            else:
                sg.popup('Por favor, selecione um e-mail para excluir.')

        elif event == '-SEARCH-':
            search_term = values['-SEARCH-']
            filtered_emails = [email for email in email_list if search_term.lower() in email.lower()]
            window['-LISTBOX-'].update(values=filtered_emails)

    window.close()

def enviar_email(destinatario, arquivo_assinatura, arquivo_instrucoes, mensagem):
    corpo_email = mensagem

    msg = MIMEMultipart()
    msg['Subject'] = "Assinatura email"
    msg['From'] = 'seu_email@example.com'
    recipients = [destinatario]
    msg['To'] = ','.join(recipients)
    password = 'sua_senha_aqui'

    # Adiciona o corpo do e-mail
    msg.attach(MIMEText(corpo_email, 'plain'))

    # Adiciona a assinatura como anexo
    with open(arquivo_assinatura, 'rb') as f:
        arquivo_anexo = MIMEApplication(f.read(), _subtype="png")
    arquivo_anexo.add_header('Content-Disposition', 'attachment', filename=arquivo_assinatura)
    msg.attach(arquivo_anexo)

    # Adiciona o arquivo de instruções como anexo
    with open(arquivo_instrucoes, 'rb') as f:
        arquivo_anexo = MIMEApplication(f.read(), _subtype="pdf")
    arquivo_anexo.add_header('Content-Disposition', 'attachment', filename=arquivo_instrucoes)
    msg.attach(arquivo_anexo)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], recipients, msg.as_string().encode('utf-8'))
    s.quit()

if __name__ == '__main__':
    main()
