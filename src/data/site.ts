export const site = {
  title: 'GW McElfresh',
  tagline: 'Stochastic dynamics of infection and immunity',
  headline: 'Stochastic processes in host–pathogen biology',
  description:
    'I study how birth–death, inheritance, and rare-state switching shape infection outcomes, and how those dynamics can be read from single-cell and spatial transcriptomes.',
  location: 'Oregon Health & Science University / Oregon National Primate Research Center',
  email: 'mcelfreshgw@gmail.com',
  github: 'GWMcElfresh',
  orcid: '0000-0002-1948-7571',
  googleScholar: 'FWOGc2oAAAAJ',
  url: 'https://GWMcElfresh.github.io',
  headshot: '/images/self/headshot.jpg',
} as const;

export const navigation = [
  { title: 'About', url: '/' },
  { title: 'Research', url: '/research/' },
  { title: 'Publications', url: '/publications/' },
  { title: 'CV', url: '/cv/' },
  { title: 'Blog', url: '/blog/' },
] as const;
