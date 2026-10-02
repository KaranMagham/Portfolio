"use client";

import { motion } from "framer-motion";
import type { PropsWithChildren } from "react";

type AnimatedSectionProps = PropsWithChildren<{
  id: string;
  labelledBy: string;
  className?: string;
}>;

export function AnimatedSection({
  id,
  labelledBy,
  className,
  children,
}: AnimatedSectionProps) {
  return (
    <motion.section
      id={id}
      aria-labelledby={labelledBy}
      className={className}
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, amount: 0.2 }}
      transition={{ duration: 0.45, ease: "easeOut" }}
    >
      {children}
    </motion.section>
  );
}
