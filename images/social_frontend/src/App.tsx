import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Register from './screens/RegisterForm';
import Signin from './screens/SigninForm';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/register" element={<Register />} />
        <Route path="/login" element={<Signin />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
