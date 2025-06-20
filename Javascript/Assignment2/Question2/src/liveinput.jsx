import React from "react";

function LiveInput({ text, onTextChange }) {
return (
    <div>
    <h2 style={{ marginTop: "2rem" }}>Live Input</h2>
    <input
        type="text"
        value={text}
        onChange={e => onTextChange(e.target.value)}
        placeholder="Type something..."
    />
    <p>Typed text: {text}</p>
    </div>
);
}

export default LiveInput;