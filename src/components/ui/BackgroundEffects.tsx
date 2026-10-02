export function BackgroundEffects() {
  return (
    <>
      <div aria-hidden className="pointer-events-none fixed inset-0 -z-20 bg-[#06070b]" />
      <div
        aria-hidden
        className="pointer-events-none fixed inset-0 -z-10 opacity-[0.14]"
        style={{
          backgroundImage:
            "linear-gradient(rgba(148,163,184,0.12) 1px, transparent 1px), linear-gradient(90deg, rgba(148,163,184,0.12) 1px, transparent 1px)",
          backgroundSize: "42px 42px",
        }}
      />
      <div aria-hidden className="pointer-events-none fixed inset-0 -z-10 noise-overlay" />
      <div aria-hidden className="pointer-events-none fixed left-[-15%] top-[-10%] -z-10 h-72 w-72 rounded-full bg-violet-600/20 blur-3xl" />
      <div aria-hidden className="pointer-events-none fixed right-[-12%] top-[20%] -z-10 h-72 w-72 rounded-full bg-cyan-500/20 blur-3xl" />
      <div aria-hidden className="pointer-events-none fixed bottom-[-16%] left-[28%] -z-10 h-80 w-80 rounded-full bg-blue-600/20 blur-3xl" />
    </>
  );
}
