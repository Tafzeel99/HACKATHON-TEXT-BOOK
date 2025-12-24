import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'A book on building AI-native physical intelligence systems.',
  favicon: '/img/Robotics and Artificial Intelligence (AI).jpg',

  future: {
    v4: true,
  },

  url: 'https://physical-ai-robotics-one.vercel.app/',
  baseUrl: '/',

  organizationName: 'your-org',
  projectName: 'ai-native-book',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  // Pass environment variables to client-side
  customFields: {
    REACT_APP_RAG_API_URL: process.env.REACT_APP_RAG_API_URL || 'http://localhost:8000',
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          editUrl:
            'https://github.com/Tafzeel99/HACKATHON-TEXT-BOOK',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: false,
    },
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'My Site Logo',
        src: '/img/Robotics and Artificial Intelligence (AI).jpg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'TextBook',
        },
        {
          href: 'https://github.com/Tafzeel99/HACKATHON-TEXT-BOOK',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Textbook',
          items: [
            {
              label: 'Physical AI & Humanoid Robotics',
              to: '/docs/intro'
            }
          ]
        },
        {
          title: 'Community',
          items: [
            {
              label: 'LinkedIn',
              href: 'https://www.linkedin.com/in/tafzeel-ahmed-khan-379510366/',
            },
            {
              label: 'Github',
              href: 'https://github.com/Tafzeel99',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Instagram',
              href: 'https://www.instagram.com/tafzeel._.here/',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()}, Built by Tafzeel®❤️.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
