import { Footer } from "@/components/layout/Footer";
import { Navbar } from "@/components/layout/Navbar";
import { AboutSection } from "@/components/sections/AboutSection";
import { ContactSection } from "@/components/sections/ContactSection";
import { ExperienceEducationSection } from "@/components/sections/ExperienceEducationSection";
import { HeroSection } from "@/components/sections/HeroSection";
import { ProjectsSection } from "@/components/sections/ProjectsSection";
import { SkillsSection } from "@/components/sections/SkillsSection";
import { BackgroundEffects } from "@/components/ui/BackgroundEffects";

export default function Home() {
  return (
    <>
      <BackgroundEffects />
      <Navbar />
      <main>
        <HeroSection />
        <AboutSection />
        <SkillsSection />
        <ProjectsSection />
        <ExperienceEducationSection />
        <ContactSection />
      </main>
      <Footer />
    </>
  );
}
