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
import Identification from "./components/Fields/Identification";
import ScrollTop from './components/ScrollTop';
import History from './components/Fields/History';
import CulexInfo from './components/homePage/CulexInfo';
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

    </>
  );
}

function App() {
  return (
    <Router>
      <ScrollTop />
      <Routes>
        <Route path="/*" element={<MainApp />} />
        <Route path="/Identification" element={<Identification />} />  
        <Route path="/history" element={<History />} />
        <Route path="/CulexInfo" element={<CulexInfo />} />      
        {/* <Route path="/Unauthorized" element={<Unauthorized />} /> */}

      </Routes>
    </Router>
  );
}

export default App;