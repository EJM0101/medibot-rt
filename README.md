# 🩺 MediBot RT — Système Expert Santé Temps Réel

**MediBot RT** est une application pédagogique qui simule un système expert embarqué dans un contexte médical.  
Elle permet de surveiller en temps réel les données vitales d’un patient (tension, pouls, température) et de déclencher automatiquement des alertes via un moteur de règles.

---

## 🎯 Objectif pédagogique

Ce projet vise à :

- Montrer comment un **système expert** peut être intégré à une application **temps réel**
- Simuler un comportement **réactif basé sur des règles médicales**
- Illustrer la logique **SI...ALORS** dans un contexte d’urgence
- Former aux concepts d’**intelligence décisionnelle embarquée**

---

## 🚀 Fonctionnalités

✅ Saisie manuelle des constantes de santé (tension, pouls, température)  
✅ Analyse immédiate via moteur de règles Python  
✅ Alerte visuelle en cas d’anomalies détectées  
✅ Interface claire pour affichage des règles déclenchées  
✅ (Optionnel) Mode surveillance automatique toutes les 5 secondes

---

## 🛠 Stack technique

| Composant     | Technologie         |
|---------------|---------------------|
| Backend       | Flask (Python)      |
| Moteur expert | `rules_engine.py` (règles simples SI-ALORS) |
| Frontend      | HTML + Bootstrap + JS |
| Déploiement   | Render.com          |

---

## 🧠 Règles médicales intégrées

```text
SI tension > 140 ET pouls > 100 → Risque de tachycardie
SI température > 39°C           → Fièvre détectée
SI tension < 90                → Hypotension
```

---

## 🖥️ Lancer localement

```bash
git clone https://github.com/monprojet/medibot-rt
cd medibot-rt
pip install -r requirements.txt
python app.py
```

---

## 🌐 Déploiement Render

Utilise ce fichier `render.yaml` :

```yaml
services:
  - type: web
    name: medibot-rt
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "python app.py"
```

---

## 📦 Structure du projet

```
medibot-rt/
├── app.py                # Serveur Flask
├── rules_engine.py       # Règles médicales
├── templates/index.html  # Interface utilisateur
├── static/app.js         # JS pour envoi AJAX
├── requirements.txt      # Dépendances
└── render.yaml           # Déploiement Render
```

---

## 👨‍⚕️ Développé par

**Emman Mlmb 🇨🇩**  
Étudiant L3 Informatique — Université de Kinshasa  
Module : Informatique Temps Réel

---

> Projet open-source destiné à l'enseignement et à la démonstration des systèmes experts embarqués.