def search_memory(query):

    results = []

    with open("data/projects.txt", "r") as file:
        projects = file.readlines()

    for project in projects:
        if query.lower() in project.lower():
            results.append(project.strip())

    return results