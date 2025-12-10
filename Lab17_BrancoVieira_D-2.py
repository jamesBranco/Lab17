"""
Program: Lab 17 – GitHub Language Repositories Visualization
Author: Dyemydym (James) Branco Vieira
Purpose: Use the GitHub API to retrieve the most-starred repositories
         for a specific programming language, and visualize the results
         in a bar chart. This program follows the style from
         Python Crash Course, Chapter 17.
Date: 2025-12-10
"""

import requests
import plotly.express as px


def get_repo_data(language="javascript", per_page=30):
    """Request repository data from GitHub's API for the chosen language."""
    url = "https://api.github.com/search/repositories"

    headers = {"Accept": "application/vnd.github.v3+json"}
    params = {
        "q": f"language:{language}",
        "sort": "stars",
        "per_page": per_page,
    }

    print("Requesting data from GitHub API...")
    response = requests.get(url, headers=headers, params=params)
    print(f"Status code: {response.status_code}")

    # Stop the program if the request failed
    response.raise_for_status()

    data = response.json()
    return data["items"]


def build_bar_chart(repo_dicts, language="JavaScript"):
    """Create a bar chart showing repo names vs. star counts."""
    repo_names = []
    stars = []

    for repo in repo_dicts:
        name = repo["name"]
        stars_count = repo["stargazers_count"]
        url = repo["html_url"]

        # Make repo names into clickable hyperlinks (like the book example)
        clickable = f"<a href='{url}'>{name}</a>"

        repo_names.append(clickable)
        stars.append(stars_count)

    title = f"Most-Starred {language} Projects on GitHub"
    labels = {"x": "Repository", "y": "Stars"}

    fig = px.bar(
        x=repo_names,
        y=stars,
        title=title,
        labels=labels,
    )

    fig.update_layout(
        title_font_size=28,
        xaxis_title_font_size=20,
        yaxis_title_font_size=20
    )

    fig.show()


def main():
    """Run the GitHub repo request and produce a visualization."""
    language = "javascript"   # You may change this to any language
    repos = get_repo_data(language=language)
    build_bar_chart(repos, language=language.capitalize())


if __name__ == "__main__":
    main()
