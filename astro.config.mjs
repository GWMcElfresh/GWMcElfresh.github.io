import { defineConfig } from 'astro/config';
import { fileURLToPath } from 'node:url';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

// https://docs.astro.build/en/guides/deploy/github/
export default defineConfig({
  site: 'https://GWMcElfresh.github.io',
  trailingSlash: 'always',
  build: {
    format: 'directory',
  },
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [rehypeKatex],
  },
  vite: {
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },
    // public/slides/<talk>/index.html is fine on static hosts, but Vite does not
    // resolve directory indexes for /slides/<talk>/ during `astro dev`.
    plugins: [
      {
        name: 'slides-directory-index',
        configureServer(server) {
          server.middlewares.use((req, _res, next) => {
            const url = req.url?.split('?')[0] ?? '';
            const match = url.match(/^\/slides\/([^/]+)\/?$/);
            if (match) {
              req.url = `/slides/${match[1]}/index.html${req.url?.includes('?') ? '?' + req.url.split('?')[1] : ''}`;
            }
            next();
          });
        },
      },
    ],
  },
});
