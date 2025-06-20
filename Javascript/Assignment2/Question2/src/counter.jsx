import React from "react";

function Counter({ count, onIncrement, onDecrement }) {
return (
    <div>
    <h2>Counter</h2>
    <button onClick={onDecrement}>-</button>
    <span style={{ margin: "0 1rem" }}>{count}</span>
    <button onClick={onIncrement}>+</button>
    </div>
);
}

export default Counter;