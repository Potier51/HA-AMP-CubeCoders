📄 Contribuer à l’intégration CubeCoders AMP pour Home Assistant

Merci de votre intérêt pour ce projet !  
Les contributions sont les bienvenues, qu’il s’agisse de corrections, d’améliorations, de nouvelles fonctionnalités ou de documentation.

Ce guide explique comment contribuer efficacement.

---

🧱 Pré-requis

- Connaissances de base en Python
- Notions sur Home Assistant et ses intégrations
- Installation locale de Home Assistant Core ou utilisation de l’addon “VSCode + Dev Container”
- Git installé

---

🛠️ Installation de l’environnement de développement

1. Cloner le dépôt

`bash
git clone https://github.com/Potier51/HA-AMP-CubeCoders.git
cd HA-AMP-CubeCoders
`

2. Installer Home Assistant en mode développement (optionnel mais recommandé)

Documentation officielle :  
https://developers.home-assistant.io/docs/developmentenvironment/ (developers.home-assistant.io in Bing)

3. Ajouter l’intégration en mode développement

Copier le dossier :

`
customcomponents/ampcubecoders
`

dans votre dossier Home Assistant :

`
/config/custom_components/
`

Redémarrer Home Assistant.

---

🧪 Tester l’intégration

1. Ouvrir Home Assistant
2. Aller dans Paramètres → Appareils & Services
3. Ajouter l’intégration CubeCoders AMP
4. Tester les différentes étapes :
   - Connexion AMP
   - Sélection des instances
   - Intervalle de mise à jour
   - Options Flow
5. Vérifier les logs en cas d’erreur :

`
Paramètres → Système → Journaux
`

Pour activer les logs détaillés :

`yaml
logger:
  default: warning
  logs:
    customcomponents.ampcubecoders: debug
`

---

📦 Structure du projet

`
customcomponents/ampcubecoders/
│
├── init.py
├── api.py
├── coordinator.py
├── sensor.py
├── config_flow.py
├── const.py
├── manifest.json
│
└── translations/
    ├── en.json
    └── fr.json
`

---

🧩 Règles de contribution

✔️ Code propre et typé
- Utiliser Python 3.12+
- Respecter les conventions Home Assistant
- Utiliser des annotations de type (str, dict, etc.)
- Préférer les f-strings

✔️ Architecture Home Assistant
- API asynchrone (async def)
- Pas de polling manuel (utiliser le coordinator)
- Pas de blocage (time.sleep interdit)
- Pas d’accès réseau en dehors de api.py

✔️ Traductions obligatoires
Toute nouvelle interface utilisateur doit être ajoutée dans :

`
translations/en.json
translations/fr.json
`

✔️ Mise à jour du CHANGELOG
Chaque contribution doit mettre à jour la section :

`

[Unreleased]
`

---

🔀 Soumettre une Pull Request

1. Créer une branche :

`bash
git checkout -b feature/ma-fonctionnalite
`

2. Faire vos modifications  
3. Mettre à jour :
   - CHANGELOG.md
   - README.md si nécessaire
   - translations/*
4. Pousser la branche :

`bash
git push origin feature/ma-fonctionnalite
`

5. Ouvrir une Pull Request sur GitHub

---

🐛 Signaler un bug

Merci d’inclure :

- Version de Home Assistant
- Version de l’intégration
- Logs pertinents
- Étapes pour reproduire
- Configuration utilisée

---

💡 Proposer une fonctionnalité

Les idées sont les bienvenues !  
Merci d’ouvrir une issue avec :

- Description claire
- Cas d’usage
- Impact sur l’intégration
- API AMP concernée

---

🤝 Merci

Merci de contribuer à rendre cette intégration plus complète et plus utile pour la communauté Home Assistant.
