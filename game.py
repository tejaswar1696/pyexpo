<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tejaswar K | Student Portfolio</title>
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Inter:wght@300;400;500&display=swap" rel="stylesheet">
    <!-- Font Awesome for Icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {
            --primary-purple: #6366f1;
            --primary-blue: #3b82f6;
            --deep-purple: #4338ca;
            --text-dark: #1f2937;
            --text-light: #6b7280;
            --bg-gradient: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);
            --card-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1), 0 8px 10px -6px rgba(0, 0, 0, 0.1);
            --transition: all 0.3s ease;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: var(--bg-gradient);
            color: var(--text-dark);
            line-height: 1.6;
            overflow-x: hidden;
        }

        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
            font-weight: 700;
        }

        /* --- Navigation --- */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(10px);
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-weight: 700;
            font-size: 1.5rem;
            color: var(--deep-purple);
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-dark);
            font-weight: 500;
            font-size: 0.9rem;
            transition: var(--transition);
        }

        .nav-links a:hover {
            color: var(--primary-purple);
        }

        /* --- Hero Section --- */
        .hero {
            padding: 160px 2rem 100px;
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 4rem;
        }

        .hero-content {
            flex: 1;
        }

        .hero-img {
            flex: 1;
            display: flex;
            justify-content: flex-start;
        }

        .profile-placeholder {
            width: 350px;
            height: 350px;
            background: linear-gradient(var(--primary-purple), var(--primary-blue));
            border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: var(--card-shadow);
            animation: morph 8s ease-in-out infinite;
        }

        @keyframes morph {
            0% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; }
            50% { border-radius: 50% 50% 33% 67% / 55% 27% 73% 45%; }
            100% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; }
        }

        .hero-content h1 {
            font-size: 3.5rem;
            margin-bottom: 0.5rem;
            background: linear-gradient(to right, var(--deep-purple), var(--primary-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .hero-content h2 {
            font-size: 1.2rem;
            color: var(--text-light);
            font-weight: 400;
            margin-bottom: 1.5rem;
        }

        .tagline {
            font-size: 1.1rem;
            color: var(--text-dark);
            margin-bottom: 2rem;
            max-width: 500px;
        }

        .btn-group {
            display: flex;
            gap: 1rem;
        }

        .btn {
            padding: 0.8rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: 600;
            transition: var(--transition);
            display: inline-block;
        }

        .btn-primary {
            background: var(--primary-purple);
            color: white;
            box-shadow: 0 4px 15px rgba(99, 102, 241, 0.4);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            background: var(--deep-purple);
        }

        .btn-secondary {
            border: 2px solid var(--primary-purple);
            color: var(--primary-purple);
        }

        .btn-secondary:hover {
            background: var(--primary-purple);
            color: white;
        }

        /* --- Sections General --- */
        section {
            padding: 100px 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .section-title {
            font-size: 2.5rem;
            text-align: center;
            margin-bottom: 4rem;
            position: relative;
        }

        .section-title::after {
            content: '';
            width: 60px;
            height: 4px;
            background: var(--primary-blue);
            position: absolute;
            bottom: -10px;
            left: 50%;
            transform: translateX(-50%);
            border-radius: 2px;
        }

        /* --- About Me --- */
        .about-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
        }

        .about-info h3 {
            margin-bottom: 1rem;
            color: var(--deep-purple);
        }

        /* --- Skills --- */
        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 3rem;
        }

        .skill-category h3 {
            margin-bottom: 1.5rem;
            font-size: 1.2rem;
            border-left: 4px solid var(--primary-blue);
            padding-left: 10px;
        }

        .skill-item {
            margin-bottom: 1.5rem;
        }

        .skill-info {
            display: flex;
            justify-content: space-between;
            margin-bottom: 0.5rem;
        }

        .skill-bar {
            height: 8px;
            background: #e5e7eb;
            border-radius: 10px;
            overflow: hidden;
        }

        .skill-progress {
            height: 100%;
            background: linear-gradient(to right, var(--primary-purple), var(--primary-blue));
            border-radius: 10px;
            width: 0;
            transition: width 1.5s ease-in-out;
        }

        /* --- Cards (Projects, Certificates, Education) --- */
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2rem;
        }

        .card {
            background: white;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: var(--card-shadow);
            transition: var(--transition);
            border: 1px solid rgba(0,0,0,0.03);
            display: flex;
            flex-direction: column;
        }

        .card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
        }

        .card h3 {
            margin-bottom: 1rem;
            color: var(--text-dark);
        }

        .card p {
            color: var(--text-light);
            margin-bottom: 1.5rem;
            font-size: 0.95rem;
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }

        .tech-tag {
            background: #f3f4f6;
            padding: 0.3rem 0.8rem;
            border-radius: 50px;
            font-size: 0.8rem;
            font-weight: 500;
            color: var(--deep-purple);
        }

        .meta-info {
            margin-top: auto;
            font-size: 0.85rem;
            color: var(--primary-blue);
            font-weight: 600;
        }

        /* --- Contact --- */
        .contact-content {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2rem;
        }

        .social-links {
            display: flex;
            gap: 2rem;
        }

        .social-links a {
            font-size: 2rem;
            color: var(--text-dark);
            transition: var(--transition);
        }

        .social-links a:hover {
            color: var(--primary-purple);
            transform: scale(1.1);
        }

        .contact-details {
            text-align: center;
        }

        /* --- Footer --- */
        footer {
            background: #fff;
            padding: 3rem;
            text-align: center;
            border-top: 1px solid #eee;
        }

        /* --- Mobile Responsiveness --- */
        @media (max-width: 968px) {
            .hero {
                flex-direction: column;
                text-align: center;
                padding-top: 120px;
            }
            .hero-img {
                order: -1;
                justify-content: center;
            }
            .profile-placeholder {
                width: 250px;
                height: 250px;
            }
            .about-grid {
                grid-template-columns: 1fr;
            }
            .hero-content h1 {
                font-size: 2.5rem;
            }
            .nav-links {
                display: none;
            }
        }
    </style>
</head>
<body>

    <!-- Navigation -->
    <nav>
        <div class="nav-container">
            <a href="#" class="logo">TEJASWAR K</a>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#skills">Skills</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#certificates">Certificates</a></li>
                <li><a href="#education">Education</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Home Section -->
    <section class="hero" id="home">
        <div class="hero-img">
            <div class="profile-placeholder">
                <!-- Replace with <img> tag if you have a photo -->
                <i class="fa-solid fa-user-graduate" style="font-size: 8rem; color: white;"></i>
            </div>
        </div>
        <div class="hero-content">
            <h1>TEJASWAR K</h1>
            <h2>Student | INFORMATION TECHNOLOGY | KGISL</h2>
            <p class="tagline">Motivated student passionate about technology and innovation. Currently exploring the world of software development and IT infrastructure.</p>
            <div class="btn-group">
                <a href="#projects" class="btn btn-primary">View My Work</a>
                <a href="#contact" class="btn btn-secondary">Contact Me</a>
            </div>
        </div>
    </section>

    <!-- About Me Section -->
    <section id="about">
        <h2 class="section-title">About Me</h2>
        <div class="about-grid">
            <div class="about-info">
                <h3>Who am I?</h3>
                <p>I am a dedicated Information Technology student at KGISL, driven by a deep curiosity for how things work in the digital world. I enjoy solving complex problems and turning ideas into functional software solutions.</p>
            </div>
            <div class="about-info">
                <h3>Career Interests & Goals</h3>
                <p>I am particularly interested in Full-Stack Development and Cloud Computing. My goal is to leverage my technical skills to build scalable applications that make a positive impact on society.</p>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills">
        <h2 class="section-title">Technical Skills</h2>
        <div class="skills-grid">
            <!-- Programming -->
            <div class="skill-category">
                <h3><i class="fa-solid fa-code"></i> Programming</h3>
                <div class="skill-item">
                    <div class="skill-info"><span>C / C++</span><span>85%</span></div>
                    <div class="skill-bar"><div class="skill-progress" data-progress="85%"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-info"><span>Python</span><span>80%</span></div>
                    <div class="skill-bar"><div class="skill-progress" data-progress="80%"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-info"><span>Java</span><span>75%</span></div>
                    <div class="skill-bar"><div class="skill-progress" data-progress="75%"></div></div>
                </div>
            </div>
            <!-- Web -->
            <div class="skill-category">
                <h3><i class="fa-solid fa-globe"></i> Web Development</h3>
                <div class="skill-item">
                    <div class="skill-info"><span>HTML / CSS</span><span>90%</span></div>
                    <div class="skill-bar"><div class="skill-progress" data-progress="90%"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-info"><span>JavaScript</span><span>70%</span></div>
                    <div class="skill-bar"><div class="skill-progress" data-progress="70%"></div></div>
                </div>
            </div>
            <!-- Tools -->
            <div class="skill-category">
                <h3><i class="fa-solid fa-terminal"></i> Tools & Soft Skills</h3>
                <div class="skill-item">
                    <div class="skill-info"><span>Git / VS Code</span><span>85%</span></div>
                    <div class="skill-bar"><div class="skill-progress" data-progress="85%"></div></div>
                </div>
                <div class="skill-item">
                    <div class="skill-info"><span>Teamwork & Problem Solving</span><span>95%</span></div>
                    <div class="skill-bar"><div class="skill-progress" data-progress="95%"></div></div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects">
        <h2 class="section-title">My Projects</h2>
        <div class="grid-container">
            <!-- Project 1 -->
            <div class="card">
                <h3>Smart Attendance System</h3>
                <p>An automated system designed to manage student attendance using facial recognition technology.</p>
                <div class="tech-stack">
                    <span class="tech-tag">Python</span>
                    <span class="tech-tag">OpenCV</span>
                    <span class="tech-tag">SQLite</span>
                </div>
                <a href="#" class="btn btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">View Project</a>
            </div>
            <!-- Project 2 -->
            <div class="card">
                <h3>Portfolio Website</h3>
                <p>A personal responsive portfolio website built to showcase skills and academic achievements.</p>
                <div class="tech-stack">
                    <span class="tech-tag">HTML</span>
                    <span class="tech-tag">CSS</span>
                    <span class="tech-tag">JavaScript</span>
                </div>
                <a href="#" class="btn btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">View Project</a>
            </div>
            <!-- Project 3 -->
            <div class="card">
                <h3>E-Commerce Interface</h3>
                <p>A clean and minimal front-end interface for a modern retail store with filtering capabilities.</p>
                <div class="tech-stack">
                    <span class="tech-tag">React</span>
                    <span class="tech-tag">Tailwind</span>
                    <span class="tech-tag">Git</span>
                </div>
                <a href="#" class="btn btn-secondary" style="padding: 0.5rem 1rem; font-size: 0.8rem;">View Project</a>
            </div>
        </div>
    </section>

    <!-- Certificates Section -->
    <section id="certificates">
        <h2 class="section-title">Certificates</h2>
        <div class="grid-container">
            <div class="card">
                <h3>Python for Data Science</h3>
                <p>Platform: Coursera</p>
                <div class="meta-info">Year: 2025</div>
            </div>
            <div class="card">
                <h3>Web Development Boot Camp</h3>
                <p>Platform: Udemy</p>
                <div class="meta-info">Year: 2024</div>
            </div>
            <div class="card">
                <h3>Problem Solving (Basic)</h3>
                <p>Platform: HackerRank</p>
                <div class="meta-info">Year: 2024</div>
            </div>
        </div>
    </section>

    <!-- Education Section -->
    <section id="education">
        <h2 class="section-title">Education</h2>
        <div class="grid-container">
            <div class="card" style="width: 100%; grid-column: 1 / -1;">
                <h3>Bachelor of Technology in Information Technology</h3>
                <p>KGISL Institute of Technology</p>
                <div class="meta-info" style="font-size: 1.1rem; display: flex; justify-content: space-between;">
                    <span>Batch: 2022 - 2026</span>
                    <span>CGPA: 8.5 (Current)</span>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2 class="section-title">Get In Touch</h2>
        <div class="contact-content">
            <div class="social-links">
                <a href="#"><i class="fa-brands fa-linkedin"></i></a>
                <a href="#"><i class="fa-brands fa-github"></i></a>
                <a href="mailto:tejaswar.k@email.com"><i class="fa-solid fa-envelope"></i></a>
            </div>
            <div class="contact-details">
                <p><strong>Email:</strong> tejaswar.k@email.com</p>
                <p><strong>Phone:</strong> +91 XXXXX XXXXX</p>
                <p><strong>Location:</strong> Coimbatore, Tamil Nadu</p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 TEJASWAR K | Student Portfolio</p>
    </footer>

    <script>
        // Smooth Animation for Skill Bars when they come into view
        const skillBars = document.querySelectorAll('.skill-progress');
        
        const observerOptions = {
            threshold: 0.5
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const progressBar = entry.target;
                    const progress = progressBar.getAttribute('data-progress');
                    progressBar.style.width = progress;
                }
            });
        }, observerOptions);

        skillBars.forEach(bar => observer.observe(bar));

        // Simple Smooth Scroll for Navigation Links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    </script>
</body>
</html>
