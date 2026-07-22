import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';
import { site } from '../data/site';

export async function GET(context) {
  const posts = (await getCollection('blog'))
    .filter((p) => !p.data.draft)
    .sort((a, b) => b.data.date.valueOf() - a.data.date.valueOf());

  return rss({
    title: `${site.title} Blog`,
    description: site.description,
    site: context.site,
    items: posts.map((post) => {
      const date = post.data.date;
      const y = date.getUTCFullYear();
      const m = String(date.getUTCMonth() + 1).padStart(2, '0');
      const d = String(date.getUTCDate()).padStart(2, '0');
      const slug = post.id.replace(/^\d{4}-\d{2}-\d{2}-/, '');
      return {
        title: post.data.title,
        pubDate: post.data.date,
        description: post.data.excerpt,
        link: `/blog/${y}/${m}/${d}/${slug}/`,
      };
    }),
  });
}
