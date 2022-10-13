- Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses
volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?

Le pipeline conçu dans cette solution reste très basique pour répondre à ce besoin dans l'état.
La manière, dont on vérifie la mention d'un médicament dans publication médicale ou un essai clinique, reste à améliorer. 
Dans le cas d'un flux important de données, le pipeline pourrait avoir une performance médiocre à cause d'une complexité exponentielle dans l'état. 


- Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de
telles volumétries ?

L'exploration de d'autres frameworks de traitement de données en grande volumétrie pourrait être intéressante. A titre d'exemple, Apache Spark pourrait améliorer significativement cette performance en parallélisant certains traitements.

Un moteur d'indexation, comme ElasticSearch, pourrait améliorer la performance de recherche également.
