import React from 'react';

import { render, screen, fireEvent } from '@testing-library/react';
import PostList from '../components/PostList';

test('renders post titles and triggers onSelect', () => {
  const posts = [
    { id: 1, title: 'Test Post', content: 'Test content' },
  ];
  const onSelect = jest.fn();
  render(<PostList posts={posts} onSelect={onSelect} />);

  const button = screen.getByText('Test Post');
  fireEvent.click(button);
  expect(onSelect).toHaveBeenCalledWith(posts[0]);
});
