import { useEffect, useState } from "react";
import "./App.css";
import axios from "axios";

function App() {
  const [products, setProducts] = useState([]);
  useEffect(() => {
    (async () => {
      try {
        const response = await axios.get("/api/products");
        setProducts(response?.data);
        console.log(response);
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    })();
  }, []);
  return (
    <div>
      <h2>Learning API Integration</h2>
      <h3>No. of Products {products?.length} </h3>
    </div>
  );
}
export default App;