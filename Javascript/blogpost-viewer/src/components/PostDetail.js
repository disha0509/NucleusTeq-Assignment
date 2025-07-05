import styles from "./PostDetail.module.css";

export default function PostDetail({ post }) {
  if (!post) {
    return (
      <div className={styles.empty}>
        <p>📌 Select a post to view its content.</p>
      </div>
    );
  }

  return (
    <div className={styles.detail}>
      <h3 className={styles.title}>{post.title}</h3>
      <p className={styles.content}>{post.content}</p>
    </div>
  );
}