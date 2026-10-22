FruitStudio — déploiement gratuit (prototype)
============================================

Fichiers :
- index.html : interface du site
- server.py : API privée qui appelle le moteur vidéo
- requirements.txt : dépendances Python
- render.yaml : réglages de déploiement Render

Étapes :
1. Crée un dépôt GitHub nommé fruitstudio. Pour utiliser le déploiement Render par dépôt, le dépôt doit être connecté à Render.
2. Téléverse ces 4 fichiers à la racine du dépôt.
3. Dans Render, crée un nouveau Web Service depuis ce dépôt. Render détectera render.yaml, ou saisis :
   Build command : pip install -r requirements.txt
   Start command : uvicorn server:app --host 0.0.0.0 --port $PORT
   Choisis le plan Free.
4. Dans les variables d'environnement/secrets de Render, ajoute HF_TOKEN avec un jeton Hugging Face ayant l'accès Inference Providers.
5. Déploie et teste l'adresse HTTPS donnée par Render.

Sécurité et coûts :
- Ne mets jamais HF_TOKEN dans index.html ni dans un dépôt GitHub.
- N'ajoute aucun moyen de paiement et n'achète pas de crédits pour ce prototype.
- Les crédits gratuits Hugging Face sont faibles et peuvent changer ; la vidéo peut échouer si le modèle ou le fournisseur n'est pas disponible ou si le crédit ne suffit pas.
- Render Free peut se mettre en veille après 15 minutes sans visite.
- Ce prototype n'a pas encore de comptes utilisateurs, de file d'attente ni de limites anti-abus : ne le diffuse pas largement sans les ajouter.
