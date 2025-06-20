import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import UserCard from './UserCard'

function App() {
  const user = {
    name: "Disha Bundela",
    age: 21,
    email: "dishabundela@gmail.com",
    city: "Indore"
  }

  return (
    <>
      <div style={styles.app}>
        <h1 style={{color: 'darkblue'}}>User Profile Card</h1>
        <UserCard user={user}/>
      </div>
    </>
  )
}

const styles = {
  app: {
    fontFamily: 'Arial, sans-serif',
    padding: '20px',
    backgroundColor: '#f3f3f3',
  }
};

export default App
