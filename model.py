def enviar(data, remetente, destinatario, corpo):
    with open(f'./cartas/{remetente}-{data}.txt', "w") as txt:
        txt.write(f'''    
        Data:           {data}
        Remetente:      {remetente}
        Destinatario:   {destinatario}
        Corpo:          {corpo}''')
