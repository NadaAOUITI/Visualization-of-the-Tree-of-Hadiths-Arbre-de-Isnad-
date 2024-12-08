import pandas as pd

class Narrateur:
    def __init__(self, الاسم, الراوي=None, ميلاد=None, وفاة=None):
        self.الاسم = الاسم
        self.الراوي = الراوي
        self.ميلاد = ميلاد
        self.وفاته = وفاة


    def __repr__(self):
        return f"(الاسم={self.الاسم}, الراوي={self.الراوي}, ميلاد={self.ميلاد}, وفاته={self.وفاته})"


def load_narrateurs(file_path):
    narrateurs = {}
    try:
        narrateurs_data = pd.read_excel(file_path)
        for _, row in narrateurs_data.iterrows():
            narrateur = Narrateur(
                الاسم=row["الاسم"],
                الراوي=row["الراوي"],
                ميلاد=row.get("ميلاد"),
                وفاة=row.get("وفاة")
            )
            narrateurs[narrateur.الاسم] = narrateur

    except FileNotFoundError:
        print(f"Erreur: Fichier non trouvé. Vérifiez votre chemin d'accès svp !")
    return narrateurs


file_path = r"annexe2_2hadith2.xlsx"
narrateurs = load_narrateurs(file_path)

for key, value in narrateurs.items():
    print(key, value, '\n')

def cr_nr():
    nom = input(":الاسم ")
    nom_nar = input(": الراوي ")
    narrateur = Narrateur(الاسم=nom, الراوي=nom_nar)
    return narrateur


def aj_nr(narrateur):
    if narrateur.الاسم not in narrateurs:
        narrateurs[narrateur.الاسم] = narrateur

        new_data = pd.DataFrame([{
            "الاسم": narrateur.الاسم,
            "الراوي": narrateur.الراوي,
            "ميلاد": narrateur.ميلاد,
            "وفاة": narrateur.وفاته
        }])

        existing_narrateurs = pd.read_excel(r"annexe2_2hadith2.xlsx")


        updated_narrateurs = pd.concat([existing_narrateurs, new_data], ignore_index=True)

        updated_narrateurs.to_excel(r"annexe2_2hadith2.xlsx", index=False)
        print("Ajout réalisé avec succès ! \n")
    else:
        print("Erreur / Le narrateur existe déjà ! \n")

def save_narrateurs_to_excel(narrateurs):

    data = []
    for narrateur in narrateurs.values():
        data.append({
            "الاسم": narrateur.الاسم,
            "الراوي": narrateur.الراوي,
            "ميلاد": narrateur.ميلاد,
            "وفاة": narrateur.وفاته
        })
    narrateurs_df = pd.DataFrame(data)
    

    narrateurs_df.to_excel(r"annexe2_2hadith2.xlsx", index=False)  
    print("Les modifications ont été sauvegardées dans le fichier Excel.")

def md_nr(narrateur, narrateurs):
    if narrateur.الاسم in narrateurs:
        print("Narrateur trouvé. Modifiez les détails :")
        nouveau_nom = input("Nouveau nom (ou laissez vide pour ne pas modifier) : ")
        nouveau_raoui = input("Nouveau raoui (ou laissez vide pour ne pas modifier) : ")
        nouveau_milad = input("Nouvelle date de naissance (ou laissez vide pour ne pas modifier) : ")
        nouveau_wafato = input("Nouvelle date de décès (ou laissez vide pour ne pas modifier) : ")


        old_name = narrateur.الاسم

 
        if nouveau_nom:
            narrateur.الاسم = nouveau_nom 

        if nouveau_raoui:
            narrateur.الراوي = nouveau_raoui  

        if nouveau_milad:
            narrateur.ميلاد = nouveau_milad 

        if nouveau_wafato:
            narrateur.وفاته = nouveau_wafato  

  
        narrateurs[narrateur.الاسم] = narrateur  
        if old_name != narrateur.الاسم:
            narrateurs.pop(old_name, None)  

        
        save_narrateurs_to_excel(narrateurs)
    else:
        print("Erreur : Narrateur non trouvé dans le dictionnaire.")

def sp_nr(narrateur):
    if narrateur.الاسم in narrateurs:
        del narrateurs[narrateur.الاسم]

        narrateurs_df = pd.read_excel(r"annexe2_2hadith2.xlsx")

        narrateurs_df = narrateurs_df[~((narrateurs_df["الاسم"] == narrateur.الاسم) & (narrateurs_df["الراوي"] == narrateur.الراوي))]

        narrateurs_df.to_excel(r"annexe2_2hadith2.xlsx", index=False)
        
        print("Suppression réalisée avec succès ! \n")
    else:
        print("Erreur : Narrateur non trouvé ! \n")

def rc_nr():
    nom = input(":الاسم à rechercher : ")
    nom_nar = input(":الراوي à rechercher (laisser vide si non applicable) : ")
    trouve = False

    if nom in narrateurs:
        narrateur = narrateurs[nom]
        if not nom_nar or narrateur.الراوي == nom_nar:
            trouve = True
            print(f"Narrateur trouvé : {narrateur}\n")
    
    if not trouve:
        print("Narrateur non trouvé.")

