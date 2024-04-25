import { useState, useEffect } from 'react'
import './App.css'

function App() {
  // State to store the questions
  const [questions, setQuestions] = useState([]);

  // State to store user responses
  const [responses, setResponses] = useState([]);
  const [predictions, setPredictions] = useState(null);
  const [textFieldValue, setTextFieldValue] = useState('');


  // Function to handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    // Send the responses to the server or process them as needed
    console.log(responses);
    
    fetch('api/submit-responses', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(responses),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error('Failed to submit responses');
        }
        // Handle successful response here
        console.log('Responses submitted successfully');
      })
      .catch((error) => {
        // Handle errors here
        console.error('Error submitting responses:', error);
      });

      setResponses([]);
      setTextFieldValue('');

    // Reset the responses

    // Fetch the predictions from the server
    fetch('api/predictions')
      .then((res) => res.json())
      .then((data) => {
        setPredictions(data.predictions);
        console.log(data);
      });
  };

  // Function to handle input change
  const handleChange = (index, response) => {
    setResponses((prevResponses) => ({
      ...prevResponses,
      [index]: response,
    }));
  };

  // Fetch the questions from the server
  useEffect(() => {
    fetch('api/questions')
      .then((res) => res.json())
      .then((data) => {
        setQuestions(data.questions);
        console.log(data);
      });
  }, []);


  // Function to render input field for the specific question
  const renderInput = (question, index) => {
    if (question.question === "What is your budget range?") {
      return (
        <input
          type="text"
          id={`question-${index}-text`}
          name={`question-${index}`}
          placeholder="Lower range-Higher Range"
          className="custom-text-input" // Add custom class
          onChange={(e) => handleChange(index, e.target.value)}

        />
      );
    }
    // Render radio buttons for other questions
    return (
      <div>
        {question.options.map((option, optionIndex) => (
          <div key={optionIndex}>
            <input
              type="radio"
              id={`question-${index}-${optionIndex}`}
              name={`question-${index}`}
              value={option}
              onChange={() => handleChange(index, option)}
              checked={responses[index] === option} // Set checked based on response state

            />
            <label htmlFor={`question-${index}-${optionIndex}`}>{option}</label>
          </div>
        ))}
      </div>
    );
  };




  return (
    <>
      <div>
        <form onSubmit={handleSubmit}>
          {questions.map((question, index) => (
            <div key={index}>
              <p>{question.question}</p>
              {renderInput(question, index)}
            </div>
          ))}
          <button type="submit">Submit</button>
        </form>

        {predictions && (
          <div>
            <h2>Predictions:</h2>
            {predictions.map((prediction, index) => (
              <div key={index}>
                <p>{prediction}</p>
                <br />
              </div>
            ))}
          </div>
        )}
      </div>
    </>
  )
}

export default App
