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
    portfolio: collection({
      label: 'Portofolio',
      slugField: 'slug',
      path: 'content/portfolio/*/',
      format: { contentField: 'content' },
      entryLayout: 'content',
      schema: {
        slug: fields.text({ label: 'Slug' }),
        title: fields.text({ label: 'Judul Proyek' }),
        title_en: fields.text({ label: 'Project Title' }),
        description: fields.text({ label: 'Deskripsi (ID)', multiline: true }),
        description_en: fields.text({ label: 'Description (EN)', multiline: true }),
        image: fields.image({
          label: 'Gambar Proyek',
          directory: 'public/img/portfolio',
          publicPath: '/img/portfolio',
        }),
        category: fields.text({ label: 'Kategori (e.g. Government, UMKM)' }),
        difficulty: fields.select({
          label: 'Tingkat Kesulitan',
          options: [
            { label: 'Basic', value: 'Basic' },
            { label: 'Intermediate', value: 'Intermediate' },
            { label: 'Advanced', value: 'Advanced' },
            { label: 'Expert', value: 'Expert' },
          ],
          defaultValue: 'Intermediate',
        }),
        link: fields.text({ label: 'Link Aplikasi' }),
        whatsapp_text: fields.text({ label: 'Custom WhatsApp Text' }),
        tech_stack: fields.array(fields.text({ label: 'Teknologi' }), { label: 'Tech Stack' }),
        highlights: fields.array(fields.text({ label: 'Poin Utama (ID)' }), { label: 'Highlights (ID)' }),
        highlights_en: fields.array(fields.text({ label: 'Poin Utama (EN)' }), { label: 'Highlights (EN)' }),
        metrics: fields.object({
          performance: fields.integer({ label: 'Performance', defaultValue: 100 }),
          accessibility: fields.integer({ label: 'Accessibility', defaultValue: 100 }),
          best_practices: fields.integer({ label: 'Best Practices', defaultValue: 100 }),
          seo: fields.integer({ label: 'SEO', defaultValue: 100 }),
        }, { label: 'Lighthouse Metrics' }),
        is_featured: fields.checkbox({ label: 'Tampilkan di Homepage', defaultValue: false }),
        content: fields.markdoc({ label: 'Detail Proyek' }),
      },
    }),
    experience: collection({
      label: 'Pengalaman Kerja',
      slugField: 'slug',
      path: 'content/experience/*/',
      format: { contentField: 'content' },
      entryLayout: 'content',
      schema: {
        slug: fields.text({ label: 'Slug' }),
        company: fields.text({ label: 'Perusahaan' }),
        position: fields.text({ label: 'Posisi (ID)' }),
        position_en: fields.text({ label: 'Position (EN)' }),
        period: fields.text({ label: 'Periode (e.g. 2017 - Present)' }),
        period_en: fields.text({ label: 'Period (e.g. 2017 - Present)' }),
        link: fields.text({ label: 'Link Perusahaan' }),
        order: fields.integer({ label: 'Urutan Tampilan', defaultValue: 0 }),
        content: fields.markdoc({ label: 'Deskripsi Pekerjaan' }),
      },
    }),
    education: collection({
      label: 'Pendidikan',
      slugField: 'slug',
      path: 'content/education/*/',
      format: { contentField: 'content' },
      entryLayout: 'content',
      schema: {
        slug: fields.text({ label: 'Slug' }),
        school: fields.text({ label: 'Institusi' }),
        degree: fields.text({ label: 'Gelar/Jurusan (ID)' }),
        degree_en: fields.text({ label: 'Degree/Major (EN)' }),
        period: fields.text({ label: 'Periode' }),
        period_en: fields.text({ label: 'Period' }),
        order: fields.integer({ label: 'Urutan Tampilan', defaultValue: 0 }),
        content: fields.markdoc({ label: 'Deskripsi Pendidikan' }),
      },
    }),
    teaching: collection({
      label: 'Pengalaman Mengajar',
      slugField: 'slug',
      path: 'content/teaching/*/',
      format: { contentField: 'content' },
      entryLayout: 'content',
      schema: {
        slug: fields.text({ label: 'Slug' }),
        event: fields.text({ label: 'Nama Acara/Kelas' }),
        topic: fields.text({ label: 'Topik/Materi' }),
        period: fields.text({ label: 'Waktu' }),
        order: fields.integer({ label: 'Urutan Tampilan', defaultValue: 0 }),
        content: fields.markdoc({ label: 'Detail Materi' }),
      },
    }),
  },
});
