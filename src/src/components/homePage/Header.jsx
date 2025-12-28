import './header.css'
function Header() {
    return (

        <header className="masthead">
            
            <div className="container">
                <div className="masthead-subheading">
                    Deep learning System {" "}
                    
                        <b>Culex </b>
                    Mosquito Detection
                    
                </div>
                <div className="masthead-heading text-uppercase">
                    Welcome 
                </div>
                <a className="btn btn-primary btn-xl text-uppercase" href="#services">
                    Tell Me More
                </a>
            </div>
        </header>
    );
}

export default Header;
