function About() {
  return (
    <section className="page-section" id="about">
      <div className="container">
        <div className="text-center">
          <h2 className="section-heading text-uppercase">About the Project</h2>
          <h3 className="section-subheading text-muted">
            Development lifecycle of the Culex Mosquito Classification System
          </h3>
        </div>

        <ul className="timeline">
          {/* Phase 1 */}
          <li>
            <div className="timeline-image">
              <img
                className="rounded-circle img-fluid"
                src="/src/assets/img/about/1.jpg"
                alt="Planning phase"
              />
            </div>
            <div className="timeline-panel">
              <div className="timeline-heading">
                <h4>Phase 1</h4>
                <h4 className="subheading">Problem Definition & Data Collection</h4>
              </div>
              <div className="timeline-body">
                <p className="text-muted">
                  Identification of the problem of mosquito species classification,
                  with a focus on distinguishing <b>Culex</b> mosquitoes from
                  non-Culex species. Collection and preprocessing of image datasets
                  for training and evaluation.
                </p>
              </div>
            </div>
          </li>

          {/* Phase 2 */}
          <li className="timeline-inverted">
            <div className="timeline-image">
              <img
                className="rounded-circle img-fluid"
                src="/src/assets/img/about/2.jpg"
                alt="Model development"
              />
            </div>
            <div className="timeline-panel">
              <div className="timeline-heading">
                <h4>Phase 2</h4>
                <h4 className="subheading">Model Design & Training</h4>
              </div>
              <div className="timeline-body">
                <p className="text-muted">
                  Development of a deep learning model using <b>Convolutional Neural
                  Networks (CNNs)</b> and EfficientNet architectures. Multiple
                  experiments were conducted to optimize accuracy, recall, and
                  generalization performance.
                </p>
              </div>
            </div>
          </li>

          {/* Phase 3 */}
          <li>
            <div className="timeline-image">
              <img
                className="rounded-circle img-fluid"
                src="/src/assets/img/about/3.jpg"
                alt="Evaluation"
              />
            </div>
            <div className="timeline-panel">
              <div className="timeline-heading">
                <h4>Phase 3</h4>
                <h4 className="subheading">Testing & Evaluation</h4>
              </div>
              <div className="timeline-body">
                <p className="text-muted">
                  Evaluation of the trained model using confusion matrices,
                  classification reports, ROC curves, and external testing images
                  to assess real-world performance and robustness.
                </p>
              </div>
            </div>
          </li>

          {/* Phase 4 */}
          <li className="timeline-inverted">
            <div className="timeline-image">
              <img
                className="rounded-circle img-fluid"
                src="/src/assets/img/about/4.jpg"
                alt="Deployment"
              />
            </div>
            <div className="timeline-panel">
              <div className="timeline-heading">
                <h4>Phase 4</h4>
                <h4 className="subheading">Deployment & User Interface</h4>
              </div>
              <div className="timeline-body">
                <p className="text-muted">
                  Integration of the trained model into a web application using
                  a React-based user interface, allowing users to upload images
                  and receive real-time predictions with confidence scores.
                </p>
              </div>
            </div>
          </li>

          {/* Future */}
          <li className="timeline-inverted">
            <div className="d-flex align-items-center justify-content-center h-100">
              <h4>
                Future
                <br />
                Improvements
                <br />
                & Research
              </h4>
            </div>
          </li>
        </ul>
      </div>
    </section>
  );
}

export default About;
