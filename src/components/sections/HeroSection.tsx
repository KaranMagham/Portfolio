"use client";

import { motion } from "framer-motion";

export function HeroSection() {
  return (
    <section
      id="home"
      aria-labelledby="hero-title"
      className="mx-auto grid w-full max-w-6xl gap-10 px-4 pb-20 pt-14 sm:px-6 lg:grid-cols-2 lg:items-center lg:pt-20"
    >
      <div>
        <p className="mb-4 inline-flex rounded-full border border-violet-300/30 bg-violet-400/10 px-3 py-1 text-xs tracking-wide text-violet-200">
          Full Stack Web Developer
        </p>
        <h1 id="hero-title" className="text-4xl font-semibold tracking-tight text-white sm:text-5xl">
          Karan Magham
        </h1>
        <p className="mt-5 max-w-xl text-zinc-300 sm:text-lg">
          I build modern web applications and AI-integrated software with fast, scalable, and user-focused product experiences.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <a
            href="#projects"
            className="rounded-full bg-gradient-to-r from-violet-500 to-cyan-500 px-5 py-2.5 text-sm font-medium text-white transition hover:opacity-90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-violet-300"
          >
            View Projects
          </a>
          <a
            href="#contact"
            className="rounded-full border border-white/20 bg-white/5 px-5 py-2.5 text-sm font-medium text-zinc-100 transition hover:bg-white/10 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-cyan-300"
          >
            Contact Me
          </a>
        </div>
        <div className="mt-6 flex items-center gap-3 text-sm">
          <a
            href="https://github.com/KaranMagham"
            target="_blank"
            rel="noreferrer"
            className="rounded-full border border-white/15 bg-white/5 px-4 py-2 text-zinc-200 transition hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-cyan-400/80"
          >
            GitHub
          </a>
          <a
            href="https://www.linkedin.com/in/karan-magham"
            target="_blank"
            rel="noreferrer"
            className="rounded-full border border-white/15 bg-white/5 px-4 py-2 text-zinc-200 transition hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-cyan-400/80"
          >
            LinkedIn
          </a>
        </div>
      </div>

      <motion.div
        className="relative rounded-2xl border border-white/10 bg-white/5 p-5 backdrop-blur"
        initial={{ opacity: 0, x: 24 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.6, ease: "easeOut", delay: 0.1 }}
      >
        <div className="mb-4 flex items-center gap-2">
          <span className="h-2.5 w-2.5 rounded-full bg-rose-400" />
          <span className="h-2.5 w-2.5 rounded-full bg-amber-300" />
          <span className="h-2.5 w-2.5 rounded-full bg-emerald-400" />
        </div>
        <div className="space-y-3 font-mono text-xs text-cyan-100/90 sm:text-sm">
          <p>
            <span className="text-cyan-300">const</span> developer = {'{'}
          </p>
          <p className="pl-4">
            name: <span className="text-violet-300">&quot;Karan Magham&quot;</span>,
          </p>
          <p className="pl-4">
            focus: [<span className="text-violet-300">&quot;Web Apps&quot;</span>, <span className="text-violet-300">&quot;AI Integration&quot;</span>],
          </p>
          <p className="pl-4">ship: () =&gt; modernProducts()</p>
          <p>{'}'}</p>
        </div>
        <motion.div
          className="mt-5 h-1.5 w-20 rounded-full bg-gradient-to-r from-violet-500 via-blue-500 to-teal-400"
          animate={{ width: [80, 180, 80] }}
          transition={{ duration: 3.2, repeat: Infinity, ease: "easeInOut" }}
        />
      </motion.div>
    </section>
  );
}
