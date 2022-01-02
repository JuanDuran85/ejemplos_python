import pywhatkit as kit

try:
    kit.sendwhatmsg('+34645885123', 'Pajuo', 15, 13, 6)
    #kit.sendwhatmsg_instantly('+584245504420', 'Mensaje enviado automaticamente con Python mediante PyWhatkit', 15, True, 5)
except Exception as e:
    print(e)