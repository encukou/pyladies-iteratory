def vypis(iterator):
    """Vypise polozky iteratoru"""
    for hodnota in iterator:
        print hodnota

def rozdel_podle_carek(iterator):
    """Kazdy radek rozdeli podle ','

    ocekava iterator retezcu
    vraci iterator seznamu
    """
    for radek in iterator:
        yield radek.split(',')

def vyber_jmeno(iterator):
    """Vybere prvni polozku kazdeho seznamu

    ocekava iterator seznamu
    vraci iterator retezcu
    """
    for polozky in iterator:
        yield polozky[0]

def filtruj_prijmeni_a(iterator):
    """Vybere jen jmena s prijmenim koncicim na A

    ocekava iterator retezcu
    vraci iterator retezcu
    """
    for jmeno in iterator:
        casti_jmena = jmeno.split()
        prijmeni = casti_jmena[-1]
        if prijmeni[0] == 'A':
            yield jmeno

def vyber_krestni(iterator):
    """Vybere jen krestni jmena

    ocekava iterator retezcu
    vraci iterator retezcu
    """
    for jmeno in iterator:
        casti_jmena = jmeno.split()
        while casti_jmena[0][-1] == '.':
            casti_jmena = casti_jmena[1:]
        yield casti_jmena[0]

with open('informace.txt') as soubor:
    # soubor je iterator retezcu
    # (pro kazdy radek jeden)

    vypis(
        vyber_krestni(
        filtruj_prijmeni_a(
        vyber_jmeno(
        rozdel_podle_carek(soubor)))))
