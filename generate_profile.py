from __future__ import annotations
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw
import html, math, textwrap, subprocess, shutil, os

ROOT = Path('/mnt/data/mouaz-profile-v3')
ASSETS = ROOT/'assets'
PREV = ROOT/'previews'
ROOT.mkdir(exist_ok=True)
ASSETS.mkdir(exist_ok=True)
PREV.mkdir(exist_ok=True)
PORTRAIT = Path('/mnt/data/portfolio-cutout.png')

THEMES = {
'dark': dict(bg='#05080B', panel='#08110F', panel2='#0B1714', line='#183D35', grid='#12312C', primary='#35F2C1', secondary='#61E7E2', gold='#E6C87A', text='#EAFEF7', muted='#8DB8AA', soft='#C8F3E7'),
'light': dict(bg='#F4F7F5', panel='#FFFFFF', panel2='#F7FBF9', line='#C9DED7', grid='#DCEBE5', primary='#0F8B6D', secondary='#0E7490', gold='#A66F00', text='#13241D', muted='#5E7B70', soft='#26493C'),
}

W,H=1200,640


def esc(s:str)->str: return html.escape(str(s))

def text(x,y,s,cls,anchor=None,fill=None):
    a=f' text-anchor="{anchor}"' if anchor else ''
    f=f' fill="{fill}"' if fill else ''
    return f'<text x="{x}" y="{y}" class="{cls}"{a}{f}>{esc(s)}</text>'

def rect(x,y,w,h,rx,fill,stroke=None,sw=1,opacity=None):
    st=f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ''
    op=f' opacity="{opacity}"' if opacity is not None else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st}{op}/>'

def line(x1,y1,x2,y2,stroke,sw=1,dash=None,opacity=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    op=f' opacity="{opacity}"' if opacity is not None else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{d}{op}/>'

def path(d,stroke,sw=1,fill='none',dash=None,opacity=None):
    ds=f' stroke-dasharray="{dash}"' if dash else ''
    op=f' opacity="{opacity}"' if opacity is not None else ''
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{ds}{op}/>'

def base_start(theme,module,title,subtitle=None,h=H):
    c=THEMES[theme]
    parts=[f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img" aria-label="{esc(title)}">
<defs>
<linearGradient id="outer" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{c['primary']}"/><stop offset="52%" stop-color="{c['secondary']}"/><stop offset="100%" stop-color="{c['gold']}"/></linearGradient>
<pattern id="grid" width="28" height="28" patternUnits="userSpaceOnUse"><path d="M28 0H0V28" fill="none" stroke="{c['grid']}" stroke-width="1" opacity="0.65"/></pattern>
<filter id="softGlow" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<style>
.tiny{{font:500 11px 'Courier New',Consolas,monospace;fill:{c['muted']}}}
.label{{font:700 14px 'Courier New',Consolas,monospace;fill:{c['text']}}}
.body{{font:500 14px 'Courier New',Consolas,monospace;fill:{c['soft']}}}
.muted{{font:500 13px 'Courier New',Consolas,monospace;fill:{c['muted']}}}
.heading{{font:700 24px 'Courier New',Consolas,monospace;fill:{c['text']}}}
.display{{font:700 58px 'Courier New',Consolas,monospace;fill:{c['text']}}}
.accent{{font:700 20px 'Courier New',Consolas,monospace;fill:{c['gold']}}}
.chip{{font:700 12px 'Courier New',Consolas,monospace;fill:{c['text']}}}
</style></defs>''']
    parts += [rect(0,0,W,h,24,c['bg']), rect(18,18,W-36,h-36,20,c['bg'],'url(#outer)',2), rect(18,18,W-36,h-36,20,'url(#grid)')]
    parts += [rect(34,34,W-68,42,13,c['panel'],c['line'],1),
              '<circle cx="58" cy="55" r="6" fill="%s"/>'%c['primary'],
              '<circle cx="82" cy="55" r="6" fill="%s"/>'%c['secondary'],
              '<circle cx="106" cy="55" r="6" fill="%s"/>'%c['gold'],
              text(130,60,title,'label'), text(1116,60,f'ONLINE · {module}','tiny','end')]
    if subtitle:
        parts += [text(58,112,subtitle,'heading')]
    return parts,c

def end_svg(parts,path_):
    parts.append('</svg>')
    Path(path_).write_text('\n'.join(parts),encoding='utf-8')


def halftone_portrait(theme, x,y,w,h):
    c=THEMES[theme]
    im=Image.open(PORTRAIT).convert('RGBA')
    # Crop transparent margins and emphasize head/torso
    bbox=im.getbbox(); im=im.crop(bbox)
    # Focus on head and upper torso so the portrait remains recognizable at README size
    im=im.crop((0, 0, im.width, int(im.height*0.62)))
    # Resize to fit panel preserving aspect
    im.thumbnail((w-34,h-60), Image.Resampling.LANCZOS)
    canvas=Image.new('RGBA',(w-34,h-60),(0,0,0,0))
    ox=(canvas.width-im.width)//2; oy=canvas.height-im.height
    canvas.alpha_composite(im,(ox,oy))
    gray=ImageOps.grayscale(canvas)
    alpha=canvas.getchannel('A')
    step=6
    pts=[]
    for py in range(2,canvas.height-2,step):
        for px in range(2,canvas.width-2,step):
            a=alpha.getpixel((px,py))/255
            if a<0.08: continue
            g=gray.getpixel((px,py))/255
            # Bigger dots for highlights, still visible in dark areas
            strength=(0.2+0.8*g)*a
            if strength<0.18: continue
            r=0.5+1.65*strength
            if g>0.72: col=c['gold']
            elif g>0.42: col=c['primary']
            else: col=c['secondary']
            op=0.4+0.6*strength
            pts.append(f'<circle cx="{x+17+px:.1f}" cy="{y+38+py:.1f}" r="{r:.2f}" fill="{col}" opacity="{op:.2f}"/>')
    return pts


def hero(theme):
    parts,c=base_start(theme,'01/08','identity.sys --profile=mouaz --view=engineering')
    # left zone
    parts += [text(58,122,'> whoami','accent'), text(58,190,'MOUAZ NAJI','display'),
              text(58,228,'Software Engineer · Backend · Systems · AI · Security','accent'),
              text(58,270,'I build reliable software systems with clear architecture,','body'),
              text(58,295,'measurable behavior and secure development practices.','body')]
    # profile block
    parts += [rect(58,330,560,164,18,c['panel'],c['line'],1),
              text(84,360,'$ cat /etc/mouaz/profile.conf','label'),
              text(84,392,'EDUCATION  = Software Engineering @ BTH','body'),
              text(84,420,'FOCUS      = Backend | AI | Systems | Security','body'),
              text(84,448,'TOOLS      = Python | C++ | Java | TypeScript | Linux','body'),
              text(84,476,'PRINCIPLES = Reliability | Architecture | Performance','body')]
    # buttons/chips
    bx=58
    for label,width_,color in [('PROJECTS',150,c['primary']),('TECH STACK',170,c['secondary']),('CONTACT',150,c['gold'])]:
        parts += [rect(bx,516,width_,42,12,c['panel2'],color,1.5),text(bx+width_/2,542,label,'chip','middle')]
        bx+=width_+18
    parts += [text(58,596,'STATUS: READY · LOCATION: SWEDEN · MODE: BUILD_TEST_REFINE','tiny')]

    # portrait panel
    px,py,pw,ph=700,102,442,480
    parts += [rect(px,py,pw,ph,22,c['panel'],c['line'],1.5),
              text(px+24,py+30,'portrait.render','label'),text(px+pw-24,py+30,'HALFTONE · LIVE','tiny','end'),
              rect(px+18,py+48,pw-36,ph-104,16,c['panel2'],c['line'],1)]
    parts += halftone_portrait(theme,px+18,py+48,pw-36,ph-104)
    # scanline and corner accents
    parts += [rect(px+30,py+240,pw-60,2,1,c['primary'],None,1,0.55),
              path(f'M{px+34} {py+70}h28M{px+34} {py+70}v28',c['primary'],2),
              path(f'M{px+pw-34} {py+70}h-28M{px+pw-34} {py+70}v28',c['secondary'],2),
              text(px+24,py+ph-24,'render: stable  ·  profile: verified  ·  signal: clear','tiny')]
    end_svg(parts,ASSETS/f'hero-{theme}.svg')


def architecture(theme):
    parts,c=base_start(theme,'02/08','architecture.map --scope=engineering','Six connected engineering domains')
    parts += [text(58,142,'One core, six practical domains, one repeatable delivery loop.','muted')]
    boxes=[
        (56,176,258,84,'BACKEND','APIs · Auth · Services',c['primary']),
        (471,148,258,84,'AI SYSTEMS','Agents · LLMs · HITL',c['gold']),
        (886,176,258,84,'SECURITY','Validation · Secrets · Gates',c['secondary']),
        (56,386,258,84,'SYSTEMS','Threads · IPC · Filesystems',c['secondary']),
        (471,414,258,84,'DATA','SQL · Firebase · Persistence',c['primary']),
        (886,386,258,84,'DEVOPS','Linux · Docker · CI/CD',c['gold'])]
    for x,y,w_,h_,head,sub,col in boxes:
        parts += [rect(x,y,w_,h_,16,c['panel'],col,1.3),'<circle cx="%s" cy="%s" r="6" fill="%s"/>'%(x+24,y+26,col),text(x+42,y+31,head,'label'),text(x+24,y+60,sub,'muted')]
    # core
    cx,cy=600,322
    parts += [f'<circle cx="{cx}" cy="{cy}" r="82" fill="{c["panel"]}" stroke="{c["secondary"]}" stroke-width="2"/>',
              f'<circle cx="{cx}" cy="{cy}" r="66" fill="none" stroke="{c["primary"]}" stroke-width="2" stroke-dasharray="8 8"/>',
              f'<circle cx="{cx}" cy="{cy}" r="50" fill="none" stroke="{c["line"]}" stroke-width="2"/>',
              text(cx,cy-4,'MOUAZ.CORE','accent','middle'),text(cx,cy+22,'BUILD · TEST · REFINE','label','middle'),text(cx,cy+44,'architecture first','tiny','middle')]
    # connections
    parts += [path('M314 218 C410 218 455 264 518 292',c['primary'],1.8,'none','7 8'),
              path('M682 292 C748 264 790 218 886 218',c['secondary'],1.8,'none','7 8'),
              path('M314 428 C410 428 455 382 518 352',c['secondary'],1.8,'none','7 8'),
              path('M682 352 C748 382 790 428 886 428',c['gold'],1.8,'none','7 8'),
              line(600,232,600,240,c['gold'],2),line(600,404,600,414,c['primary'],2)]
    parts += [rect(56,534,1088,42,12,c['panel'],c['line'],1),text(78,560,'FLOW: requirements → design → implementation → verification → iteration','body')]
    end_svg(parts,ASSETS/f'architecture-{theme}.svg')


def capabilities(theme):
    parts,c=base_start(theme,'03/08','capabilities.matrix --evidence=projects','Technical capability matrix')
    parts += [text(58,142,'Practical skills shown through coursework, systems projects and integrations.','muted')]
    left=[('BACKEND ENGINEERING',88,'APIs · auth · persistence'),('SYSTEMS PROGRAMMING',82,'threads · IPC · memory'),('AI INTEGRATIONS',80,'agents · orchestration · evaluation'),('DATABASES',78,'SQL · Firebase · data modelling')]
    right=[('NETWORKING',72,'TCP · UDP · throughput'),('SECURE SOFTWARE',70,'validation · secrets · HITL'),('MOBILE DEVELOPMENT',68,'Kotlin · Android · MVVM'),('FRONTEND',66,'React · TypeScript · responsive UI')]
    def column(x,items):
        y=184
        for label_,score,detail in items:
            parts.extend([rect(x,y,500,84,16,c['panel'],c['line'],1),text(x+22,y+28,label_,'label'),text(x+22,y+54,detail,'muted'),
                          rect(x+318,y+24,156,14,7,c['panel2'],c['line'],1),rect(x+318,y+24,156*score/100,14,7,c['primary']),text(x+474,y+59,f'{score}%','tiny','end')])
            y+=96
    column(58,left); column(642,right)
    parts += [rect(58,570,1084,28,10,c['panel'],c['line'],1),text(78,589,'METHOD: learn → build → verify → document → improve','tiny')]
    end_svg(parts,ASSETS/f'capabilities-{theme}.svg')


def projects(theme):
    parts,c=base_start(theme,'04/08','projects.console --sort=impact','Selected projects')
    parts += [text(58,142,'Compact project index. Detailed engineering notes continue below in README.','muted')]
    rows=[
    ('Auto-Healing AI DevOps','Python · LLMs · Jenkins','multi-agent repair + HITL','RESEARCH'),
    ('Campus360','Kotlin · Firebase · Maps','hybrid navigation + MVVM','COMPLETE'),
    ('PongPal','React · Slack · Firebase','web + Slack + IoT','SHOWCASE'),
    ('Chess Game','C++20 · SFML 3.0','game logic + OOP + UI','ACTIVE'),
    ('Concurrency Systems','C · Linux · POSIX','threads + IPC + memory','LAB'),
    ('OS Filesystem','C++ · Linux · Make','FAT storage + shell','COMPLETE')]
    cols=[58,382,676,996]
    parts += [rect(58,174,1084,48,12,c['panel'],c['line'],1),text(cols[0]+20,204,'PROJECT','accent'),text(cols[1]+20,204,'STACK','accent'),text(cols[2]+20,204,'FOCUS','accent'),text(cols[3]+20,204,'STATUS','accent')]
    y=232
    for i,row in enumerate(rows):
        fill=c['panel2'] if i%2==0 else c['panel']
        parts += [rect(58,y,1084,52,10,fill,c['line'],1),text(cols[0]+20,y+32,row[0],'body'),text(cols[1]+20,y+32,row[1],'muted'),text(cols[2]+20,y+32,row[2],'muted'),text(cols[3]+20,y+32,row[3],'tiny')]
        y+=58
    parts += [rect(58,586,1084,28,10,c['panel'],c['line'],1),text(78,605,'STATUS: curated · pipeline: build → validate → document → present','tiny')]
    end_svg(parts,ASSETS/f'projects-{theme}.svg')


def roadmap(theme):
    parts,c=base_start(theme,'05/08','engineering.roadmap --horizon=next','Current direction')
    parts += [text(58,142,'From strong foundations toward broader production engineering.','muted')]
    xs=[130,365,600,835,1070]
    items=[('BUILD','Backend systems','APIs · modular services',c['primary']),('DEEPEN','Systems','threads · IPC · performance',c['secondary']),('EXPAND','AI engineering','agents · evaluation · trust',c['gold']),('LEARN','Cloud & DevOps','CI/CD · containers · ops',c['secondary']),('REFINE','Production quality','security · tests · reviews',c['primary'])]
    parts += [line(130,318,1070,318,c['line'],4)]
    for x,(stage,head,detail,col) in zip(xs,items):
        parts += [f'<circle cx="{x}" cy="318" r="14" fill="{col}"/>',text(x,275,stage,'accent','middle'),text(x,360,head,'label','middle'),text(x,386,detail,'tiny','middle')]
    parts += [rect(58,432,1084,126,18,c['panel'],c['line'],1),text(82,464,'active.objectives','label'),
              text(82,494,'• distributed systems and service communication','body'),
              text(82,520,'• cloud deployment and observability','body'),
              text(616,494,'• AI evaluation and trust controls','body'),
              text(616,520,'• security, performance and architecture','body')]
    end_svg(parts,ASSETS/f'roadmap-{theme}.svg')

for th in THEMES:
    hero(th); architecture(th); capabilities(th); projects(th); roadmap(th)

README = r'''<a href="https://github.com/Mouaz7/Mouaz7">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/hero-dark.svg">
    <img width="100%" alt="Mouaz Naji — Software Engineer" src="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/hero-light.svg">
  </picture>
</a>

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0D1117?style=for-the-badge&logo=linkedin&logoColor=E6C87A)](https://www.linkedin.com/in/mouaz-naji-9307531b6/)
[![GitHub](https://img.shields.io/badge/GitHub-0D1117?style=for-the-badge&logo=github&logoColor=E6C87A)](https://github.com/Mouaz7)
[![Instagram](https://img.shields.io/badge/Instagram-0D1117?style=for-the-badge&logo=instagram&logoColor=E6C87A)](https://instagram.com/mouaz_naji8)

![Profile views](https://komarev.com/ghpvc/?username=Mouaz7&style=flat-square&color=E6C87A&labelColor=0D1117&label=Profile+Views)
![Followers](https://img.shields.io/github/followers/Mouaz7?style=flat-square&color=E6C87A&labelColor=0D1117&logo=github&label=Followers)
![Stars](https://img.shields.io/github/stars/Mouaz7?style=flat-square&color=E6C87A&labelColor=0D1117&logo=github&label=Stars)

</div>

---

## `> navigation --quick`

<div align="center">

[About](#-whoami) • [Architecture](#-architecturemap) • [Capabilities](#-capabilitiesmatrix) • [Tech Stack](#-ls-tech-stack) • [Projects](#-ls-projects---sortimpact) • [Education](#-cat-educationlog) • [Roadmap](#-engineeringroadmap) • [Stats](#-git-stats---user-mouaz7) • [Contact](#-connect---with-mouaz)

</div>

---

## `> whoami`

I am **Mouaz Naji**, a Software Engineering student at **Blekinge Institute of Technology (BTH)** focused on building dependable software across backend systems, AI-assisted workflows, operating-system concepts, networking and security.

I am especially interested in work where several engineering areas meet: APIs connected to automation, AI agents constrained by safety gates, concurrent systems measured for performance, and applications designed with clear architectural boundaries.

### What I optimize for

| Principle | What it means in practice |
| :-- | :-- |
| **Reliability** | Clear failure handling, observable behavior and predictable system states |
| **Architecture** | Explicit boundaries, directional dependencies and maintainable components |
| **Security** | Validation, protected credentials, review gates and least-privilege thinking |
| **Performance** | Measurement before optimization, efficient algorithms and resource awareness |
| **Quality** | Tests, readable code, documentation and repeatable development workflows |

```bash
$ cat /etc/mouaz/profile.conf

NAME          = Mouaz Naji
ROLE          = Software Engineer
EDUCATION     = Software Engineering @ BTH
LOCATION      = Sweden
PRIMARY       = Backend Systems | Generative AI | System Design
SYSTEMS       = Linux | Processes | Threads | IPC | Filesystems | Networks
LANGUAGES     = Python | C++ | C | Java | TypeScript | JavaScript | Kotlin
DATA          = PostgreSQL | MySQL | MariaDB | SQLite | Firebase
TOOLS         = Git | GitHub | Docker | Bash | Android Studio | VS Code
PRINCIPLES    = Reliability | Security | Performance | Clean Architecture
OPEN_TO       = Collaboration | Open Source | Software Engineering Projects
```

---

## `> architecture.map`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/architecture-dark.svg">
  <img width="100%" alt="Mouaz engineering architecture map" src="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/architecture-light.svg">
</picture>

### Engineering domains

| Domain | What I work with | Key themes |
| :-- | :-- | :-- |
| **Backend Systems** | APIs, services, validation and authentication | Modularity, error handling, reliability |
| **AI Engineering** | LLM integrations, autonomous agents and developer automation | Orchestration, memory, evaluation, HITL |
| **Systems Programming** | Software close to the operating system | Processes, threads, synchronization, IPC |
| **Secure Software** | Controls that reduce unsafe changes | Secret handling, static checks, protected paths |
| **Networking** | Communication behavior and protocol trade-offs | TCP, UDP, throughput, packet loss |
| **Data Engineering** | Persistent state and structured data | SQL, Firebase, schemas, queries |
| **DevOps** | Repeatable delivery and operational workflows | Linux, Docker, CI/CD, observability |
| **Software Architecture** | Systems that remain understandable as they grow | Clean Architecture, interfaces, testing |

---

## `> capabilities.matrix`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/capabilities-dark.svg">
  <img width="100%" alt="Mouaz capability matrix" src="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/capabilities-light.svg">
</picture>

> The percentages are visual self-assessments, not certifications. The evidence is in the linked projects and technical work below.

---

## `> ls /tech-stack`

<div align="center">

### `[ Languages ]`
<img src="https://skillicons.dev/icons?i=python,cpp,c,java,js,ts,kotlin,bash&theme=dark" alt="Programming languages" />

### `[ Frontend & Mobile ]`
<img src="https://skillicons.dev/icons?i=html,css,react,nextjs,vue,tailwind,androidstudio&theme=dark" alt="Frontend and mobile technologies" />

### `[ Backend & Data ]`
<img src="https://skillicons.dev/icons?i=nodejs,express,postgres,mysql,sqlite,firebase&theme=dark" alt="Backend and data technologies" />

### `[ Systems, DevOps & Tools ]`
<img src="https://skillicons.dev/icons?i=linux,docker,git,github,vscode,cmake&theme=dark" alt="Systems and DevOps tools" />

</div>

### Engineering practices

![Clean Architecture](https://img.shields.io/badge/Clean%20Architecture-E6C87A?style=flat-square&labelColor=0D1117)
![REST APIs](https://img.shields.io/badge/REST%20APIs-E6C87A?style=flat-square&labelColor=0D1117)
![Concurrency](https://img.shields.io/badge/Concurrency-E6C87A?style=flat-square&labelColor=0D1117)
![IPC](https://img.shields.io/badge/IPC-E6C87A?style=flat-square&labelColor=0D1117)
![TCP/UDP](https://img.shields.io/badge/TCP%20%2F%20UDP-E6C87A?style=flat-square&labelColor=0D1117)
![Authentication](https://img.shields.io/badge/Authentication-E6C87A?style=flat-square&labelColor=0D1117)
![Testing](https://img.shields.io/badge/Testing-E6C87A?style=flat-square&labelColor=0D1117)
![Generative AI](https://img.shields.io/badge/Generative%20AI-E6C87A?style=flat-square&labelColor=0D1117)
![Performance](https://img.shields.io/badge/Performance-E6C87A?style=flat-square&labelColor=0D1117)

---

## `> cat engineering_principles.yaml`

```yaml
architecture:
  - separate responsibilities before adding features
  - keep dependencies explicit and directional
  - design interfaces around behavior, not implementation details

reliability:
  - handle failure as a normal system state
  - prefer observable workflows over silent automation
  - add limits, deduplication and auditability to autonomous systems

security:
  - validate inputs and protect credentials
  - use least privilege and protected paths
  - keep humans in control of high-impact decisions

quality:
  - test behavior, not only individual functions
  - keep code readable enough to review under pressure
  - optimize after measuring, not before understanding
```

---

## `> ls /projects --sort=impact`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/projects-dark.svg">
  <img width="100%" alt="Mouaz selected projects" src="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/projects-light.svg">
</picture>

<details open>
<summary><b>▶ Auto-Healing AI DevOps Platform — Bachelor Thesis Project</b></summary>

A self-healing CI/CD research prototype that detects failed builds, compresses and analyses logs, generates candidate fixes, runs quality and security checks, opens a pull request and notifies a human reviewer.

| Aspect | Detail |
| :-- | :-- |
| **Stack** | Python · LLMs · GitHub · Jenkins · Slack · Docker |
| **Architecture** | Six-agent pipeline coordinated through an orchestrator and specialized services |
| **Safety** | Enforced human review, protected paths, secret scanning and regression blocking |
| **Quality** | Bandit, Pylint, syntax validation, retry limits and audit logging |
| **Repository** | [`Mouaz7/auto-healing-devops-platform`](https://github.com/Mouaz7/auto-healing-devops-platform) |

</details>

<details>
<summary><b>▶ Campus360 — Hybrid Campus Navigation</b></summary>

An Android application that combines outdoor maps and indoor floor plans with search, favorites, localization and secure Firebase authentication.

| Aspect | Detail |
| :-- | :-- |
| **Stack** | Kotlin · Android · Firebase · Google Maps |
| **Architecture** | MVVM with Clean Architecture boundaries |
| **Features** | Hybrid navigation, smart search, favorites, dark mode and localization |
| **Repository** | [`Mouaz7/Campus360`](https://github.com/Mouaz7/Campus360) |

</details>

<details>
<summary><b>▶ PongPal — Slack, Web and IoT Booking Ecosystem</b></summary>

An internal Softhouse project connecting a web application, Slack commands, Firebase services and Raspberry Pi camera control for booking and match tracking.

| Aspect | Detail |
| :-- | :-- |
| **Stack** | React · TypeScript · Slack API · Firebase · Python · Raspberry Pi |
| **Integrations** | Bookings, match results, leaderboards, statistics and table status |
| **Repository** | [`Mouaz7/PongPal-Showcase`](https://github.com/Mouaz7/PongPal-Showcase) |

</details>

<details>
<summary><b>▶ Chess Game — Modern C++ and SFML</b></summary>

A graphical chess application with legal move validation, special rules, timers, history tracking and a Chess.com-inspired interface.

| Aspect | Detail |
| :-- | :-- |
| **Stack** | C++20 · SFML 3.0 · vcpkg · Visual Studio |
| **Design** | Abstract piece hierarchy, polymorphism, RAII and smart pointers |
| **Rules** | Castling, en passant, promotion, checkmate, stalemate and draw conditions |
| **Repository** | [`Mouaz7/chess-game`](https://github.com/Mouaz7/chess-game) |

</details>

<details>
<summary><b>▶ Concurrency Systems — POSIX and Operating-System Concepts</b></summary>

A systems-programming collection demonstrating concurrency, synchronization, IPC and page-replacement algorithms in C.

| Aspect | Detail |
| :-- | :-- |
| **Stack** | C · Linux · POSIX Threads |
| **Concurrency** | pthreads, mutexes, semaphores and parallel matrix multiplication |
| **IPC** | Shared memory and System V message queues |
| **Memory** | FIFO, LRU and Optimal page-replacement algorithms |
| **Repository** | [`Mouaz7/Concurrency-Systems`](https://github.com/Mouaz7/Concurrency-Systems) |

</details>

<details>
<summary><b>▶ OS Filesystem — FAT-Based Virtual Storage</b></summary>

A simulated filesystem with a command shell, hierarchical directories, permission flags, path resolution and virtual block storage.

| Aspect | Detail |
| :-- | :-- |
| **Stack** | C++ · Linux · Make |
| **Architecture** | Interactive shell → filesystem core → disk I/O layer |
| **Features** | Files, directories, permissions, path resolution and formatting |
| **Repository** | [`Mouaz7/Os_filesystem`](https://github.com/Mouaz7/Os_filesystem) |

</details>

<details>
<summary><b>▶ C++ Transport System — OOP and Persistence</b></summary>

A terminal-based transport-management application for shuttles, passenger groups and time-constrained schedules.

| Aspect | Detail |
| :-- | :-- |
| **Stack** | C++ · Visual Studio |
| **Design** | Encapsulation, inheritance, polymorphism and modular managers |
| **Persistence** | File streams for shuttles, passengers and schedules |
| **Repository** | [`Mouaz7/Cpp-TransportSystem`](https://github.com/Mouaz7/Cpp-TransportSystem) |

</details>

<details>
<summary><b>▶ Network UDP/TCP Analysis — Protocol Behavior</b></summary>

Python senders and receivers used to study delivery behavior at different packet rates.

| Aspect | Detail |
| :-- | :-- |
| **Stack** | Python · TCP · UDP |
| **Measurements** | Packet rate, throughput, ordering and loss |
| **Analysis** | UDP loss under load versus TCP ordering and retransmission |
| **Repository** | [`Mouaz7/network-udp-tcp-analysis`](https://github.com/Mouaz7/network-udp-tcp-analysis) |

</details>

---

## `> cat education.log`

### Software Engineering @ BTH

```text
FOUNDATION
├── Programming in Python, C, C++ and Java
├── Algorithms and Data Structures
├── Object-Oriented Design
└── Computational Problem Solving

SYSTEMS
├── Operating Systems
├── Processes, Threads and IPC
├── Computer Networks
├── Embedded and Assembly Programming
└── Performance and Resource Management

SOFTWARE ENGINEERING
├── Requirements Engineering
├── Software Architecture and Design Patterns
├── Verification, Validation and Testing
├── Team-Based Development
└── Maintainability and Quality

DATA, SECURITY AND AI
├── Database Technology
├── Security and Cryptography
├── Artificial Intelligence
├── Generative AI Integrations
└── Safe Automation and Human Control
```

---

## `> engineering.roadmap`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/roadmap-dark.svg">
  <img width="100%" alt="Mouaz engineering roadmap" src="https://raw.githubusercontent.com/Mouaz7/Mouaz7/main/assets/roadmap-light.svg">
</picture>

### Areas I am deepening

- Distributed systems and service-to-service communication.
- Cloud-native deployment, observability and production operations.
- Advanced backend performance and database optimization.
- AI agent evaluation, trust and controlled autonomy.
- Security engineering integrated throughout the development lifecycle.

---

## `> ps aux | grep current-work`

| Process | State | Description |
| :-- | :-- | :-- |
| `backend.systems` | `RUNNING` | Designing APIs and modular application services |
| `ai.devtools` | `RUNNING` | Exploring AI-assisted repair, orchestration and evaluation |
| `cloud.devops` | `LEARNING` | Improving deployment, automation and infrastructure knowledge |
| `security.practice` | `ACTIVE` | Applying secure defaults, quality gates and review controls |
| `performance.lab` | `ACTIVE` | Measuring concurrency, networking and algorithmic behavior |
| `open.source` | `READY` | Looking for useful projects and collaborative engineering work |

---

## `> git stats --user Mouaz7`

<div align="center">

<img height="175" src="https://github-readme-stats.vercel.app/api?username=Mouaz7&show_icons=true&hide_border=true&bg_color=05080B&title_color=E6C87A&text_color=EAFEF7&icon_color=35F2C1" alt="Mouaz GitHub statistics" />
<img height="175" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Mouaz7&layout=compact&hide_border=true&bg_color=05080B&title_color=E6C87A&text_color=EAFEF7" alt="Most used languages" />

<br/>

<img src="https://streak-stats.demolab.com?user=Mouaz7&hide_border=true&background=05080B&ring=35F2C1&fire=E6C87A&currStreakLabel=61E7E2&sideLabels=EAFEF7&currStreakNum=EAFEF7&sideNums=EAFEF7&dates=8DB8AA" alt="GitHub contribution streak" />

</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-activity-graph.vercel.app/graph?username=Mouaz7&bg_color=05080B&color=8DB8AA&line=35F2C1&point=E6C87A&area=true&area_color=35F2C1&hide_border=true&custom_title=Contribution%20Matrix">
  <img width="100%" alt="Mouaz contribution graph" src="https://github-readme-activity-graph.vercel.app/graph?username=Mouaz7&bg_color=F4F7F5&color=5E7B70&line=0F8B6D&point=A66F00&area=true&area_color=0F8B6D&hide_border=true&custom_title=Contribution%20Matrix">
</picture>

---

## `> cat /personal/interests.txt`

<div align="center">

![Coding](https://img.shields.io/badge/Coding-0D1117?style=for-the-badge&logo=codeforces&logoColor=E6C87A)
![Learning](https://img.shields.io/badge/Continuous%20Learning-0D1117?style=for-the-badge&logo=readme&logoColor=E6C87A)
![Gaming](https://img.shields.io/badge/Gaming-0D1117?style=for-the-badge&logo=steam&logoColor=E6C87A)
![Music](https://img.shields.io/badge/Music-0D1117?style=for-the-badge&logo=spotify&logoColor=E6C87A)
![Fitness](https://img.shields.io/badge/Fitness-0D1117?style=for-the-badge&logo=strava&logoColor=E6C87A)
![Coffee](https://img.shields.io/badge/Coffee-0D1117?style=for-the-badge&logo=buymeacoffee&logoColor=E6C87A)

</div>

---

## `> connect --with Mouaz`

<div align="center">

I am interested in conversations and collaborations around **backend engineering, system design, AI-assisted development, security, performance and open-source software**.

<br/>

[![Connect on LinkedIn](https://img.shields.io/badge/Connect%20on%20LinkedIn-E6C87A?style=for-the-badge&logo=linkedin&logoColor=0D1117)](https://www.linkedin.com/in/mouaz-naji-9307531b6/)
[![Explore repositories](https://img.shields.io/badge/Explore%20my%20repositories-E6C87A?style=for-the-badge&logo=github&logoColor=0D1117)](https://github.com/Mouaz7?tab=repositories)
[![Follow on Instagram](https://img.shields.io/badge/Instagram-E6C87A?style=for-the-badge&logo=instagram&logoColor=0D1117)](https://instagram.com/mouaz_naji8)

<br/>

```text
mouaz@engineering:~$ echo "Build carefully. Measure honestly. Improve continuously."
```

</div>
'''
(ROOT/'README.md').write_text(README,encoding='utf-8')

INSTALL='''# Installation\n\nUpload the complete `assets` folder and `README.md` to the root of `Mouaz7/Mouaz7`.\n\n```text\nMouaz7/\n├── README.md\n└── assets/\n    ├── hero-dark.svg\n    ├── hero-light.svg\n    ├── architecture-dark.svg\n    ├── architecture-light.svg\n    ├── capabilities-dark.svg\n    ├── capabilities-light.svg\n    ├── projects-dark.svg\n    ├── projects-light.svg\n    ├── roadmap-dark.svg\n    └── roadmap-light.svg\n```\n\nThe README uses GitHub dark/light theme detection through `<picture>` elements.\n'''
(ROOT/'INSTALL.md').write_text(INSTALL,encoding='utf-8')

# Copy generator
shutil.copy('/mnt/data/build_mouaz_profile_v3.py', ROOT/'generate_profile.py')

# Render previews using ImageMagick/inkscape backend
for name in ['hero-dark','hero-light','architecture-dark','architecture-light','capabilities-dark','capabilities-light','projects-dark','projects-light','roadmap-dark','roadmap-light']:
    src=ASSETS/f'{name}.svg'; out=PREV/f'{name}.png'
    subprocess.run(['magick','-background','none',str(src),str(out)],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

# Create stacked preview dark and light
for th in ['dark','light']:
    ims=[Image.open(PREV/f'{n}-{th}.png').convert('RGB') for n in ['hero','architecture','capabilities','projects','roadmap']]
    pad=26
    total_h=sum(i.height for i in ims)+pad*(len(ims)-1)
    bg=THEMES[th]['bg']
    canvas=Image.new('RGB',(W,total_h),bg)
    y=0
    for im in ims:
        canvas.paste(im,(0,y)); y+=im.height+pad
    canvas.save(ROOT/f'preview-{th}.png',quality=95)

# zip
zip_path=Path('/mnt/data/mouaz-profile-v3.zip')
if zip_path.exists(): zip_path.unlink()
subprocess.run(['zip','-qr',str(zip_path),ROOT.name],cwd=ROOT.parent,check=True)
print('created',ROOT,zip_path)
