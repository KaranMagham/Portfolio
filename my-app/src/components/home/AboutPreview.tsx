import { ArrowUpRight } from "lucide-react";
import { Reveal } from "./Reveal";
import { SectionLabel } from "./SectionLabel";

export function AboutPreview() { return <section className="about section-shell" id="about"><Reveal className="about-intro"><SectionLabel index="02">A little about me</SectionLabel><h2>Curious by default.<br /><em>Intentional</em> by design.</h2></Reveal><Reveal className="about-body"><p>I&apos;m a Computer Science student and Full Stack Web Developer who enjoys building practical, modern applications. I&apos;m strengthening my software engineering fundamentals, expanding into C#/.NET, and exploring how AI can make digital products more useful.</p><a className="text-link" href="#journey">More about my journey <ArrowUpRight size={16} /></a></Reveal></section>; }