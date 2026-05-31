from forgotten_projects import get_forgotten_projects
from timeline import build_timeline
from ai_summary import generate_summary
from pdf_search import search_pdfs
from flask import Flask, render_template, request
from search_engine import search_memory
from github_search import search_github_repos

app = Flask(__name__)

search_history = []


def simulate_answer(query, local_results, github_results, pdf_results):
    sections = []

    if local_results:
        sections.append("📂 Local Projects:\n" + "\n".join(f"- {item}" for item in local_results))

    if github_results:
        sections.append("🐙 GitHub Repositories:\n" + "\n".join(f"- {item}" for item in github_results))

    if pdf_results:
        sections.append("📄 PDF Reports:\n" + "\n".join(f"- {item}" for item in pdf_results))

    if not sections:
        return "No related memory found for that query. Try a broader keyword."

    return "\n\n".join(sections)


@app.route("/", methods=["GET", "POST"])
def home():
    answer = "Start a search to unlock your memory archive."
    ai_summary = "EchoVault is ready to summarize your stored memories."
    with open("data/projects.txt", "r", encoding="utf-8") as project_file:
        project_count = sum(1 for _ in project_file)
    timeline = build_timeline()
    forgotten_projects = get_forgotten_projects()

    if request.method == "POST":
        query = request.form.get("query", "").strip()

        if query:
            search_history.append(query)
            local_results = search_memory(query)
            github_results = search_github_repos(query)
            pdf_results = search_pdfs(query)

            answer = simulate_answer(query, local_results, github_results, pdf_results)
            ai_summary = generate_summary(query, answer)

    recent_history = list(reversed(search_history[-5:]))

    return render_template(
        "index.html",
        answer=answer,
        ai_summary=ai_summary,
        project_count=project_count,
        search_count=len(search_history),
        history=recent_history,
        timeline=timeline,
        forgotten_projects=forgotten_projects,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

