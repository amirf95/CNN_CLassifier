

function Team() {
    return(
                <section className="page-section bg-light" id="team">
            <div className="container">
                <div className="text-center">
                    <h2 className="section-heading text-uppercase"> Team & Acknowledgment </h2>
                    <h3 className="section-subheading text-muted">As a lead developer for this project i want to thank my supervisor Precious whom without him this project would not have been possible.</h3>
                </div>
                <div className="row">
                    <div className="col-lg-4">
                        <div className="team-member">
                            <img className="mx-auto rounded-circle" src="/src/assets/img/team/1725103950354.jpg" alt="amir fenina" />
                            <h4>Amir Fenina</h4>
                            <p className="text-muted">Lead Developer</p>
                            <a className="btn btn-dark btn-social mx-2" href="https://github.com/amirf95" target="_blank" aria-label="Amir Fenina github Profile"><i className="fa-brands fa-github"></i></a>
                            <a className="btn btn-dark btn-social mx-2" href="https://www.facebook.com/fenina.emir" target="_blank"  aria-label="Amir Fenina Facebook Profile"><i className="fab fa-facebook-f"></i></a>
                            <a className="btn btn-dark btn-social mx-2" href="https://www.linkedin.com/in/amir-fenina-3b299b244/" target="_blank" aria-label="Amir Fenina LinkedIn Profile"><i className="fab fa-linkedin-in"></i></a>
                        </div>
                    </div>
                    <div className="col-lg-4">
                        <div className="team-member">
                            <img className="mx-auto rounded-circle" src="/src/assets/img/team/66078848_1114392442077683_7684471064126029824_n.jpg" alt="photo bekir" />
                                <h4>Precious</h4>
                            <p className="text-muted">Software engineer</p>
                            <a className="btn btn-dark btn-social mx-2" href="https://www.facebook.com/bekir.rassil" target="_blank" aria-label="Bekir Rassil Facebook Profile"><i className="fab fa-facebook-f"></i></a>
                            <a className="btn btn-dark btn-social mx-2" href="" aria-label="Bekir Rassil LinkedIn Profile" target="_blank"><i className="fab fa-linkedin-in"></i></a>
                        </div>
                    </div>
                    
                </div>
                <div className="row">
                    <div className="col-lg-8 mx-auto text-center">
                        <p className="large text-muted"> This project showcase the hard work and the detection made to make this project possible .</p>
                    </div>
                </div>
            </div>
        </section>
    )
}
export default Team
