import type { Metadata } from "next";

import "./globals.css";

export const metadata: Metadata = {
  title: "Karan Magham | Full Stack Web Developer",
  description:
    "Portfolio of Karan Magham, a full stack web developer building modern web applications and AI-integrated software.",
};

export default function RootLayout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en" className="h-full scroll-smooth antialiased">
      <body className="min-h-full bg-[#06070b] font-sans text-zinc-100">{children}</body>
    </html>
  );
}
