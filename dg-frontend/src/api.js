import axios from 'axios';

const api = axios.create({
  baseURL: 'https://dg-app.strab.io/backend', // Production only
  // baseURL: 'http://dg-backend:8000', // Within cluster only
  // baseURL: 'http://localhost:8000', // Local testing only
});

export const submitRound = async (roundData) => {
  try {
    const response = await api.post('/rounds', roundData);
    return response.data;
  } catch (error) {
    console.error('Error submitting round:', error);
    return null;
  }
};
