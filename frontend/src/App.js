import React, { useState } from 'react';
import { Container, Form, Button, FormGroup, FormControl, FormLabel } from 'react-bootstrap';

function App() {
  const [tweet, setTweet] = useState('');
  const [prediction, setPrediction] = useState(null);

  const handleChange = (event) => {
    setTweet(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
  
    try {
      const response = await fetch('http://127.0.0.1:8080/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ tweet }),
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
      }
  
      const prediction = await response.json();
      setPrediction(prediction);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const renderPrediction = () => {
    if (!prediction) return null;

    let message, emoji;

    console.log('prediction result ', prediction.prediction);
    if (prediction.prediction === 0) {
      message = 'Normal tweet';
      emoji = '😃';
    } else if (prediction.prediction === 1) {
      message = 'Depressive tweet';
      emoji = '😔';
    } else {
      message = 'Unknown prediction';
      emoji = '❓';
    }

    return (
      <div className="my-4">
        <strong>Prediction:</strong> {message} {emoji}
      </div>
    );
  };

  return (
    <Container className="App">
      <h1 className="my-4">Depressive Tweet Predictor</h1>
      <Form onSubmit={handleSubmit}>
        <FormGroup controlId="tweet">
          <FormLabel>Enter your tweet:</FormLabel>
          <FormControl
            as="textarea"
            rows={3}
            value={tweet}
            onChange={handleChange}
          />
        </FormGroup>
        <Button type="submit">Predict</Button>
      </Form>
      {renderPrediction()}
    </Container>
  );
}

export default App;