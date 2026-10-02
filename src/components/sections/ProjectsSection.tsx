import { AnimatedSection } from "@/components/ui/AnimatedSection";
import { SectionHeading } from "@/components/ui/SectionHeading";
import { projects } from "@/data/projects";
import type { Project } from "@/types/portfolio";

function ProjectCard({ project }: { project: Project }) {
  return (
    <article className="rounded-2xl border border-violet-300/20 bg-gradient-to-br from-violet-500/10 via-blue-500/5 to-teal-500/10 p-6 backdrop-blur">
      {project.status ? (
        <p className="mb-3 inline-flex rounded-full border border-violet-300/30 bg-violet-500/10 px-3 py-1 text-xs text-violet-200">
          {project.status}
        </p>
      ) : null}
      <h3 className="text-xl font-semibold text-white">{project.name}</h3>
      <p className="mt-3 leading-7 text-zinc-300">{project.description}</p>
      <ul className="mt-5 flex flex-wrap gap-2">
        {project.techStack.map((tech) => (
          <li key={tech} className="rounded-full border border-white/15 px-3 py-1 text-xs text-zinc-200">
            {tech}
          </li>
        ))}
      </ul>
    </article>
  );
}

export function ProjectsSection() {
  return (
    <AnimatedSection id="projects" labelledBy="projects-title" className="mx-auto w-full max-w-6xl px-4 py-14 sm:px-6">
      <h2 id="projects-title" className="sr-only">
        Featured Projects
      </h2>
      <SectionHeading
        title="Featured Projects"
        subtitle="Project cards are reusable, so new projects can be added quickly as the portfolio grows."
      />
      <div className="grid gap-5 md:grid-cols-2">
        {projects.map((project) => (
          <ProjectCard key={project.name} project={project} />
        ))}
      </div>
    </AnimatedSection>
  );
}
