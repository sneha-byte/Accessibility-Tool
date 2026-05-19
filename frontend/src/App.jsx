import { useState, useEffect, use } from "react";

export default function App() {

  [imageUrl, setImageUrl] = useState("");

  useEffect(() => {
    setImageUrl("http://localhost:8000/screenshot");
  }, []);


  return (
    <img
      src={imageUrl}
      width="100%"
    />
  );
}