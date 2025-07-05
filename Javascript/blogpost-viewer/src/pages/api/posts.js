export default function handler(req, res) {
  const articles = [
    {
      id: 1,
      title: 'Mastering Async JavaScript',
      content: `Async JavaScript includes callbacks, promises, and async/await. Understanding these concepts helps you write non-blocking code and handle operations like API calls, timers, and file reading efficiently.`,
    },
    {
      id: 2,
      title: 'Getting Started with Node.js',
      content: `Node.js allows you to run JavaScript on the server. It is event-driven, non-blocking, and perfect for building scalable network applications such as APIs, real-time chat, and streaming services.`,
    },
    {
      id: 3,
      title: 'CSS Grid vs Flexbox',
      content: `CSS Grid and Flexbox are powerful layout systems. Flexbox is best for one-dimensional layouts (row or column), while Grid is ideal for two-dimensional layouts, giving you more control over rows and columns.`,
    },
    {
      id: 4,
      title: 'The Power of Git & GitHub',
      content: `Git is a version control system that tracks code changes, while GitHub is a platform for hosting and collaborating on Git repositories. Together, they enable teamwork, code review, and open-source contributions.`,
    },
    {
      id: 5,
      title: 'Understanding JWT Authentication',
      content: `JWT (JSON Web Token) is a compact, URL-safe means of representing claims to be transferred between two parties. It is commonly used for authentication in web applications, enabling stateless and secure user sessions.`,
    },
    {
      id: 6,
      title: 'Frontend Performance Optimization',
      content: `Optimizing frontend performance involves techniques like code splitting, lazy loading, image optimization, and minimizing bundle size. These practices help improve load times and user experience.`,
    },
    {
      id: 7,
      title: 'State Management in React',
      content: `State management in React can be handled using useState, useReducer, Context API, or external libraries like Redux and Zustand. Choosing the right approach depends on your application's complexity and requirements.`,
    },
  ];

  res.status(200).json(articles);
}