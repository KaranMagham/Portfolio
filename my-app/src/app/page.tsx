import { AboutPreview } from "@/components/home/AboutPreview";
import { FeaturedProject } from "@/components/home/FeaturedProject";
import { Hero } from "@/components/home/Hero";
import { Journey } from "@/components/home/Journey";
import { SkillsPreview } from "@/components/home/SkillsPreview";

export default function Home() {
  return (
    <main className="site-shell">
      <header className="site-header">
        <a className="wordmark" href="#top"><span>KM</span><b>Karan Magham</b></a>
        <nav className="site-nav" aria-label="Primary navigation"><a href="#about">About</a><a href="#skills">Stack</a><a href="#journey">Journey</a><a href="#projects">Projects</a></nav>
        <a className="header-contact" href="mailto:hello@karanmagham.dev">Let&apos;s talk <span>↗</span></a>
      </header>
      <Hero /><AboutPreview /><SkillsPreview /><Journey /><FeaturedProject />
      <footer className="site-footer"><div><span className="footer-mark">KM</span><p>Designed &amp; built by Karan Magham<br /><small>© 2025 — Making useful things for the web.</small></p></div><div className="footer-socials"><a href="https://github.com/" aria-label="Karan on GitHub">GH</a><a href="https://www.linkedin.com/" aria-label="Karan on LinkedIn">in</a><a href="#top" className="back-top">Back to top ↗</a></div></footer>
    </main>
  );
}
