import axios from 'axios';

const api = axios.create({
  baseURL: 'http://dg-backend:8000', // Production only
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
