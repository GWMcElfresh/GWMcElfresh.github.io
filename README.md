# GWMcElfresh.github.io

Personal academic site for **GW McElfresh** — infectious disease computational biologist with a mathematics background.

**Live:** [https://GWMcElfresh.github.io](https://GWMcElfresh.github.io)

## Stack

- **[Astro](https://astro.build/)** static site (content collections + islands)
- **GitHub Actions → GitHub Pages** (`withastro/action` + `actions/deploy-pages`)
- Visual thesis: **stochastic processes in biology** (canvas Gillespie-like hero, KaTeX, Fraunces + IBM Plex)

Jekyll / Tactile has been retired from the public path.

## Local development

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # output → dist/
npm run preview
```

Requires Node 18+.

## Site map

| Route | Source |
|-------|--------|
| `/` | `src/pages/index.astro` + `StochasticHero` |
| `/research/` | `src/pages/research/index.astro` |
| `/research/:slug/` | `src/content/research/` |
| `/publications/` | `src/pages/publications.md` |
| `/cv/` | `src/pages/cv.md` (+ PDF at `/assets/cv/McElfresh_CV.pdf`) |
| `/blog/` | `src/pages/blog/` + `src/content/blog/` |
| `/rss.xml` | `src/pages/rss.xml.ts` |

Identity strings live in [`src/data/site.ts`](src/data/site.ts). Design tokens: [`src/styles/tokens.css`](src/styles/tokens.css).

## Content editing

- **Blog:** add `src/content/blog/YYYY-MM-DD-slug.md` (frontmatter: `title`, `date`, `excerpt`). URLs preserve `/blog/YYYY/MM/DD/slug/`.
- **Research projects:** add `src/content/research/slug.md` (`title`, `excerpt`, `status`, `order`). They appear automatically on `/research/`.
- **Math:** use `$inline$` or `$$display$$` (remark-math + rehype-katex).
- **CV PDF source:** `assets/cv/McElfresh_CV.tex` (dual-maintained with `src/pages/cv.md` — keep in sync).

## Deploy cutover (one-time)

1. Merge this Astro site to `master`.
2. Repo **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Confirm the **Deploy to GitHub Pages** workflow succeeds.
4. Site publishes from the Actions artifact (not the old branch/Jekyll build).

Workflow: [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

## Mycelium / analysis dirs

`.living/`, `analysis/`, `data/`, `todo/`, etc. are **not** part of the public Astro build. Only `src/`, `public/`, and config drive `dist/`.
