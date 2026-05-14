import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import keystatic from '@keystatic/astro';
import react from '@astrojs/react';

export default defineConfig({
  integrations: [
    tailwind(), 
    sitemap(), 
    react(), 
    process.env.NODE_ENV === 'development' ? keystatic() : null
  ].filter(Boolean),
  output: 'static',
  site: 'https://muhdanfyan.github.io',
  build: {
    assets: 'assets'
  }
});
