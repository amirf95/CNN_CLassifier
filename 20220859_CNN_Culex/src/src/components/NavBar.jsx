import { useEffect, useState } from 'react';
import './NavBar.css';
import { useLocation } from 'react-router-dom';

function NavBar({ variant }) {
  const location = useLocation();
  const isHomePage = location.pathname === '/';
  const [isCollapsed, setIsCollapsed] = useState(true);

  const toggleNavbar = () => {
    setIsCollapsed(!isCollapsed);
  };

  useEffect(() => {
    // Navbar shrink on scroll
    const navbarShrink = () => {
      const navbar = document.querySelector('#mainNav');
      if (!navbar) return;

      if (window.scrollY === 0) {
        navbar.classList.remove('navbar-shrink');
      } else {
        navbar.classList.add('navbar-shrink');
      }
    };

    const mainNav = document.querySelector('#mainNav');
    const navbarToggler = document.querySelector('.navbar-toggler');
    const responsiveNavItems = document.querySelectorAll('#navbarResponsive .nav-link');

    navbarShrink();
    document.addEventListener('scroll', navbarShrink);

    if (mainNav && window.bootstrap?.ScrollSpy) {
      new window.bootstrap.ScrollSpy(document.body, {
        target: '#mainNav',
        rootMargin: '0px 0px -40%',
      });
    }

    responsiveNavItems.forEach((item) => {
      item.addEventListener('click', () => {
        if (window.getComputedStyle(navbarToggler).display !== 'none') {
          navbarToggler.click();
        }
      });
    });

    return () => {
      document.removeEventListener('scroll', navbarShrink);
    };
  }, []);

  return (
    <nav
      className={`navbar navbar-expand-lg navbar-dark fixed-top ${
        variant === 'login' ? 'login-navbar' : ''
      }`}
      id="mainNav"
    >
      <div className="container">
        <a className="navbar-brand" href="/">Culex</a>

        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarResponsive"
          aria-controls="navbarResponsive"
          aria-expanded={!isCollapsed}
          aria-label="Toggle navigation"
          onClick={toggleNavbar}
        >
          Menu <i className="fas fa-bars ms-1"></i>
        </button>

        <div className="collapse navbar-collapse" id="navbarResponsive">
          <ul className="navbar-nav text-uppercase ms-auto py-4 py-lg-0">
            {isHomePage && (
              <>
                <li className="nav-item">
                  <a className="nav-link" href="#services">Our Services</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#about">About Us</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#team">Our Team</a>
                </li>
                <li className="nav-item">
                  <a className="nav-link" href="#contact">Contact Us</a>
                </li>
              </>
            )}
          </ul>
        </div>
      </div>
    </nav>
  );
}

export default NavBar;
