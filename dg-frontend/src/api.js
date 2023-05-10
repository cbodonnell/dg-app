import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Replace with your FastAPI server URL
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
