# Exercice : Comprendre HTTP et HTTPS

## Explication simple 🟡

### HTTP vs HTTPS  
Imagine que tu envoies une lettre à un ami. Si tu utilises **HTTP**, c'est comme si tu enverrais la lettre sans enveloppe, donc n'importe qui pourrait la lire pendant le voyage. C’est ce qui peut arriver avec les informations envoyées sur internet avec HTTP, elles ne sont pas protégées. 

**HTTPS**, c’est comme si tu mettais ta lettre dans une enveloppe super sécurisée. Personne ne pourrait la lire ou la modifier pendant le voyage. C’est pour cela que **HTTPS** est utilisé sur les sites où des informations sensibles sont partagées, comme pour les banques ou les emails. La différence principale est que **HTTPS** ajoute une couche de sécurité grâce à un système spécial appelé **SSL/TLS**.

---

### Structure d’une requête HTTP  
Lorsque tu vas sur un site web, ton ordinateur envoie une **requête HTTP** au serveur qui héberge ce site. Cette requête contient des informations comme :
- **Méthode** : Demande de récupérer des données (par exemple, **GET**), ou de les envoyer (**POST**).
- **URL** : C’est l’adresse que tu veux visiter.
- **En-têtes** : Ce sont des informations supplémentaires comme ton navigateur ou ta langue préférée.

Le **serveur** répond avec une **réponse HTTP** qui contient :
1. **Code de statut** : Pour dire si tout s'est bien passé, par exemple **200** veut dire "OK".
2. **En-têtes** : Des infos supplémentaires.
3. **Contenu** : Comme la page web que tu vois ou les données demandées.

---

### Les méthodes HTTP  
Les **méthodes HTTP** sont comme des actions que tu demandes à un serveur de faire. Par exemple :
1. **GET** : C'est pour demander des données, comme une page web.
2. **POST** : C’est pour envoyer des informations, comme quand tu remplis un formulaire.
3. **PUT** : C’est pour mettre à jour des informations sur le serveur.
4. **DELETE** : C’est pour supprimer des données.

### Les codes de statut HTTP  
Les **codes de statut HTTP** disent si ta demande a été traitée correctement ou s'il y a eu un problème. Par exemple :
1. **200** : Tout va bien, la page a été trouvée.
2. **404** : La page n’a pas été trouvée.
3. **500** : Le serveur a un problème.
4. **301** : La page a été déplacée.
5. **403** : Tu n’as pas la permission d’accéder à la page.

---

## Liste des choses à faire étape par étape 🟡

1. **Comprendre la différence entre HTTP et HTTPS**  
   - Lire les ressources sur HTTP et HTTPS.
   - Écrire les différences principales, en particulier celles liées à la sécurité.

2. **Explorer la structure d’une requête HTTP**  
   - Aller sur un site comme **httpbin.org** pour tester les requêtes.
   - Utiliser l'outil "Inspecter" dans ton navigateur pour voir les requêtes et les réponses HTTP.
   - Observer les détails comme les méthodes, les en-têtes et les codes de statut.

3. **Faire une liste des méthodes HTTP**  
   - Rédiger une liste de méthodes courantes : **GET**, **POST**, **PUT**, **DELETE**.
   - Expliquer à quoi sert chaque méthode avec un exemple simple.

4. **Faire une liste des codes de statut HTTP**  
   - Créer une liste de codes courants comme **200**, **404**, **500**, **301**, **403**.
   - Expliquer chaque code et donner un exemple de situation où il apparaît.

5. **Utiliser un outil de sniffing (facultatif)**  
   - Si tu veux explorer encore plus, utilise un outil comme **Wireshark** pour observer les requêtes HTTP et HTTPS et voir les différences de sécurité.

---

Avec ces étapes, tu auras une bonne compréhension de comment HTTP et HTTPS fonctionnent, et tu sauras lire les échanges entre ton ordinateur et les serveurs sur internet. 🚀

Source intéressante pour comprendre les API HTTP/HTTPS :
https://httpbin.org/#/
