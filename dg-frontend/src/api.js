import axios from 'axios';

const api = axios.create({
  baseURL: process.env.API_URL || 'http://localhost:8000',
})

export const submitRound = async (roundData) => {
  try {
    const response = await api.post('/rounds', roundData);
    return response.data;
  } catch (error) {
    console.error('Error submitting round:', error);
    return null;
  }
};
