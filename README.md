# GWMcElfresh.github.io

Personal academic website for GW McElfresh - Computational Biology PhD

🔗 **Live Site**: [https://gwmcelfresh.github.io](https://gwmcelfresh.github.io)

---

## About

This is an academic portfolio website built with [Jekyll](https://jekyllrb.com/) and hosted on [GitHub Pages](https://pages.github.com/). It showcases research, publications, CV, and blog posts related to computational biology, transcriptomics, and mathematical modeling.

## Features

- **Multi-page structure**: Separate pages for About, Research, Publications, CV, and Blog
- **Modern navigation**: Clean navigation bar with active page highlighting
- **Responsive design**: Mobile-friendly layout
- **Custom styling**: Purple gradient theme with modern CSS
- **Research project pages**: Collection-based system for individual research projects
- **Blog functionality**: Jekyll blog with post archives and RSS feed
- **SEO optimized**: Using jekyll-seo-tag plugin

## Site Structure

```
.
├── _config.yml              # Jekyll configuration
├── index.md                 # Home/About page
├── research.md              # Research overview
├── publications.md          # Publications list
├── cv.md                    # Curriculum Vitae
├── blog.md                  # Blog landing page
├── _layouts/
│   └── default.html         # Custom layout with navigation
├── _includes/
│   └── navigation.html      # Navigation component
├── _posts/                  # Blog posts (YYYY-MM-DD-title.md format)
├── _research/               # Individual research project pages
├── assets/
│   └── css/
│       └── custom.css       # Custom styling
└── images/                  # Image assets
    └── self/                # Personal photos
```

## Local Development

### Prerequisites

- Ruby 2.5.0 or higher
- Bundler
- Git

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/GWMcElfresh/GWMcElfresh.github.io.git
   cd GWMcElfresh.github.io
   ```

2. Install dependencies:
   ```bash
   bundle install
   ```

3. Run local server:
   ```bash
   bundle exec jekyll serve
   ```

4. View site at `http://localhost:4000`

### Making Changes

- **Pages**: Edit `.md` files in the root directory
- **Blog posts**: Add to `_posts/` as `YYYY-MM-DD-title.md` with YAML front matter
- **Research projects**: Add to `_research/` directory
- **Styling**: Modify `assets/css/custom.css`
- **Configuration**: Update `_config.yml`

## Content Organization

### Adding a Blog Post

Create a file in `_posts/` with the format `YYYY-MM-DD-post-title.md`:

```markdown
---
title: "Your Post Title"
date: YYYY-MM-DD
---

Your content here...
```

### Adding a Research Project

Create a file in `_research/` with descriptive name:

```markdown
---
layout: default
title: "Project Title"
---

# Project Title

Project content...
```

The project will automatically be available at `/research/filename/`

## Customization

### Update Personal Information

Edit `_config.yml`:

```yaml
title: Your Name
tagline: Your Title
email: your.email@domain.com
github_username: yourusername
orcid: your-orcid-id
google_scholar: your-scholar-id
```

### Change Color Scheme

Edit `assets/css/custom.css` and modify the gradient colors in `.site-nav` and `.btn`:

```css
background: linear-gradient(135deg, #yourcolor1 0%, #yourcolor2 100%);
```

### Add Pages to Navigation

Edit the `navigation` section in `_config.yml`:

```yaml
navigation:
  - title: Your Page
    url: /your-page
```

## Deployment

The site automatically deploys via GitHub Pages when you push to the `master` branch. Changes are typically live within 1-2 minutes.

## Technologies Used

- **Jekyll**: Static site generator
- **GitHub Pages**: Hosting
- **Tactile Theme**: Base theme (pages-themes/tactile@v0.2.0)
- **Markdown**: Content authoring
- **Liquid**: Templating
- **CSS3**: Custom styling
- **jekyll-seo-tag**: SEO optimization
- **jekyll-feed**: RSS feed generation

## License

Content © 2026 GW McElfresh. All rights reserved.

Code is available under the MIT License.

## Contact

For questions or collaboration inquiries, please contact via:
- Email: [Your email from _config.yml]
- GitHub: [@GWMcElfresh](https://github.com/GWMcElfresh)

---

*Last updated: February 2026*
