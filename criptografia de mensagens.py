mensagem=input("digite a sua mensagem")

cripitografada=""


for letra in mensagem:
    cripitografada+=chr(ord(letra)+3)

print ("mensagem cripitografa:",cripitografada)


mensagem=input("digite a sua mensagem ")

descripitografada=""

for letra in mensagem:
    descripitografada+=chr(ord(letra)-3)

    print ("mensagem descripitografada:",descripitografada)