import styles from "./PostList.module.css";

export default function PostList({ posts, onSelect }) {
  return (
    <ul className={styles.list}>
      {posts.map((post) => (
        <li key={post.id} className={styles.listItem}>
          <button
            onClick={() => onSelect(post)}
            className={styles.button}
          >
            {post.title}
          </button>
        </li>
      ))}
    </ul>
  );
}