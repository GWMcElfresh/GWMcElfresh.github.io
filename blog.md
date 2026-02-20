---
layout: default
title: Blog
permalink: /blog/
---

# Blog

Thoughts on computational biology, research methods, and scientific computing.

---

## Recent Posts

{% for post in site.posts %}
<article class="blog-post-preview">
  <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
  <p class="post-meta">
    <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time>
  </p>
  {% if post.excerpt %}
  <p class="post-excerpt">{{ post.excerpt | strip_html | truncatewords: 50 }}</p>
  {% endif %}
  <a href="{{ post.url | relative_url }}" class="read-more">Read more →</a>
</article>
<hr>
{% endfor %}

---

## Topics

I write about:

- **Transcriptomics & Single-Cell Analysis**: Tutorials, best practices, and insights from working with spatial and single-cell RNA-seq data
- **Computational Methods**: Mathematical modeling, machine learning applications, and statistical analysis in biology
- **Research Workflows**: Tools, pipelines, and reproducible research practices
- **Scientific Computing**: Python, R, and HPC tips for biological research
- **Career & Academia**: Reflections on graduate school, research, and computational biology

---

## Archive

Browse posts by year:

{% assign posts_by_year = site.posts | group_by_exp: "post", "post.date | date: '%Y'" %}
{% for year in posts_by_year %}
### {{ year.name }}
<ul class="post-list">
  {% for post in year.items %}
  <li>
    <span class="post-date">{{ post.date | date: "%b %d" }}</span> —
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  </li>
  {% endfor %}
</ul>
{% endfor %}

---

## Subscribe

Stay updated with new posts via [RSS feed]({{ "/feed.xml" | relative_url }}).
