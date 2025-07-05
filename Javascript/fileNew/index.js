import express from "express";

const app = express();

const PORT = process.env.PORT || 3000;

// GET all products
app.get("/api/products", (req, res) => {
  const products = [
    { id: 1, name: "Laptop", price: 60000 },
    { id: 2, name: "Phone", price: 30000 },
    { id: 3, name: "Headphones", price: 2000 },
  ];

  setTimeout(() => {
    console.log("Sending products");
    res.send(products);
  }, 3000);
});

app.get("/", (req, res) => {
  res.send("Hello, World!");
});

app.listen(PORT, () => {
  console.log("Server is running on http://localhost:${PORT}");
});