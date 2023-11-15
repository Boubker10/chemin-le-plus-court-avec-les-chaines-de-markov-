import pandas as pd
import math
import folium
import webbrowser
import time
import numpy as np
import random

# Fonction permettant de trouver la distance entre deux villes selon leur latitudes et longitudes
def distance(lat1, lat2, lon1, lon2):
    R = 6372800  # Rayon de la Terre en mètre

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + \
        math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2

    return round((2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))) * 10**(-3), 2)


ville = pd.read_csv('/content/selected.csv', sep=';', header=None)

# Renommez la colonne 0 en 'Info'
ville = ville.rename(columns={0: 'Info'})

# Supprimez les espaces supplémentaires dans la colonne 'Info'
ville['Info'] = ville['Info'].str.strip()

# Séparez les données dans la colonne 'Info' en colonnes distinctes
ville[['Nom Ville', 'MAJ', 'Code Postal', 'Code INSEE', 'Code Région', 'Latitude', 'Longitude', 'Eloignement']] = ville['Info'].str.split(',', expand=True)

# Sélectionnez uniquement les colonnes nécessaires
villes = ville[['Nom Ville', 'Latitude', 'Longitude']].copy()

# Renommez les colonnes
villes.columns = ['Ville', 'Latitude', 'Longitude']

# Conversion des colonnes de latitude et de longitude en types numériques
villes['Latitude'] = pd.to_numeric(villes['Latitude'], errors='coerce')
villes['Longitude'] = pd.to_numeric(villes['Longitude'], errors='coerce')

villes.dropna(subset=['Latitude', 'Longitude'], inplace=True)

villes.reset_index(drop=True, inplace=True)

print(villes)

# Creation d'un DataFrame avec toutes les distances entre chaque ville
dist = pd.DataFrame(index=villes.index, columns=villes.index)
for i in dist.index:
    for j in dist.columns:
        if i != j:
            dist.at[i, j] = distance(villes.at[i, 'Latitude'], villes.at[j, 'Latitude'], villes.at[i, 'Longitude'], villes.at[j, 'Longitude'])
        else:
            dist.at[i, j] = 0.0

def Visualisation_carte(Parcours, lat, long):
    fmap = folium.Map(location=[lat[Parcours[0]], long[Parcours[0]]])
    points = (len(Parcours) + 1) * [0]
    for k in range(len(points) - 1):
        points[k] = lat[Parcours[k]], long[Parcours[k]]
        folium.Marker(points[k]).add_to(fmap)
    points[-1] = lat[Parcours[0]], long[Parcours[0]]
    folium.PolyLine(points, color='blue', weight=2.5, opacity=0.8).add_to(fmap)
    fmap.save('chemin2.html')
    return 0

def Representation(chemin, villes_utilisées):
    lat = len(villes_utilisées) * [0]
    long = len(villes_utilisées) * [0]
    for i in range(len(villes_utilisées)):
        lat[i] = villes_utilisées.iloc[i]['Latitude']
        long[i] = villes_utilisées.iloc[i]['Longitude']
    Visualisation_carte(chemin, lat, long)
    return 0

def Markov_Question2(itération, nbr_villes):
    if nbr_villes > len(villes):
        print("Erreur : nbr_villes dépasse le nombre de villes disponibles.")
        return None

    villes_utilisées = villes.iloc[:nbr_villes]
    X = random.sample(range(nbr_villes), nbr_villes)


    for n in range(0, itération):
        T = 2
        g = list(X)  # g nommé sigma (ou gigma pour les intimes)
        # On crée sigma prime
        g_prime = list(X)
        k = np.random.randint(nbr_villes)
        l = np.random.randint(nbr_villes)

        while k == l:
            k = np.random.randint(nbr_villes)

        intermediaire = g_prime[k]
        g_prime[k] = g_prime[l]
        g_prime[l] = intermediaire

        # Distance de g et distance de g_prime
        h_g = 0
        h_g_prime = 0
        d = 0
        i = 0
        while g[i] != g[-1]:
            h_g = h_g + dist[g[i]][g[i + 1]]
            h_g_prime = h_g_prime + dist[g_prime[i]][g_prime[i + 1]]
            i = i + 1

        h_g = h_g + dist[g[-1]][g[0]]
        h_g_prime = h_g_prime + dist[g_prime[-1]][g_prime[0]]

        rau = math.exp((h_g - h_g_prime) / T)
        if(rau >= 1):
            X = g_prime
            d = h_g_prime
        else:
            d = h_g
            U = random.uniform(0, 1)
            if (U < rau):
                X = g_prime
                d = h_g_prime

    print("chemin retenu:", X)
    print("Meilleure distance:", d)
    Representation(X, villes_utilisées)
    return X


start = time.time()

Markov_Question2(1000, 40)
webbrowser.open('chemin2.html')

end = time.time()
print(end - start, "secondes d'exécution")
print(round((end - start) / 60, 2), "minutes d'exécution")
