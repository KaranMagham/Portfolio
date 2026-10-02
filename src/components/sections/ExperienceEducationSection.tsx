import { AnimatedSection } from "@/components/ui/AnimatedSection";
import { SectionHeading } from "@/components/ui/SectionHeading";
import { education, experience } from "@/data/timeline";
import type { TimelineItem } from "@/types/portfolio";

function TimelineCard({ item }: { item: TimelineItem }) {
  return (
    <article className="rounded-2xl border border-white/10 bg-white/5 p-5 backdrop-blur">
      <p className="text-sm text-cyan-200">{item.period || ""}</p>
      <h3 className="mt-2 text-lg font-semibold text-white">{item.title}</h3>
      <p className="text-sm text-zinc-300">{item.organization}</p>
      <p className="mt-3 text-sm leading-6 text-zinc-300">{item.description}</p>
    </article>
  );
}

export function ExperienceEducationSection() {
  return (
    <AnimatedSection id="experience" labelledBy="experience-title" className="mx-auto w-full max-w-6xl px-4 py-14 sm:px-6">
      <h2 id="experience-title" className="sr-only">
        Experience and Education
      </h2>
      <SectionHeading title="Experience & Education" subtitle="A concise overview with room to expand over time." />
      <div className="grid gap-5 md:grid-cols-2">
        <div className="space-y-4">
          {experience.map((item) => (
            <TimelineCard key={`${item.title}-${item.organization}`} item={item} />
          ))}
        </div>
        <div className="space-y-4">
          {education.map((item) => (
            <TimelineCard key={`${item.title}-${item.organization}`} item={item} />
          ))}
        </div>
      </div>
    </AnimatedSection>
  );
}
