# Muhdan Fyan Portfolio - Claude Development Guide

## Project Overview
Modern portfolio website built with **Astro 6** and **Tailwind CSS**. It serves as a centralized hub for projects and writings, supporting bilingual (ID/EN) content.

## Technology Stack
- **Framework**: Astro 6 (Static Site Generation)
- **Styling**: Tailwind CSS
- **Testing**: Vitest (Unit), Playwright (E2E)
- **Data**: JSON Manifest (`data/manifest.json`) & Markdown articles

## Project Structure
- `src/pages/`: Astro pages (routing)
- `src/layouts/`: Base templates
- `src/components/`: Reusable UI components
- `src/utils/`: Logic helpers
- `data/`: Content manifest and metadata
- `tulisan/`: Markdown articles in ID and EN

## Development Commands
- `npm run dev`: Start local development server
- `npm run build`: Generate production static site (`dist/`)
- `npm run test`: Run unit tests via Vitest
- `npm run preview`: Preview the production build locally

## Agentic System (ECC)
This project uses the **Everything Claude Code (ECC)** system for advanced automation.
- **Skills Directory**: `.claude/skills/`
- **Agents Directory**: `.claude/agents/`
- **Rules Directory**: `.claude/rules/`

## Content Guidelines
When adding new writings:
1. Update `data/manifest.json` with the new entry.
2. Specify `available_langs` (e.g., `["id", "en"]`).
3. Create the corresponding Markdown files in `tulisan/[slug]/`.
4. Use `.en.md` suffix for English versions.
