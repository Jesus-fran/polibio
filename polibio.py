print("=========================");
print("");
print("   CIFRADO POLIBIO");
print("");
print("========================");
print("");
print("");

pal = {'A':11, 'B':12, 'C':13, 'D':14, 'E':15, 'F':21, 'G':22, 'H':23, 'I':24, 'J':24, 'K':25,'L':31, 'M':32, 'N':33, 'Ñ':33, 'O':34, 'P':35, 'Q':41, 'R':42, 'S':43, 'T':44, 'U':45, 'V':51, 'W':52, 'X':53, 'Y':54, 'Z':55};
num_pal = {'11':'A', '12':'B', '13':'C', '14':'D', '15':'E', '21':'F', '22':'G', '23':'H', '24':'I', '24':'J', '25':'K','31':'L', '32':'M', '33':'N', '34':'O', '35':'P', '41':'Q', '42':'R', '43':'S', '44':'T', '45':'U', '51':'V', '52':'W', '53':'X', '54':'Y', '55':'Z'};

option = '';

def menu():
    print("Eliga una opción: ");
    print("");
    print("1. Cifrar una palabra");
    print("2. Descifrar una palabra");
    print("");
    return input("Opción: ");

option = menu();

def cifrar(txt_plano):
    txt_cifrado = '';
    if txt_plano.isnumeric():
        return "Ingrese texto, bye :(";
    for caracter in txt_plano.replace(" ", ""):
        if caracter.isnumeric():
            return "Ingrese texto, bye :(";
        txt_cifrado += str(pal[caracter.upper()])+" ";
    print("Cifrado: ");
    print("");
    return txt_cifrado;

def descifrar(caracter):
    txt_descrifrado = '';
    if txt_plano.isalpha():
        return "Ingrese numeros, bye :(";
    cont = 0;
    num_par = '';
    for caracter in txt_plano.replace(" ", ""):
        cont += 1;
        if caracter.isalpha():
            return "Ingrese numeros, bye :(";
        num_par += str(caracter);
        if (cont%2)==0:
            txt_descrifrado += str(num_pal[num_par]);
            num_par = '';
    print("Descifrado: ");
    print("");
    return txt_descrifrado;

if option == '1':
    print("");
    txt_plano = input("Ingrese un texto a cifrar: ");
    print("");
    print(cifrar(txt_plano));

elif option == "2":
    print("");
    txt_plano = input("Ingrese numeros para descifrar: ");
    print("");
    print(descifrar(txt_plano));
else:
    print("");
    print("Elige una opción correcta, bye :(");