import { useState, useEffect } from 'react';
import PostList from '../components/PostList';
import PostDetail from '../components/PostDetail';
import styles from './PostsPage.module.css';

export async function getStaticProps() {
  const res = await fetch('http://localhost:3000/api/posts');
  const posts = await res.json();
  return { props: { posts } };
}

export default function PostsPage({ posts }) {
  const [selectedPost, setSelectedPost] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const timer = setTimeout(() => setLoading(false), 800);
    return () => clearTimeout(timer);
  }, []);

  if (loading) {
    return (
      <div className={styles.centered}>
        <p className={styles.loadingText}>Loading blog posts...</p>
      </div>
    );
  }

  return (
    <main className={styles.bgGradient}>
      <div className={styles.wrapper}>
        <h1 className={styles.heading}>📝 Blog Viewer</h1>
        <div className={styles.grid}>
          <div>
            <h2 className={styles.sectionTitle}>All Posts</h2>
            <PostList posts={posts} onSelect={setSelectedPost} />
          </div>
          <div>
            <h2 className={styles.sectionTitle}>Post Details</h2>
            <PostDetail post={selectedPost} />
          </div>
        </div>
      </div>
    </main>
  );
}