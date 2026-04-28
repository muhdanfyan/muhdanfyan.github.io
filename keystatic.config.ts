import { config, fields, collection } from '@keystatic/core';

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
      label: 'Tulisan',
      slugField: 'slug', 
      path: 'tulisan/*/',
      format: { contentField: 'content' },
      entryLayout: 'content',
      schema: {
        slug: fields.text({ 
          label: 'Slug (Nama Folder)',
          description: 'Gunakan huruf kecil dan tanda hubung (contoh: judul-artikel-saya)',
          validation: { length: { min: 1 } }
        }),
        title_id: fields.text({ label: 'Judul (Indonesia)' }),
        title_en: fields.text({ label: 'Judul (English)' }),
        date: fields.date({ label: 'Tanggal Publish', defaultValue: { kind: 'today' } }),
        
        image: fields.image({
          label: 'Gambar Sampul',
          directory: 'public/img/tulisan',
          publicPath: '/img/tulisan',
        }),
        
        // Kategori dalam bentuk Dropdown
        category_id: fields.select({
          label: 'Kategori (ID)',
          options: [
            { label: 'Technology', value: 'Technology' },
            { label: 'Education', value: 'Education' },
            { label: 'Psychology & Health', value: 'Psychology & Health' },
            { label: 'Technology & Career', value: 'Technology & Career' },
            { label: 'Philosophy & History', value: 'Philosophy & History' },
            { label: 'Media', value: 'Media' },
            { label: 'Technology & Culture', value: 'Technology & Culture' },
            { label: 'Technology & Law', value: 'Technology & Law' },
            { label: 'Technology & AI', value: 'Technology & AI' },
          ],
          defaultValue: 'Technology',
        }),
        
        description_id: fields.text({ label: 'Deskripsi Singkat (ID)', multiline: true }),
        
        category_en: fields.text({ label: 'Kategori (EN)' }),
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

        content_en_markdown: fields.text({
          label: 'Isi Tulisan (English Markdown)',
          multiline: true,
        }),
      },
    }),
  },
});
