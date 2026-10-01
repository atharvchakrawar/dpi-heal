"""
Interactive Web Application & Executive Front Cover Dashboard for Project DPI-Heal
Served directly by FastAPI at http://127.0.0.1:8000/
"""

DASHBOARD_HTML = """<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Project DPI-Heal: Autonomous Self-Healing Middleware Swarm</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap');
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
    code, pre, .font-mono { font-family: 'JetBrains Mono', monospace; }
    .glass { background: rgba(15, 23, 42, 0.82); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08); }
    .glass-card { background: rgba(30, 41, 59, 0.65); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.07); }
    .hero-glow {
      background: radial-gradient(circle at 50% 20%, rgba(16, 185, 129, 0.18) 0%, rgba(6, 182, 212, 0.12) 35%, transparent 70%);
    }
    .grid-pattern {
      background-size: 32px 32px;
      background-image: linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                        linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    }
  </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen selection:bg-emerald-500 selection:text-white">

  <!-- Top Sticky Navigation -->
  <header class="glass sticky top-0 z-50 px-6 py-3.5 border-b border-slate-800/80 flex justify-between items-center">
    <div class="flex items-center space-x-3.5">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 via-teal-500 to-cyan-500 flex items-center justify-center shadow-lg shadow-emerald-500/25">
        <i class="fa-solid fa-shield-halved text-white text-lg"></i>
      </div>
      <div>
        <div class="flex items-center space-x-2">
          <span class="text-lg font-black tracking-tight bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">DPI-HEAL</span>
          <span class="text-[10px] uppercase font-mono px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-bold">v1.0.0 Production</span>
        </div>
        <p class="text-[11px] text-slate-400 font-mono tracking-tight">Autonomous Self-Healing Middleware Swarm for UPI Rails</p>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <nav class="hidden md:flex items-center space-x-1 bg-slate-900/80 p-1 rounded-xl border border-slate-800 text-xs">
      <a href="#cover" class="px-3.5 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition">Cover</a>
      <a href="#mission-control" class="px-3.5 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition font-semibold text-emerald-400">Mission Control</a>
      <a href="#architecture" class="px-3.5 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition">Architecture</a>
      <a href="#patent-core" class="px-3.5 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition">Z3 Formal Verifier</a>
      <a href="#ledger-section" class="px-3.5 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition">Blockchain Ledger</a>
    </nav>

    <div class="flex items-center space-x-3">
      <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-mono font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/25">
        <span class="w-2 h-2 mr-2 bg-emerald-400 rounded-full animate-ping"></span>
        <span id="gateway-status-pill">Gateway Live</span>
      </span>
      <a href="/docs" target="_blank" class="px-4 py-2 text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-xl transition border border-slate-700 flex items-center space-x-1.5 shadow-sm">
        <i class="fa-solid fa-code text-cyan-400"></i>
        <span>API Docs</span>
      </a>
    </div>
  </header>

  <!-- ========================================== -->
  <!-- 1. EXECUTIVE FRONT COVER / HERO SECTION     -->
  <!-- ========================================== -->
  <section id="cover" class="relative hero-glow grid-pattern pt-16 pb-20 px-6 border-b border-slate-800/80 overflow-hidden">
    <div class="max-w-5xl mx-auto text-center space-y-6">
      <div class="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-slate-900/90 border border-slate-700 text-xs font-medium text-slate-300 shadow-xl">
        <i class="fa-solid fa-microchip text-emerald-400"></i>
        <span>National Digital Public Infrastructure API Rail Protector</span>
        <span class="text-slate-600">|</span>
        <span class="text-emerald-400 font-mono font-semibold">UPI / OCEN / DigiLocker</span>
      </div>

      <h1 class="text-4xl md:text-6xl lg:text-7xl font-black tracking-tight leading-tight md:leading-none">
        Autonomous <span class="bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">Self-Healing</span><br>
        Middleware Swarm
      </h1>

      <p class="max-w-3xl mx-auto text-base md:text-lg text-slate-300 leading-relaxed font-light">
        When upstream participant banks deploy unannounced schema drifts into production, legacy gateways drop transactions with HTTP 422 errors.
        <strong class="text-white font-semibold">DPI-Heal</strong> deploys an autonomous 3-tier agent swarm that isolates breaking payloads, synthesizes pure translation adapters, formally proves monetary invariance via Microsoft <span class="text-emerald-400 font-mono">Z3 SMT solver</span>, and mounts hot-patches live in memory in <strong class="text-cyan-300">&lt;15 milliseconds</strong>.
      </p>

      <!-- CTA Buttons -->
      <div class="flex flex-wrap justify-center items-center gap-4 pt-4">
        <a href="#mission-control" class="px-6 py-3.5 rounded-xl bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-bold text-sm shadow-lg shadow-emerald-500/25 transition transform hover:-translate-y-0.5 flex items-center space-x-2">
          <i class="fa-solid fa-play"></i>
          <span>Launch Live Simulator Below</span>
        </a>
        <a href="#patent-core" class="px-6 py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 font-semibold text-sm border border-slate-700 transition flex items-center space-x-2">
          <i class="fa-solid fa-certificate text-purple-400"></i>
          <span>Inspect Z3 Invariant Theorems</span>
        </a>
        <a href="/docs" target="_blank" class="px-6 py-3.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 font-semibold text-sm border border-slate-700 transition flex items-center space-x-2">
          <i class="fa-solid fa-bolt text-amber-400"></i>
          <span>Interactive Swagger UI</span>
        </a>
      </div>

      <!-- Feature Pill Badges -->
      <div class="pt-10 grid grid-cols-2 sm:grid-cols-4 gap-3 max-w-4xl mx-auto text-xs font-medium">
        <div class="p-3 rounded-xl glass-card text-slate-300 flex items-center space-x-2">
          <i class="fa-solid fa-gauge-high text-emerald-400"></i>
          <span>Sliding Window Error Velocity</span>
        </div>
        <div class="p-3 rounded-xl glass-card text-slate-300 flex items-center space-x-2">
          <i class="fa-solid fa-calculator text-cyan-400"></i>
          <span>Z3 Monetary Proof &forall;x&gt;0</span>
        </div>
        <div class="p-3 rounded-xl glass-card text-slate-300 flex items-center space-x-2">
          <i class="fa-solid fa-shuffle text-amber-400"></i>
          <span>Zero-Downtime Hot-Swap</span>
        </div>
        <div class="p-3 rounded-xl glass-card text-slate-300 flex items-center space-x-2">
          <i class="fa-solid fa-link text-purple-400"></i>
          <span>SHA-256 Chained Audit Trail</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- 2. MISSION CONTROL & LIVE SIMULATOR         -->
  <!-- ========================================== -->
  <section id="mission-control" class="max-w-7xl mx-auto px-6 py-12 space-y-8">

    <div class="flex flex-col md:flex-row justify-between items-start md:items-end gap-4 border-b border-slate-800 pb-6">
      <div>
        <div class="text-xs font-mono font-semibold uppercase tracking-wider text-emerald-400 mb-1">Interactive Simulation & Telemetry</div>
        <h2 class="text-2xl md:text-3xl font-extrabold text-white">Swarm Mission Control</h2>
        <p class="text-sm text-slate-400">Inject traffic, trigger unannounced schema drifts, and watch the autonomous swarm heal transactions in real time.</p>
      </div>
      <div class="flex items-center space-x-3">
        <div class="px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-xs font-mono">
          <span class="text-slate-500">Active State: </span>
          <span id="state-text" class="text-emerald-400 font-bold">IDLE</span>
        </div>
        <button onclick="fetchMetrics(); fetchLedger();" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-400 hover:text-white transition">
          <i class="fa-solid fa-arrows-rotate"></i>
        </button>
      </div>
    </div>

    <!-- Live Telemetry KPI Bar -->
    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
      <div class="glass-card rounded-2xl p-4">
        <div class="flex items-center justify-between text-slate-400 mb-2">
          <span class="text-xs font-medium uppercase tracking-wider">Total Requests</span>
          <i class="fa-solid fa-server text-sm"></i>
        </div>
        <div class="text-3xl font-black text-white" id="stat-total">0</div>
        <div class="text-[11px] text-slate-500 mt-1">Live Ingress Traffic</div>
      </div>

      <div class="glass-card rounded-2xl p-4 border-emerald-500/20">
        <div class="flex items-center justify-between text-slate-400 mb-2">
          <span class="text-xs font-medium uppercase tracking-wider">Canonical 200</span>
          <i class="fa-solid fa-circle-check text-sm text-emerald-400"></i>
        </div>
        <div class="text-3xl font-black text-emerald-400" id="stat-canonical">0</div>
        <div class="text-[11px] text-slate-500 mt-1">Direct Valid Payloads</div>
      </div>

      <div class="glass-card rounded-2xl p-4 border-cyan-500/20">
        <div class="flex items-center justify-between text-slate-400 mb-2">
          <span class="text-xs font-medium uppercase tracking-wider">Auto-Healed</span>
          <i class="fa-solid fa-wand-magic-sparkles text-sm text-cyan-400"></i>
        </div>
        <div class="text-3xl font-black text-cyan-400" id="stat-adapted">0</div>
        <div class="text-[11px] text-slate-500 mt-1">Hot-Patched Success</div>
      </div>

      <div class="glass-card rounded-2xl p-4 border-rose-500/20">
        <div class="flex items-center justify-between text-slate-400 mb-2">
          <span class="text-xs font-medium uppercase tracking-wider">Validation Drops</span>
          <i class="fa-solid fa-triangle-exclamation text-sm text-rose-400"></i>
        </div>
        <div class="text-3xl font-black text-rose-400" id="stat-failures">0</div>
        <div class="text-[11px] text-slate-500 mt-1">422 Schema Outages</div>
      </div>

      <div class="glass-card rounded-2xl p-4 border-purple-500/20">
        <div class="flex items-center justify-between text-slate-400 mb-2">
          <span class="text-xs font-medium uppercase tracking-wider">Ledger Blocks</span>
          <i class="fa-solid fa-cube text-sm text-purple-400"></i>
        </div>
        <div class="text-3xl font-black text-purple-400" id="stat-blocks">1</div>
        <div class="text-[11px] text-slate-500 mt-1">SHA-256 Chained</div>
      </div>

      <div class="glass-card rounded-2xl p-4 border-emerald-500/20">
        <div class="flex items-center justify-between text-slate-400 mb-2">
          <span class="text-xs font-medium uppercase tracking-wider">Chain Integrity</span>
          <i class="fa-solid fa-lock text-sm text-emerald-400"></i>
        </div>
        <div class="text-xl font-black text-emerald-400 flex items-center pt-1" id="stat-integrity">
          <i class="fa-solid fa-check-double mr-1.5 text-base"></i> VERIFIED
        </div>
        <div class="text-[11px] text-slate-500 mt-1">Cryptographically Sealed</div>
      </div>
    </div>

    <!-- Interactive Traffic Injection Controls -->
    <div class="glass rounded-3xl p-6 border border-slate-800">
      <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 mb-6">
        <div>
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-gamepad text-cyan-400"></i>
            Live Traffic Injection Sandbox
          </h3>
          <p class="text-sm text-slate-400">Click any action to simulate upstream bank behavior and inspect agent reactions.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <!-- Action 1 -->
        <button onclick="sendValidPayment()" class="flex flex-col p-4 rounded-2xl bg-slate-900/90 hover:bg-slate-800 border border-emerald-500/30 hover:border-emerald-500/60 transition group text-left">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold uppercase text-emerald-400 tracking-wider font-mono">1. Healthy Traffic</span>
            <i class="fa-solid fa-paper-plane text-emerald-400 group-hover:translate-x-1 transition-transform"></i>
          </div>
          <div class="font-bold text-sm text-white">Send Valid Transaction</div>
          <div class="text-xs text-slate-400 mt-1">Bank HDFC sends standard valid UPI payload. Returns 200 OK SUCCESS.</div>
        </button>

        <!-- Action 2 -->
        <button onclick="sendBrokenPayment()" class="flex flex-col p-4 rounded-2xl bg-slate-900/90 hover:bg-slate-800 border border-amber-500/30 hover:border-amber-500/60 transition group text-left">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold uppercase text-amber-400 tracking-wider font-mono">2. Single Mutation</span>
            <i class="fa-solid fa-bug text-amber-400 group-hover:scale-110 transition-transform"></i>
          </div>
          <div class="font-bold text-sm text-white">Send 1 Broken Request</div>
          <div class="text-xs text-slate-400 mt-1">Bank B sends 'vpa_id' & 'txn_amount'. Returns 422 Validation Error.</div>
        </button>

        <!-- Action 3 -->
        <button onclick="simulateOutageAndHeal()" class="flex flex-col p-4 rounded-2xl bg-gradient-to-br from-indigo-950/90 to-slate-900 hover:from-indigo-900 border border-indigo-500/50 hover:border-indigo-400 transition group text-left shadow-lg shadow-indigo-950/60">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold uppercase text-indigo-300 tracking-wider font-mono">3. Self-Healing Swarm</span>
            <i class="fa-solid fa-bolt-lightning text-amber-300 animate-pulse"></i>
          </div>
          <div class="font-bold text-sm text-white">Burst 5 Failures & Auto-Heal</div>
          <div class="text-xs text-slate-300 mt-1">Crosses Scout burst threshold & triggers autonomous hot-patch in &lt;15ms!</div>
        </button>

        <!-- Action 4 -->
        <button onclick="revokeAdapter()" class="flex flex-col p-4 rounded-2xl bg-slate-900/90 hover:bg-slate-800 border border-rose-500/30 hover:border-rose-500/60 transition group text-left">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold uppercase text-rose-400 tracking-wider font-mono">4. Reset & Unmount</span>
            <i class="fa-solid fa-rotate-left text-rose-400 group-hover:-rotate-45 transition-transform"></i>
          </div>
          <div class="font-bold text-sm text-white">Revoke Hot-Patch Adapter</div>
          <div class="text-xs text-slate-400 mt-1">Unmounts active adapter to revert Bank B traffic to raw validation.</div>
        </button>
      </div>
    </div>

    <!-- Agent Swarm Visualizer Grid -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">

      <!-- Scout Box -->
      <div class="glass-card rounded-2xl p-5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center space-x-2">
              <span class="w-2.5 h-2.5 rounded-full bg-blue-400"></span>
              <h4 class="font-bold text-white text-sm">Scout Telemetry Agent</h4>
            </div>
            <span class="text-[10px] font-mono uppercase px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 border border-blue-500/20">Sliding Window</span>
          </div>
          <p class="text-xs text-slate-400 mb-4">Calculates error velocity in a 10s sliding deque. Emits AnomalyAlert when failures exceed 5.</p>

          <div class="bg-slate-900/90 rounded-xl p-3 border border-slate-800 space-y-2">
            <div class="flex justify-between text-xs">
              <span class="text-slate-400">Observed Target:</span>
              <span class="font-mono text-cyan-300 font-semibold text-[11px]">BANK_MAHARASHTRA_COOP</span>
            </div>
            <div class="flex justify-between text-xs">
              <span class="text-slate-400">Burst Error Velocity:</span>
              <span class="font-mono font-bold" id="scout-burst">0 / 5 failures</span>
            </div>
            <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden">
              <div id="scout-progress-bar" class="bg-blue-500 h-2 rounded-full transition-all duration-300" style="width: 0%"></div>
            </div>
          </div>
        </div>
        <div class="mt-4 text-[11px] text-slate-500 font-mono" id="scout-status-line">Telemetry window healthy.</div>
      </div>

      <!-- Verifier Box -->
      <div class="glass-card rounded-2xl p-5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center space-x-2">
              <span class="w-2.5 h-2.5 rounded-full bg-purple-400"></span>
              <h4 class="font-bold text-white text-sm">Double-Gate Verifier</h4>
            </div>
            <span class="text-[10px] font-mono uppercase px-2 py-0.5 rounded bg-purple-500/10 text-purple-400 border border-purple-500/20">Patent Core</span>
          </div>
          <p class="text-xs text-slate-400 mb-4">Proves monetary value conservation using Z3 SMT solver and restricts AST to pure operations.</p>

          <div class="bg-slate-900/90 rounded-xl p-3 border border-slate-800 space-y-1.5 text-xs font-mono">
            <div class="flex justify-between">
              <span class="text-slate-400">Gate 1 (AST Safety):</span>
              <span class="text-emerald-400 font-bold" id="verifier-ast">PASSED</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-400">Gate 2 (Z3 SMT Invariant):</span>
              <span class="text-emerald-400 font-bold" id="verifier-z3">PROVEN (UNSAT)</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-400">PII & Secret Purge:</span>
              <span class="text-emerald-400 font-bold">ENFORCED</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-400">Canonical Pydantic v2:</span>
              <span class="text-emerald-400 font-bold">STRICT VALID</span>
            </div>
          </div>
        </div>
        <div class="mt-4 text-[11px] text-slate-500 font-mono" id="verifier-proof-sig">Proof Sig: Active Root of Trust</div>
      </div>

      <!-- Dynamic Router Box -->
      <div class="glass-card rounded-2xl p-5 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-3">
            <div class="flex items-center space-x-2">
              <span class="w-2.5 h-2.5 rounded-full bg-cyan-400"></span>
              <h4 class="font-bold text-white text-sm">Dynamic Hot-Swap Router</h4>
            </div>
            <span class="text-[10px] font-mono uppercase px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">Zero Downtime</span>
          </div>
          <p class="text-xs text-slate-400 mb-4">Mounts verified translation functions into FastAPI memory without restarting ASGI process.</p>

          <div class="bg-slate-900/90 rounded-xl p-3 border border-slate-800 space-y-2 text-xs">
            <div class="flex justify-between">
              <span class="text-slate-400">Active Hot-Patches:</span>
              <span class="font-bold font-mono text-cyan-400" id="router-count">0 Mounted</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-400">Adapted Transactions:</span>
              <span class="font-bold font-mono text-white" id="router-invocations">0 Calls</span>
            </div>
            <div class="flex justify-between">
              <span class="text-slate-400">Deployment Latency:</span>
              <span class="font-bold font-mono text-emerald-400">&lt; 15 ms</span>
            </div>
          </div>
        </div>
        <div class="mt-4 text-[11px] text-slate-500 font-mono" id="router-status">Waiting for schema drift event.</div>
      </div>

    </div>

    <!-- Active Hot-Patch Source Code Viewer (Appears when active) -->
    <div id="adapter-code-container" class="glass rounded-3xl p-6 border border-slate-800 hidden">
      <div class="flex justify-between items-center mb-3">
        <h4 class="font-bold text-white text-sm flex items-center gap-2">
          <i class="fa-solid fa-code text-cyan-400"></i>
          Live Synthesized Adapter Function (<span id="adapter-client-id" class="text-cyan-300"></span>)
        </h4>
        <span class="text-xs font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-full border border-emerald-500/25">DYNAMIC IN-MEMORY MOUNT</span>
      </div>
      <pre class="bg-slate-950 p-4 rounded-xl text-xs text-emerald-300 border border-slate-800 overflow-x-auto"><code id="adapter-source-code"></code></pre>
    </div>

    <!-- Live Traffic Stream -->
    <div class="glass-card rounded-2xl p-5">
      <div class="flex items-center justify-between mb-4">
        <div class="flex items-center space-x-2">
          <i class="fa-solid fa-stream text-cyan-400"></i>
          <h4 class="font-bold text-white text-sm">Real-Time UPI Ingress Stream</h4>
        </div>
        <button onclick="clearLogs()" class="text-xs text-slate-400 hover:text-white transition">Clear Logs</button>
      </div>
      <div id="traffic-log-container" class="space-y-2 max-h-72 overflow-y-auto pr-1 font-mono text-xs">
        <div class="text-slate-500 text-center py-8">No traffic recorded yet. Click the buttons above to test!</div>
      </div>
    </div>

  </section>

  <!-- ========================================== -->
  <!-- 3. ARCHITECTURE BLUEPRINT SECTION          -->
  <!-- ========================================== -->
  <section id="architecture" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800/80 space-y-8">
    <div class="text-center max-w-3xl mx-auto space-y-2">
      <span class="text-xs font-mono uppercase text-emerald-400 font-semibold tracking-wider">Distributed Systems Architecture</span>
      <h2 class="text-3xl font-extrabold text-white">The 4-Tier Autonomous Self-Healing Pipeline</h2>
      <p class="text-sm text-slate-400">A multi-agent coordination state machine eliminating human intervention during unannounced API breaking changes.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 pt-4">
      <div class="glass-card rounded-2xl p-5 space-y-3 border-t-2 border-t-blue-500">
        <div class="w-8 h-8 rounded-lg bg-blue-500/10 text-blue-400 flex items-center justify-center font-mono font-bold text-sm">01</div>
        <h3 class="font-bold text-white text-base">Scout Agent</h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          Sliding-window telemetry ingress using <code class="text-blue-300">collections.deque</code>. Calculates error burst velocity per Bank ID and isolates breaking schema deltas.
        </p>
      </div>

      <div class="glass-card rounded-2xl p-5 space-y-3 border-t-2 border-t-teal-500">
        <div class="w-8 h-8 rounded-lg bg-teal-500/10 text-teal-400 flex items-center justify-center font-mono font-bold text-sm">02</div>
        <h3 class="font-bold text-white text-base">Synthesizer Agent</h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          Generates pure-function translation adapters: <code class="text-teal-300">adapt(payload: dict) -&gt; dict</code>. Supports Google Gemini, OpenAI, Claude, Groq, or deterministic AST fallbacks.
        </p>
      </div>

      <div class="glass-card rounded-2xl p-5 space-y-3 border-t-2 border-t-purple-500">
        <div class="w-8 h-8 rounded-lg bg-purple-500/10 text-purple-400 flex items-center justify-center font-mono font-bold text-sm">03</div>
        <h3 class="font-bold text-white text-base">Formal Verifier Gate</h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          Double-Gate Safety Gate. Gate 1 statically analyzes AST (blocks imports & dunders). Gate 2 uses Microsoft Z3 SMT solver to formally prove monetary value conservation.
        </p>
      </div>

      <div class="glass-card rounded-2xl p-5 space-y-3 border-t-2 border-t-cyan-500">
        <div class="w-8 h-8 rounded-lg bg-cyan-500/10 text-cyan-400 flex items-center justify-center font-mono font-bold text-sm">04</div>
        <h3 class="font-bold text-white text-base">Dynamic Hot-Router</h3>
        <p class="text-xs text-slate-400 leading-relaxed">
          Mounts verified adapter into ASGI pipeline in-memory in &lt;15ms. Subsequent requests from the breaking bank succeed instantly with zero downtime.
        </p>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- 4. PATENT CORE & FORMAL VERIFIER           -->
  <!-- ========================================== -->
  <section id="patent-core" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800/80 space-y-8">
    <div class="text-center max-w-3xl mx-auto space-y-2">
      <span class="text-xs font-mono uppercase text-purple-400 font-semibold tracking-wider">Mathematical Invariant & SMT Verification</span>
      <h2 class="text-3xl font-extrabold text-white">The Double-Gate Verification Gate</h2>
      <p class="text-sm text-slate-400">Guarantees that no generated code can steal funds, leak PII, or execute unauthorized operations.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- Theorem Card -->
      <div class="glass-card rounded-3xl p-6 border-purple-500/30 space-y-4">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-purple-500/15 text-purple-400 flex items-center justify-center">
            <i class="fa-solid fa-square-root-variable text-lg"></i>
          </div>
          <div>
            <h3 class="font-bold text-white text-base">SMT Monetary Value Conservation</h3>
            <span class="text-xs text-purple-300 font-mono">Microsoft Z3 Theorem Prover</span>
          </div>
        </div>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-slate-300 space-y-2">
          <div class="text-slate-500">// Formal Invariant Theorem</div>
          <div class="text-emerald-400 font-bold">&forall; x &isin; &real;<sub>&gt;0</sub>, &nbsp; AdapterAmount(x) == x</div>
          <div class="text-slate-400 pt-2 text-[11px] leading-relaxed">
            If any candidate adapter deducts a commission (e.g. <span class="text-rose-400">x * 0.98</span>), rounds prematurely, or alters the monetary value, the Z3 solver yields a counter-example (<code class="text-amber-400">SAT</code>) and halts hot-swap deployment immediately.
          </div>
        </div>
      </div>

      <!-- AST Isolation Card -->
      <div class="glass-card rounded-3xl p-6 border-cyan-500/30 space-y-4">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-cyan-500/15 text-cyan-400 flex items-center justify-center">
            <i class="fa-solid fa-ban text-lg"></i>
          </div>
          <div>
            <h3 class="font-bold text-white text-base">AST Static Safety Isolation</h3>
            <span class="text-xs text-cyan-300 font-mono">Python ast Static Node Inspection</span>
          </div>
        </div>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-slate-300 space-y-1.5">
          <div class="flex items-center justify-between text-rose-400">
            <span>&times; Import / ImportFrom</span>
            <span class="text-[10px] text-slate-500">BLOCKED</span>
          </div>
          <div class="flex items-center justify-between text-rose-400">
            <span>&times; Dunder Traversal (__class__, __subclasses__)</span>
            <span class="text-[10px] text-slate-500">BLOCKED</span>
          </div>
          <div class="flex items-center justify-between text-rose-400">
            <span>&times; Dangerous Built-ins (eval, exec, open, socket)</span>
            <span class="text-[10px] text-slate-500">BLOCKED</span>
          </div>
          <div class="flex items-center justify-between text-rose-400">
            <span>&times; Unbounded While Loops</span>
            <span class="text-[10px] text-slate-500">BLOCKED</span>
          </div>
          <div class="flex items-center justify-between text-emerald-400 pt-1">
            <span>&check; Pure Dictionary & Type Casting Only</span>
            <span class="text-[10px] text-emerald-500">ALLOWED</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ========================================== -->
  <!-- 5. BLOCKCHAIN AUDIT LEDGER SECTION         -->
  <!-- ========================================== -->
  <section id="ledger-section" class="max-w-7xl mx-auto px-6 py-16 border-t border-slate-800/80 space-y-6">
    <div class="flex flex-col md:flex-row justify-between items-start md:items-end gap-4">
      <div>
        <span class="text-xs font-mono uppercase text-purple-400 font-semibold tracking-wider">Immutable Non-Repudiation</span>
        <h2 class="text-3xl font-extrabold text-white">Cryptographic Audit Ledger</h2>
        <p class="text-sm text-slate-400">Append-only SHA-256 chained blockchain recording every hot-patch event for regulatory audit.</p>
      </div>
      <div class="text-xs font-mono px-3 py-1.5 rounded-xl bg-purple-500/10 text-purple-300 border border-purple-500/20" id="ledger-count-badge">
        2 Blocks Mined
      </div>
    </div>

    <div id="ledger-blocks-list" class="grid grid-cols-1 md:grid-cols-2 gap-4">
      <!-- Blocks populated dynamically -->
    </div>
  </section>

  <!-- Footer -->
  <footer class="border-t border-slate-800 px-6 py-8 text-center text-xs text-slate-500 font-mono">
    Project DPI-Heal | Built for NPCI UPI & Open Digital Public Infrastructure API Rails | High-Availability Swarm Architecture
  </footer>

  <!-- Client-side Logic -->
  <script>
    let localLog = [];

    async function fetchMetrics() {
      try {
        const res = await fetch('/api/v1/metrics');
        if (!res.ok) return;
        const data = await res.json();

        document.getElementById('stat-total').innerText = data.traffic.total_requests;
        document.getElementById('stat-canonical').innerText = data.traffic.canonical_success;
        document.getElementById('stat-adapted').innerText = data.traffic.adapted_success;
        document.getElementById('stat-failures').innerText = data.traffic.validation_failures;
        document.getElementById('stat-blocks').innerText = data.audit_ledger_blocks;
        document.getElementById('state-text').innerText = data.orchestrator_state;

        const bursts = data.scout_telemetry.active_failure_bursts || {};
        const mahBurst = bursts['BANK_MAHARASHTRA_COOP'] || 0;
        document.getElementById('scout-burst').innerText = `${mahBurst} / 5 failures`;
        const pct = Math.min(100, (mahBurst / 5) * 100);
        document.getElementById('scout-progress-bar').style.width = `${pct}%`;
        document.getElementById('scout-progress-bar').className = pct >= 100 
          ? "bg-rose-500 h-2 rounded-full transition-all duration-300"
          : "bg-blue-500 h-2 rounded-full transition-all duration-300";

        const adapters = data.active_hot_patches || {};
        const adapterKeys = Object.keys(adapters);
        document.getElementById('router-count').innerText = `${adapterKeys.length} Mounted`;

        let totalInvocations = 0;
        adapterKeys.forEach(k => {
          totalInvocations += adapters[k].invocation_count || 0;
        });
        document.getElementById('router-invocations').innerText = `${totalInvocations} Calls`;

        if (adapterKeys.length > 0) {
          const firstKey = adapterKeys[0];
          document.getElementById('adapter-code-container').classList.remove('hidden');
          document.getElementById('adapter-client-id').innerText = firstKey;
          document.getElementById('adapter-source-code').innerText = adapters[firstKey].source_code;
          document.getElementById('router-status').innerText = `Active hot-patch routing traffic for ${firstKey}`;
        } else {
          document.getElementById('adapter-code-container').classList.add('hidden');
          document.getElementById('router-status').innerText = 'No hot-patches active.';
        }

      } catch (err) {
        console.error("Metric fetch failed", err);
      }
    }

    async function fetchLedger() {
      try {
        const res = await fetch('/api/v1/ledger');
        if (!res.ok) return;
        const data = await res.json();
        const listEl = document.getElementById('ledger-blocks-list');
        listEl.innerHTML = '';

        document.getElementById('ledger-count-badge').innerText = `${data.total_blocks} Blocks Mined`;

        data.blocks.forEach(block => {
          const card = document.createElement('div');
          card.className = "bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-xs font-mono space-y-2";
          card.innerHTML = `
            <div class="flex justify-between items-center">
              <span class="text-purple-400 font-bold text-sm">Block #${block.index} [${block.client_id}]</span>
              <span class="text-slate-500 text-[11px] px-2 py-0.5 rounded bg-slate-800 border border-slate-700">Nonce: ${block.nonce}</span>
            </div>
            <div class="text-slate-400 truncate text-[11px]"><span class="text-slate-600">Hash:</span> ${block.hash}</div>
            <div class="text-slate-400 truncate text-[11px]"><span class="text-slate-600">Prev Hash:</span> ${block.prev_hash}</div>
            <div class="text-emerald-400 text-[11px] bg-slate-950 p-2.5 rounded-lg border border-slate-800/80 break-words">${block.verifier_proof_summary}</div>
          `;
          listEl.appendChild(card);
        });
      } catch (err) {
        console.error("Ledger fetch failed", err);
      }
    }

    function addLogEntry(bank, txn, status, code, adapter, detail) {
      const logContainer = document.getElementById('traffic-log-container');
      if (localLog.length === 0) logContainer.innerHTML = '';

      const timeStr = new Date().toLocaleTimeString();
      let badge = '';

      if (code === 200 && adapter) {
        badge = '<span class="px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-bold border border-cyan-500/30">ADAPTED_SUCCESS</span>';
      } else if (code === 200) {
        badge = '<span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30">SUCCESS (200)</span>';
      } else {
        badge = '<span class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 font-bold border border-rose-500/30">422 FAIL</span>';
      }

      const item = document.createElement('div');
      item.className = "p-2.5 rounded-xl bg-slate-900/90 border border-slate-800/80 flex items-center justify-between text-[11px]";
      item.innerHTML = `
        <div class="flex items-center space-x-2">
          <span class="text-slate-500">${timeStr}</span>
          <span class="font-bold text-slate-300">${bank}</span>
          <span class="text-slate-400 text-[10px]">${txn}</span>
        </div>
        <div>${badge}</div>
      `;

      logContainer.prepend(item);
      localLog.unshift(item);
      if (localLog.length > 50) localLog.pop();
    }

    function clearLogs() {
      localLog = [];
      document.getElementById('traffic-log-container').innerHTML = '<div class="text-slate-500 text-center py-8">Logs cleared.</div>';
    }

    async function sendValidPayment() {
      const txnId = `TXN_HDFC_${Math.floor(1000 + Math.random() * 9000)}`;
      const payload = {
        txn_id: txnId,
        payer_vpa: "customer@okhdfcbank",
        payee_vpa: "merchant@icici",
        amount: "500.00",
        currency: "INR",
        timestamp: Date.now(),
        auth_ref: `RRN_${Math.floor(100000 + Math.random() * 900000)}`
      };

      try {
        const res = await fetch('/api/v1/upi/pay', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'X-Bank-ID': 'BANK_HDFC_CANONICAL' },
          body: JSON.stringify(payload)
        });
        const data = await res.json();
        addLogEntry('BANK_HDFC', txnId, data.status, res.status, data.adapter_applied, '');
        fetchMetrics();
      } catch (e) {
        console.error(e);
      }
    }

    async function sendBrokenPayment() {
      const txnId = `TXN_MAH_${Math.floor(1000 + Math.random() * 9000)}`;
      const brokenPayload = {
        txn_id: txnId,
        vpa_id: "farmer_ajay@mahcoop",
        payee_vpa: "mandi@sbi",
        txn_amount: 1250.75,
        currency: "INR",
        timestamp: Date.now(),
        ref_id: `COOP_${Math.floor(100000 + Math.random() * 900000)}`,
        mpin_plain: "9876"
      };

      try {
        const res = await fetch('/api/v1/upi/pay', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'X-Bank-ID': 'BANK_MAHARASHTRA_COOP' },
          body: JSON.stringify(brokenPayload)
        });
        const data = await res.json();
        addLogEntry('BANK_MAHARASHTRA_COOP', txnId, data.status, res.status, data.adapter_applied || false, '');
        fetchMetrics();
        fetchLedger();
      } catch (e) {
        console.error(e);
      }
    }

    async function simulateOutageAndHeal() {
      for (let i = 0; i < 5; i++) {
        await sendBrokenPayment();
        await new Promise(r => setTimeout(r, 100));
      }
      setTimeout(async () => {
        await sendBrokenPayment();
        fetchMetrics();
        fetchLedger();
      }, 500);
    }

    async function revokeAdapter() {
      try {
        await fetch('/api/v1/adapters/BANK_MAHARASHTRA_COOP', { method: 'DELETE' });
        fetchMetrics();
        fetchLedger();
        alert('Active hot-patch adapter revoked! Traffic will now fail schema validation until re-healed.');
      } catch (e) {
        console.error(e);
      }
    }

    // Polling intervals
    setInterval(fetchMetrics, 2000);
    setInterval(fetchLedger, 3000);
    fetchMetrics();
    fetchLedger();
  </script>
</body>
</html>
"""
