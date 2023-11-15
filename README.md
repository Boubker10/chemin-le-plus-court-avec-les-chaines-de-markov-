Problème voyageur de Commerce ( Chaines de Markov ) 

Problème du Voyageur de Commerce (PVC)
Description
Le Problème du Voyageur de Commerce (PVC) est un problème classique d'optimisation combinatoire. Un voyageur de commerce, basé dans la ville 
�
1
v1, doit visiter les villes 
�
2
,
.
.
.
,
�
�
v2,...,vm avant de revenir à son point de départ. Connaissant les distances entre toutes ces villes, l'objectif est de déterminer l'ordre de visite qui minimise la distance totale parcourue.

Hypothèses Initiales
Les positions des 
�
m villes sont supposées être distribuées uniformément et de manière indépendante dans le carré 
[
0
,
1
]
2
[0,1] 
2
 . La distance entre deux villes 
�
�
vi et 
�
�
vj est notée 
�
(
�
�
,
�
�
)
d(vi,vj).

Formulation Mathématique
Soit 
�
=
(
�
1
,
.
.
.
,
�
�
)
σ=(σ1,...,σ 
m
​
 ) une permutation de l'ensemble 
�
1
,
.
.
.
,
�
�
v1,...,vm. 
�
σ représente un chemin possible pour le voyageur. Le PVC consiste à trouver un chemin 
�
σ minimisant la distance totale parcourue 
�
(
�
)
H(σ), définie par :

�
(
�
)
=
∑
�
=
1
�
−
1
�
(
�
�
,
�
�
+
1
)
+
�
(
�
�
,
�
1
)
H(σ)=∑ 
i=1
m−1
​
 d(σ 
i
​
 ,σ 
i+1
​
 )+d(σ 
m
​
 ,σ 
1
​
 )

Explosion Combinatoire
La recherche exhaustive de la meilleure solution devient impraticable à mesure que 
�
m augmente, en raison de l'explosion combinatoire.

Optimisation Stochastique
Les algorithmes d’optimisation stochastique, tels que le recuit simulé, sont utilisés pour résoudre ce problème. La mesure de Gibbs à température 
�
>
0
T>0, définie sur l'ensemble des permutations 
�
E, est :

�
�
�
(
�
)
=
1
�
�
�
−
1
�
�
(
�
)
IPT(σ)= 
Z 
T
​
 
1
​
 e 
− 
T
1
​
 H(σ)
 

où 
�
�
Z 
T
​
  est la constante de normalisation.

Recuit Simulé
Le recuit simulé est une méthode MCMC pour simuler la mesure de probabilité IPT. La température 
�
T est ajustée au cours du temps pour équilibrer l'exploration de l'espace de solutions et l'exploitation des minima locaux.

Théorème de Convergence
Un schéma de température spécifique assure la convergence de l'algorithme du recuit simulé :

∀
�
∈
�
∗
,
∀
�
∈
]
�
(
�
−
1
)
ℎ
,
�
�
ℎ
]
,
�
(
�
)
:
=
1
�
∀k∈N 
∗
 ,∀n∈]e 
(k−1)h
 ,e 
kh
 ],T(n):= 
k
1
​
 

Il existe 
ℎ
∗
>
0
h 
∗
 >0 tel que pour tout 
ℎ
>
ℎ
∗
h>h 
∗
 , l'algorithme converge.
