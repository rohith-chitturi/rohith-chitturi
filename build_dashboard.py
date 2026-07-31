import random

svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 1050" width="100%" height="100%">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=JetBrains+Mono:wght@400;500;700&amp;display=swap');
      * { box-sizing: border-box; }
      .bg { fill: #0B0618; }
      .card-bg { fill: #110826; stroke: #2a114f; stroke-width: 1.5; }
      .card-inner { fill: #170b33; stroke: #31165a; stroke-width: 1; rx: 8; ry: 8; }
      .text-primary { font-family: 'Inter', sans-serif; fill: #ffffff; }
      .text-secondary { font-family: 'Inter', sans-serif; fill: #a78bfa; }
      .text-code { font-family: 'JetBrains Mono', monospace; fill: #A855F7; }
      .text-sm { font-size: 12px; }
      .text-md { font-size: 14px; }
      .text-lg { font-size: 16px; }
      .text-xl { font-size: 20px; }
      .text-xxl { font-size: 28px; font-weight: 700; }
      .title-glow { filter: url(#glow); }
      .tag-bg { fill: #24114f; rx: 12; ry: 12; }
      .icon { fill: #A855F7; }
      
      @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-5px); }
      }
      .anim-float { animation: float 6s ease-in-out infinite; }
      
      @keyframes pulseBorder {
        0%, 100% { stroke: #2a114f; }
        50% { stroke: #6D28D9; }
      }
      .anim-border { animation: pulseBorder 4s infinite; }
      
      .heatmap-1 { fill: #2a114f; }
      .heatmap-2 { fill: #4c1d95; }
      .heatmap-3 { fill: #6D28D9; }
      .heatmap-4 { fill: #9333ea; }
      .heatmap-5 { fill: #A855F7; }
    </style>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="5" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
    <linearGradient id="purple-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#6D28D9"/>
      <stop offset="100%" stop-color="#A855F7"/>
    </linearGradient>
    <clipPath id="avatar-clip">
      <rect width="240" height="240" rx="12" ry="12"/>
    </clipPath>
  </defs>

  <rect width="1200" height="1050" class="bg" />

  <!-- SIDEBAR -->
  <rect x="20" y="20" width="300" height="1010" rx="16" class="card-bg anim-border" />
  <!-- Avatar -->
  <g transform="translate(50, 40)">
    <rect width="240" height="240" rx="12" fill="#0B0618" />
    <image href="https://raw.githubusercontent.com/rohith-chitturi/rohith-chitturi/main/assets/avatar.png" width="240" height="240" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)"/>
    <rect width="240" height="240" rx="12" fill="none" stroke="#6D28D9" stroke-width="2" opacity="0.5"/>
  </g>
  <!-- Name & Title -->
  <text x="170" y="315" text-anchor="middle" class="text-primary text-lg" font-weight="700">CHITTURI NAGA RAJA TEJA ROHITH</text>
  <text x="170" y="340" text-anchor="middle" class="text-secondary text-sm" font-family="'JetBrains Mono', monospace">IT Student | AI &amp; Systems Builder</text>
  <line x1="40" y1="365" x2="300" y2="365" stroke="#2a114f" stroke-width="1"/>

  <!-- Info List -->
  <g transform="translate(40, 395)" class="text-secondary text-sm">
    <text x="0" y="0" font-family="'JetBrains Mono', monospace">📍</text>
    <text x="25" y="0">Hyderabad, India</text>
    
    <text x="0" y="35" font-family="'JetBrains Mono', monospace">🎓</text>
    <text x="25" y="35">CBIT (2024–2027)</text>
    
    <text x="0" y="70" font-family="'JetBrains Mono', monospace">📧</text>
    <text x="25" y="70">chitturinagarajatejarohith@gmail.com</text>
    
    <text x="0" y="105" font-family="'JetBrains Mono', monospace">🌐</text>
    <text x="25" y="105">rohithforge.vercel.app</text>
    
    <text x="0" y="140" font-family="'JetBrains Mono', monospace">🐙</text>
    <text x="25" y="140">rohith-chitturi</text>
  </g>
  <line x1="40" y1="560" x2="300" y2="560" stroke="#2a114f" stroke-width="1"/>

  <!-- Focus Areas -->
  <g transform="translate(40, 590)">
    <text x="0" y="0" class="text-code text-md">🎯 FOCUS AREAS</text>
    <g class="text-secondary text-sm" transform="translate(0, 30)">
      <circle cx="5" cy="-4" r="3" class="icon"/> <text x="15" y="0">Retrieval-Augmented Generation</text>
      <circle cx="5" cy="21" r="3" class="icon"/> <text x="15" y="25">Agentic AI &amp; Multi-Agent Systems</text>
      <circle cx="5" cy="46" r="3" class="icon"/> <text x="15" y="50">Distributed Systems &amp; Backends</text>
      <circle cx="5" cy="71" r="3" class="icon"/> <text x="15" y="75">AI for Finance &amp; Healthcare</text>
    </g>
  </g>
  <line x1="40" y1="720" x2="300" y2="720" stroke="#2a114f" stroke-width="1"/>

  <!-- Open To -->
  <g transform="translate(40, 750)">
    <text x="0" y="0" class="text-code text-md">🚀 OPEN TO</text>
    <g class="text-secondary text-sm" transform="translate(0, 30)">
      <text x="0" y="0">SDE Internships • Full-time Roles</text>
      <text x="0" y="25">AI/ML Engineer Roles • Research</text>
    </g>
  </g>

  <!-- Quote -->
  <g transform="translate(40, 890)">
    <rect width="240" height="100" rx="8" class="card-inner" />
    <text x="15" y="30" class="text-code text-xxl" fill="#4c1d95">"</text>
    <text x="120" y="50" text-anchor="middle" class="text-primary text-sm" font-family="'JetBrains Mono', monospace">Building intelligent systems</text>
    <text x="120" y="70" text-anchor="middle" class="text-primary text-sm" font-family="'JetBrains Mono', monospace">that solve real-world problems.</text>
    <text x="225" y="80" class="text-code text-xxl" fill="#4c1d95">"</text>
  </g>

  <!-- BANNER -->
  <rect x="340" y="20" width="840" height="250" rx="16" class="card-bg anim-border" />
  <text x="360" y="45" class="text-code text-sm">$ whoami</text>
  <text x="1160" y="45" text-anchor="end" class="text-secondary text-sm">Building systems. Solving problems. Creating impact.</text>
  <line x1="340" y1="55" x2="1180" y2="55" stroke="#2a114f" stroke-width="1"/>

  <text x="360" y="105" class="text-primary text-xxl title-glow" font-size="32">CHITTURI NAGA RAJA TEJA ROHITH <tspan class="text-code" font-size="20">✔</tspan></text>

  <g transform="translate(360, 140)" class="text-secondary text-md">
    <text x="0" y="0">Information Technology student at Chaitanya Bharathi Institute of Technology (CBIT) with a</text>
    <text x="0" y="22">strong interest in building intelligent, scalable, and impactful systems.</text>
    <text x="0" y="44">I specialize in RAG, Agentic AI, and distributed architectures. I enjoy turning complex ideas</text>
    <text x="0" y="66">into production-grade solutions that empower users and drive real-world value.</text>
  </g>

  <g transform="translate(950, 70)" class="anim-float">
    <polygon points="100,20 160,50 160,110 100,140 40,110 40,50" fill="none" stroke="url(#purple-grad)" stroke-width="2"/>
    <polygon points="100,30 150,55 150,105 100,130 50,105 50,55" fill="#150a2b" stroke="#A855F7" stroke-width="1"/>
    <text x="100" y="90" text-anchor="middle" class="text-primary" font-weight="bold" font-size="24">AI</text>
    <circle cx="30" cy="40" r="2" fill="#A855F7"/>
    <circle cx="170" cy="120" r="3" fill="#6D28D9"/>
    <circle cx="90" cy="150" r="1.5" fill="#A855F7"/>
    <path d="M0,80 L20,90 L20,110" fill="none" stroke="#2a114f"/>
    <path d="M180,60 L200,50 L220,60" fill="none" stroke="#2a114f"/>
    <!-- Additional grid lines -->
    <path d="M100,130 L100,160 M50,105 L20,120 M150,105 L180,120" fill="none" stroke="#A855F7" stroke-width="0.5" opacity="0.5"/>
  </g>

  <g transform="translate(360, 230)">
    <rect x="0" y="0" width="130" height="26" rx="13" class="card-inner" />
    <text x="65" y="17" text-anchor="middle" class="text-code text-sm">Problem Solver</text>
    
    <rect x="140" y="0" width="120" height="26" rx="13" class="card-inner" />
    <text x="200" y="17" text-anchor="middle" class="text-code text-sm">AI Enthusiast</text>
    
    <rect x="270" y="0" width="140" height="26" rx="13" class="card-inner" />
    <text x="340" y="17" text-anchor="middle" class="text-code text-sm">System Designer</text>
    
    <rect x="420" y="0" width="170" height="26" rx="13" class="card-inner" />
    <text x="505" y="17" text-anchor="middle" class="text-code text-sm">Full-Stack Developer</text>
  </g>

  <!-- FEATURED PROJECTS -->
  <rect x="340" y="290" width="840" height="280" rx="16" class="card-bg" />
  <text x="360" y="325" class="text-code text-lg" font-weight="bold">⭐ FEATURED PROJECTS</text>
  <line x1="340" y1="340" x2="1180" y2="340" stroke="#2a114f" stroke-width="1"/>

  <!-- P1 -->
  <g transform="translate(355, 355)">
    <rect width="195" height="200" rx="10" class="card-inner"/>
    <text x="15" y="25" class="text-primary text-md" font-weight="bold">🤖 MediAgent AI</text>
    <text x="15" y="45" class="text-secondary text-sm" font-size="11">Multi-Agent Hospital</text>
    <text x="15" y="60" class="text-secondary text-sm" font-size="11">Operations Platform</text>
    
    <text x="15" y="85" class="text-secondary text-sm" font-size="11">Autonomous multi-agent</text>
    <text x="15" y="100" class="text-secondary text-sm" font-size="11">system for hospital ops</text>
    <text x="15" y="115" class="text-secondary text-sm" font-size="11">with AI-driven triage,</text>
    <text x="15" y="130" class="text-secondary text-sm" font-size="11">bed allocation, dashboard.</text>
    
    <rect x="15" y="150" width="60" height="20" rx="4" class="tag-bg"/>
    <text x="45" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">LangGraph</text>
    <rect x="80" y="150" width="50" height="20" rx="4" class="tag-bg"/>
    <text x="105" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">FastAPI</text>
    <rect x="135" y="150" width="50" height="20" rx="4" class="tag-bg"/>
    <text x="160" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">Redis</text>
    
    <rect x="15" y="175" width="70" height="20" rx="4" class="tag-bg"/>
    <text x="50" y="189" text-anchor="middle" class="text-code text-sm" font-size="10">PostgreSQL</text>
    <rect x="90" y="175" width="60" height="20" rx="4" class="tag-bg"/>
    <text x="120" y="189" text-anchor="middle" class="text-code text-sm" font-size="10">Docker</text>
  </g>

  <!-- P2 -->
  <g transform="translate(560, 355)">
    <rect width="195" height="200" rx="10" class="card-inner"/>
    <text x="15" y="25" class="text-primary text-md" font-weight="bold">🛡️ FinCrime AI</text>
    <text x="15" y="45" class="text-secondary text-sm" font-size="11">Investigation Platform</text>
    
    <text x="15" y="70" class="text-secondary text-sm" font-size="11">AI-powered platform to</text>
    <text x="15" y="85" class="text-secondary text-sm" font-size="11">detect suspicious activity,</text>
    <text x="15" y="100" class="text-secondary text-sm" font-size="11">generate explainable risk</text>
    <text x="15" y="115" class="text-secondary text-sm" font-size="11">scores, AML compliance.</text>
    
    <rect x="15" y="150" width="55" height="20" rx="4" class="tag-bg"/>
    <text x="42" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">FastAPI</text>
    <rect x="75" y="150" width="60" height="20" rx="4" class="tag-bg"/>
    <text x="105" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">LangGraph</text>
    <rect x="140" y="150" width="45" height="20" rx="4" class="tag-bg"/>
    <text x="162" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">Neo4j</text>
    
    <rect x="15" y="175" width="70" height="20" rx="4" class="tag-bg"/>
    <text x="50" y="189" text-anchor="middle" class="text-code text-sm" font-size="10">PostgreSQL</text>
    <rect x="90" y="175" width="45" height="20" rx="4" class="tag-bg"/>
    <text x="112" y="189" text-anchor="middle" class="text-code text-sm" font-size="10">Redis</text>
  </g>

  <!-- P3 -->
  <g transform="translate(765, 355)">
    <rect width="195" height="200" rx="10" class="card-inner"/>
    <text x="15" y="25" class="text-primary text-md" font-weight="bold">🎯 InterviewAce</text>
    <text x="15" y="45" class="text-secondary text-sm" font-size="11">AI Interview Coach</text>
    
    <text x="15" y="70" class="text-secondary text-sm" font-size="11">AI-powered interview</text>
    <text x="15" y="85" class="text-secondary text-sm" font-size="11">preparation with mock</text>
    <text x="15" y="100" class="text-secondary text-sm" font-size="11">interviews, real-time</text>
    <text x="15" y="115" class="text-secondary text-sm" font-size="11">feedback &amp; suggestions.</text>
    
    <rect x="15" y="150" width="55" height="20" rx="4" class="tag-bg"/>
    <text x="42" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">Next.js</text>
    <rect x="75" y="150" width="55" height="20" rx="4" class="tag-bg"/>
    <text x="102" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">FastAPI</text>
    <rect x="135" y="150" width="55" height="20" rx="4" class="tag-bg"/>
    <text x="162" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">LangChain</text>
    
    <rect x="15" y="175" width="50" height="20" rx="4" class="tag-bg"/>
    <text x="40" y="189" text-anchor="middle" class="text-code text-sm" font-size="10">SQLite</text>
    <rect x="70" y="175" width="70" height="20" rx="4" class="tag-bg"/>
    <text x="105" y="189" text-anchor="middle" class="text-code text-sm" font-size="10">TailwindCSS</text>
  </g>

  <!-- P4 -->
  <g transform="translate(970, 355)">
    <rect width="195" height="200" rx="10" class="card-inner"/>
    <text x="15" y="25" class="text-primary text-md" font-weight="bold">🧠 Second Brain AI</text>
    <text x="15" y="45" class="text-secondary text-sm" font-size="11">Knowledge Management</text>
    
    <text x="15" y="70" class="text-secondary text-sm" font-size="11">Personal AI knowledge base</text>
    <text x="15" y="85" class="text-secondary text-sm" font-size="11">to capture, organize, and</text>
    <text x="15" y="100" class="text-secondary text-sm" font-size="11">retrieve information using</text>
    <text x="15" y="115" class="text-secondary text-sm" font-size="11">semantic search and RAG.</text>
    
    <rect x="15" y="150" width="55" height="20" rx="4" class="tag-bg"/>
    <text x="42" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">Next.js</text>
    <rect x="75" y="150" width="60" height="20" rx="4" class="tag-bg"/>
    <text x="105" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">Supabase</text>
    <rect x="140" y="150" width="45" height="20" rx="4" class="tag-bg"/>
    <text x="162" y="164" text-anchor="middle" class="text-code text-sm" font-size="10">Gemini</text>
    
    <rect x="15" y="175" width="70" height="20" rx="4" class="tag-bg"/>
    <text x="50" y="189" text-anchor="middle" class="text-code text-sm" font-size="10">PostgreSQL</text>
    <rect x="90" y="175" width="50" height="20" rx="4" class="tag-bg"/>
    <text x="115" y="189" text-anchor="middle" class="text-code text-sm" font-size="10">pgvector</text>
  </g>

  <!-- SKILLS & TECHNOLOGIES -->
  <rect x="340" y="590" width="480" height="320" rx="16" class="card-bg" />
  <text x="360" y="625" class="text-code text-lg" font-weight="bold">&lt;/&gt; SKILLS &amp; TECHNOLOGIES</text>
  <line x1="340" y1="640" x2="820" y2="640" stroke="#2a114f" stroke-width="1"/>

  <g transform="translate(360, 670)" class="text-sm">
    <text x="0" y="0" class="text-code">Languages &amp; Runtime</text>
    <g class="text-secondary" transform="translate(0, 25)">
      <circle cx="0" cy="-4" r="2" fill="#A855F7"/> <text x="10" y="0">Java</text>
      <circle cx="0" cy="21" r="2" fill="#A855F7"/> <text x="10" y="25">Python</text>
      <circle cx="0" cy="46" r="2" fill="#A855F7"/> <text x="10" y="50">TypeScript</text>
      <circle cx="0" cy="71" r="2" fill="#A855F7"/> <text x="10" y="75">JavaScript</text>
      <circle cx="0" cy="96" r="2" fill="#A855F7"/> <text x="10" y="100">SQL</text>
    </g>
    
    <text x="0" y="150" class="text-code">Frontend</text>
    <g class="text-secondary" transform="translate(0, 175)">
      <circle cx="0" cy="-4" r="2" fill="#A855F7"/> <text x="10" y="0">React / Next.js</text>
      <circle cx="0" cy="21" r="2" fill="#A855F7"/> <text x="10" y="25">Tailwind CSS</text>
      <circle cx="0" cy="46" r="2" fill="#A855F7"/> <text x="10" y="50">HTML5 / CSS3</text>
    </g>

    <text x="160" y="0" class="text-code">Distributed Systems</text>
    <g class="text-secondary" transform="translate(160, 25)">
      <circle cx="0" cy="-4" r="2" fill="#A855F7"/> <text x="10" y="0">Apache Kafka</text>
      <circle cx="0" cy="21" r="2" fill="#A855F7"/> <text x="10" y="25">Docker</text>
      <circle cx="0" cy="46" r="2" fill="#A855F7"/> <text x="10" y="50">Redis</text>
      <circle cx="0" cy="71" r="2" fill="#A855F7"/> <text x="10" y="75">Socket.IO</text>
      <circle cx="0" cy="96" r="2" fill="#A855F7"/> <text x="10" y="100">REST APIs</text>
    </g>

    <text x="160" y="150" class="text-code">Developer Tools</text>
    <g class="text-secondary" transform="translate(160, 175)">
      <circle cx="0" cy="-4" r="2" fill="#A855F7"/> <text x="10" y="0">Git / GitHub Actions</text>
      <circle cx="0" cy="21" r="2" fill="#A855F7"/> <text x="10" y="25">Docker Compose</text>
      <circle cx="0" cy="46" r="2" fill="#A855F7"/> <text x="10" y="50">Linux</text>
    </g>

    <text x="310" y="0" class="text-code">Intelligence &amp; Data</text>
    <g class="text-secondary" transform="translate(310, 25)">
      <circle cx="0" cy="-4" r="2" fill="#A855F7"/> <text x="10" y="0">PostgreSQL / MySQL</text>
      <circle cx="0" cy="21" r="2" fill="#A855F7"/> <text x="10" y="25">Supabase / pgvector</text>
      <circle cx="0" cy="46" r="2" fill="#A855F7"/> <text x="10" y="50">LangGraph/Chain</text>
      <circle cx="0" cy="71" r="2" fill="#A855F7"/> <text x="10" y="75">FastAPI</text>
      <circle cx="0" cy="96" r="2" fill="#A855F7"/> <text x="10" y="100">Vector Storage</text>
      <circle cx="0" cy="121" r="2" fill="#A855F7"/> <text x="10" y="125">RAG &amp; AI Agents</text>
    </g>
  </g>

  <!-- GITHUB ANALYTICS -->
  <rect x="840" y="590" width="340" height="320" rx="16" class="card-bg" />
  <text x="860" y="625" class="text-code text-lg" font-weight="bold">📈 GITHUB ACTIVITY</text>
  <line x1="840" y1="640" x2="1180" y2="640" stroke="#2a114f" stroke-width="1"/>

  <g transform="translate(860, 670)">
    <text x="0" y="10" class="text-secondary text-sm">Total Contributions</text>
    <text x="140" y="10" class="text-primary text-sm" font-weight="bold">1.2K+</text>
    
    <text x="0" y="40" class="text-secondary text-sm">Repositories</text>
    <text x="140" y="40" class="text-primary text-sm" font-weight="bold">45+</text>
    
    <text x="0" y="70" class="text-secondary text-sm">Followers</text>
    <text x="140" y="70" class="text-primary text-sm" font-weight="bold">350+</text>
    
    <text x="0" y="100" class="text-secondary text-sm">Pull Requests</text>
    <text x="140" y="100" class="text-primary text-sm" font-weight="bold">120+</text>
    
    <text x="0" y="130" class="text-secondary text-sm">Stars Earned</text>
    <text x="140" y="130" class="text-primary text-sm" font-weight="bold">600+</text>
  </g>

  <g transform="translate(860, 830)">
"""
# Generate Heatmap grid
for week in range(25):
    for day in range(7):
        intensity = random.choices([1, 2, 3, 4, 5], weights=[0.4, 0.2, 0.2, 0.1, 0.1])[0]
        x = week * 12
        y = day * 12
        svg += f'    <rect x="{x}" y="{y}" width="10" height="10" rx="2" class="heatmap-{intensity}"/>\n'

svg += """
    <text x="-20" y="10" class="text-secondary" font-size="8">Mon</text>
    <text x="-20" y="34" class="text-secondary" font-size="8">Wed</text>
    <text x="-20" y="58" class="text-secondary" font-size="8">Fri</text>
    <text x="-20" y="82" class="text-secondary" font-size="8">Sun</text>
  </g>

  <!-- LETS CONNECT -->
  <rect x="340" y="930" width="840" height="100" rx="16" class="card-bg" />
  <text x="360" y="965" class="text-code text-lg" font-weight="bold">🤝 LET'S CONNECT</text>
  <line x1="340" y1="980" x2="1180" y2="980" stroke="#2a114f" stroke-width="1"/>
  
  <g transform="translate(360, 1005)">
    <!-- Button 1 -->
    <a href="https://www.linkedin.com/in/rohithchitturi-/">
      <rect x="0" y="0" width="180" height="30" rx="15" class="card-inner" />
      <text x="90" y="19" text-anchor="middle" class="text-code text-md">💼 LinkedIn</text>
    </a>
    
    <!-- Button 2 -->
    <a href="mailto:chitturinagarajatejarohith@gmail.com">
      <rect x="200" y="0" width="180" height="30" rx="15" class="card-inner" />
      <text x="290" y="19" text-anchor="middle" class="text-code text-md">📧 Reach Me Out</text>
    </a>
    
    <!-- Button 3 -->
    <a href="https://rohithforge.vercel.app">
      <rect x="400" y="0" width="180" height="30" rx="15" class="card-inner" />
      <text x="490" y="19" text-anchor="middle" class="text-code text-md">🌐 Visit Portfolio</text>
    </a>
    
    <!-- Button 4 -->
    <a href="https://github.com/rohith-chitturi">
      <rect x="600" y="0" width="180" height="30" rx="15" class="card-inner" />
      <text x="690" y="19" text-anchor="middle" class="text-code text-md">🐙 GitHub</text>
    </a>
  </g>

</svg>
"""

with open("assets/dashboard.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("dashboard.svg generated.")
