import { config, fields, collection } from '@keystatic/core';

// Kategori tunggal untuk semua bahasa
const categoryOptions = [
  { label: 'Technology', value: 'Technology' },
  { label: 'Education', value: 'Education' },
  { label: 'Psychology & Health', value: 'Psychology & Health' },
  { label: 'Technology & Career', value: 'Technology & Career' },
  { label: 'Philosophy & History', value: 'Philosophy & History' },
  { label: 'Media', value: 'Media' },
  { label: 'Technology & Culture', value: 'Technology & Culture' },
  { label: 'Technology & Law', value: 'Technology & Law' },
  { label: 'Technology & AI', value: 'Technology & AI' },
];

export default config({
  storage: 
    process.env.NODE_ENV === 'development'
      ? { kind: 'local' }
      : {
          kind: 'github',
          repo: {
            owner: 'muhdanfyan',
            name: 'muhdanfyan.github.io',
          },
        },
  collections: {
    writing: collection({
      label: 'Tulisan (Utama/ID)',
      slugField: 'slug', 
      path: 'tulisan/*/',
      format: { contentField: 'content' },
      entryLayout: 'content',
      schema: {
        slug: fields.text({ label: 'Slug (Folder Name)' }),
        title_id: fields.text({ label: 'Judul (Indonesia)' }),
        title_en: fields.text({ label: 'Judul (English)' }),
        date: fields.date({ label: 'Tanggal Publish', defaultValue: { kind: 'today' } }),
        
        image: fields.image({
          label: 'Gambar Sampul',
          directory: 'public/img/tulisan',
          publicPath: '/img/tulisan',
        }),
        
        // Hanya satu kategori, dropdown canggih
        category: fields.select({
          label: 'Kategori',
          options: categoryOptions,
          defaultValue: 'Technology',
        }),
        
        description_id: fields.text({ label: 'Deskripsi Singkat (ID)', multiline: true }),
        description_en: fields.text({ label: 'Deskripsi Singkat (EN)', multiline: true }),

        content: fields.markdoc({
          label: 'Isi Tulisan (Indonesia)',
          formatting: true,
          dividers: true,
          links: true,
          images: {
            directory: 'public/img/tulisan/content',
            publicPath: '/img/tulisan/content',
          },
        }),
      },
    }),
    writing_en: collection({
      label: 'Tulisan (Versi English)',
      slugField: 'slug', 
      path: 'tulisan/*/index.en',
      format: { contentField: 'content' },
      entryLayout: 'content',
      schema: {
        slug: fields.text({ label: 'Slug (Sesuai Folder ID)' }),
        content: fields.markdoc({
          label: 'Isi Tulisan (English)',
          formatting: true,
          dividers: true,
          links: true,
          images: {
            directory: 'public/img/tulisan/content',
            publicPath: '/img/tulisan/content',
          },
        }),
      },
    }),
  },
});
