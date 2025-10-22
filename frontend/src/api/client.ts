/**
 * Simple REST API client using fetch
 * To be migrated to Apollo Client + GraphQL
 */

const API_BASE_URL = 'http://localhost:8000/api';

export const api = {
  // Users endpoints
  async getUsers() {
    const response = await fetch(`${API_BASE_URL}/users`);
    return response.json();
  },

  async getUser(id: number) {
    const response = await fetch(`${API_BASE_URL}/users/${id}`);
    return response.json();
  },

  async createUser(name: string, email: string) {
    const response = await fetch(`${API_BASE_URL}/users`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email }),
    });
    return response.json();
  },

  // Posts endpoints
  async getPosts() {
    const response = await fetch(`${API_BASE_URL}/posts`);
    return response.json();
  },

  async getPost(id: number) {
    const response = await fetch(`${API_BASE_URL}/posts/${id}`);
    return response.json();
  },

  async createPost(title: string, content: string, author_id: number) {
    const response = await fetch(`${API_BASE_URL}/posts`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ title, content, author_id }),
    });
    return response.json();
  },
};
