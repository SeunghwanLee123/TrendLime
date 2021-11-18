import './App.css';
import { useEffect } from "react";

function App() {

  useEffect(() => {
     try {
            const res = await fetch('http://127.0.0.1:8000/api/');
       console.log(res);
        } catch (e) {
            console.log(e);
        }
  }, [])
  
  return (
    <div className="App">
      <header className="App-header">
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
