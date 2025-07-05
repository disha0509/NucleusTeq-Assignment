import React from 'react';

import { render, screen } from '@testing-library/react';

import PostDetail from '../components/PostDetail';

test('shows fallback when no post selected', () => {
  render(<PostDetail post={null} />);
  expect(screen.getByText(/select a post/i)).toBeInTheDocument();
});

test('shows post content when selected', () => {
  const post = { id: 1, title: 'Demo', content: 'Demo Content' };
  render(<PostDetail post={post} />);
  expect(screen.getByText('Demo')).toBeInTheDocument();
  expect(screen.getByText('Demo Content')).toBeInTheDocument();
});
