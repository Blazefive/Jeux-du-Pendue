from random import*

def pendue():
    Mot_probable=["BONJOUR","ORDINATEUR","SOURIS","ZERO"",ANGLE", "ARMOIRE", "BANC", "BUREAU","CABINET", "CARREAU", "CHAISE", "CLASSE","POINTE", "MINE", "GOMME","DESSIN", "COLORIAGE", "RAYURE", "PEINTURE","PINCEAU", "COULEUR", "CRAIE","PAPIER","FEUILLE", "CAHIER", "CARNET","CARTON", "CISEAUX"]
    deja_essayer=[]
    masquer=[]
    compteur=0
    I=randint(0,len(Mot_probable)-1)
    a_chercher=Mot_probable[I]
    masquer.append(a_chercher[0])
    for i in range (0,len(a_chercher)-1):
        masquer.append("*")
    for k in range(0,7):
        print('\n \n')
        print ("Compteur :",compteur," /  7")
        print("Voici votre mot :",masquer)
        compteur=compteur+1
        x=input(str("Tapez La lettre choisit ou tapez 1 pour proposez un mot !"))
        x=x.upper()
        if len(x)!=1:
            compteur=compteur-1
            print ("Veuillez ne renseigné que une seul lettre !")
        else :
            if x=="1":
                print('\n')
                print ("Proposez un mot")
                print("Voici votre mot :",masquer)
                proposition=input(str())
                if proposition==a_chercher:
                    print('\n \n \n \n')
                    return ("Bravo vous avez trouvé ! Le mot était "+a_chercher+" !")
                else :
                    print ("Bien essayer mais ce n'est pas cela !")
            else :
                if compteur==7:
                    return ("Trop d'éssai")
                else :
                    if x in deja_essayer:
                        compteur=compteur-1
                        print ("Cette lettre a déja été dite !")
                    else:
                        deja_essayer.append(x)
                        if x in a_chercher:
                            for y in range (1,len(masquer)):
                                if a_chercher[y]==x:
                                    masquer[y]=x
                        else :
                            print ("Cette lettre n'est pas dans le mot !")
    return masquer
















print(pendue())