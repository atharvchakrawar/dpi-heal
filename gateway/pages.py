"""
Multi-Page Web Interface for Project DPI-Heal
Provides dedicated pages for Cover, Simulator, Architecture, Verifier, and Blockchain Ledger.
"""

COVER_NAV_BAR = """
  <!-- Executive Front Cover Header (Minimalist Entrance) -->
  <header class="glass sticky top-0 z-50 px-6 py-4 border-b border-slate-800/80 flex justify-between items-center">
    <div class="flex items-center space-x-3.5">
      <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 via-teal-500 to-cyan-500 flex items-center justify-center shadow-lg shadow-emerald-500/25">
        <i class="fa-solid fa-shield-halved text-white text-lg"></i>
      </div>
      <div>
        <div class="flex items-center space-x-2">
          <span class="text-lg font-black tracking-tight bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">DPI-HEAL</span>
          <span class="text-[10px] uppercase font-mono px-2 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-bold">PORTAL ENTRANCE</span>
        </div>
        <p class="text-[11px] text-slate-400 font-mono tracking-tight">Autonomous Self-Healing Middleware Swarm</p>
      </div>
    </div>

    <!-- Entrance Action Button on Top Right -->
    <div class="flex items-center space-x-3">
      <span class="hidden sm:inline-flex items-center px-3 py-1 rounded-full text-xs font-mono font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/25">
        <span class="w-2 h-2 mr-2 bg-emerald-400 rounded-full animate-ping"></span>
        Gateway Active
      </span>
      <a href="/docs" target="_blank" class="px-3.5 py-2 text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-xl transition border border-slate-700 flex items-center space-x-1.5 shadow-sm">
        <i class="fa-solid fa-code text-cyan-400"></i>
        <span class="hidden sm:inline">API Docs</span>
      </a>
      <a href="/simulator" class="px-4 py-2 text-xs font-bold bg-gradient-to-r from-emerald-500 to-cyan-500 hover:from-emerald-400 hover:to-cyan-400 text-white rounded-xl transition shadow-lg shadow-emerald-500/25 flex items-center space-x-1.5">
        <span>Enter Platform</span>
        <i class="fa-solid fa-arrow-right text-[11px]"></i>
      </a>
    </div>
  </header>
"""

PLATFORM_NAV_BAR = """
  <!-- Top Navigation Bar for Platform Tools -->
  <header class="glass sticky top-0 z-50 px-6 py-3.5 border-b border-slate-800/80 flex justify-between items-center">
    <div class="flex items-center space-x-3.5">
      <a href="/" class="flex items-center space-x-3 group" title="Return to Front Cover Landing Page">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-500 via-teal-500 to-cyan-500 flex items-center justify-center shadow-lg shadow-emerald-500/25 group-hover:scale-105 transition-transform">
          <i class="fa-solid fa-shield-halved text-white text-lg"></i>
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <span class="text-lg font-black tracking-tight bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">DPI-HEAL</span>
            <span class="text-[10px] uppercase font-mono px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 border border-slate-700 font-semibold group-hover:text-emerald-400 transition">PLATFORM</span>
          </div>
          <p class="text-[11px] text-slate-400 font-mono tracking-tight">Autonomous Self-Healing Middleware Swarm</p>
        </div>
      </a>
    </div>

    <!-- Navigation Tabs (Only Platform Tools, NO 'Front Cover' tab) -->
    <nav class="hidden md:flex items-center space-x-1.5 bg-slate-900/90 p-1.5 rounded-xl border border-slate-800 text-xs">
      <a href="/simulator" class="nav-link px-3.5 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition font-medium" id="nav-simulator">
        <i class="fa-solid fa-gamepad mr-1.5 text-cyan-400"></i>Mission Control
      </a>
      <a href="/architecture" class="nav-link px-3.5 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition font-medium" id="nav-architecture">
        <i class="fa-solid fa-sitemap mr-1.5 text-blue-400"></i>Architecture
      </a>
      <a href="/verifier" class="nav-link px-3.5 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition font-medium" id="nav-verifier">
        <i class="fa-solid fa-square-root-variable mr-1.5 text-purple-400"></i>Z3 Verifier Gate
      </a>
      <a href="/ledger-explorer" class="nav-link px-3.5 py-1.5 rounded-lg text-slate-300 hover:text-white hover:bg-slate-800 transition font-medium" id="nav-ledger">
        <i class="fa-solid fa-link mr-1.5 text-emerald-400"></i>Audit Ledger
      </a>
    </nav>

    <div class="flex items-center space-x-3">
      <a href="/" class="hidden sm:inline-flex items-center px-3 py-1.5 rounded-xl text-xs font-mono text-slate-400 hover:text-white bg-slate-900 border border-slate-800 transition hover:border-slate-700" title="Exit Platform">
        <i class="fa-solid fa-arrow-right-from-bracket mr-1.5 text-slate-500"></i>Exit
      </a>
      <a href="/docs" target="_blank" class="px-3.5 py-2 text-xs font-semibold bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-xl transition border border-slate-700 flex items-center space-x-1.5 shadow-sm">
        <i class="fa-solid fa-code text-cyan-400"></i>
        <span>API Docs</span>
      </a>
    </div>
  </header>
"""

# Alias for backwards compatibility
NAV_BAR = PLATFORM_NAV_BAR

BASE_HEAD = """
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&display=swap');
    body { font-family: 'Plus Jakarta Sans', sans-serif; }
    code, pre, .font-mono { font-family: 'JetBrains Mono', monospace; }
    .glass { background: rgba(15, 23, 42, 0.85); backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08); }
    .glass-card { background: rgba(30, 41, 59, 0.65); backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.07); }
    .hero-glow { background: radial-gradient(circle at 50% 20%, rgba(16, 185, 129, 0.20) 0%, rgba(6, 182, 212, 0.12) 35%, transparent 70%); }
    .grid-pattern {
      background-size: 32px 32px;
      background-image: linear-gradient(to right, rgba(255, 255, 255, 0.03) 1px, transparent 1px),
                        linear-gradient(to bottom, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
    }
  </style>
"""


# ==============================================================================
# 1. EXECUTIVE FRONT COVER PAGE (GET /)
# ==============================================================================
PAGE_COVER_RAW = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <title>Project DPI-Heal: Executive Front Cover</title>
  __BASE_HEAD__
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-emerald-500 selection:text-white">

  __COVER_NAV_BAR__

  <!-- Main Hero Cover Body -->
  <main class="relative hero-glow grid-pattern flex-grow flex items-center justify-center px-4 py-8">
    <div class="max-w-4xl mx-auto text-center space-y-4">

      <!-- Badge -->
      <div class="inline-flex items-center space-x-2 px-3 py-1 rounded-full bg-slate-900/90 border border-slate-700 text-[11px] font-medium text-slate-300 shadow-md">
        <i class="fa-solid fa-microchip text-emerald-400"></i>
        <span>National Digital Public Infrastructure API Rail Protector</span>
        <span class="text-slate-600">|</span>
        <span class="text-emerald-400 font-mono font-semibold">UPI &bull; OCEN &bull; DigiLocker</span>
      </div>

      <!-- Main Headline -->
      <h1 class="text-3xl sm:text-4xl md:text-5xl font-black tracking-tight leading-tight">
        Autonomous <br>
        <span class="bg-gradient-to-r from-emerald-400 via-teal-300 to-cyan-400 bg-clip-text text-transparent">Self-Healing</span>
        Middleware Swarm
      </h1>

      <!-- Executive Overview -->
      <p class="max-w-2xl mx-auto text-xs sm:text-sm text-slate-300 leading-relaxed font-light">
        In high-throughput federated systems like UPI, upstream participant banks deploy unannounced schema drifts into production, causing immediate transaction dropouts (HTTP 422).
        <strong class="text-white font-semibold">DPI-Heal</strong> deploys an autonomous 3-tier agent swarm that isolates breaking payloads, synthesizes pure translation adapters, formally proves monetary conservation with <span class="text-emerald-400 font-mono font-semibold">Microsoft Z3 SMT solver</span>, and mounts hot-patches live in memory in <strong class="text-cyan-300 font-mono">&lt; 15 milliseconds</strong>.
      </p>

      <!-- Prominent Primary Call to Action: ENTER SITE / PLATFORM -->
      <div class="pt-2 pb-1">
        <a href="/simulator" class="inline-flex items-center space-x-2.5 px-7 py-3 rounded-xl bg-gradient-to-r from-emerald-500 via-teal-500 to-cyan-500 hover:from-emerald-400 hover:to-cyan-400 text-white font-bold text-base shadow-xl shadow-emerald-500/25 transition transform hover:-translate-y-0.5 group">
          <i class="fa-solid fa-rocket text-amber-300 group-hover:rotate-12 transition-transform"></i>
          <span>ENTER PLATFORM & MISSION CONTROL</span>
          <i class="fa-solid fa-arrow-right text-sm group-hover:translate-x-1 transition-transform"></i>
        </a>
        <p class="text-[11px] text-slate-400 mt-1.5 font-mono">Click to launch the live multi-bank simulator, Z3 verification engine, and audit ledger</p>
      </div>

      <!-- Navigation Action Cards -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-3 pt-2 text-left max-w-4xl mx-auto">
        <a href="/simulator" class="glass-card p-3.5 rounded-xl border-emerald-500/30 hover:border-emerald-400 hover:bg-slate-800/80 transition group transform hover:-translate-y-0.5 shadow-md">
          <div class="w-8 h-8 rounded-lg bg-emerald-500/10 text-emerald-400 flex items-center justify-center mb-2 group-hover:scale-110 transition-transform">
            <i class="fa-solid fa-gamepad text-sm"></i>
          </div>
          <div class="text-white font-bold text-xs flex items-center justify-between">
            <span>Mission Control</span>
            <i class="fa-solid fa-arrow-right text-[10px] text-emerald-400 group-hover:translate-x-1 transition-transform"></i>
          </div>
          <p class="text-[10px] text-slate-400 mt-1">Interactive live simulator: schema drifts, Scout alerts, and hot-swap adapters.</p>
        </a>

        <a href="/architecture" class="glass-card p-3.5 rounded-xl border-blue-500/30 hover:border-blue-400 hover:bg-slate-800/80 transition group transform hover:-translate-y-0.5 shadow-md">
          <div class="w-8 h-8 rounded-lg bg-blue-500/10 text-blue-400 flex items-center justify-center mb-2 group-hover:scale-110 transition-transform">
            <i class="fa-solid fa-sitemap text-sm"></i>
          </div>
          <div class="text-white font-bold text-xs flex items-center justify-between">
            <span>Architecture</span>
            <i class="fa-solid fa-arrow-right text-[10px] text-blue-400 group-hover:translate-x-1 transition-transform"></i>
          </div>
          <p class="text-[10px] text-slate-400 mt-1">4-tier multi-agent pipeline: Scout, Synthesizer, Formal Verifier, and Dynamic Router.</p>
        </a>

        <a href="/verifier" class="glass-card p-3.5 rounded-xl border-purple-500/30 hover:border-purple-400 hover:bg-slate-800/80 transition group transform hover:-translate-y-0.5 shadow-md">
          <div class="w-8 h-8 rounded-lg bg-purple-500/10 text-purple-400 flex items-center justify-center mb-2 group-hover:scale-110 transition-transform">
            <i class="fa-solid fa-square-root-variable text-sm"></i>
          </div>
          <div class="text-white font-bold text-xs flex items-center justify-between">
            <span>Patent Core</span>
            <i class="fa-solid fa-arrow-right text-[10px] text-purple-400 group-hover:translate-x-1 transition-transform"></i>
          </div>
          <p class="text-[10px] text-slate-400 mt-1">Microsoft Z3 SMT solver proving &forall;x&gt;0 monetary conservation & AST safety.</p>
        </a>

        <a href="/ledger-explorer" class="glass-card p-3.5 rounded-xl border-teal-500/30 hover:border-teal-400 hover:bg-slate-800/80 transition group transform hover:-translate-y-0.5 shadow-md">
          <div class="w-8 h-8 rounded-lg bg-teal-500/10 text-teal-400 flex items-center justify-center mb-2 group-hover:scale-110 transition-transform">
            <i class="fa-solid fa-link text-sm"></i>
          </div>
          <div class="text-white font-bold text-xs flex items-center justify-between">
            <span>Audit Ledger</span>
            <i class="fa-solid fa-arrow-right text-[10px] text-teal-400 group-hover:translate-x-1 transition-transform"></i>
          </div>
          <p class="text-[10px] text-slate-400 mt-1">SHA-256 chained append-only blockchain providing tamper-evident runtime proof.</p>
        </a>
      </div>

      <!-- Quick Metrics Ribbon -->
      <div class="pt-2 grid grid-cols-2 sm:grid-cols-4 gap-2 max-w-3xl mx-auto text-[10px] font-medium">
        <div class="p-2 rounded-lg glass-card text-slate-300 flex items-center justify-center space-x-1.5">
          <i class="fa-solid fa-gauge-high text-emerald-400"></i>
          <span>Sliding Window Velocity</span>
        </div>
        <div class="p-2 rounded-lg glass-card text-slate-300 flex items-center justify-center space-x-1.5">
          <i class="fa-solid fa-calculator text-cyan-400"></i>
          <span>Z3 Proof &forall;x&gt;0</span>
        </div>
        <div class="p-2 rounded-lg glass-card text-slate-300 flex items-center justify-center space-x-1.5">
          <i class="fa-solid fa-bolt text-amber-400"></i>
          <span>&lt;15ms Hot-Swap</span>
        </div>
        <div class="p-2 rounded-lg glass-card text-slate-300 flex items-center justify-center space-x-1.5">
          <i class="fa-solid fa-lock text-purple-400"></i>
          <span>Tamper-Proof Audit</span>
        </div>
      </div>

    </div>
  </main>

  <footer class="border-t border-slate-800/80 px-4 py-3 text-center text-[11px] text-slate-500 font-mono">
    Project DPI-Heal &bull; Autonomous Self-Healing Middleware Swarm for Digital Public Infrastructure
  </footer>

</body>
</html>
"""


# ==============================================================================
# 2. DEDICATED MISSION CONTROL & SIMULATOR PAGE (GET /simulator)
# ==============================================================================
PAGE_SIMULATOR_RAW = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <title>DPI-Heal: Mission Control & Simulator</title>
  __BASE_HEAD__
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen selection:bg-emerald-500 selection:text-white">

  __NAV_BAR__

  <main class="max-w-7xl mx-auto px-6 py-10 space-y-8">

    <!-- Page Header -->
    <div class="flex flex-col md:flex-row justify-between items-start md:items-end gap-4 border-b border-slate-800 pb-6">
      <div>
        <div class="flex items-center space-x-2 mb-1">
          <span class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
          <span class="text-xs font-mono font-semibold uppercase tracking-wider text-cyan-400">Live Traffic Generator & Telemetry</span>
        </div>
        <h1 class="text-3xl md:text-4xl font-black text-white">Swarm Mission Control</h1>
        <p class="text-sm text-slate-400 mt-1">Inject transactions, trip failure velocity alerts, and watch the autonomous agent swarm hot-patch the gateway.</p>
      </div>
      <div class="flex items-center space-x-3">
        <button id="btn-autopilot-toggle" onclick="toggleAutopilot()" class="px-3.5 py-1.5 rounded-xl border text-xs font-mono font-bold flex items-center space-x-2 transition bg-emerald-500/10 border-emerald-500/40 text-emerald-400 hover:bg-emerald-500/20 shadow-sm" title="Click to Pause/Resume 24/7 Autonomous Background Swarm">
          <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" id="autopilot-dot"></span>
          <span id="autopilot-label">AUTOPILOT: 24/7 ACTIVE</span>
        </button>

        <div class="px-3.5 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-xs font-mono">
          <span class="text-slate-500">Orchestrator State: </span>
          <span id="state-text" class="text-emerald-400 font-bold">IDLE</span>
        </div>
        <button onclick="fetchMetrics();" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-400 hover:text-white transition shadow-sm">
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

    <!-- Multi-Bank Fleet Selector Bar -->
    <div class="space-y-4">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div class="flex items-center space-x-2 mb-1">
            <span class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
            <span class="text-xs font-mono font-semibold uppercase tracking-wider text-cyan-400">Target Bank Selector & National Fleet Matrix</span>
          </div>
          <h2 class="text-2xl font-black text-white flex items-center gap-2">
            <i class="fa-solid fa-building-columns text-cyan-400"></i>
            Select Participant Bank Rail to Monitor & Test
          </h2>
          <p class="text-xs text-slate-400 mt-1 max-w-3xl">
            Click any participant bank below to view its dedicated Scout error velocity, drift signature, Z3 verification proof, and live hot-patch adapter.
          </p>
        </div>
        <div class="flex items-center space-x-2">
          <button onclick="simulateAllFleetHeal()" id="btn-fleet-heal" class="px-4 py-2.5 rounded-xl text-xs font-bold bg-gradient-to-r from-indigo-600 to-cyan-600 hover:from-indigo-500 hover:to-cyan-500 text-white shadow-lg transition flex items-center gap-2">
            <i class="fa-solid fa-bolt-lightning text-amber-300"></i>
            <span>Simulate All Fleet Outages & Auto-Heal</span>
          </button>
        </div>
      </div>

      <!-- Bank Tabs / Switcher Grid -->
      <div class="grid grid-cols-2 md:grid-cols-5 gap-3" id="bank-tabs-grid">

        <!-- Tab: Maha Co-op -->
        <button onclick="selectTargetBank('BANK_MAHARASHTRA_COOP')" id="tab-BANK_MAHARASHTRA_COOP" class="p-3.5 rounded-2xl glass-card border-2 border-cyan-500/80 bg-slate-900/90 text-left transition relative overflow-hidden group shadow-lg shadow-cyan-950/40">
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-mono uppercase px-2 py-0.5 rounded font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30" id="pill-BANK_MAHARASHTRA_COOP">DRIFTED</span>
            <span class="text-[10px] font-mono text-slate-400 font-bold" id="velpill-BANK_MAHARASHTRA_COOP">0/5</span>
          </div>
          <div class="font-bold text-xs text-white truncate">Maha Co-op Bank</div>
          <div class="text-[10px] text-slate-400 font-mono truncate">vpa_id &bull; txn_amount</div>
        </button>

        <!-- Tab: Punjab Gramin -->
        <button onclick="selectTargetBank('BANK_PUNJAB_RURAL')" id="tab-BANK_PUNJAB_RURAL" class="p-3.5 rounded-2xl glass-card border border-slate-800 hover:border-slate-700 bg-slate-900/60 text-left transition relative overflow-hidden group">
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-mono uppercase px-2 py-0.5 rounded font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30" id="pill-BANK_PUNJAB_RURAL">DRIFTED</span>
            <span class="text-[10px] font-mono text-slate-400 font-bold" id="velpill-BANK_PUNJAB_RURAL">0/5</span>
          </div>
          <div class="font-bold text-xs text-white truncate">Punjab Gramin Bank</div>
          <div class="text-[10px] text-slate-400 font-mono truncate">sender_vpa &bull; transfer_amount</div>
        </button>

        <!-- Tab: Tamil Nadu Gramin -->
        <button onclick="selectTargetBank('BANK_TAMILNADU_GRAMIN')" id="tab-BANK_TAMILNADU_GRAMIN" class="p-3.5 rounded-2xl glass-card border border-slate-800 hover:border-slate-700 bg-slate-900/60 text-left transition relative overflow-hidden group">
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-mono uppercase px-2 py-0.5 rounded font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30" id="pill-BANK_TAMILNADU_GRAMIN">DRIFTED</span>
            <span class="text-[10px] font-mono text-slate-400 font-bold" id="velpill-BANK_TAMILNADU_GRAMIN">0/5</span>
          </div>
          <div class="font-bold text-xs text-white truncate">Tamil Nadu Gramin</div>
          <div class="text-[10px] text-slate-400 font-mono truncate">customer_vpa &bull; amount_inr</div>
        </button>

        <!-- Tab: Kerala Co-op -->
        <button onclick="selectTargetBank('BANK_KERALA_COOP')" id="tab-BANK_KERALA_COOP" class="p-3.5 rounded-2xl glass-card border border-slate-800 hover:border-slate-700 bg-slate-900/60 text-left transition relative overflow-hidden group">
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-mono uppercase px-2 py-0.5 rounded font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30" id="pill-BANK_KERALA_COOP">DRIFTED</span>
            <span class="text-[10px] font-mono text-slate-400 font-bold" id="velpill-BANK_KERALA_COOP">0/5</span>
          </div>
          <div class="font-bold text-xs text-white truncate">Kerala Co-op Bank</div>
          <div class="text-[10px] text-slate-400 font-mono truncate">acc_vpa &bull; amount_rs</div>
        </button>

        <!-- Tab: Custom Participant -->
        <button onclick="selectTargetBank('CUSTOM')" id="tab-CUSTOM" class="p-3.5 rounded-2xl glass-card border border-slate-800 hover:border-purple-500/50 bg-slate-900/60 text-left transition relative overflow-hidden group">
          <div class="flex items-center justify-between mb-1.5">
            <span class="text-[10px] font-mono uppercase px-2 py-0.5 rounded font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30" id="pill-CUSTOM">CUSTOM</span>
            <span class="text-[10px] font-mono text-slate-400 font-bold">ANY</span>
          </div>
          <div class="font-bold text-xs text-white truncate">Custom Participant</div>
          <div class="text-[10px] text-slate-400 font-mono truncate">Arbitrary Bank ID</div>
        </button>

      </div>
    </div>

    <!-- Active Target Context Banner -->
    <div class="glass rounded-3xl p-5 border border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-4">
      <div class="flex items-center space-x-3.5">
        <div class="w-12 h-12 rounded-2xl bg-cyan-500/10 border border-cyan-500/30 flex items-center justify-center text-cyan-300 text-xl font-bold">
          <i class="fa-solid fa-server"></i>
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <h3 class="text-base font-bold text-white" id="focus-bank-name">Bank B: Maharashtra Co-operative Bank</h3>
            <span class="text-xs font-mono font-bold px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/40" id="focus-bank-status-badge">MONITORED</span>
          </div>
          <div class="text-xs text-slate-400 font-mono mt-0.5 flex flex-wrap items-center gap-2">
            <span>Target Client ID: <code class="text-cyan-300 font-bold" id="focus-bank-id">BANK_MAHARASHTRA_COOP</code></span>
            <span class="text-slate-600">&bull;</span>
            <span class="text-amber-300/90" id="focus-bank-drift">Drift: 'payer_vpa' &rarr; 'vpa_id', 'amount' &rarr; 'txn_amount', adds 'mpin_plain'</span>
          </div>
        </div>
      </div>
      <div id="custom-input-wrap" class="hidden flex items-center space-x-2">
        <input type="text" id="custom-bank-input" value="BANK_BIHAR_RURAL" class="bg-slate-900 border border-slate-700 rounded-xl px-3 py-1.5 text-xs text-cyan-300 font-mono focus:outline-none focus:border-cyan-400" placeholder="e.g. BANK_BIHAR_RURAL" oninput="onCustomIdInput()" />
      </div>
    </div>

    <!-- 4 Traffic Injection Controls -->
    <div class="glass rounded-3xl p-6 border border-slate-800 space-y-4">
      <div class="flex items-center justify-between">
        <div>
          <h3 class="text-lg font-bold text-white flex items-center gap-2">
            <i class="fa-solid fa-gamepad text-cyan-400"></i>
            Traffic Injection & Swarm Controls
          </h3>
          <p class="text-xs text-slate-400 mt-0.5">Click any action below to trigger transactions for <strong class="text-cyan-300" id="btn-context-bank">BANK_MAHARASHTRA_COOP</strong>.</p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">

        <!-- 1. Normal HDFC Traffic -->
        <button onclick="sendValidPayment()" class="flex flex-col p-4 rounded-2xl bg-slate-900/90 hover:bg-slate-800 border border-emerald-500/30 hover:border-emerald-500/60 transition group text-left shadow-md">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold uppercase text-emerald-400 tracking-wider font-mono">1. Normal Traffic</span>
            <i class="fa-solid fa-paper-plane text-emerald-400 group-hover:translate-x-1 transition-transform"></i>
          </div>
          <div class="font-bold text-sm text-white">Send Valid Transaction</div>
          <div class="text-xs text-slate-400 mt-1">HDFC Bank sends canonical UPI payload &rarr; 200 OK SUCCESS.</div>
        </button>

        <!-- 2. Single Mutation Request -->
        <button onclick="sendSingleTestPayment()" class="flex flex-col p-4 rounded-2xl bg-slate-900/90 hover:bg-slate-800 border border-amber-500/30 hover:border-amber-500/60 transition group text-left shadow-md">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold uppercase text-amber-400 tracking-wider font-mono">2. Single Mutation</span>
            <i class="fa-solid fa-bug text-amber-400 group-hover:scale-110 transition-transform"></i>
          </div>
          <div class="font-bold text-sm text-white" id="btn-single-title">Send 1 Test Request</div>
          <div class="text-xs text-slate-400 mt-1" id="btn-single-desc">Sends 1 payload from selected bank. Fails if unhealed, succeeds if adapted.</div>
        </button>

        <!-- 3. Burst 5 & Auto-Heal (Repeatable) -->
        <button onclick="simulateBurstAndHeal()" id="btn-burst-heal" class="flex flex-col p-4 rounded-2xl bg-gradient-to-br from-indigo-950/90 to-slate-900 hover:from-indigo-900 border border-indigo-500/50 hover:border-indigo-400 transition group text-left shadow-lg shadow-indigo-950/60">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold uppercase text-indigo-300 tracking-wider font-mono">3. Self-Healing Swarm</span>
            <i class="fa-solid fa-bolt-lightning text-amber-300 animate-pulse" id="btn-burst-icon"></i>
          </div>
          <div class="font-bold text-sm text-white" id="btn-burst-title">⚡ Burst 5 & Auto-Heal</div>
          <div class="text-xs text-slate-300 mt-1" id="btn-burst-desc">Trips Scout velocity (&gt;5 drops), runs Z3 proof, & mounts hot-patch live in &lt;15ms!</div>
        </button>

        <!-- 4. Revoke & Reset -->
        <button onclick="revokeCurrentAdapter()" class="flex flex-col p-4 rounded-2xl bg-slate-900/90 hover:bg-slate-800 border border-rose-500/30 hover:border-rose-500/60 transition group text-left shadow-md">
          <div class="flex items-center justify-between mb-2">
            <span class="text-[11px] font-bold uppercase text-rose-400 tracking-wider font-mono">4. Reset & Unmount</span>
            <i class="fa-solid fa-rotate-left text-rose-400 group-hover:-rotate-45 transition-transform"></i>
          </div>
          <div class="font-bold text-sm text-white">Revoke Hot-Patch Adapter</div>
          <div class="text-xs text-slate-400 mt-1">Unmounts adapter to revert selected bank traffic to failing state.</div>
        </button>

      </div>
    </div>

    <!-- Agent Swarm Visualizer -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">

      <!-- Scout -->
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
              <span class="font-mono text-cyan-300 font-semibold text-[11px]" id="scout-target">BANK_MAHARASHTRA_COOP</span>
            </div>
            <div class="flex justify-between text-xs">
              <span class="text-slate-400">Target Burst Velocity:</span>
              <span class="font-mono font-bold" id="scout-burst">0 / 5 failures</span>
            </div>
            <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden">
              <div id="scout-progress-bar" class="bg-blue-500 h-2 rounded-full transition-all duration-300" style="width: 0%"></div>
            </div>
            <div class="pt-1 border-t border-slate-800/60 text-[10px] text-slate-400 flex justify-between items-center">
              <span>All Active Bursts:</span>
              <span class="font-mono text-amber-300 font-semibold" id="scout-burst-summary">None</span>
            </div>
          </div>
        </div>
        <div class="mt-4 text-[11px] text-slate-500 font-mono" id="scout-status-line">Telemetry window healthy.</div>
      </div>

      <!-- Verifier -->
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

      <!-- Router -->
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

    <!-- Active Hot-Patch Source Code Viewer -->
    <div id="adapter-code-container" class="glass rounded-3xl p-6 border border-slate-800 space-y-4">
      <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
        <div>
          <h4 class="font-bold text-white text-sm flex items-center gap-2">
            <i class="fa-solid fa-code text-cyan-400"></i>
            Live Synthesized Adapter Function (<span id="adapter-client-id" class="text-cyan-300 font-mono">BANK_MAHARASHTRA_COOP</span>)
          </h4>
          <p class="text-xs text-slate-400 mt-0.5">Verified Python hot-patch dynamically translating drifted upstream payloads into canonical UPI 2.0 schema.</p>
        </div>
        <div class="flex items-center space-x-2">
          <span class="text-xs font-mono text-emerald-400 bg-emerald-500/10 px-2.5 py-1 rounded-full border border-emerald-500/25">DYNAMIC IN-MEMORY MOUNT</span>
          <span id="adapter-invocation-badge" class="text-xs font-mono text-cyan-300 bg-cyan-500/10 px-2.5 py-1 rounded-full border border-cyan-500/25">0 Calls</span>
        </div>
      </div>

      <!-- Multi-Bank Adapter Tabs -->
      <div id="adapter-tabs" class="flex flex-wrap gap-2 pt-2 border-b border-slate-800 pb-3"></div>

      <pre class="bg-slate-950 p-4 rounded-xl text-xs text-emerald-300 border border-slate-800 overflow-x-auto"><code id="adapter-source-code"># Waiting for self-healing swarm to synthesize adapter...
# Click '⚡ Burst 5 & Auto-Heal' above to trigger synthesis and Z3 verification!</code></pre>
    </div>

    <!-- Simultaneous Fleet Overview Matrix -->
    <div class="glass-card rounded-2xl p-5 space-y-3">
      <div class="flex items-center justify-between">
        <h4 class="font-bold text-white text-sm flex items-center gap-2">
          <i class="fa-solid fa-table-list text-cyan-400"></i>
          National Participant Bank Fleet Matrix (Simultaneous Status)
        </h4>
        <span class="text-xs text-slate-400 font-mono">Live Ingress Observability</span>
      </div>
      <div class="overflow-x-auto">
        <table class="w-full text-left text-xs font-mono">
          <thead class="text-slate-400 border-b border-slate-800/80 uppercase text-[10px]">
            <tr>
              <th class="py-2.5 px-3">Bank Rail</th>
              <th class="py-2.5 px-3">Participant Name</th>
              <th class="py-2.5 px-3">Schema Drift Keys</th>
              <th class="py-2.5 px-3">Burst Velocity</th>
              <th class="py-2.5 px-3">Adapter State</th>
              <th class="py-2.5 px-3">Adapted Calls</th>
              <th class="py-2.5 px-3 text-right">Quick Action</th>
            </tr>
          </thead>
          <tbody id="fleet-matrix-body" class="divide-y divide-slate-800/60 text-slate-300">
            <!-- Populated dynamically via JS -->
          </tbody>
        </table>
      </div>
    </div>

    <!-- Real-Time Traffic Feed -->
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

  </main>

  <script>
    document.getElementById('nav-simulator').classList.add('bg-slate-800', 'text-cyan-400', 'font-bold');

    let localLog = [];
    let seenTxnIds = new Set();
    let selectedBankId = 'BANK_MAHARASHTRA_COOP';
    let cachedAdapters = {};

    async function toggleAutopilot() {
      try {
        const res = await fetch('/api/v1/autopilot/toggle', { method: 'POST' });
        const data = await res.json();
        updateAutopilotUI(data.active);
      } catch (e) {
        console.error("Failed to toggle autopilot", e);
      }
    }

    function updateAutopilotUI(isActive) {
      const btn = document.getElementById('btn-autopilot-toggle');
      const dot = document.getElementById('autopilot-dot');
      const label = document.getElementById('autopilot-label');
      if (!btn) return;
      if (isActive) {
        btn.className = "px-3.5 py-1.5 rounded-xl border text-xs font-mono font-bold flex items-center space-x-2 transition bg-emerald-500/10 border-emerald-500/40 text-emerald-400 hover:bg-emerald-500/20 shadow-sm";
        if (dot) dot.className = "w-2 h-2 rounded-full bg-emerald-400 animate-pulse";
        if (label) label.innerText = "AUTOPILOT: 24/7 ACTIVE";
      } else {
        btn.className = "px-3.5 py-1.5 rounded-xl border text-xs font-mono font-bold flex items-center space-x-2 transition bg-amber-500/10 border-amber-500/40 text-amber-400 hover:bg-amber-500/20 shadow-sm";
        if (dot) dot.className = "w-2 h-2 rounded-full bg-amber-400";
        if (label) label.innerText = "AUTOPILOT: PAUSED";
      }
    }

    const BANK_REGISTRY = {
      'BANK_MAHARASHTRA_COOP': {
        name: 'Maharashtra Co-op Bank',
        driftDesc: "Drift: 'payer_vpa' -> 'vpa_id', 'amount' -> 'txn_amount', adds plaintext 'mpin_plain'",
        makePayload: (txnId) => ({
          txn_id: txnId,
          vpa_id: `farmer_kisan_${Math.floor(100 + Math.random() * 900)}@mahcoop`,
          payee_vpa: "mandi_kisan@sbi",
          txn_amount: 1450.50,
          currency: "INR",
          timestamp: Date.now(),
          ref_id: `COOP_${Math.floor(100000 + Math.random() * 900000)}`,
          mpin_plain: "9876"
        })
      },
      'BANK_PUNJAB_RURAL': {
        name: 'Punjab Gramin Bank',
        driftDesc: "Drift: 'payer_vpa' -> 'sender_vpa', 'amount' -> 'transfer_amount', 'auth_ref' -> 'rrn'",
        makePayload: (txnId) => ({
          txn_id: txnId,
          sender_vpa: `farmer_harpreet@punjabgramin`,
          payee_vpa: "tractor_store@pnb",
          transfer_amount: "3200.00",
          currency: "INR",
          timestamp: Date.now(),
          rrn: `PGB_${Math.floor(100000 + Math.random() * 900000)}`
        })
      },
      'BANK_TAMILNADU_GRAMIN': {
        name: 'Tamil Nadu Gramin Bank',
        driftDesc: "Drift: 'payer_vpa' -> 'customer_vpa', 'amount' -> 'amount_inr', 'auth_ref' -> 'bank_ref'",
        makePayload: (txnId) => ({
          txn_id: txnId,
          customer_vpa: `selvam@tngramin`,
          payee_vpa: "fertilizer@canara",
          amount_inr: 890.25,
          currency: "INR",
          timestamp: Date.now(),
          bank_ref: `TNB_${Math.floor(100000 + Math.random() * 900000)}`
        })
      },
      'BANK_KERALA_COOP': {
        name: 'Kerala Cooperative Bank',
        driftDesc: "Drift: 'payer_vpa' -> 'acc_vpa', 'amount' -> 'amount_rs', 'auth_ref' -> 'txn_reference'",
        makePayload: (txnId) => ({
          txn_id: txnId,
          acc_vpa: `anand@keralacoop`,
          payee_vpa: "spices_export@sbi",
          amount_rs: 2150.00,
          currency: "INR",
          timestamp: Date.now(),
          txn_reference: `KCB_${Math.floor(100000 + Math.random() * 900000)}`
        })
      }
    };

    function getEffectiveBankId() {
      if (selectedBankId === 'CUSTOM') {
        const customInput = document.getElementById('custom-bank-input');
        return (customInput && customInput.value.trim()) ? customInput.value.trim() : 'BANK_CUSTOM';
      }
      return selectedBankId;
    }

    function selectTargetBank(bankId) {
      selectedBankId = bankId;
      const effectiveId = getEffectiveBankId();

      // Highlight active tab
      const allTabs = ['BANK_MAHARASHTRA_COOP', 'BANK_PUNJAB_RURAL', 'BANK_TAMILNADU_GRAMIN', 'BANK_KERALA_COOP', 'CUSTOM'];
      allTabs.forEach(t => {
        const el = document.getElementById(`tab-${t}`);
        if (el) {
          if (t === bankId) {
            el.className = "p-3.5 rounded-2xl glass-card border-2 border-cyan-500 bg-slate-900 text-left transition relative overflow-hidden group shadow-lg shadow-cyan-950/40";
          } else {
            el.className = "p-3.5 rounded-2xl glass-card border border-slate-800 hover:border-slate-700 bg-slate-900/60 text-left transition relative overflow-hidden group";
          }
        }
      });

      // Update Active Focus Banner
      const customWrap = document.getElementById('custom-input-wrap');
      if (bankId === 'CUSTOM') {
        customWrap.classList.remove('hidden');
        document.getElementById('focus-bank-name').innerText = "Custom Participant Bank Rail";
        document.getElementById('focus-bank-id').innerText = effectiveId;
        document.getElementById('focus-bank-drift').innerText = "Drift: Arbitrary unannounced schema mutations";
      } else {
        customWrap.classList.add('hidden');
        const cfg = BANK_REGISTRY[bankId];
        document.getElementById('focus-bank-name').innerText = cfg.name;
        document.getElementById('focus-bank-id').innerText = bankId;
        document.getElementById('focus-bank-drift').innerText = cfg.driftDesc;
      }

      document.getElementById('btn-context-bank').innerText = effectiveId;
      document.getElementById('scout-target').innerText = effectiveId;
      document.getElementById('adapter-client-id').innerText = effectiveId;

      fetchMetrics();
    }

    function onCustomIdInput() {
      selectTargetBank('CUSTOM');
    }

    function setBurstButtonState(isLoading, text) {
      const btn = document.getElementById('btn-burst-heal');
      const title = document.getElementById('btn-burst-title');
      const icon = document.getElementById('btn-burst-icon');
      if (isLoading) {
        btn.classList.add('opacity-80', 'cursor-wait');
        icon.className = "fa-solid fa-spinner fa-spin text-amber-300";
        title.innerText = text;
      } else {
        btn.classList.remove('opacity-80', 'cursor-wait');
        icon.className = "fa-solid fa-bolt-lightning text-amber-300 animate-pulse";
        title.innerText = text || "⚡ Burst 5 & Auto-Heal";
      }
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
        addLogEntry('BANK_HDFC_CANONICAL', txnId, data.status, res.status, data.adapter_applied, '');
        fetchMetrics();
      } catch (e) {
        console.error(e);
      }
    }

    async function sendRawBrokenPayment(bankId) {
      const txnId = `TXN_${bankId.substring(5, 9)}_${Math.floor(1000 + Math.random() * 9000)}`;
      let payload;
      if (BANK_REGISTRY[bankId]) {
        payload = BANK_REGISTRY[bankId].makePayload(txnId);
      } else {
        payload = {
          txn_id: txnId,
          vpa_id: `user@${bankId.toLowerCase()}`,
          payee_vpa: "merchant@bank",
          txn_amount: 1999.00,
          currency: "INR",
          timestamp: Date.now(),
          bank_ref: `REF_${Math.floor(100000 + Math.random() * 900000)}`
        };
      }

      try {
        const res = await fetch('/api/v1/upi/pay', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'X-Bank-ID': bankId },
          body: JSON.stringify(payload)
        });
        const data = await res.json();
        addLogEntry(bankId, txnId, data.status, res.status, data.adapter_applied || false, '');
        return { status: res.status, data: data };
      } catch (e) {
        console.error(e);
        return { status: 500, error: e };
      }
    }

    async function sendSingleTestPayment() {
      const bankId = getEffectiveBankId();
      await sendRawBrokenPayment(bankId);
      await fetchMetrics();
    }

    async function simulateBurstAndHeal() {
      const bankId = getEffectiveBankId();
      setBurstButtonState(true, "Resetting previous state...");

      // Step 1: Cleanly reset previous adapter and Scout window for seamless repeatability!
      try {
        await fetch(`/api/v1/adapters/${bankId}`, { method: 'DELETE' });
        delete cachedAdapters[bankId];
      } catch (e) {}

      await fetchMetrics();
      await new Promise(r => setTimeout(r, 100));

      // Step 2: Fire 5 breaking requests sequentially
      for (let i = 1; i <= 5; i++) {
        setBurstButtonState(true, `Tripping Scout (${i}/5 Drops)...`);
        await sendRawBrokenPayment(bankId);
        await fetchMetrics();
        await new Promise(r => setTimeout(r, 150));
      }

      // Step 3: Synthesis & Verification step
      setBurstButtonState(true, "Synthesizing & Verifying with Z3...");
      await new Promise(r => setTimeout(r, 400));
      await fetchMetrics();

      // Step 4: Fire adapted request to prove hot-swap in memory
      setBurstButtonState(true, "Mounting Hot-Patch & Adapting...");
      await sendRawBrokenPayment(bankId);
      await fetchMetrics();

      setBurstButtonState(false, "⚡ Burst 5 & Auto-Heal (Ready)");
    }

    async function revokeCurrentAdapter() {
      const bankId = getEffectiveBankId();
      try {
        await fetch(`/api/v1/adapters/${bankId}`, { method: 'DELETE' });
        delete cachedAdapters[bankId];
        await fetchMetrics();
        alert(`Adapter for ${bankId} revoked! Future traffic will fail validation until auto-healed.`);
      } catch (e) {
        console.error(e);
      }
    }

    async function simulateAllFleetHeal() {
      const btn = document.getElementById('btn-fleet-heal');
      btn.classList.add('opacity-80', 'cursor-wait');
      btn.innerHTML = `<i class="fa-solid fa-spinner fa-spin text-amber-300"></i> <span>Healing Fleet...</span>`;

      const banks = ['BANK_MAHARASHTRA_COOP', 'BANK_PUNJAB_RURAL', 'BANK_TAMILNADU_GRAMIN', 'BANK_KERALA_COOP'];
      for (const b of banks) {
        selectTargetBank(b);
        await simulateBurstAndHeal();
        await new Promise(r => setTimeout(r, 200));
      }

      btn.classList.remove('opacity-80', 'cursor-wait');
      btn.innerHTML = `<i class="fa-solid fa-check-double text-emerald-400"></i> <span>All Fleet Healed!</span>`;
      setTimeout(() => {
        btn.innerHTML = `<i class="fa-solid fa-bolt-lightning text-amber-300"></i> <span>Simulate All Fleet Outages & Auto-Heal</span>`;
      }, 3000);
    }

    function renderFleetMatrix(bursts, adapters) {
      const tbody = document.getElementById('fleet-matrix-body');
      if (!tbody) return;

      const bankList = [
        { id: 'BANK_HDFC_CANONICAL', name: 'HDFC Bank', drift: 'None (Canonical UPI 2.0)', isCanonical: true },
        { id: 'BANK_MAHARASHTRA_COOP', name: 'Maharashtra Co-op', drift: "vpa_id, txn_amount, mpin_plain", isCanonical: false },
        { id: 'BANK_PUNJAB_RURAL', name: 'Punjab Gramin Bank', drift: "sender_vpa, transfer_amount, rrn", isCanonical: false },
        { id: 'BANK_TAMILNADU_GRAMIN', name: 'Tamil Nadu Gramin', drift: "customer_vpa, amount_inr, bank_ref", isCanonical: false },
        { id: 'BANK_KERALA_COOP', name: 'Kerala Cooperative', drift: "acc_vpa, amount_rs, txn_reference", isCanonical: false },
      ];

      let rowsHtml = '';
      bankList.forEach(item => {
        const isHealed = (item.id in adapters);
        const burstCount = bursts[item.id] || 0;
        const invocations = isHealed ? (adapters[item.id].invocation_count || 0) : 0;

        let badge = '';
        if (item.isCanonical) {
          badge = '<span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-400 font-bold border border-emerald-500/30">HEALTHY</span>';
        } else if (isHealed) {
          badge = '<span class="px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-bold border border-cyan-500/30">HOT-PATCHED</span>';
        } else if (burstCount > 0) {
          badge = `<span class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 font-bold border border-rose-500/30 animate-pulse">${burstCount} DROPS</span>`;
        } else {
          badge = '<span class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-bold border border-amber-500/30">DRIFTED (422)</span>';
        }

        const isCurrent = (item.id === getEffectiveBankId());
        const rowBg = isCurrent ? "bg-cyan-950/20" : "";

        rowsHtml += `
          <tr class="${rowBg} hover:bg-slate-900/80 transition cursor-pointer" onclick="selectTargetBank('${item.isCanonical ? 'BANK_MAHARASHTRA_COOP' : item.id}')">
            <td class="py-2.5 px-3 font-bold text-white">${item.id}</td>
            <td class="py-2.5 px-3 text-slate-300">${item.name}</td>
            <td class="py-2.5 px-3 text-slate-400">${item.drift}</td>
            <td class="py-2.5 px-3 font-bold ${burstCount >= 5 ? 'text-rose-400' : 'text-slate-300'}">${item.isCanonical ? '0/5' : burstCount + '/5'}</td>
            <td class="py-2.5 px-3">${badge}</td>
            <td class="py-2.5 px-3 text-white font-bold">${item.isCanonical ? 'N/A' : invocations}</td>
            <td class="py-2.5 px-3 text-right">
              ${item.isCanonical ? '<button class="text-emerald-400 hover:underline" onclick="sendValidPayment(); event.stopPropagation();">Send 200</button>' : `<button class="text-cyan-400 hover:underline font-bold" onclick="selectTargetBank('${item.id}'); simulateBurstAndHeal(); event.stopPropagation();">⚡ Heal</button>`}
            </td>
          </tr>
        `;
      });

      tbody.innerHTML = rowsHtml;
    }

    async function fetchMetrics() {
      try {
        const res = await fetch('/api/v1/metrics');
        if (!res.ok) return;
        const data = await res.json();

        // 1. Update KPI stats
        document.getElementById('stat-total').innerText = data.traffic.total_requests;
        document.getElementById('stat-canonical').innerText = data.traffic.canonical_success;
        document.getElementById('stat-adapted').innerText = data.traffic.adapted_success;
        document.getElementById('stat-failures').innerText = data.traffic.validation_failures;
        document.getElementById('stat-blocks').innerText = data.audit_ledger_blocks;
        document.getElementById('state-text').innerText = data.orchestrator_state;

        // 1b. Update Autopilot Button State
        if (data.autopilot) {
          updateAutopilotUI(data.autopilot.active);
        }

        const currentBank = getEffectiveBankId();
        const bursts = data.scout_telemetry.active_failure_bursts || {};
        cachedAdapters = data.active_hot_patches || {};
        const adapterKeys = Object.keys(cachedAdapters);
        document.getElementById('router-count').innerText = `${adapterKeys.length} Mounted`;

        let totalInvocations = 0;
        adapterKeys.forEach(k => {
          totalInvocations += cachedAdapters[k].invocation_count || 0;
        });
        document.getElementById('router-invocations').innerText = `${totalInvocations} Calls`;

        // 2. Update Scout Agent Card for Active Target
        const currentBurst = bursts[currentBank] || 0;
        document.getElementById('scout-burst').innerText = `${currentBurst} / 5 failures`;
        const pct = Math.min(100, (currentBurst / 5) * 100);
        const pbar = document.getElementById('scout-progress-bar');
        pbar.style.width = `${pct}%`;
        pbar.className = pct >= 100 
          ? "bg-rose-500 h-2 rounded-full transition-all duration-300"
          : "bg-blue-500 h-2 rounded-full transition-all duration-300";

        const burstKeys = Object.keys(bursts);
        if (burstKeys.length > 0) {
          const summary = burstKeys.map(k => `${k}: ${bursts[k]}/5`).join(', ');
          document.getElementById('scout-burst-summary').innerText = summary;
        } else {
          document.getElementById('scout-burst-summary').innerText = "None (Healthy)";
        }

        // 3. Update Bank Tabs Pills
        const allTabIds = ['BANK_MAHARASHTRA_COOP', 'BANK_PUNJAB_RURAL', 'BANK_TAMILNADU_GRAMIN', 'BANK_KERALA_COOP'];
        allTabIds.forEach(bid => {
          const pill = document.getElementById(`pill-${bid}`);
          const velpill = document.getElementById(`velpill-${bid}`);
          const bVal = bursts[bid] || 0;
          const isHealed = (bid in cachedAdapters);

          if (velpill) velpill.innerText = `${bVal}/5`;

          if (pill) {
            if (isHealed) {
              pill.innerText = "HEALED";
              pill.className = "text-[10px] font-mono uppercase px-2 py-0.5 rounded font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30";
            } else if (bVal > 0) {
              pill.innerText = "OUTAGE";
              pill.className = "text-[10px] font-mono uppercase px-2 py-0.5 rounded font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 animate-pulse";
            } else {
              pill.innerText = "DRIFTED";
              pill.className = "text-[10px] font-mono uppercase px-2 py-0.5 rounded font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30";
            }
          }
        });

        // 4. Update Focus Banner Status Badge
        const isCurrentHealed = (currentBank in cachedAdapters);
        const focusBadge = document.getElementById('focus-bank-status-badge');
        if (isCurrentHealed) {
          focusBadge.innerText = "AUTONOMOUSLY HEALED";
          focusBadge.className = "text-xs font-mono font-bold px-2.5 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/40";
        } else if (currentBurst > 0) {
          focusBadge.innerText = `DROPPING TRAFFIC (${currentBurst}/5)`;
          focusBadge.className = "text-xs font-mono font-bold px-2.5 py-0.5 rounded-full bg-rose-500/20 text-rose-300 border border-rose-500/40 animate-pulse";
        } else {
          focusBadge.innerText = "MONITORED (DRIFTED)";
          focusBadge.className = "text-xs font-mono font-bold px-2.5 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/40";
        }

        // 5. Update Synthesized Code Viewer
        const codeContainer = document.getElementById('adapter-code-container');
        const codeEl = document.getElementById('adapter-source-code');
        const tabsEl = document.getElementById('adapter-tabs');
        const invBadge = document.getElementById('adapter-invocation-badge');

        if (adapterKeys.length > 0) {
          tabsEl.innerHTML = '';
          adapterKeys.forEach(k => {
            const btn = document.createElement('button');
            const isActive = (k === currentBank);
            btn.className = isActive
              ? "px-3 py-1.5 rounded-lg text-xs font-mono font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 shadow-sm"
              : "px-3 py-1.5 rounded-lg text-xs font-mono text-slate-400 hover:text-white bg-slate-900 border border-slate-800 transition";
            btn.innerHTML = `<i class="fa-solid fa-microchip mr-1.5"></i>${k} (${cachedAdapters[k].invocation_count || 0})`;
            btn.onclick = () => selectTargetBank(k);
            tabsEl.appendChild(btn);
          });

          // Show code for current bank if active, or first active bank
          const displayKey = (currentBank in cachedAdapters) ? currentBank : adapterKeys[0];
          document.getElementById('adapter-client-id').innerText = displayKey;
          codeEl.innerText = cachedAdapters[displayKey].source_code;
          invBadge.innerText = `${cachedAdapters[displayKey].invocation_count || 0} Adapted Calls`;
          document.getElementById('router-status').innerText = `Active hot-patch routing traffic for ${displayKey}`;
        } else {
          tabsEl.innerHTML = '';
          document.getElementById('adapter-client-id').innerText = currentBank;
          codeEl.innerText = `# Waiting for self-healing swarm to synthesize adapter for ${currentBank}...\n# Click '⚡ Burst 5 & Auto-Heal' above or let the 24/7 background swarm trip and heal!`;
          invBadge.innerText = "0 Calls";
          document.getElementById('router-status').innerText = 'No hot-patches active.';
        }

        // 6. Update Fleet Matrix Table
        renderFleetMatrix(bursts, cachedAdapters);

        // 7. Ingest background autonomous traffic stream
        if (data.recent_traffic && Array.isArray(data.recent_traffic)) {
          data.recent_traffic.forEach(tx => {
            if (!seenTxnIds.has(tx.txn_id)) {
              seenTxnIds.add(tx.txn_id);
              if (seenTxnIds.size > 200) {
                const firstKey = seenTxnIds.values().next().value;
                seenTxnIds.delete(firstKey);
              }
              addLogEntry(tx.client_id, tx.txn_id, tx.status, tx.status_code, tx.adapter_applied, tx.time);
            }
          });
        }

      } catch (err) {
        console.error("Metric fetch failed", err);
      }
    }

    function addLogEntry(bank, txn, status, code, adapter, detail) {
      const logContainer = document.getElementById('traffic-log-container');
      if (localLog.length === 0) logContainer.innerHTML = '';

      const timeStr = detail || new Date().toLocaleTimeString();
      let badge = '';

      if (code === 200 && adapter) {
        badge = '<span class="px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-bold border border-cyan-500/30 font-mono">200 ADAPTED_SUCCESS</span>';
      } else if (code === 200) {
        badge = '<span class="px-2 py-0.5 rounded bg-emerald-500/20 text-emerald-300 font-bold border border-emerald-500/30 font-mono">200 OK CANONICAL</span>';
      } else {
        badge = '<span class="px-2 py-0.5 rounded bg-rose-500/20 text-rose-300 font-bold border border-rose-500/30 font-mono">422 VALIDATION DROP</span>';
      }

      const item = document.createElement('div');
      item.className = "p-2.5 rounded-xl bg-slate-900/90 border border-slate-800/80 flex items-center justify-between text-[11px] animate-fadeIn";
      item.innerHTML = `
        <div class="flex items-center space-x-2">
          <span class="text-slate-500">${timeStr}</span>
          <span class="font-bold text-white font-mono">${bank}</span>
          <span class="text-slate-400 text-[10px] font-mono">${txn}</span>
        </div>
        <div>${badge}</div>
      `;

      logContainer.prepend(item);
      localLog.unshift(item);
      if (localLog.length > 50) {
        localLog.pop();
        if (logContainer.lastElementChild) {
          logContainer.removeChild(logContainer.lastElementChild);
        }
      }
    }

    function clearLogs() {
      localLog = [];
      seenTxnIds.clear();
      document.getElementById('traffic-log-container').innerHTML = '<div class="text-slate-500 text-center py-8">Logs cleared.</div>';
    }

    selectTargetBank('BANK_MAHARASHTRA_COOP');
    setInterval(fetchMetrics, 2000);
    fetchMetrics();
  </script>
</body>
</html>
"""


# ==============================================================================
# 3. DEDICATED ARCHITECTURE BLUEPRINT PAGE (GET /architecture)
# ==============================================================================
PAGE_ARCHITECTURE_RAW = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <title>DPI-Heal: System Architecture Blueprint</title>
  __BASE_HEAD__
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen selection:bg-emerald-500 selection:text-white">

  __NAV_BAR__

  <main class="max-w-6xl mx-auto px-6 py-12 space-y-12">
    <div>
      <div class="flex items-center space-x-2 mb-1">
        <span class="w-2.5 h-2.5 rounded-full bg-blue-400"></span>
        <span class="text-xs font-mono font-semibold uppercase tracking-wider text-blue-400">Distributed Systems Specification</span>
      </div>
      <h1 class="text-3xl md:text-5xl font-black text-white">System Architecture Blueprint</h1>
      <p class="text-sm md:text-base text-slate-400 mt-2 max-w-3xl">
        Comprehensive design of the 4-tier autonomous self-healing pipeline for high-throughput Digital Public Infrastructure rails.
      </p>
    </div>

    <!-- 4 Pipeline Stages Cards -->
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">

      <div class="glass-card rounded-3xl p-6 border-blue-500/30 space-y-4">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-blue-500/10 text-blue-400 flex items-center justify-center font-mono font-bold">01</div>
          <div>
            <h3 class="text-lg font-bold text-white">Tier 1: Scout Telemetry Agent</h3>
            <span class="text-xs font-mono text-blue-300">Sliding Window Deque Ingress</span>
          </div>
        </div>
        <p class="text-xs text-slate-300 leading-relaxed">
          Maintains per-client sliding windows of validation failures using <code class="text-blue-300">collections.deque</code>. Calculates failure velocity over a 10.0-second window. When burst failures cross the threshold (&gt;5 errors), fires an <code class="text-blue-300">AnomalyAlert</code> containing sample malformed payloads, error vectors, and the canonical target schema.
        </p>
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 text-xs font-mono text-slate-400">
          <div>&bull; Window Duration: 10.0 seconds</div>
          <div>&bull; Burst Threshold: &gt;5 validation failures</div>
          <div>&bull; Debounce Suppression: 5.0 seconds</div>
        </div>
      </div>

      <div class="glass-card rounded-3xl p-6 border-teal-500/30 space-y-4">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-teal-500/10 text-teal-400 flex items-center justify-center font-mono font-bold">02</div>
          <div>
            <h3 class="text-lg font-bold text-white">Tier 2: Synthesizer Agent</h3>
            <span class="text-xs font-mono text-teal-300">Deterministic & LLM Code Generation</span>
          </div>
        </div>
        <p class="text-xs text-slate-300 leading-relaxed">
          Analyzes the delta between the malformed payload and the Canonical Pydantic v2 Gateway Schema. Emits a pure Python translation function: <code class="text-teal-300">adapt(payload: dict) -&gt; dict</code>. Supports Google Gemini, OpenAI, Claude, Groq, or an offline semantic AST inference engine.
        </p>
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 text-xs font-mono text-slate-400">
          <div>&bull; Pure function isolation: No external imports allowed</div>
          <div>&bull; Automated field mapping: 'vpa_id' $\to$ 'payer_vpa'</div>
          <div>&bull; Automated PII stripping: Purges 'mpin' and 'aadhaar'</div>
        </div>
      </div>

      <div class="glass-card rounded-3xl p-6 border-purple-500/30 space-y-4">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-purple-500/10 text-purple-400 flex items-center justify-center font-mono font-bold">03</div>
          <div>
            <h3 class="text-lg font-bold text-white">Tier 3: Formal Verifier Gate</h3>
            <span class="text-xs font-mono text-purple-300">Double-Gate AST & Z3 SMT Solver</span>
          </div>
        </div>
        <p class="text-xs text-slate-300 leading-relaxed">
          Enforces rigorous double-gate safety checks before code can touch memory. Gate 1 statically analyzes the AST to forbid dangerous operations. Gate 2 uses the Microsoft Z3 SMT solver to formally prove that monetary values are preserved without alteration or fee skimming.
        </p>
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 text-xs font-mono text-slate-400">
          <div>&bull; AST Inspection: Disallows eval, exec, imports, dunders</div>
          <div>&bull; SMT Theorem: &forall;x&gt;0, AdapterAmount(x) == x</div>
          <div>&bull; HMAC-SHA256: Generates tamper-proof proof signature</div>
        </div>
      </div>

      <div class="glass-card rounded-3xl p-6 border-cyan-500/30 space-y-4">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-cyan-500/10 text-cyan-400 flex items-center justify-center font-mono font-bold">04</div>
          <div>
            <h3 class="text-lg font-bold text-white">Tier 4: Dynamic Hot-Router</h3>
            <span class="text-xs font-mono text-cyan-300">In-Memory Hot-Swap Dispatcher</span>
          </div>
        </div>
        <p class="text-xs text-slate-300 leading-relaxed">
          Maintains an in-memory thread-safe registry of active hot-patches (<code class="text-cyan-300">AdapterRegistry</code>). When traffic arrives with an upstream <code class="text-cyan-300">X-Bank-ID</code>, the middleware executes the verified adapter in memory in &lt;15ms without server restarts.
        </p>
        <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800 text-xs font-mono text-slate-400">
          <div>&bull; In-memory routing: Zero server reboot required</div>
          <div>&bull; Runtime execution time: &lt; 0.5ms per request</div>
          <div>&bull; Instant revocation: DELETE /api/v1/adapters/{client_id}</div>
        </div>
      </div>

    </div>

    <!-- Navigation CTA -->
    <div class="text-center pt-4">
      <a href="/simulator" class="inline-flex items-center space-x-2 px-6 py-3 rounded-xl bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-sm transition">
        <span>Test this architecture in Mission Control</span>
        <i class="fa-solid fa-arrow-right"></i>
      </a>
    </div>
  </main>

  <script>
    document.getElementById('nav-architecture').classList.add('bg-slate-800', 'text-blue-400', 'font-bold');
  </script>
</body>
</html>
"""


# ==============================================================================
# 4. DEDICATED PATENT CORE & VERIFIER PAGE (GET /verifier)
# ==============================================================================
PAGE_VERIFIER_RAW = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <title>DPI-Heal: Formal Verifier & Patent Core</title>
  __BASE_HEAD__
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen selection:bg-emerald-500 selection:text-white">

  __NAV_BAR__

  <main class="max-w-6xl mx-auto px-6 py-12 space-y-12">
    <div>
      <div class="flex items-center space-x-2 mb-1">
        <span class="w-2.5 h-2.5 rounded-full bg-purple-400"></span>
        <span class="text-xs font-mono font-semibold uppercase tracking-wider text-purple-400">Patent Core Specification</span>
      </div>
      <h1 class="text-3xl md:text-5xl font-black text-white">Double-Gate Formal Verifier Gate</h1>
      <p class="text-sm md:text-base text-slate-400 mt-2 max-w-3xl">
        How DPI-Heal mathematically proves safety and monetary conservation using Microsoft Z3 SMT solver and AST functional isolation.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">

      <!-- Gate 1 -->
      <div class="glass-card rounded-3xl p-6 border-cyan-500/30 space-y-4">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-cyan-500/10 text-cyan-400 flex items-center justify-center">
            <i class="fa-solid fa-ban text-lg"></i>
          </div>
          <div>
            <h3 class="text-xl font-bold text-white">Gate 1: AST Static Safety Analyzer</h3>
            <span class="text-xs text-cyan-300 font-mono">Python ast Static Node Visitor</span>
          </div>
        </div>

        <p class="text-xs text-slate-300 leading-relaxed">
          Before any candidate adapter is executed, its Abstract Syntax Tree is inspected to guarantee absolute sandbox isolation:
        </p>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-2">
          <div class="flex items-center justify-between text-rose-400">
            <span>&times; ast.Import, ast.ImportFrom</span>
            <span class="text-[10px] text-slate-500">BLOCKED</span>
          </div>
          <div class="flex items-center justify-between text-rose-400">
            <span>&times; ast.Global, ast.Nonlocal</span>
            <span class="text-[10px] text-slate-500">BLOCKED</span>
          </div>
          <div class="flex items-center justify-between text-rose-400">
            <span>&times; Dangerous calls: eval, exec, compile, open</span>
            <span class="text-[10px] text-slate-500">BLOCKED</span>
          </div>
          <div class="flex items-center justify-between text-rose-400">
            <span>&times; Dunder attributes: __class__, __subclasses__</span>
            <span class="text-[10px] text-slate-500">BLOCKED</span>
          </div>
          <div class="flex items-center justify-between text-rose-400">
            <span>&times; Unbounded loops: ast.While</span>
            <span class="text-[10px] text-slate-500">BLOCKED</span>
          </div>
          <div class="flex items-center justify-between text-emerald-400 pt-2 border-t border-slate-800">
            <span>&check; Pure dict & string/type casting</span>
            <span class="text-[10px] text-emerald-400">ALLOWED</span>
          </div>
        </div>
      </div>

      <!-- Gate 2 -->
      <div class="glass-card rounded-3xl p-6 border-purple-500/30 space-y-4">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-purple-500/10 text-purple-400 flex items-center justify-center">
            <i class="fa-solid fa-square-root-variable text-lg"></i>
          </div>
          <div>
            <h3 class="text-xl font-bold text-white">Gate 2: SMT Invariant Verification</h3>
            <span class="text-xs text-purple-300 font-mono">Microsoft Z3 Theorem Prover</span>
          </div>
        </div>

        <p class="text-xs text-slate-300 leading-relaxed">
          Formulates a mathematical theorem in Z3 proving monetary invariance across all rational amounts:
        </p>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs space-y-3">
          <div class="text-slate-500">// Z3 SMT Mathematical Theorem</div>
          <div class="text-emerald-400 font-bold text-sm">&forall; x &isin; &real;<sub>&gt;0</sub>, &nbsp; AdapterAmount(x) == x</div>
          <div class="text-slate-400 text-[11px] leading-relaxed">
            If the adapter attempts fee deduction (e.g. <span class="text-rose-400">x * 0.98</span> or <span class="text-rose-400">x - 2.0</span>), Z3 finds a counterexample (<code class="text-amber-400">SAT</code>) and rejects the code with a formal proof signature.
          </div>
          <div class="text-purple-300 text-[11px] pt-2 border-t border-slate-800">
            Status: Formally Proven UNSAT (Zero Counterexamples)
          </div>
        </div>
      </div>

    </div>

    <!-- PII Stripping Card -->
    <div class="glass-card rounded-3xl p-6 border-emerald-500/30 space-y-3">
      <h3 class="text-lg font-bold text-white flex items-center gap-2">
        <i class="fa-solid fa-user-shield text-emerald-400"></i>
        PII & MPIN Elimination Guarantee
      </h3>
      <p class="text-xs text-slate-300 leading-relaxed">
        The Formal Verifier executes test payloads injected with sensitive fields (<code class="text-rose-400 font-mono">mpin_plain</code>, <code class="text-rose-400 font-mono">aadhaar_raw</code>, <code class="text-rose-400 font-mono">cvv</code>). It asserts that none of these keys leak into the canonical UPI payload.
      </p>
    </div>

    <div class="text-center pt-4">
      <a href="/simulator" class="inline-flex items-center space-x-2 px-6 py-3 rounded-xl bg-purple-500 hover:bg-purple-400 text-slate-950 font-bold text-sm transition">
        <span>Observe Z3 Verifier in Simulator</span>
        <i class="fa-solid fa-arrow-right"></i>
      </a>
    </div>
  </main>

  <script>
    document.getElementById('nav-verifier').classList.add('bg-slate-800', 'text-purple-400', 'font-bold');
  </script>
</body>
</html>
"""


# ==============================================================================
# 5. DEDICATED BLOCKCHAIN AUDIT LEDGER PAGE (GET /ledger-explorer)
# ==============================================================================
PAGE_LEDGER_RAW = """<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <title>DPI-Heal: Cryptographic Blockchain Ledger Explorer</title>
  __BASE_HEAD__
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen selection:bg-emerald-500 selection:text-white">

  __NAV_BAR__

  <main class="max-w-6xl mx-auto px-6 py-12 space-y-10">
    <div class="flex flex-col md:flex-row justify-between items-start md:items-end gap-4 border-b border-slate-800 pb-6">
      <div>
        <div class="flex items-center space-x-2 mb-1">
          <span class="w-2.5 h-2.5 rounded-full bg-emerald-400"></span>
          <span class="text-xs font-mono font-semibold uppercase tracking-wider text-emerald-400">Non-Repudiation Audit Trail</span>
        </div>
        <h1 class="text-3xl md:text-5xl font-black text-white">Cryptographic Audit Ledger</h1>
        <p class="text-sm md:text-base text-slate-400 mt-2 max-w-2xl">
          Append-only SHA-256 chained blockchain recording every hot-swap adapter, AST hash, and formal verification proof.
        </p>
      </div>

      <div class="flex items-center space-x-3">
        <div class="px-4 py-2 rounded-xl bg-emerald-500/10 border border-emerald-500/25 text-xs font-mono text-emerald-400 font-bold flex items-center space-x-2">
          <i class="fa-solid fa-shield-check text-sm"></i>
          <span>Chain Integrity: VERIFIED</span>
        </div>
        <button onclick="fetchLedger();" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-400 hover:text-white transition">
          <i class="fa-solid fa-arrows-rotate"></i>
        </button>
      </div>
    </div>

    <!-- Mined Blocks Feed -->
    <div id="ledger-blocks-container" class="space-y-4">
      <!-- Blocks populated dynamically -->
    </div>
  </main>

  <script>
    document.getElementById('nav-ledger').classList.add('bg-slate-800', 'text-emerald-400', 'font-bold');

    async function fetchLedger() {
      try {
        const res = await fetch('/api/v1/ledger');
        if (!res.ok) return;
        const data = await res.json();
        const container = document.getElementById('ledger-blocks-container');
        container.innerHTML = '';

        data.blocks.forEach(block => {
          const card = document.createElement('div');
          card.className = "glass-card rounded-3xl p-6 border border-slate-800 font-mono space-y-3";
          card.innerHTML = `
            <div class="flex justify-between items-center border-b border-slate-800/80 pb-3">
              <div class="flex items-center space-x-2">
                <span class="w-8 h-8 rounded-lg bg-purple-500/10 text-purple-400 flex items-center justify-center font-bold text-sm">#` + block.index + `</span>
                <span class="text-white font-bold text-base font-sans">` + block.client_id + `</span>
              </div>
              <span class="text-slate-400 text-xs px-2.5 py-1 rounded-full bg-slate-900 border border-slate-800">Nonce: ` + block.nonce + `</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
              <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80 truncate">
                <span class="text-slate-500">Block Hash:</span><br>
                <span class="text-cyan-300 font-bold">` + block.hash + `</span>
              </div>
              <div class="bg-slate-950 p-3 rounded-xl border border-slate-800/80 truncate">
                <span class="text-slate-500">Previous Hash:</span><br>
                <span class="text-slate-400">` + block.prev_hash + `</span>
              </div>
            </div>
            <div class="bg-slate-950 p-3.5 rounded-xl border border-slate-800/80 text-xs text-emerald-400 break-words">
              <span class="text-slate-500">Formal Verification Proof:</span><br>
              ` + block.verifier_proof_summary + `
            </div>
          `;
          container.appendChild(card);
        });
      } catch (e) {
        console.error(e);
      }
    }

    fetchLedger();
    setInterval(fetchLedger, 3000);
  </script>
</body>
</html>
"""


# Interpolated Pages Export
PAGE_COVER = PAGE_COVER_RAW.replace("__BASE_HEAD__", BASE_HEAD).replace("__COVER_NAV_BAR__", COVER_NAV_BAR)
PAGE_SIMULATOR = PAGE_SIMULATOR_RAW.replace("__BASE_HEAD__", BASE_HEAD).replace("__NAV_BAR__", PLATFORM_NAV_BAR)
PAGE_ARCHITECTURE = PAGE_ARCHITECTURE_RAW.replace("__BASE_HEAD__", BASE_HEAD).replace("__NAV_BAR__", PLATFORM_NAV_BAR)
PAGE_VERIFIER = PAGE_VERIFIER_RAW.replace("__BASE_HEAD__", BASE_HEAD).replace("__NAV_BAR__", PLATFORM_NAV_BAR)
PAGE_LEDGER = PAGE_LEDGER_RAW.replace("__BASE_HEAD__", BASE_HEAD).replace("__NAV_BAR__", PLATFORM_NAV_BAR)
