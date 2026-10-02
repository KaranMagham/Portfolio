import { AnimatedSection } from "@/components/ui/AnimatedSection";
import { SectionHeading } from "@/components/ui/SectionHeading";
import { skills } from "@/data/skills";

export function SkillsSection() {
  return (
    <AnimatedSection id="skills" labelledBy="skills-title" className="mx-auto w-full max-w-6xl px-4 py-14 sm:px-6">
      <h2 id="skills-title" className="sr-only">
        Skills
      </h2>
      <SectionHeading title="Skills" subtitle="Technologies and tools I use to build full stack web products." />
      <ul className="grid grid-cols-2 gap-3 sm:grid-cols-3 md:grid-cols-4">
        {skills.map((skill) => (
          <li
            key={skill.name}
            className="rounded-xl border border-white/10 bg-white/5 px-4 py-3 text-sm text-zinc-200 backdrop-blur transition hover:border-cyan-300/35"
          >
            {skill.name}
          </li>
        ))}
      </ul>
    </AnimatedSection>
  );
}
