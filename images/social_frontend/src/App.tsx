import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Register from './screens/RegisterForm';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/register" element={<Register />} />
        {/* other routes */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;
