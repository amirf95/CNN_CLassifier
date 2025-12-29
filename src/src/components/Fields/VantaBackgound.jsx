import React, { useEffect, useRef } from "react";
import * as THREE from "three"; // use npm package
import p5 from "p5";
window.p5 = p5;
window.THREE = THREE; // Vanta requires THREE on window

function VantaBackground({ children }) {
  const vantaRef = useRef(null);
  const vantaEffect = useRef(null);

  useEffect(() => {
    let vantaScript = document.createElement("script");
    vantaScript.src =
      "https://cdn.jsdelivr.net/npm/vanta/dist/vanta.topology.min.js";
    vantaScript.onload = () => {
      if (!vantaEffect.current && vantaRef.current) {
        vantaEffect.current = window.VANTA.TOPOLOGY({
          el: vantaRef.current,
          mouseControls: true,
          touchControls: true,
          gyroControls: false,
          minHeight: 200,
          minWidth: 200,
          scale: 1,
          scaleMobile: 1,
          color: 0x439028,
          backgroundColor: 0xa0a0a,
        });
      }
    };
    document.body.appendChild(vantaScript);

    return () => {
      if (vantaEffect.current) vantaEffect.current.destroy();
      if (vantaScript) document.body.removeChild(vantaScript);
    };
  }, []);

  return (
    <div style={{ position: "relative", width: "100%", height: "100vh" }}>
      <div
        ref={vantaRef}
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          width: "100%",
          height: "100%",
          zIndex: -1,
        }}
      />
      <div style={{ position: "relative", zIndex: 1 }}>{children}</div>
    </div>
  );
}

export default VantaBackground;
