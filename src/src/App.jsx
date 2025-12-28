import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import About from './components/homePage/About';
import Clients from './components/homePage/Clients';
import Contact from './components/homePage/Contact';
import Footer from './components/Footer';
import Header from './components/homePage/Header';
import NavBar from './components/NavBar';
import Services from './components/homePage/Services';
import Team from './components/homePage/Team';
import Login from './components/authentification/LoginForm';
import Register from './components/authentification/Register';
import UserProfile from './components/authentification/userprofil';
import Identification from "./components/Fields/Identification";
import ScrollTop from './components/ScrollTop';
import History from './components/Fields/History';
// import Unauthorized from './components/authentification/Unauthorized';



import Chatbot from './components/Chatbot/ChatBot';
function MainApp() {
  return (
    <>
      <NavBar >
      </NavBar>
      <Header />
      <Services />
      <About />
      <Team />
      <Clients />
      <Contact />
      <Footer />
      <Chatbot />

    </>
  );
}

function App() {
  return (
    <Router>
      <ScrollTop />
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/*" element={<MainApp />} />
        <Route path="/register" element={<Register />} />
        <Route path="/profile" element={<UserProfile />} />
        <Route path="/Identification" element={<Identification />} />  
        <Route path="/history" element={<History />} />      
        {/* <Route path="/Unauthorized" element={<Unauthorized />} /> */}

      </Routes>
    </Router>
  );
}

export default App;