import time
import os
os.chdir(r"/var/www/html")

infini = 0
prog = 0

while infini != 1:

    while prog != 1:
    
        #Variable
        operateur = str()
        affaire = str()
        etat = str()
        codeArticle = str()
        fin = str()
        nombreA = str()
        nombreB = str()
        data = str()

        operateur = input("Opérateur : ")
        if operateur == "ANNULE":
            break
        affaire = input("Affaire : ")
        if affaire == "ANNULE":
            break
        etat = input("ENTREE ou SORTIE : ")
        if etat == "ANNULE":
            break
        codeArticle = input("Code Article : ")
        if codeArticle == "ANNULE":
            break

        while (nombreA != "TERMINE"):
            nombreB = nombreB + nombreA    
            nombreA = input ("Nombre article : ")
            if nombreA == "ANNULE":
                break
        if nombreA == "ANNULE":
            break
        
        print (operateur, ";",affaire, ";",etat, ";",codeArticle, ";",nombreB, ";",time.strftime("%d/%m/%Y;%H:%M:%S"))
        data = operateur + ";" + affaire + ";" + etat + ";" + codeArticle + ";" + nombreB + ";" + time.strftime("%d/%m/%Y;%H:%M:%S"+"\n")
        fichierData = open("data.csv", "a")
        fichierData.write(data)
        fichierData.close()


    
