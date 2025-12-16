import React from 'react';
import styles from './styles.module.css';

function ChapterFooter(): JSX.Element {
  return (
    <div className={styles.chapterFooter}>
      <hr className={styles.divider} />
      <p className={styles.message}>
        Thank you for reading this chapter. We hope you found it informative and engaging.
        Feel free to explore other chapters or dive deeper into the topics.
      </p>
    </div>
  );
}

export default ChapterFooter;
