import React from "react";

function VisibilityToggle({ visible, onToggle }) {
return (
    <div>
    <h2 style={{ marginTop: "2rem" }}>Visibility Toggle</h2>
    <button onClick={onToggle}>
        {visible ? "Hide" : "Show"} Paragraph
    </button>
    {visible && (
        <p style={{ marginTop: "1rem" }}>
        This paragraph can be shown or hidden.
        </p>
    )}
    </div>
);
}

export default VisibilityToggle;