---
name: muhdanfyan-standard
description: Standardized workflows and agentic mandates for Muhdan Fyan's workspace. Ensures backups, publications, and coding tasks follow advanced "Claude Agentic" patterns (SDD, Anti-Vibe Coding, Deep-Linking, Comprehensive Content).
---

# Muhdan Fyan Standard Skill (Agentic Edition)

This skill mandates how agents must behave and execute tasks within Muhdan Fyan's environment, integrating advanced agentic workflows and premium publication standards.

## 🤖 Core Agentic Directives (Anti-Vibe Coding)

### 1. Spec-Driven Development (SDD) & Anti-Truncation
Agents MUST NOT engage in "Vibe Coding" or simplify complex topics.
- **The Cycle:** `Explore ➔ Plan ➔ Code`.
- **Anti-Truncation:** Every point from a reference or article MUST be explained in depth. Never simplify or omit technical details.
- **The No-Stop Directive:** When testing, use the mindset: "Do not stop until the script passes 100% via otonom self-correction."

### 2. Context Management (Handovers)
- **Action:** Proactively suggest a `handover.md` when context exceeds 80% capacity to maintain agent "intelligence" levels.

---

## ✍️ Content & Publication Standards (Premium UX)

### 1. Manual Publication Procedure (Critical for Live Updates)
To ensure articles and images appear correctly on `muhdanfyan.github.io`, agents MUST follow these post-build steps:
- **Image Validation:**
  - Verify extension match (e.g., if file is `.jpg`, code MUST NOT seek `.png`).
  - **Asset Sync:** Copy images from `public/img/screenshots/` to root `/img/screenshots/` and `/dist/img/screenshots/`.
- **Static HTML Generation:**
  - Every new article MUST have an `index.html` file in its directory (e.g., `tulisan/[slug]/index.html`).
  - Use the Premium Layout template (ID/EN support, OG Tags, responsive design).
- **Link Logic:**
  - Use **Relative Paths** for all assets (e.g., `/img/screenshots/name.jpg` instead of full URLs) to ensure compatibility across environments.
- **Deployment & Synchronization:**
  - **Git Workflow:** `git add .` -> `git commit -m "feat/fix: [desc]"` -> `git push origin main`.
  - **Force Sync:** If files are git-ignored but needed live (like `/dist/`), use `git add -f [path]` to force inclusion.

### 2. File Structure & Manifest
Every article must follow this strictly:
- **Markdown:** `tulisan/[slug]/tulisan.md`.
- **SEO Static:** `tulisan/[slug]/index.html` (Must match the premium article layout and contain FULL content).
- **Manifest:** Sync `data/manifest.json` with valid high-res image URLs.

### 2. Article Formatting Mandates
- **Publication Date:** Placed at the very top (below title) with 📅 **Day Month Year**.
- **Visual & Typography Standards:**
  - **Semantic Links:** AI Agent MUST map Markdown links `[Text](URL)` to semantic `<a>` tags with `target="_blank"` and appropriate hover styles.
  - **Drop Cap:** Paragraph 1 MUST use the `.dropcap` class (huruf pertama besar dan artistik).
  - **Gradient Headlines:** `h2` elements MUST use CSS gradients (Indigo to Purple).
  - **Custom Callouts:** Crucial quotes/insights MUST be wrapped in a `.callout` box with a light background and accent border.
  - **High-End Visuals:** Primary images MUST use `.glass-img` (rounded 2rem, deep shadow, hover effect).
  - **Code Highlights:** Technical terms or inline code MUST use the `.highlight` span (Indigo background, JetBrains Mono font).
- **Language:** Foreign terms (English/etc.) MUST be *italicized*.
- **Deep Linking:** Every technical term, tool, or advanced concept MUST be hyper-linked to its official documentation or a reputable reference.
- **Indonesia Perspective:** Include context relevant to Indonesian developers (e.g., Termux, local culture).
- **Footer:** Mandatory footer: **Sumber:** [Link] | **Penulis:** Muhdan Fyan Syah Sofian | **Standardized via Gemini CLI**.

### 3. SEO & Rich Preview (WhatsApp/Social)
- **Link Preview Standards:**
  - **Absolute URLs for Meta Tags:** OG Tags (`og:image`) and Twitter Cards MUST use absolute URLs (e.g., `https://muhdanfyan.github.io/img/...`).
  - **Relative Paths for Content:** Internal `<img>` tags SHOULD use relative paths (`/img/...`) for portability.
- **Image Optimization:** 
  - **Dimensions:** Aim for 1200x630px for optimal social media scaling.
  - **Compatibility:** Use `.jpg` or `.png`. Verify the extension matches the file exactly (case-sensitive).
- **JSON-LD:** `TechArticle` schema with correct author metadata.

---

## 📦 Infrastructure & Backup Standards
- **Pattern:** `rclone move /sdcard/ gdrive:Backup_HP_Deep/` with standard excludes.
- **Hierarchy:** `Media/`, `Documents_All/`, `System_Apps/`.

---
*Standard established in April 2026. This skill is the single source of truth for the muhdanfyan workspace. Never compromise on depth or quality.*
