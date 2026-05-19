backend/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── api/
│   │   └── websocket/
│   │       └── control_ws.py
│   │
│   ├── services/
│   │   │
│   │   ├── browser/
│   │   │   ├── playwright_service.py
│   │   │   ├── dom_service.py
│   │   │   ├── interaction_service.py
│   │   │   └── screenshot_service.py
│   │   │
│   │   └── session/
│   │       ├── session_manager.py
│   │       └── connection_manager.py
│   │
│   ├── models/
│   │   ├── dom_models.py
│   │   ├── interaction_models.py
│   │   └── websocket_models.py
│   │
│   └── utils/
│       └── dom_utils.py


frontend/
│
├── src/
│   │
│   ├── components/
│   │   ├── AccessibleButton.jsx
│   │   ├── AccessibleInput.jsx
│   │   ├── AccessibilityOverlay.jsx
│   │   ├── HighlightBox.jsx
│   │   └── BrowserRenderer.jsx
│   │
│   ├── hooks/
│   │   └── useBrowserSocket.js
│   │
│   ├── store/
│   │   └── browserStore.js
│   │
│   ├── pages/
│   │   └── BrowserPage.jsx
│   │
│   └── services/
│       └── websocket.js