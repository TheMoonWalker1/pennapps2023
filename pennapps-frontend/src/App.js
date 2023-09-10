import React from 'react';
import './css/App.css';


import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainLayout from "./components/layouts/MainLayout";
import Home from "./pages/Home";
import Demo from "./pages/Demo";


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/">
            <Route element={<MainLayout />}>
              <Route index element={<Home />}> 
              </Route>

              <Route path="demo" element={<Demo />} />
            
            </Route>
          </Route>
        </Routes>
      </BrowserRouter>
      
    </div>
  );
}

export default App;
