import { useState } from 'react'
import Counter from './Counter'
import LiveInput from './LiveInput'
import VisibilityToggle from './VisibilityToggle'
import './App.css'

function App() {
  const [count, setCount] = useState(0)
  const [toggle, setToggle] = useState(false)
  const [text, setText] = useState("")

  return (
    <div style={{ padding: "2rem" }}>
      <Counter
        count={count}
        onIncrement={() => setCount(count + 1)}
        onDecrement={() => setCount(count - 1)}
      />
      <LiveInput
        text={text}
        onTextChange={setText}
      />
      <VisibilityToggle
        visible={toggle}
        onToggle={() => setToggle(!toggle)}
      />
    </div>
  )
}

export default App