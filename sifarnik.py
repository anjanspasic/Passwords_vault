sifre={}

while True:

    print('1. Unesite aplikaciju i sifru \n 2. Prikazi aplikacije i njihove sifre \n 3.Izmeni sifru \n 4.Obrisi sifru \n 5.Obrisi aplikaciju')

    odabir=input('Odaberite sta hocete: ')


    if odabir not in ['1','2','3','4','5']:
        print('Ne moze')

    if odabir=='1':
        aplikacija=input('Koja aplikacija')
        sifra=input('Koja je sifra')
        sifre[aplikacija]=sifra

    if odabir=='2':
        for aplikacija,sifra in sifre.items():
            print(f'{aplikacija} : {sifra}')


    if odabir=='3':
        pass

    if odabir=='4':
        pass

    if odabir=='5':
        
        break

