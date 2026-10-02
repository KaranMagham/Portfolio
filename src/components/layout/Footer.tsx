export function Footer() {
  return (
    <footer className="border-t border-white/10 py-7">
      <div className="mx-auto flex w-full max-w-6xl flex-col gap-2 px-4 text-sm text-zinc-400 sm:flex-row sm:items-center sm:justify-between sm:px-6">
        <p>© {new Date().getFullYear()} Karan Magham</p>
        <p>Built with Next.js, TypeScript, Tailwind CSS, and Framer Motion.</p>
      </div>
    </footer>
  );
}
