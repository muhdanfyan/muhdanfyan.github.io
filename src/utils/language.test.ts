import { describe, it, expect } from 'vitest';

// Sederhana helper untuk tes
export function getAvailableLangs(item) {
  return item.available_langs || ['id'];
}

describe('Language Utility', () => {
  it('should return default [id] if available_langs is missing', () => {
    const item = { title: 'Test' };
    expect(getAvailableLangs(item)).toEqual(['id']);
  });

  it('should return the correct available_langs if present', () => {
    const item = { available_langs: ['id', 'en'] };
    expect(getAvailableLangs(item)).toEqual(['id', 'en']);
  });
});
