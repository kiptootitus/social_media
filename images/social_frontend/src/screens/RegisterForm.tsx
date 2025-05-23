import React, { useState } from 'react';
import { registerUser } from '../utils/api'; // Adjust path if needed

interface FormData {
  username: string;
  email: string;
  password: string;
  password2: string;
}

interface Errors {
  username?: string;
  email?: string;
  password?: string;
  password2?: string;
  non_field_errors?: string;
}
// ... (interface definitions stay the same)

const RegisterForm: React.FC = () => {
  const [formData, setFormData] = useState<FormData>({
    username: '',
    email: '',
    password: '',
    password2: '',
  });

  const [errors, setErrors] = useState<Errors>({});
  const [success, setSuccess] = useState<string>('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErrors({});
    setSuccess('');

    try {
      await registerUser(formData);
      setSuccess('Registration successful!');
      setFormData({ username: '', email: '', password: '', password2: '' });
      console.log('Token:', localStorage.getItem('authToken')); // Optional debug
    } catch (error: any) {
      if (error.response && error.response.data) {
        setErrors(error.response.data);
      } else {
        setErrors({ non_field_errors: 'Something went wrong.' });
      }
    }
  };

  return  (
    <div className="max-w-md mx-auto mt-10 p-6 border rounded shadow">
      <h2 className="text-2xl font-bold mb-4">Register</h2>
      {success && <p className="text-green-600">{success}</p>}
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block font-medium">Username</label>
          <input
            type="text"
            name="username"
            className="w-full p-2 border rounded"
            value={formData.username}
            title="Enter your username"
            placeholder="Username"
            onChange={handleChange}
          />
          {errors.username && <p className="text-red-500">{errors.username}</p>}
        </div>
        <div>
          <label className="block font-medium">Email</label>
          <input
            type="email"
            name="email"
            className="w-full p-2 border rounded"
            value={formData.email}
            title="Enter your email address"
            placeholder="Email"
            onChange={handleChange}
          />
          {errors.email && <p className="text-red-500">{errors.email}</p>}
        </div>
        <div>
          <label className="block font-medium">Password</label>
          <input
            type="password"
            name="password"
            className="w-full p-2 border rounded"
            value={formData.password}
            title="Enter your password"
            placeholder="Password"
            onChange={handleChange}
          />
          {errors.password && <p className="text-red-500">{errors.password}</p>}
        </div>
        <div>
          <label className="block font-medium">Confirm Password</label>
          <input
            type="password"
            name="password2"
            className="w-full p-2 border rounded"
            value={formData.password2}
            title="Confirm your password"
            placeholder="Confirm Password"
            onChange={handleChange}
          />
          {errors.password2 && <p className="text-red-500">{errors.password2}</p>}
        </div>
        {errors.non_field_errors && <p className="text-red-500">{errors.non_field_errors}</p>}
        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
        >
          Register
        </button>
      </form>
    </div>
  );
};

export default RegisterForm;
