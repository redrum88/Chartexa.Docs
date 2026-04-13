# Chartexa.Docs

Official documentation for [Chartexa](https://github.com/redrum88/Chartexa) — a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

## Live Site

[https://redrum88.github.io/Chartexa.Docs/](https://redrum88.github.io/Chartexa.Docs/)

## How It Works

```
Chartexa (private repo)
  └── push to main
        └── GitHub Action: sync-docs.yml
              └── runs scripts/generate-docs.ps1
                    └── generates placeholder .md files
                          └── pushes to Chartexa.Docs (this repo)
                                └── GitHub Action: deploy.yml
                                      └── builds with MkDocs
                                            └── deploys to GitHub Pages
```

### Documentation Pipeline

1. **Source sync** — when code changes in the private Chartexa repo, a GitHub Action generates/updates placeholder doc scaffolds and pushes them here
2. **AI expansion** — placeholder docs (`status: placeholder`) are expanded into full content (`status: draft`) by AI agents following the guidelines in `AI_DOCS_GUIDELINES.md`
3. **Human review** — drafts are reviewed and promoted to `status: published`
4. **Deploy** — on push to `main`, MkDocs builds and deploys to GitHub Pages

### Page Status

| Status | Meaning |
|---|---|
| `placeholder` | Auto-generated scaffold with section headers only |
| `draft` | AI-expanded with real content, needs review |
| `published` | Reviewed and approved |

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally with hot reload
mkdocs serve

# Build static site
mkdocs build
```

## Structure

```
Chartexa.Docs/
├── mkdocs.yml                 ← MkDocs + Material configuration
├── requirements.txt           ← Python dependencies
├── AI_DOCS_GUIDELINES.md      ← Instructions for AI doc expansion
├── overrides/                 ← Material theme overrides
├── docs/
│   ├── index.md               ← Landing page
│   ├── stylesheets/extra.css  ← Custom CSS
│   ├── getting-started/       ← Installation, first chart
│   ├── chart-types/           ← 2D, 3D, gauges, instruments
│   ├── axes/                  ← Axis types and configuration
│   ├── data/                  ← Data series and data sources
│   ├── domains/               ← Domain packages and integration patterns
│   ├── interaction/           ← Zoom, pan, tooltips, hit testing
│   ├── rendering/             ← DirectX 12, Skia, WPF, Web
│   ├── theming/               ← Theme system
│   ├── layout/                ← Dashboard layout
│   ├── python/                ← Python wrapper docs
│   ├── performance/           ← Optimization, benchmarks
│   ├── examples/              ← Production-ready examples
│   ├── api-reference/         ← Public API reference
│   └── architecture/          ← High-level architecture
```

## License

Documentation content is licensed under MIT.
