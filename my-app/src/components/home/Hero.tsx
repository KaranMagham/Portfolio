"use client";

import { motion } from "framer-motion";
import { ArrowUpRight, MoveRight } from "lucide-react";
import { useEffect, useState } from "react";
import { portfolio } from "@/data/portfolio";
import { ProfileVisual } from "./ProfileVisual";

export function Hero() {
  const [roleIndex, setRoleIndex] = useState(0);

  useEffect(() => {
    const timer = window.setInterval(() => setRoleIndex((current) => (current + 1) % portfolio.roles.length), 3200);
    return () => window.clearInterval(timer);
  }, []);

  return (
    <section className="hero section-shell" id="top">
      <div className="hero-copy">
        <motion.div className="availability" initial={{ opacity: 0, y: 10 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.2 }}><span className="availability-pulse" />Available for opportunities</motion.div>
        <motion.p className="eyebrow" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.35 }}><span>01</span> / 04 — Introduction</motion.p>
        <motion.h1 initial={{ opacity: 0, y: 24 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.42, duration: 0.7 }}>Hi, I&apos;m <span>Karan</span><br />Magham.</motion.h1>
        <div className="role-line" aria-live="polite"><span className="role-mark">&gt;_</span><motion.span key={portfolio.roles[roleIndex]} initial={{ opacity: 0, y: 12 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.35 }}>{portfolio.roles[roleIndex]}</motion.span></div>
        <motion.p className="hero-intro" initial={{ opacity: 0, y: 18 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.7 }}>{portfolio.intro}</motion.p>
        <motion.div className="hero-actions" initial={{ opacity: 0, y: 18 }} animate={{ opacity: 1, y: 0 }} transition={{ delay: 0.82 }}><a className="button button-primary" href="#projects">View my projects <ArrowUpRight size={17} /></a><a className="button button-quiet" href="mailto:hello@karanmagham.dev">Contact me <MoveRight size={17} /></a></motion.div>
        <motion.div className="social-links" initial={{ opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 1 }}><span>Find me online</span><a href={portfolio.social.github} aria-label="Karan on GitHub">GH</a><a href={portfolio.social.linkedin} aria-label="Karan on LinkedIn">in</a></motion.div>
      </div>
      <motion.div className="hero-visual" initial={{ opacity: 0, scale: 0.92 }} animate={{ opacity: 1, scale: 1 }} transition={{ duration: 1, delay: 0.25 }}><ProfileVisual /></motion.div>
      <div className="scroll-cue"><span /> Scroll to explore</div>
    </section>
  );
}