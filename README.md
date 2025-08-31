<h1 align="center">Hi 👋, I'm Mouaz Naji</h1>
<h3 align="center">A passionate Software Engineer from Syria</h3>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=mouaz7&label=Profile%20views&color=0e75b6&style=flat" alt="mouaz7" />
</p>

<!-- ===== CLEAN HERO (no external GIF) ===== -->
<p align="center">
  <i>Full-stack engineer building practical products with Node.js, SQL, C++, and systems thinking.</i>
</p>

<!-- ===== NEW: SVG DEMO (built from scratch) ===== -->
<h2 align="left">🎥 Demo</h2>
<p align="center">
  <!-- Inline SVG storyboard: Create → Share (PIN) → Scan -->
  <a href="https://github.com/Mouaz7/moveout" title="Open MoveOut repository">
  <svg width="980" height="300" viewBox="0 0 980 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="MoveOut flow: Create label, Share with PIN, Scan QR">
    <defs>
      <linearGradient id="card" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#0f172a" />
        <stop offset="100%" stop-color="#111827" />
      </linearGradient>
      <linearGradient id="accent" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stop-color="#22d3ee" />
        <stop offset="100%" stop-color="#38bdf8" />
      </linearGradient>
      <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#0b0f1a" flood-opacity="0.6"/>
      </filter>
      <style>
        .card { fill: url(#card); stroke: #1f2937; stroke-width: 1; rx: 18; }
        .title { fill:#e5e7eb; font: 700 16px/1.2 system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Helvetica, Arial, "Apple Color Emoji","Segoe UI Emoji"; }
        .caption { fill:#9ca3af; font: 500 13px/1.4 system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Helvetica, Arial; }
        .label { fill:#e5e7eb; font: 600 13px/1.4 system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Helvetica, Arial; }
        .accent { fill:url(#accent); }
        .wire { stroke:#334155; stroke-width:2; stroke-dasharray:5 6; marker-end:url(#arrow); }
      </style>
      <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
        <polygon points="0 0, 10 3, 0 6" fill="#334155"/>
      </marker>
    </defs>

    <!-- Cards container -->
    <g transform="translate(20,20)">

      <!-- Card 1: Create Label -->
      <g filter="url(#softShadow)" transform="translate(0,0)">
        <rect class="card" x="0" y="0" width="300" height="260" />
        <text class="title" x="24" y="36">1) Create Label</text>
        <text class="caption" x="24" y="60">Title, description, media (image/audio)</text>

        <!-- Document + plus icon -->
        <rect x="40" y="90" width="140" height="100" rx="10" fill="#0b1220" stroke="#374151"/>
        <rect x="55" y="110" width="110" height="12" rx="6" fill="#1f2937"/>
        <rect x="55" y="130" width="90" height="10" rx="5" fill="#1f2937"/>
        <rect x="55" y="147" width="70" height="10" rx="5" fill="#1f2937"/>
        <circle cx="210" cy="140" r="28" class="accent"/>
        <rect x="206" y="130" width="8" height="20" rx="2" fill="#0b1320"/>
        <rect x="201" y="137" width="18" height="6" rx="2" fill="#0b1320"/>

        <!-- Small thumbnail for media -->
        <rect x="200" y="200" width="60" height="40" rx="8" fill="#0b1220" stroke="#334155"/>
        <rect x="205" y="205" width="50" height="30" rx="6" fill="#111827" stroke="#1f2937"/>
        <text class="label" x="24" y="220">QR auto-generated on save</text>
      </g>

      <!-- Wire 1→2 -->
      <path class="wire" d="M320,150 C360,150 360,150 400,150" />

      <!-- Card 2: Share with PIN -->
      <g filter="url(#softShadow)" transform="translate(420,0)">
        <rect class="card" x="0" y="0" width="300" height="260" />
        <text class="title" x="24" y="36">2) Secure Share (PIN)</text>
        <text class="caption" x="24" y="60">Generate link + 4–6 digit PIN</text>

        <!-- Share icon -->
        <circle cx="80" cy="140" r="36" fill="#0b1220" stroke="#374151"/>
        <path d="M70 140 L90 126 M90 154 L70 140" stroke="#38bdf8" stroke-width="3" fill="none" />
        <circle cx="90" cy="126" r="6" fill="#38bdf8"/>
        <circle cx="90" cy="154" r="6" fill="#38bdf8"/>
        <circle cx="70" cy="140" r="6" fill="#38bdf8"/>

        <!-- Lock -->
        <rect x="150" y="120" width="70" height="50" rx="8" fill="#0b1220" stroke="#374151"/>
        <rect x="165" y="108" width="40" height="22" rx="11" fill="#0b1220" stroke="#374151"/>
        <circle cx="185" cy="145" r="6" fill="#38bdf8"/>
        <rect x="183" y="147" width="4" height="10" rx="2" fill="#38bdf8"/>

        <text class="label" x="24" y="220">One-time link + expiration supported</text>
      </g>

      <!-- Wire 2→3 -->
      <path class="wire" d="M740,150 C780,150 780,150 820,150" />

      <!-- Card 3: Scan QR -->
      <g filter="url(#softShadow)" transform="translate(840,0)">
        <rect class="card" x="0" y="0" width="300" height="260" />
        <text class="title" x="24" y="36">3) Scan QR</text>
        <text class="caption" x="24" y="60">View contents after PIN check</text>

        <!-- Phone frame -->
        <rect x="110" y="80" width="90" height="150" rx="18" fill="#0b1220" stroke="#374151"/>
        <rect x="118" y="100" width="74" height="106" rx="8" fill="#111827" stroke="#1f2937"/>
        <!-- Simple QR (finder squares) -->
        <rect x="126" y="108" width="16" height="16" fill="#e5e7eb"/>
        <rect x="126" y="108" width="10" height="10" x="129" y="111" fill="#111827"/>
        <rect x="166" y="108" width="16" height="16" fill="#e5e7eb"/>
        <rect x="169" y="111" width="10" height="10" fill="#111827"/>
        <rect x="126" y="148" width="16" height="16" fill="#e5e7eb"/>
        <rect x="129" y="151" width="10" height="10" fill="#111827"/>
        <!-- small modules -->
        <rect x="150" y="148" width="8" height="8" fill="#e5e7eb"/>
        <rect x="170" y="168" width="8" height="8" fill="#e5e7eb"/>
        <rect x="154" y="172" width="6" height="6" fill="#e5e7eb"/>

        <text class="label" x="24" y="220">Privacy by design (no public data)</text>
      </g>
    </g>
  </svg>
  </a>
</p>

<!-- Intro -->
<h2 align="left">🌍 About Me</h2>
<p>
  I build practical software across the stack — from Node.js/Express + SQL databases to C++ and ARM assembly — and I care about simple architectures, clean code, and measurable results.
</p>

<h2 align="left">💼 Current Focus</h2>
<ul>
  <li>🔭 Shipping full-stack projects (Node.js, EJS, SQL) and tooling that simplifies real workflows</li>
  <li>🌱 Going deeper with TypeScript, Node.js internals, and advanced React patterns</li>
  <li>📱 Exploring mobile workflows (Android toolchain) alongside back-end services</li>
  <li>🤝 Open to contributing to OSS and collaborating on impactful ideas</li>
</ul>

<!-- ===== FEATURED PROJECTS ===== -->
<h2 align="left">🚀 Featured Projects</h2>
<ul>
  <li><a href="https://github.com/Mouaz7/Eshop-management-system"><b>Eshop-management-system</b></a> — Full-stack e-commerce (Node.js, Express, EJS, MariaDB) with stored procedures & triggers.</li>
  <li><a href="https://github.com/Mouaz7/moveout"><b>MoveOut</b></a> — Box labels with text/images/audio, QR codes, PIN-protected sharing, and insurance labels.</li>
  <li><a href="https://github.com/Mouaz7/BurgerProject"><b>BurgerProject</b></a> — Ordering app with kitchen view & DB integration (Node.js, MySQL, EJS).</li>
  <li><a href="https://github.com/Mouaz7/Cpp-TransportSystem"><b>Cpp-TransportSystem</b></a> — C++ OOP for transport schedules and bookings.</li>
  <li><a href="https://github.com/Mouaz7/Python-Table-Implementations"><b>Python-Table-Implementations</b></a> — ADT Table (Array/List/MTF) with performance tests.</li>
  <li><a href="https://github.com/Mouaz7/ARM-Interrupt-UART-Display"><b>ARM-Interrupt-UART-Display</b></a> — Cortex-A9 button interrupts, UART commands, 7-segment display.</li>
</ul>

<!-- ===== SKILLS / TOOLS (incl. Android & C#) ===== -->
<h2 align="left">🧰 Languages & Tools</h2>
<p align="left">
  <!-- Web core -->
  <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/></a>
  <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/></a>
  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/></a>
  <a href="https://www.typescriptlang.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/typescript/typescript-original.svg" alt="typescript" width="40" height="40"/></a>

  <!-- Backend / Frameworks -->
  <a href="https://nodejs.org" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original-wordmark.svg" alt="nodejs" width="40" height="40"/></a>
  <a href="https://expressjs.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original.svg" alt="express" width="40" height="40"/></a>

  <!-- Frontend libs -->
  <a href="https://react.dev/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/></a>
  <a href="https://ejs.co/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="ejs" width="40" height="40"/></a>

  <!-- Databases -->
  <a href="https://mariadb.org/" target="_blank" rel="noreferrer"><img src="https://www.vectorlogo.zone/logos/mariadb/mariadb-icon.svg" alt="mariadb" width="40" height="40"/></a>
  <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/></a>
  <a href="https://www.microsoft.com/en-us/sql-server" target="_blank" rel="noreferrer"><img src="https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg" alt="mssql" width="40" height="40"/></a>

  <!-- Systems / Languages -->
  <a href="https://www.w3schools.com/cpp/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/cplusplus/cplusplus-original.svg" alt="cplusplus" width="40" height="40"/></a>
  <a href="https://www.python.org" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a>

  <!-- Mobile & .NET -->
  <a href="https://www.android.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/android/android-original.svg" alt="android" width="40" height="40"/></a>
  <a href="https://learn.microsoft.com/dotnet/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/dotnetcore/dotnetcore-original.svg" alt=".NET" width="40" height="40"/></a>
  <a href="https://learn.microsoft.com/dotnet/csharp/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/csharp/csharp-original.svg" alt="csharp" width="40" height="40"/></a>

  <!-- Tooling -->
  <a href="https://git-scm.com/" target="_blank" rel="noreferrer"><img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/></a>
  <a href="https://www.gnu.org/software/bash/" target="_blank" rel="noreferrer"><img src="https://www.vectorlogo.zone/logos/gnu_bash/gnu_bash-icon.svg" alt="bash" width="40" height="40"/></a>
  <a href="https://www.linux.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/></a>
</p>

<!-- ===== CONTACT ===== -->
<h2 align="left">🤝 Connect with me</h2>
<p align="left">
  <a href="https://www.linkedin.com/in/mouaz-naji-9307531b6/" target="_blank">
    <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="LinkedIn" height="30" width="40" />
  </a>
  <a href="https://instagram.com/mouaz_naji8" target="_blank">
    <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="Instagram" height="30" width="40" />
  </a>
  <a href="https://discord.gg/mouaz77" target="_blank">
    <img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg" alt="Discord" height="30" width="40" />
  </a>
</p>

<!-- ===== STATS ===== -->
<h2 align="left">📈 GitHub Stats</h2>
<p>
  <img align="center" src="https://github-readme-stats.vercel.app/api?username=mouaz7&show_icons=true&locale=en" alt="mouaz7" />
</p>
