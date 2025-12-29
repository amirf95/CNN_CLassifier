import  {useState}  from "react";
import Swal from "sweetalert2";
import "./Identification.css";
import VantaBackground from "./VantaBackgound";
import p5 from "p5";
window.p5 = p5;
function Identification() {
    const [image, setImage] = useState(null);
    const [preview, setPreview] = useState(null);
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);
    const [dragging, setDragging] = useState(false);


    
    const handleFile = (file) => {
        if (!file || !file.type.startsWith("image/")) {
            Swal.fire("Invalid file", "Please upload an image file", "error");
            return;
        }
        setImage(file);
        setPreview(URL.createObjectURL(file));
        setResult(null);
    };

    const handleDrop = (e) => {
        e.preventDefault();
        setDragging(false);
        handleFile(e.dataTransfer.files[0]);
    };

    const handleSubmit = async () => {
        if (!image) {
            Swal.fire("No image", "Please upload an image first", "warning");
            return;
        }

        const formData = new FormData();
        formData.append("image", image);

        try {
            setLoading(true);

            const response = await fetch("http://127.0.0.1:8000/predict", {
                method: "POST",
                body: formData,
            });

            if (!response.ok) throw new Error("Server error");

            const data = await response.json();
            setResult(data);
        } catch (err) {
            Swal.fire("Prediction failed", err.message, "error");
        } finally {
            setLoading(false);
        }
    };

    const glowClass =
        result?.label === "culex"
            ? "glow-danger"
            : result?.label === "non_culex"
                ? "glow-success"
                : "glow-warning";
const handleSave = async () => {
  if (!result) {
    Swal.fire("Nothing to save", "Run a prediction first", "info");
    return;
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/save", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        label: result.label,
        confidence: result.confidence,
        image_name: image?.name || "unknown",
      }),
    });

    if (!response.ok) throw new Error("Save failed");

    Swal.fire("Saved!", "Prediction stored successfully", "success");
  } catch (err) {
    Swal.fire("Error", err.message, "error");
  }
};

    const handleHome = () => {
        window.location.href = "/";
    };
    return (
        <div className="page" >
            <div className={`card ${glowClass}`}>
                <h1>Culex Detection</h1>
                <p className="subtitle">AI-powered mosquito classifier</p>

                {/* Drag & Drop */}
                <div>
                    <label
                        className={`upload-box ${dragging ? "dragging" : ""}`}
                        onDragOver={(e) => {
                            e.preventDefault();
                            setDragging(true);
                        }}
                        onDragLeave={() => setDragging(false)}
                        onDrop={handleDrop}
                    >
                        <input
                            type="file"
                            accept="image/*"
                            onChange={(e) => handleFile(e.target.files[0])}
                        />
                        <span>Drag & drop or click to upload</span>
                    </label>
                </div>

                {preview && <img src={preview} className="preview" />}

                <button onClick={handleSubmit} disabled={loading}>
                    {loading ? "Analyzing..." : "Predict"}
                </button>

                {/* Loading Skeleton */}
                {loading && (
                    <div className="skeleton">
                        <div className="skeleton-bar" />
                        <div className="skeleton-text" />
                    </div>
                )}

                {/* Result */}
                {result && !loading && (
                    <div className={`result ${result.label}`}>
                        <h3>{result.label.toUpperCase()}</h3>

                        <div className="confidence-bar">
                            <div
                                className="fill"
                                style={{ width: `${result.confidence * 100}%` }}
                            />
                        </div>

                        <p>{(result.confidence * 100).toFixed(2)}% confidence</p>
                    </div>
                )}
                

                <div className="action-buttons">
                    <button
                        className="secondary"
                        onClick={handleSave}
                        disabled={!result}
                    >
                        💾 Save Result
                    </button>

                    <button className="secondary" onClick={handleHome}>
                        🏠 Home
                    </button>
                </div>
            </div>
            
        </div>
    );
}

export default Identification;
