const navItems = [
  { label: "About", href: "#about" },
  { label: "Skills", href: "#skills" },
  { label: "Projects", href: "#projects" },
  { label: "Experience", href: "#experience" },
  { label: "Contact", href: "#contact" },
];

export function Navbar() {
  return (
    <header className="sticky top-0 z-40 border-b border-white/10 bg-black/50 backdrop-blur-xl">
      <nav
        className="mx-auto flex h-16 w-full max-w-6xl items-center justify-between px-4 sm:px-6"
        aria-label="Main navigation"
      >
        <a href="#home" className="text-sm font-semibold tracking-wide text-white sm:text-base">
          Karan Magham
        </a>
        <ul className="hidden items-center gap-5 md:flex">
          {navItems.map((item) => (
            <li key={item.href}>
              <a
                href={item.href}
                className="text-sm text-zinc-300 transition hover:text-white focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-cyan-400/60"
              >
                {item.label}
              </a>
            </li>
          ))}
        </ul>
        <a
          href="#contact"
          className="rounded-full border border-cyan-400/40 bg-cyan-400/10 px-4 py-2 text-xs font-medium text-cyan-200 transition hover:bg-cyan-400/20 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-cyan-400/70"
        >
          Let&apos;s Talk
        </a>
      </nav>
    </header>
  );
}
