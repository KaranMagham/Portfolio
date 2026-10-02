import { Mail } from "lucide-react";

import { AnimatedSection } from "@/components/ui/AnimatedSection";
import { SectionHeading } from "@/components/ui/SectionHeading";

export function ContactSection() {
  return (
    <AnimatedSection id="contact" labelledBy="contact-title" className="mx-auto w-full max-w-6xl px-4 py-14 sm:px-6">
      <h2 id="contact-title" className="sr-only">
        Contact
      </h2>
      <SectionHeading title="Contact" subtitle="Interested in collaborating? Let&apos;s connect." />
      <article className="rounded-2xl border border-white/10 bg-white/5 p-6 backdrop-blur">
        <a
          href="mailto:karan.magham@gmail.com"
          className="inline-flex items-center gap-2 rounded-full border border-cyan-400/30 bg-cyan-400/10 px-4 py-2 text-sm text-cyan-100 transition hover:bg-cyan-400/20 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-cyan-300"
        >
          <Mail size={16} />
          karan.magham@gmail.com
        </a>
        <p className="mt-4 text-sm leading-6 text-zinc-300">
          You can also reach out via GitHub or LinkedIn for project discussions, freelance opportunities, and full-time roles.
        </p>
      </article>
    </AnimatedSection>
  );
}
