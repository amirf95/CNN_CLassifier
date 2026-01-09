import React, { useEffect, useState } from "react";
import Swal from "sweetalert2";
import "./History.css";

function History() {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/history")
      .then((res) => res.json())
      .then((data) => setHistory(data))
      .catch(() =>
        Swal.fire("Error", "Failed to load history", "error")
      )
      .finally(() => setLoading(false));
  }, []);
 const handleHome = () => {
        window.location.href = "/";
    };
  return (
    <div className="history-page">
      <h1>Prediction History</h1>

      {loading && <p>Loading history...</p>}

      {!loading && history.length === 0 && (
        <p>No predictions saved yet.</p>
      )}

      <div className="history-grid">
        {history.map((item) => (
          <div key={item.id} className={`history-card ${item.label}`}>
            <h3>{item.label.toUpperCase()}</h3>

            <p>
              <strong>Confidence:</strong>{" "}
              {(item.confidence * 100).toFixed(2)}%
            </p>

            <p>
              <strong>Image:</strong> {item.image_name}
            </p>

            <p className="date">
              {new Date(item.created_at).toLocaleString()}
            </p>
            
          </div>
        ))}
        <div>
            <button className="secondary" onClick={handleHome}>
                        🏠 Home
            </button>
        </div>
      </div>
      
    </div>
  );
}

export default History;
