alfabet = 'AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻaąbcćdeęfghijklłmnńoóprsśtuwyzźż '
litery = [litera for litera in alfabet]
#print(litery)

def szyfruj_znak(znak, klucz):
    return chr((ord(znak) - 97 + klucz) % 26 + 97)

def szyfruj(tekst, klucz):
    pom = ""
    for znak in tekst:
        pom = pom + szyfruj_znak(znak, klucz)

    return pom

def deszyfruj(tekst, klucz):
    return szyfruj(tekst, 26-klucz)

def szyfruj_znak_pl(znak, klucz):
    for i, litera in enumerate(litery):
        if znak == litera: 
            return litery[(i+klucz)%65]

def szyfruj_pl(tekst, klucz):
    pom = ""
    for znak in tekst:
        pom = pom + szyfruj_znak_pl(znak, klucz)
    return pom

def deszyfruj_pl(tekst, klucz):
    return szyfruj_pl(tekst, 65-klucz)

#print(szyfruj("tajne", 3))
#print(deszyfruj("wdmqh", 3))

#łamanie szyfru
#for i in range(1,27):
    #print(i, deszyfruj('xvrqlfcbgxnavr', i))

zaszyfrowany = szyfruj_pl("Cześć kiedy spotkanie", 3)
odszyfrowany = deszyfruj_pl(zaszyfrowany, 3)

print(zaszyfrowany)
print(odszyfrowany)