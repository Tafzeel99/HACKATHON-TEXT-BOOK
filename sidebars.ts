import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    'intro',
    {
      type: 'category',
      label: 'Module 1: ROS 2',
      link: {
        type: 'generated-index',
        title: 'Module 1: ROS 2',
        description: 'Learn the fundamentals of ROS 2, Python agents, and URDF.',
        slug: '/module1-ros2',
      },
      items: ['module1-ros2/chapter1-core-concepts', 'module1-ros2/chapter2-python-agents', 'module1-ros2/chapter3-urdf-humanoids'],
    },
    {
      type: 'category',
      label: 'Module 2: Digital Twin',
      link: {
        type: 'generated-index',
        title: 'Module 2: Digital Twin',
        description: 'Explore digital twins with Gazebo and Unity.',
        slug: '/module2-digital-twin',
      },
      items: ['module2-digital-twin/chapter1-gazebo-simulation', 'module2-digital-twin/chapter2-unity-digital-twins', 'module2-digital-twin/chapter3-sensor-simulation'],
    },
    {
      type: 'category',
      label: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
      link: {
        type: 'generated-index',
        title: 'Module 3: The AI-Robot Brain (NVIDIA Isaac™)',
        description: 'Explore the AI-Robot Brain using NVIDIA Isaac technologies.',
        slug: '/module3-ros2-nervous-system',
      },
      items: ['module3-ros2-nervous-system/chapter1-core-components', 'module3-ros2-nervous-system/chapter2-ros2-architecture', 'module3-ros2-nervous-system/chapter3-building-a-nervous-system'],
    },
    {
      type: 'category',
      label: 'Module 4: Vision-Language-Action (VLA)',
      link: {
        type: 'generated-index',
        title: 'Module 4: Vision-Language-Action (VLA)',
        description: 'Explore the convergence of LLMs and Robotics for Vision-Language-Action (VLA).',
        slug: '/module4-vla',
      },
      items: [
        'module4-vla/chapter1-introduction',
        'module4-vla/chapter2-voice-command-processing',
        'module4-vla/chapter3-cognitive-planning',
        'module4-vla/chapter4-robot-perception',
        'module4-vla/chapter5-robot-navigation',
        'module4-vla/chapter6-robot-manipulation',
        'module4-vla/chapter7-system-orchestration',
        'module4-vla/chapter8-conclusion',
      ],
    },
  ],
};

export default sidebars;
