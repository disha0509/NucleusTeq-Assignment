import Link from "next/link";
import styles from "./Home.module.css";

export default function Home() {
  return (
    <main className={styles.main}>
      <div className={styles.container}>
        <h1 className={styles.heading}>
          Welcome to the Blog Viewer👩🏻‍💻
        </h1>
        <p className={styles.description}>
          You can view, search, and explore blog posts from various authors.
        </p>
        <Link
          href="/posts"
          className={styles.button}
        >
          View Blog Posts
        </Link>
      </div>
    </main>
  );
}