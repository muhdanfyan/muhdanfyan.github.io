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
      slugField: 'slug', // Menggunakan slug (nama folder) sebagai identifier
      path: 'tulisan/*/',
      format: { contentField: 'content' },
      entryLayout: 'content',
      schema: {
        slug: fields.text({ label: 'Slug (Folder Name)' }),
        title_id: fields.text({ label: 'Indonesian Title' }),
        title_en: fields.text({ label: 'English Title' }),
        date: fields.date({ label: 'Date', defaultValue: { kind: 'today' } }),
        image: fields.text({ label: 'Image Path/URL' }),
        
        category_id: fields.text({ label: 'Category (ID)' }),
        description_id: fields.text({ label: 'Description (ID)', multiline: true }),
        
        category_en: fields.text({ label: 'Category (EN)' }),
        description_en: fields.text({ label: 'Description (EN)', multiline: true }),

        content: fields.document({
          label: 'Konten Utama (Indonesian)',
          formatting: true,
          dividers: true,
          links: true,
          images: true,
        }),

        content_en_markdown: fields.text({
          label: 'Content (English Markdown)',
          multiline: true,
        }),
      },
    }),
  },
});
