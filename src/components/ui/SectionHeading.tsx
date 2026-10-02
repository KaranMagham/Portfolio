type SectionHeadingProps = {
  title: string;
  subtitle?: string;
};

export function SectionHeading({ title, subtitle }: SectionHeadingProps) {
  return (
    <div className="mb-8">
      <h2 className="text-2xl font-semibold tracking-tight text-white md:text-3xl">{title}</h2>
      {subtitle ? <p className="mt-3 max-w-2xl text-zinc-300">{subtitle}</p> : null}
    </div>
  );
}
