"use client";

import { motion, useMotionValue, useSpring, useTransform } from "framer-motion";
import { Code2, Database, Sparkles, Terminal } from "lucide-react";
import Image from "next/image";
import { useRef, useState } from "react";

const floatingTools = [
  { icon: Code2, label: "React", position: "tool-react" },
  { icon: Database, label: "MongoDB", position: "tool-db" },
  { icon: Terminal, label: "Node", position: "tool-node" },
  { icon: Sparkles, label: "AI", position: "tool-ai" },
];

export function ProfileVisual() {
  const areaRef = useRef<HTMLDivElement>(null);
  const [photoAvailable, setPhotoAvailable] = useState(true);
  const pointerX = useMotionValue(0);
  const pointerY = useMotionValue(0);
  const rotateX = useSpring(useTransform(pointerY, [-0.5, 0.5], [5, -5]), { stiffness: 120, damping: 22 });
  const rotateY = useSpring(useTransform(pointerX, [-0.5, 0.5], [-5, 5]), { stiffness: 120, damping: 22 });

  function handlePointerMove(event: React.PointerEvent<HTMLDivElement>) {
    if (!areaRef.current) return;
    const bounds = areaRef.current.getBoundingClientRect();
    pointerX.set((event.clientX - bounds.left) / bounds.width - 0.5);
    pointerY.set((event.clientY - bounds.top) / bounds.height - 0.5);
  }

  function resetPointer() {
    pointerX.set(0);
    pointerY.set(0);
  }

  return (
    <div className="profile-stage" ref={areaRef} onPointerMove={handlePointerMove} onPointerLeave={resetPointer}>
      <div className="stage-grid" aria-hidden="true" />
      <div className="stage-orbit orbit-one" aria-hidden="true" />
      <div className="stage-orbit orbit-two" aria-hidden="true" />
      <div className="stage-glow" aria-hidden="true" />
      <motion.div className="profile-object" style={{ rotateX, rotateY }}>
        <motion.div
          className="profile-frame"
          animate={{
            rotateX: [0, 4, 0, -3, 0],
            rotateY: [0, -5, 3, 0, 0],
            rotateZ: [0, 1.5, 0, -1, 0],
            y: [0, -7, 2, 7, 0],
            x: [0, 2, -2, 1, 0],
          }}
          transition={{ duration: 26, repeat: Infinity, ease: "easeInOut" }}
        >
          <div className="profile-image-shell">
            {photoAvailable ? <Image className="profile-photo" src="/profile.jpg" alt="Karan Magham" fill sizes="(max-width: 640px) 200px, 290px" onError={() => setPhotoAvailable(false)} /> : <div className="profile-photo-placeholder"><span className="profile-monogram">KM</span><span className="profile-photo-note">Your photo here</span></div>}
            <div className="profile-scanline" aria-hidden="true" />
          </div>
          <div className="profile-caption"><span className="caption-dot" /><span>Building in public</span></div>
        </motion.div>
      </motion.div>
      {floatingTools.map(({ icon: Icon, label, position }) => (
        <motion.div className={`floating-tool ${position}`} key={label} animate={{ y: [0, -8, 0], rotate: [0, 3, 0] }} transition={{ duration: 5 + label.length / 2, repeat: Infinity, ease: "easeInOut", delay: label.length / 8 }}>
          <Icon size={15} strokeWidth={1.8} /><span>{label}</span>
        </motion.div>
      ))}
      <span className="coordinate coordinate-top">19.0760° N</span>
      <span className="coordinate coordinate-bottom">72.8777° E</span>
    </div>
  );
}