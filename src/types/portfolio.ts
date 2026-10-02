export type Skill = {
  name: string;
};

export type Project = {
  name: string;
  description: string;
  techStack: string[];
  href?: string;
  status?: string;
};

export type TimelineItem = {
  title: string;
  organization: string;
  period: string;
  description: string;
};
