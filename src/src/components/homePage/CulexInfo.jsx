// src/pages/CulexInfo.jsx
import React from "react";
import "./CulexInfo.css";
function CulexInfo() {
  return (
    <section className="culex-info-section">
  <span className="culex-badge">Mosquito Vector</span>

  <h2>🦟 Culex Mosquito</h2>

  <p>
    Culex mosquitoes are widespread insects commonly found near stagnant water
    sources such as drains, ponds, and containers. They are most active during
    the evening and nighttime.
  </p>

  <p>
    These mosquitoes are significant disease carriers, responsible for
    transmitting <strong>West Nile Virus</strong> and various forms of
    encephalitis, posing serious risks to public health.
  </p>

  <p>
    Early and accurate detection of Culex mosquitoes enables better disease
    prevention strategies and supports intelligent surveillance systems using
    artificial intelligence.
  </p>
<div className="Buttons">
  <a
    href="https://www.pestworld.org/pest-guide/mosquitoes/culex-mosquitoes/"
    target="_blank"
    rel="noopener noreferrer"
  >
    Learn More →
  </a>
  <a className="go-home-btn" onClick={() => window.location.href = "/"}>
  ⬅ Go to Home
</a>
</div>
</section>

  );
}

export default CulexInfo;
