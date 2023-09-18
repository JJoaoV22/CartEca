def enviar(data, remetente, destinatario, corpo):
    t = open(f'./cartas/{remetente}-{destinatario}.txt', "w")
    t.write(f'''    
    Data:           {data}
    Remetente:      {remetente}
    Destinatario:   {destinatario}
    Corpo:          {corpo}''')
