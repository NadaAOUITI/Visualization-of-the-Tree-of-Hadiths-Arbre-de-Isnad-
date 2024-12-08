import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import arabic_reshaper
from bidi.algorithm import get_display
from Narrateur import Narrateur, narrateurs
from Arbredeisnedv2 import chains  
from collections import deque
#Ceci est le fichier main à exécuter .
#J'ai inlcus les fichiers xlsx parceque je l'ai modifié (la méthode de diacritisation d'un meme nom etc)
 #Méthode de re-ing : Donner un niveau à chaque noeud.
        #Pour chaque nœud, la position horizontale est déterminée par le nombre de nœuds déjà sur ce niveau. La position verticale est simplement le niveau négatif du nœud pour créer un agencement de haut en bas.
        #x le niveau 0  
        #tous les neouds de niveau 1 ont x=1 
        #tous les noeuds de niveau 2 ont x=2 et y=-2

class GrapheDeNarrateurs:
    def __init__(self):
        self.adj_list = {}

    def ajouter_narrateur(self, narrateur):
        if narrateur.الاسم not in self.adj_list:
            self.adj_list[narrateur.الاسم] = []
           
            narrateurs[narrateur.الاسم] = narrateur

    def supprimer_narrateur(self, nom):
        if nom in self.adj_list:
            del self.adj_list[nom]
            for connexions in self.adj_list.values():
                if nom in connexions:
                    connexions.remove(nom)
        else:
            print(f"Le narrateur {nom} n'existe pas dans le graphe.")

    def ajouter_connexion(self, nom1, nom2):
        if nom1 in self.adj_list and nom2 in self.adj_list:
            if nom2 not in self.adj_list[nom1]:
                if (nom2 in self.adj_list and narrateurs[nom2].وفاته and
                        narrateurs[nom1].وفاته):
                    diff_years = (pd.to_datetime(narrateurs[nom2].وفاته) - pd.to_datetime(narrateurs[nom1].وفاته)).days / 365.25
                    if abs(diff_years) <= 40:
                        self.adj_list[nom1].append(nom2)
                        print(f"La connexion {nom1}->{nom2} est ajoutée avec succès !")
                    else:
                        print(f"{nom2} est trop éloigné en date de décès par rapport à {nom1}.")
                else:
                    self.adj_list[nom1].append(nom2)
                    print(f"La connexion {nom1}->{nom2} est ajoutée sans comparaison des dates.")
        else:
            print(f"Un des narrateurs {nom1} ou {nom2} n'existe pas.")

    def supprimer_connexion(self, nom1, nom2):
        if nom1 in self.adj_list and nom2 in self.adj_list[nom1]:
            self.adj_list[nom1].remove(nom2)
        else:
            print(f"Pas de connexion / narrateurs n'existent pas.")

    def rechercher_narrateur(self, nom):
        return self.adj_list.get(nom, None)

    def inserer_chaines_dans_graphe(self, chains, graphe, root_node):
        
        narrateur_successors = {}

        
        for chain_key, chain in chains.items():
            previous_narrator = None 

            for i, narrateur in enumerate(chain):
                
                if narrateur not in graphe.adj_list:
                    graphe.ajouter_narrateur(Narrateur(narrateur))

                
                if narrateur not in narrateur_successors:
                    narrateur_successors[narrateur] = set()

                if previous_narrator:
                    
                    narrateur_successors[previous_narrator].add(narrateur)

               
                previous_narrator = narrateur

    
        for narrateur, successors in narrateur_successors.items():
            for successor in successors:
                
                graphe.ajouter_connexion(narrateur, successor)

        if chains:
       
            for chain_key, chain in chains.items():
                if chain:  
                    first_narrateur = chain[0]
                    graphe.ajouter_connexion(root_node, first_narrateur)  
    def calculer_positions_layers(self, root_node):
        niveaux = {}
        pos = {}
        queue = deque([(root_node, 0)]) 
        niveaux[root_node] = 0
        

        while queue:
            node, level = queue.popleft()
            niveaux[node] = level
            for neighbor in self.adj_list[node]:
                if neighbor not in niveaux:
                    queue.append((neighbor, level + 1))
        

        layer_widths = {i: 0 for i in range(max(niveaux.values()) + 1)}
        for node, level in niveaux.items():
            pos[node] = (layer_widths[level], -level)
            layer_widths[level] += 1

        for level in layer_widths:
            offset = layer_widths[level] / 2.0
            for node, (x, y) in pos.items():
                if niveaux[node] == level:
                    pos[node] = (x - offset, y)
                    
        return pos

    def visualiser_graphe(self):
        G = nx.DiGraph()
        for narrateur, connexions in self.adj_list.items():
            G.add_node(narrateur)
            for voisin in connexions:
                G.add_edge(narrateur, voisin)

        # Arabic labels reshaped
        labels = {node: get_display(arabic_reshaper.reshape(node)) for node in G.nodes()}

        # Calculate positions using layers
        pos = self.calculer_positions_layers("الإسناد")

        # Draw the graph
        nx.draw(G, pos, labels=labels, with_labels=True, node_color='lightpink', 
                font_weight='bold', node_size=4000, font_size=7)
        plt.show()

# Create the graph
graphe = GrapheDeNarrateurs()
root_node = "الإسناد"
graphe.ajouter_narrateur(Narrateur(root_node))

# Insert chains into the graph
graphe.inserer_chaines_dans_graphe(chains, graphe, root_node)

# Visualize the graph
graphe.visualiser_graphe()
plt.show()

        #yaati niveau lchaque noeud
        #Pour chaque nœud, la position horizontale est déterminée par le nombre de nœuds déjà sur ce niveau. La position verticale est simplement le niveau négatif du nœud pour créer un agencement de haut en bas.
        #x le niveau 0  
        #tous les neouds de niveau 1 ont x=1 
        #tous les noeuds de niveau 2 ont x=2 et y=-2