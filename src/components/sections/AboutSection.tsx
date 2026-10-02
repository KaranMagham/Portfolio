import { AnimatedSection } from "@/components/ui/AnimatedSection";
import { SectionHeading } from "@/components/ui/SectionHeading";

export function AboutSection() {
  return (
    <AnimatedSection id="about" labelledBy="about-title" className="mx-auto w-full max-w-6xl px-4 py-14 sm:px-6">
      <SectionHeading
        title="About"
        subtitle="I enjoy creating polished full stack experiences that combine strong engineering fundamentals with practical AI-driven capabilities."
      />
      <article className="rounded-2xl border border-white/10 bg-white/5 p-6 text-zinc-300 backdrop-blur">
        <h3 id="about-title" className="sr-only">
          About Karan Magham
        </h3>
        <p className="leading-7">
          My work centers around delivering responsive, maintainable products with clean architecture, thoughtful UX, and scalable APIs. I focus on meaningful product outcomes while keeping implementation quality high.
        </p>
      </article>
    </AnimatedSection>
  );
}
