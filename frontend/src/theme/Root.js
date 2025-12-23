import React from 'react';

// Default theme Root component that wraps the entire app
export default function Root({ children }) {
  return (
    <div>
      {children}
    </div>
  );
}