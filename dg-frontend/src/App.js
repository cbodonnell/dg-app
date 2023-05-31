import logo from './logo.svg';
import './App.css';

import React, { useState } from 'react';
import { Container, TextField, Button, Typography, Grid } from '@mui/material';
import { submitRound } from './api';


const NewRound = () => {
  const [course, setCourse] = useState('');
  const [datetime, setDatetime] = useState('');
  const [players, setPlayers] = useState([]);

  const handleAddPlayer = () => {
    const scores = {};
    for (let i = 1; i <= 18; i++) {
      scores[`h${i}_score`] = 0;
    }
    setPlayers([...players, { name: '', scores }]);
  };

  const handleRemovePlayer = (index) => {
    const updatedPlayers = players.filter((_, i) => i !== index);
    setPlayers(updatedPlayers);
  };

  const handlePlayerNameChange = (index, name) => {
    const updatedPlayers = players.map((player, i) =>
      i === index ? { ...player, name } : player
    );
    setPlayers(updatedPlayers);
  };

  const handleScoreChange = (playerIndex, holeIndex, score) => {
    const updatedPlayers = players.map((player, i) => {
      if (i === playerIndex) {
        const updatedScores = { ...player.scores, [`h${holeIndex + 1}_score`]: parseInt(score) };
        return { ...player, scores: updatedScores };
      }
      return player;
    });
    setPlayers(updatedPlayers);
  };

  const handleSubmit = async () => {
    const roundData = {
      course,
      datetime,
      isactive: true,
      players: players.map((player, index) => ({
        player: player.name,
        scores: player.scores,
        id: index + 1,
      })),
    };

    const result = await submitRound(roundData);
    if (result) {
      console.log('Round submitted successfully:', result);
    } else {
      console.error('Error submitting round');
    }
  };

  return (
    <Container>
      <Typography variant="h4">New Round</Typography>
      <TextField
        label="Course"
        value={course}
        onChange={(e) => setCourse(e.target.value)}
      />
      <TextField
        label="Date and Time"
        type="datetime-local"
        value={datetime}
        onChange={(e) => setDatetime(e.target.value)}
        InputLabelProps={{
          shrink: true,
        }}
      />
      {players.map((player, playerIndex) => (
        <Grid container key={playerIndex} spacing={2}>
          <Grid item xs={12}>
            <TextField
              label={`Player ${playerIndex + 1} Name`}
              value={player.name}
              onChange={(e) => handlePlayerNameChange(playerIndex, e.target.value)}
            />
            <Button onClick={() => handleRemovePlayer(playerIndex)}>Remove Player</Button>
          </Grid>
          {[...Array(18)].map((_, holeIndex) => (
            <Grid item xs={1} key={holeIndex}>
              <TextField
                label={`H${holeIndex + 1}`}
                type="number"
                value={player.scores[`h${holeIndex + 1}_score`]}
                onChange={(e) =>
                  handleScoreChange(playerIndex, holeIndex, e.target.value)
                }
                InputLabelProps={{
                  shrink: true,
                }}
              />
            </Grid>
          ))}
        </Grid>
      ))}
      <Button onClick={handleAddPlayer}>Add Player</Button>
      <Button onClick={handleSubmit}>Submit Round</Button>
    </Container>
  );
};

const App = () => {
  return (
    <div>
      <NewRound />
    </div>
  );
};

export default App;
