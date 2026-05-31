def generate_summary(query, results):
    if not results or "No related memory found" in results:
        return f"EchoVault did not find matching memory sources for '{query}'. Try a different phrase."

    insights = []

    if "📂 Local Projects" in results:
        insights.append("Your local project history contains relevant memory links.")

    if "🐙 GitHub Repositories" in results:
        insights.append("GitHub memories surfaced code and repository insights.")

    if "📄 PDF Reports" in results:
        insights.append("PDF documents contributed research and reference data.")

    if not insights:
        insights.append("EchoVault discovered memory fragments across your archive.")

    return " ".join(insights) + f" Summary based on '{query}'."
