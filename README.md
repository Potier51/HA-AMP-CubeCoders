---

🧩 Intégration Home Assistant pour CubeCoders AMP

CubeCoders AMP – Home Assistant Integration

Intégration personnalisée permettant de connecter CubeCoders AMP à Home Assistant.  
Elle offre une découverte automatique des instances, des capteurs de statut et de joueurs, ainsi qu’une interface de configuration moderne inspirée de l’intégration Proxmox.

---

✨ Fonctionnalités

- 🔍 Découverte automatique des instances AMP
- 🧩 Sélection des instances à intégrer (comme Proxmox)
- 📡 Intervalle de mise à jour configurable
- 📊 Capteurs intégrés :
  - Statut de l’instance
  - Nombre de joueurs connectés
- 🔧 Options Flow pour modifier les paramètres après installation
- ⚙️ Architecture moderne basée sur :
  - DataUpdateCoordinator
  - Config Flow
  - Options Flow
  - API asynchrone

---

📦 Installation

🔹 Via HACS (recommandé)
(Disponible lorsque tu publieras ton dépôt dans HACS Community Store)

1. Ouvrir HACS → Intégrations
2. Cliquer sur Custom repositories
3. Ajouter :  
   https://github.com/Potier51/HA-AMP-CubeCoders
4. Catégorie : Integration
5. Installer l’intégration
6. Redémarrer Home Assistant

🔹 Installation manuelle

1. Télécharger le dépôt
2. Copier le dossier :

`
customcomponents/ampcubecoders
`

dans :

`
/config/custom_components/
`

3. Redémarrer Home Assistant

---

⚙️ Configuration

1. Aller dans Paramètres → Appareils & Services
2. Cliquer sur Ajouter une intégration
3. Rechercher CubeCoders AMP
4. Entrer :
   - Adresse du serveur AMP
   - API Key
5. L’intégration teste automatiquement la connexion
6. Sélectionner les instances à intégrer
7. Choisir l’intervalle de mise à jour

---

📊 Capteurs disponibles

Chaque instance sélectionnée crée automatiquement :

| Capteur | Description |
|--------|-------------|
| Status | État de l’instance (Running, Stopped, etc.) |
| Players | Nombre de joueurs connectés |

---

🛠️ Options Flow

Après installation, tu peux modifier :

- les instances sélectionnées  
- l’intervalle de mise à jour  

Depuis :

Paramètres → Appareils & Services → CubeCoders AMP → Configurer

---

🔐 Permissions nécessaires

L’intégration utilise uniquement :

- l’adresse du serveur AMP  
- une API Key  

Aucune autre permission n’est requise.

---

❗ Dépannage

🔸 Erreur : cannot_connect
Causes possibles :

- Mauvaise adresse IP ou port
- API Key incorrecte
- AMP ne répond pas
- Pare-feu ou NAT bloquant l’accès

🔸 Aucune instance détectée
- Vérifier que le compte API a accès aux instances
- Vérifier que le module ADS est actif dans AMP

---

🧭 Roadmap

Fonctionnalités prévues :

- Capteurs CPU / RAM / Uptime
- Actions Start / Stop / Restart
- Capteurs de logs
- Capteurs de ports ouverts
- Capteurs de version AMP
- Support des serveurs distants multi‑ADS

---

🤝 Contribuer

Les contributions sont les bienvenues !  
N’hésite pas à ouvrir une issue ou une pull request.

---

📄 Licence

MIT License

---
