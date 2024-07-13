"""rechercher fontion"""
import tkinter
def searchuser(biblios):
    search = open(biblios, 'r')
    f = search.readline()
    w=input("Saisir votre recherche ici : ")
    res = False
    nb=0
    liste=[]
    for f in search :
        if w in f :
            res = True
            print(f)
            nb=nb+1
    print("Votre recherche comporte ",nb,"résultats avec le mot '",w,"' :\n")
    if res == False :
        print("Aucun résultat.\n")
    search.close()
    return


#_____________________________________ajouter fontion
def adduser(biblios):
    newuser=["le nom", "le postnom", "le prenom", "l'age", "'matricule"]
    k=0
    while k<5 :
        n=input("Saisir " + newuser[k] + " de l'utilisateur : ")
        newuser[k]=n
        k=k+1
    else :
        v=input("Etes-vous sur d'entrer cet utilisateur ? oui/non ")
        if v=="oui" :
            fichier = open(biblios,'a')
            fichier.write(str(newuser)+"\n")
            fichier.close()
            print(newuser[0]+" de "+newuser[1]+", ("+newuser[2]+", "+newuser[3]+"), "+" matricule: "+newuser[4]+" a été ajouté avec succès.")
        elif v=="non" :
            q=input("Voulez-vous entrer cet utilisateur à nouveau ? oui/non ")
            if q=="oui" :
                adduser(biblios)
            elif q=="non" :
                return
        else :
            print("Votre choix n'est ni un 'oui' ni un 'non'. Veuillez recommencer s'il vous plaît.")
    return


#__________________________________supprimer_fonction
def delete(biblios):
    d=input("Saisir un élément de l'utilisateur à SUPPRIMER : ")
    with open(biblios, 'r') as source, open(trash, 'w') as target:
        for l in source :
            if not d in l :
                target.write(l)
        source.close()
        target.close()
    with open(trash, 'r') as source, open(biblios, 'w') as target:
        for l in source :
            target.write(l)
        source.close()
        target.close()
    return


#____________________________________afficher_fontion
def alluser(biblios):
    show = open(biblios, 'r')
    f = show.read()
    print("Voici la liste des utilisateurs : ")
    print(f)
    show.close()
    return
#________________________MAIN________________________
biblios = 'biblios.txt'
trash = 'trash.txt'

print("1. Ajouter un utilisateur")
print("2. Rechercher un utilisateur")
print("3. Supprimer un utilisateur")
print("4. Afficher tous les utilisateurs")
print("0. Quitter le programme")

choix=int(input("Que voulez vous faire ?"))

while (choix < 5):
    if choix==1:
        adduser(biblios)
    elif (choix == 0):
        print("ce projet a été réalisé par\n: 1.CIKURU MUSHARAMINA GEDEON\n2.DIBWE GEORGE STEPHANE\n3.DINUMBE KITENGE MARDOCHEE\n4.DJUMA MUSSA RODRIGUE ")
        import sys
        sys.exit()     
    elif choix==2:
        searchuser(biblios)
    elif choix==3:
        delete(biblios)
    elif choix==4:
        alluser(biblios)
    else :
        print("Votre choix n'est pas disponible. Essayez encore.")
    
    print("1. Ajouter un utilisateur")
    print("2. Rechercher un utilisateur")
    print("3. Supprimer un utilisateur")
    print("4. Afficher tous les utilisateurs")
    print("0. Quitter le programme")
    choix=int(input("\nQue voulez vous faire ?\n"))



