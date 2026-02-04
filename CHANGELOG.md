# Changelog
Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

---

## [Unreleased]
- Ajout prévu : capteurs CPU / RAM / Uptime
- Ajout prévu : actions Start / Stop / Restart
- Ajout prévu : capteurs de logs AMP
- Ajout prévu : support multi‑serveurs AMP

---

## [1.0.0] - 2026-02-04
### Added
- Première version publique de l’intégration CubeCoders AMP pour Home Assistant
- Découverte automatique des instances AMP
- Sélection des instances à intégrer (interface type Proxmox)
- Configuration de l’intervalle de mise à jour
- Capteur de statut par instance
- Capteur du nombre de joueurs connectés
- Options Flow pour modifier les paramètres après installation
- API asynchrone complète (list_instances, get_status, get_players)
- DataUpdateCoordinator pour centraliser les données
- Traductions FR / EN
- Documentation complète

### Fixed
- Gestion des erreurs API (timeouts, codes HTTP, exceptions)
- Nettoyage des entités lors du déchargement de l’intégration

### Changed
- Intervalle de mise à jour désormais configurable via l’UI
