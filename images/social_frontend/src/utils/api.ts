import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/', // Change this if your API runs on a different host/port
  headers: {
    'Content-Type': 'application/json',
  },
});

export const registerUser = async (formData: {
  username: string;
  email: string;
  password: string;
  password2: string;
}) => {
  const response = await api.post('/register/', formData);
  
  // Assuming the token is in response.data.token (customize based on your backend)
  const token = response.data.token;
  
  // Save the token (optional: adjust based on your auth strategy)
  if (token) {
    localStorage.setItem('authToken', token);
  }

  return response.data;
};

export default api;
