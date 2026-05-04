import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import keystatic from '@keystatic/astro';
import react from '@astrojs/react';

// https://astro.build/config
export default defineConfig({
  integrations: [
    tailwind(), 
    sitemap(), 
    react(), 
    // Keystatic dashboard is only for local development on static hosts like GitHub Pages
    process.env.NODE_ENV === 'development' ? keystatic() : null
  ].filter(Boolean),
  output: 'static',
  site: 'https://muhdanfyan.github.io',
  redirects: {
    '/tulisan/[slug]': '/writing/[slug]',
    '/tulisan': '/writing',
    '/mengajar/[slug]': '/teach/[slug]',
    '/mengajar': '/teach'
  }
});
