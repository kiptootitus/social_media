/* eslint-disable @typescript-eslint/no-explicit-any */
import axios, { type AxiosInstance, type AxiosResponse, AxiosError } from 'axios';

// Interface for standard API response
interface ApiResponse<T> {
  data: T;
  status: number;
  statusText: string;
  headers: any;
}

// Interface for error response
interface ApiError {
  message: string;
  code?: string;
  details?: any;
}

// Create axios instance with default configuration
const api: AxiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/',
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 10000, // 10 seconds timeout
});

// Request interceptor to add auth token to headers
api.interceptors.response.use(
  response => response,
  error => {
    if (axios.isAxiosError(error) && error.response?.status === 401) {
      removeAuthToken();
      window.location.href = '/login'; // or use router to redirect
    }
    return Promise.reject(handleError(error));
  }
);

// Response interceptor for consistent response handling
api.interceptors.response.use(
  (response: AxiosResponse): AxiosResponse => response,

  (error: AxiosError): Promise<ApiError> => {
    const apiError: ApiError = {
      message: error.message || 'An error occurred',
      code: error.code,
      details: error.response?.data,
    };
    return Promise.reject(apiError);
  }
);

// Authentication endpoints
export const registerUser = async (formData: {
  username: string;
  email: string;
  password: string;
  password2: string;
}): Promise<ApiResponse<any>> => {
  try {
    const response = await api.post('/register/', formData);
    
    // Handle token if present in response
    if (response.data.token) {
      localStorage.setItem('authToken', response.data.token);
    }
    
    return response;
  } catch (error) {
    throw handleError(error);
  }
};

export const loginUser = async (formData: {
  username: string;
  password: string;
}): Promise<ApiResponse<any>> => {
  try {
    const response = await api.post('/login/', formData);
    
    // Handle token if present in response
    if (response.data.token) {
      localStorage.setItem('authToken', response.data.token);
    }
    
    return response;
  } catch (error) {
    throw handleError(error);
  }
};

// Helper function to handle errors consistently
const handleError = (error: unknown): ApiError => {
  if (axios.isAxiosError(error)) {
    return {
      message: error.response?.data?.message || error.message || 'Request failed',
      code: error.response?.status?.toString(),
      details: error.response?.data,
    };
  }

  return {
    message: 'An unexpected error occurred',
    details: error,
  };
};


// Token management utilities
export const setAuthToken = (token: string) => {
  localStorage.setItem('authToken', token);
};

export const getAuthToken = (): string | null => {
  return localStorage.getItem('authToken');
};

export const removeAuthToken = () => {
  localStorage.removeItem('authToken');
};

// Example of a protected endpoint
export const getUserProfile = async (): Promise<ApiResponse<any>> => {
  try {
    const response = await api.get('/profile/');
    return response;
  } catch (error) {
    throw handleError(error);
  }
};

export default api;