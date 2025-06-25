def evaluate_rules(data):
    tension = data.get("tension", 0)
    pouls = data.get("pouls", 0)
    temperature = data.get("temperature", 0)

    alerts = []

    if tension > 140 and pouls > 100:
        alerts.append("🟥 Risque de tachycardie détecté.")
    if temperature > 39:
        alerts.append("🟥 Température élevée : possible fièvre.")
    if tension < 90:
        alerts.append("🟥 Hypotension détectée.")
    if not alerts:
        return "✅ Toutes les constantes sont dans les normes.", alerts
    return "⚠️ Anomalies détectées !", alerts