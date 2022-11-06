```{include} ../README.md
---
end-before: <!-- github-only -->
---
```

[license]: license

```{toctree}
---
hidden:
maxdepth: 1
---

reference
License <license>
{% if cookiecutter.use_github_org == 'y' -%}
Changelog = "https://github.com/{{cookiecutter.github_org}}/{{cookiecutter.repo_name}}/releases"
{% else %}
Changelog = "https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}/releases"
{% endif -%}
```
