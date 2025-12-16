import type { ReactNode } from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
import Link from '@docusaurus/Link';

type FeatureItem = {
  title: string;
  imgSrc: string; // Changed from Svg
  description: ReactNode;
  link: string;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Module 1: ROS 2 Fundamentals',
    imgSrc: '/img/module1.png', // Changed to PNG path
    link: '/docs/module1-ros2',
    description: (
      <>
        Establishes the foundational concepts of the Robot Operating System (ROS 2),
        Python agent development, and URDF modeling.
      </>
    ),
  },
  {
    title: 'Module 2: Digital Twin Simulation',
    imgSrc: '/img/module2.png', // Changed to PNG path
    link: '/docs/module2-digital-twin',
    description: (
      <>
        Explores digital twins using Gazebo and Unity to enable high-fidelity
        robot simulation and realistic sensor data generation.
      </>
    ),
  },
  {
    title: 'Module 3: The AI-Robot Brain',
    imgSrc: '/img/module3.png', // Changed to PNG path
    link: '/docs/module3-ros2-nervous-system',
    description: (
      <>
        Focuses on the architecture of an AI-powered robot brain,
        integrating perception, planning, and decision-making systems.
      </>
    ),
  },
  {
    title: 'Module 4: Vision-Language-Action (VLA)',
    imgSrc: '/img/module4.png', // Changed to PNG path
    link: '/docs/module4-vla',
    description: (
      <>
        Demonstrates the integration of Large Language Models (LLMs)
        with robotics to enable natural language-driven robot actions.
      </>
    ),
  },
];

function Feature({ title, imgSrc, description, link }: FeatureItem) {
  return (
    <div className={clsx('col col--3')}>
      <div className={styles.featureCard}>
        <img src={imgSrc} className={styles.featureSvg} alt={title} /> {/* Changed to img tag */}

        <Link to={link} className={styles.featureLink}>
          <Heading as="h3">{title}</Heading>
        </Link>

        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
