import { useState } from 'react'
import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

import Login from './routes/Login'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
  
        <Router>
          <Routes>
            <Route path='/login' element={<Login />} />
          </Routes>
        </Router>
     
    </div>
  )
}

export default App
