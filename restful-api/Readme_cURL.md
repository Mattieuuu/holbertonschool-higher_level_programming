# Exercice : Utiliser curl pour interagir avec des API

## Explication simple 🟡

### Qu'est-ce que cURL ?  
**cURL** (Client URL) est un outil en ligne de commande qui te permet d'envoyer et de recevoir des données à travers différents protocoles de communication, comme **HTTP**, **HTTPS**, **FTP**, etc. C'est souvent utilisé pour tester et déboguer les API et les serveurs web. 

Avec **cURL**, tu peux facilement envoyer des requêtes à des API, voir les réponses, et tester des fonctionnalités directement depuis ton terminal. C'est un outil très puissant pour interagir avec des API RESTful.

---

## Objectif de l'exercice 🟡

À la fin de cet exercice, tu devrais être capable de :

1. Installer et utiliser **curl** depuis la ligne de commande.
2. Créer et exécuter des requêtes API de base avec **curl**, comme définir des en-têtes et inspecter la sortie.
3. Interpréter les résultats des requêtes API courantes.

---

## Étapes à suivre 🟡

### 1. Installer et utiliser curl

- Installe **curl** sur ton système.  
  Sur **Linux/Mac**, il est généralement disponible dans les dépôts standard.  
  Pour **Windows**, tu peux utiliser le **Windows Subsystem for Linux (WSL)** ou télécharger une version spécifique de **curl** pour Windows.

- Une fois installé, vérifie sa version avec la commande suivante :
  curl --version
  Cela te montrera la version de **curl** installée et les protocoles pris en charge.

- Utilise **curl** pour récupérer le contenu d'une page web, par exemple :  
  curl http://example.com

### 2. Récupérer des données depuis une API

- Utilise **curl** pour récupérer des **posts** depuis une API publique, comme **JSONPlaceholder** :  
  curl https://jsonplaceholder.typicode.com/posts

- Tu devrais obtenir une sortie au format **JSON** qui contient une liste de posts, chacun avec des attributs comme `userId`, `id`, `title`, et `body`.

### 3. Utiliser des en-têtes et autres options avec curl

- Si tu veux uniquement obtenir les en-têtes de la réponse (sans le contenu), utilise l'option **-I** :  
  curl -I https://jsonplaceholder.typicode.com/posts

- Pour faire une requête **POST** et envoyer des données à l'API, utilise l'option **-X POST** avec **-d** pour envoyer les données :  
  curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts


---

## Indices 🟡

- L'option **-I** te permet de récupérer uniquement les en-têtes de la réponse, ce qui est utile pour diagnostiquer les paramètres du serveur, les contrôles de cache, et les types de contenu.
- L'option **-X** te permet de spécifier une méthode HTTP pour ta requête. Par exemple, **-X POST** pour faire une requête POST.
- L'option **-d** te permet de passer des données dans ta requête. En général, cette option est utilisée avec les méthodes **POST**, **PUT** ou **PATCH** pour envoyer des données au serveur.
- Si la sortie est trop longue et que tu veux la rendre plus lisible, tu peux utiliser un outil comme **jq** pour formater et colorier le JSON.

---

## Résultats attendus 🟡

1. **curl --version** : Tu devrais voir des informations sur la version de **curl** installée, y compris les protocoles supportés (HTTP, HTTPS, etc.).
2. **Récupérer les posts de JSONPlaceholder** : Tu devrais obtenir une sortie **JSON** avec divers posts, chacun ayant des attributs comme `userId`, `id`, `title`, et `body`.
3. **Obtenir uniquement les en-têtes** : La commande **curl -I** devrait afficher un résumé des en-têtes de la réponse (statut, type de contenu, etc.), sans le contenu réel.
4. **Faire une requête POST** : Lorsque tu envoies des données via POST, tu devrais recevoir une réponse du serveur qui simule la création d'un nouveau post, avec un `id` retourné (par exemple, `id: 101`), bien que le post ne soit pas réellement enregistré.

---

Avec cet exercice, tu apprendras à utiliser **curl** pour interagir avec des API et à examiner les résultats de tes requêtes. Cela te permettra de tester facilement des services web, de récupérer des données, et de comprendre les réponses des serveurs. 🚀
