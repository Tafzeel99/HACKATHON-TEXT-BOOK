import React, { useState } from 'react';

const SimpleChatbot = () => {
  const [isOpen, setIsOpen] = useState(false);

  if (isOpen) {
    return (
      <div style={{
        position: 'fixed',
        bottom: '90px',
        right: '20px',
        width: '300px',
        height: '400px',
        backgroundColor: 'white',
        border: '1px solid #ccc',
        borderRadius: '8px',
        zIndex: 10000,
        boxShadow: '0 4px 12px rgba(0,0,0,0.15)'
      }}>
        <div style={{
          backgroundColor: '#301934',
          color: 'white',
          padding: '10px',
          borderTopLeftRadius: '8px',
          borderTopRightRadius: '8px',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center'
        }}>
          <span>Chatbot</span>
          <button
            onClick={() => setIsOpen(false)}
            style={{ background: 'none', border: 'none', color: 'white', fontSize: '18px', cursor: 'pointer' }}
          >
            ×
          </button>
        </div>
        <div style={{ padding: '10px', height: 'calc(100% - 80px)', overflowY: 'auto' }}>
          <p>Simple Chatbot Interface</p>
        </div>
        <div style={{ padding: '10px', borderTop: '1px solid #eee' }}>
          <input
            type="text"
            placeholder="Type a message..."
            style={{ width: 'calc(100% - 60px)', padding: '8px', marginRight: '5px' }}
          />
          <button style={{ padding: '8px 12px' }}>Send</button>
        </div>
      </div>
    );
  }

  return (
    <button
      onClick={() => setIsOpen(true)}
      style={{
        position: 'fixed',
        bottom: '20px',
        right: '20px',
        width: '50px',
        height: '50px',
        borderRadius: '50%',
        backgroundColor: '#301934',
        color: 'white',
        border: 'none',
        cursor: 'pointer',
        zIndex: 10000,
        boxShadow: '0 4px 12px rgba(0,0,0,0.15)'
      }}
      aria-label="Open chatbot"
    >
      💬
    </button>
  );
};

export default SimpleChatbot;