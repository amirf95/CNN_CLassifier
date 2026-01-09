import { Link } from 'react-router-dom';


function Services() {
    return (
        <section id="services">
            <div className="container">
                <div className="text-center">
                    <h2 className="section-heading text-uppercase">Our services</h2>
                    <h3 className="typewriter">Choose the service that suits you More.</h3>
                </div>
                <div className="row text-center justify-content-center">
                    <Link 
                    to="/history" 
                    className="col-md-6"
                    style={{ textDecoration: "none", color: "inherit" }}
                    >
                        <div className="estimation-card">
                            <span className="fa-stack fa-4x">
                                <i className="fas fa-circle fa-stack-2x text-warning"></i>
                                <i className="fas fa-history fa-stack-1x fa-inverse"></i>
                            </span>
                            <h4 className="my-3">History</h4>
                            <p className="text-muted">View your detection history and previous results.</p>
                        </div>
                    </Link>


                    <Link to="/Identification" className="col-md-6" style={{ textDecoration: 'none', color: 'inherit' }}>
                        <div className="devis-card" style={{ cursor: 'pointer' }}>
                            <span className="fa-stack fa-4x">
                                <i className="fas fa-circle fa-stack-2x text-warning"></i>
                                <i className="fas fa-search fa-stack-1x fa-inverse"></i>
                            </span>
                            <h4 className="my-3">Culex Detection</h4>
                            <p className="text-muted">
                                Detect from a photo either it's a Culex or not.
                            </p>
                        </div>
                    </Link>
                </div>
            </div>
        </section>
    )

}
export default Services