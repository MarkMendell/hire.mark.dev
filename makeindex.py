import collections, json, re, sys
sys.stdout = open("index.html", "w")

print('''<!doctype html>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
	background-color: #fefae0;
	color: #283618;
	font-family: -apple-system, BlinkMacSystemFont, avenir next, avenir, segoe ui, helvetica neue, helvetica, Cantarell, Ubuntu, roboto, noto, arial, sans-serif;;
	margin: 0 auto;
	max-width: 800px;
	padding: 0 16px 80px 16px;
}

h2 {
	color: #bc6c25;
}

#hi {
	margin-top: 16px;
}

@media (max-width: 550px) {
#hi {
	margin-bottom: 12px;
}}

@media (min-width: 550px) {
#hi {
	padding: 32px;
}}

#firstpair {
	display: flex;
}

@media (max-width: 660px) {
#firstpair {
	flex-direction: column;
}}

@media (min-width: 660px) {
#firstpair {
	align-items: center;
}}

#picme {
	align-self: center;
	border-radius: 16px;
	max-height: 200px;
}

@media (min-width: 660px) {
#picme {
	margin-right: 24px;
}}

#greeting {
	color: #222222;
	font-size: 32px;
	font-weight: bold;
}

@media (max-width: 660px) {
#greeting {
	margin-top: 24px;
	text-align: center;
}}

#toolbar {
	align-items: center;
	display: flex;
}

@media (max-width: 660px) {
#toolbar {
	justify-content: center;
}}

.pitch {
	font-size: 18px;
	line-height: 1.3;
}

.dash {
	/*border: 1px dotted black;*/
			background-image: linear-gradient(to right, #bc6c25 50%, rgba(255,255,255,0) 0%);
background-position: left bottom;
background-size: 16px 1px;
background-repeat: repeat-x;
			height: 6px;

	flex-grow: 1;
	margin: 0 16px;
	min-width: 80px;
	opacity: 0.3;
}

@media (max-width: 550px) {
.dash {
	display: none;
}}

.tech {
	font-weight: 500;
	opacity: 0.7;
	color: #bc6c25;
}

a {
	color: #606c38;
}

.licon {
	transition: opacity 0.3s;
}

.licon:hover {
	opacity: 0.4;
}

.licon:not(:first-child) {
	margin-left: 12px;
}

.pic {
	border-radius: 8px;
	box-shadow: rgba(149,157,165,0.2) 0px 8px 24px;
 	display: block;
 	margin: 16px auto;
 	max-height: 400px;
 	max-width: 100%;
	transition: box-shadow 0.3s;
}

.pic:hover {
	box-shadow: rgba(149,157,165,0.5) 0px 8px 24px;
}

.hproj {
	display: flex;
	margin-bottom: 4px;
}

@media (max-width: 550px) {
.hproj {
	flex-direction: column;
}}

@media (min-width: 550px) {
.hproj {
	align-items: center;
}}
</style>
<div id="hi">
	<div id="firstpair" style="">
		<img id="picme" src="1644558965003.jpg">
		<div>
			<div id="greeting">Hi, I’m Mark!</div>
			<span class="pitch">
				<p>I'm an expert at every layer of the web stack:
				<ul>
					<li>TLS cryptography algorithms in C</li>
					<li>deploying networked Linux VPSs</li>
					<li>Python/Go/JS/C routes and SQL databases</li>
					<li>custom HTML video players with canvas</li>
					<li>TypeScript/React components</li>
				</ul>
			</span>
		</div>
	</div>
	<span class="pitch">
		<p>I've worked with Duolingo, Indeed, Thumbtack, and more on products used by millions of users.
		<p>I've also built native cross-platform apps for macOS, Windows, Android, and iOS, and done graphics programming in Vulkan, Direct3D, and Metal.
		<p>After graduating CMU and doing my rounds of the big tech companies, I found I could best leverage my agency working as an independent consultant. My strength lies in an empathetic approach to existing codebases and a love of simplicity and performance.
	</span>
	<div id="toolbar" style="">
		<a class="licon" href="mailto:hire@mark.dev">hire@mark.dev</a>
		<a class="licon" href="https://x.com/markdotdev" target="_blank"><svg width="15" height="15" viewbox="0 0 300 300" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M178.57 127.15 290.27 0h-26.46l-97.03 110.38L89.34 0H0l117.13 166.93L0 300.25h26.46l102.4-116.59 81.8 116.59h89.34M36.01 19.54H76.66l187.13 262.13h-40.66"/></svg></a>
		<a class="licon" href="https://github.com/markmendell" target="_blank"><svg width="18" height="18" viewBox="0 0 64 64" id="i-github" xmlns="http://www.w3.org/2000/svg"> <path stroke-width="0" fill="#000000" d="M32 0 C14 0 0 14 0 32 0 53 19 62 22 62 24 62 24 61 24 60 L24 55 C17 57 14 53 13 50 13 50 13 49 11 47 10 46 6 44 10 44 13 44 15 48 15 48 18 52 22 51 24 50 24 48 26 46 26 46 18 45 12 42 12 31 12 27 13 24 15 22 15 22 13 18 15 13 15 13 20 13 24 17 27 15 37 15 40 17 44 13 49 13 49 13 51 20 49 22 49 22 51 24 52 27 52 31 52 42 45 45 38 46 39 47 40 49 40 52 L40 60 C40 61 40 62 42 62 45 62 64 53 64 32 64 14 50 0 32 0 Z" /></svg></a>
	</div>
</div>
<div style="background-color:#fffcec; border-radius:16px; box-shadow:rgba(149,157,165,0.2) 0px 8px 24px; display:flex; margin-top:32px; padding:12px 24px">
	<svg xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd" viewBox="0 0 512 379.51" width="16" height="16" style="flex-shrink:0; opacity:0.5"><path d="M212.27 33.98C131.02 56.52 78.14 103.65 64.99 185.67c-3.58 22.32 1.42 5.46 16.55-5.86 49.4-36.96 146.53-23.88 160.01 60.56 27.12 149.48-159.79 175.36-215.11 92.8-12.87-19.19-21.39-41.59-24.46-66.19C-11.35 159.99 43.48 64.7 139.8 19.94c17.82-8.28 36.6-14.76 56.81-19.51 10.12-2.05 17.47 3.46 20.86 12.77 2.87 7.95 3.85 16.72-5.2 20.78zm267.78 0c-81.25 22.54-134.14 69.67-147.28 151.69-3.58 22.32 1.42 5.46 16.55-5.86 49.4-36.96 146.53-23.88 160 60.56 27.13 149.48-159.78 175.36-215.1 92.8-12.87-19.19-21.39-41.59-24.46-66.19C256.43 159.99 311.25 64.7 407.58 19.94 425.4 11.66 444.17 5.18 464.39.43c10.12-2.05 17.47 3.46 20.86 12.77 2.87 7.95 3.85 16.72-5.2 20.78z"/></svg>
	<blockquote style="font-style:italic; margin:14px">
		Mark is an incredibly talented and efficient engineer. He has impeccable craft and can build sites at a very high bar at impressive speeds. He helped me bring my design portfolio to life, creating custom media controls, implementing unique transitions and more. What I love the most about Mark is his attention to detail. He will go the extra mile to get it perfect. He is a product designer's dream to work with!
		<footer style="margin-left:8px; margin-top:4px">
			-
			<a class="licon" href="https://www.linkedin.com/in/ademler/" target="_blank">Aya Demler</a>
		</footer>
	</blockquote>
	<svg xmlns="http://www.w3.org/2000/svg" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd" viewBox="0 0 512 379.51" width="16" height="16" style="flex-shrink:0; opacity:0.5; transform:rotate(180deg)"><path d="M212.27 33.98C131.02 56.52 78.14 103.65 64.99 185.67c-3.58 22.32 1.42 5.46 16.55-5.86 49.4-36.96 146.53-23.88 160.01 60.56 27.12 149.48-159.79 175.36-215.11 92.8-12.87-19.19-21.39-41.59-24.46-66.19C-11.35 159.99 43.48 64.7 139.8 19.94c17.82-8.28 36.6-14.76 56.81-19.51 10.12-2.05 17.47 3.46 20.86 12.77 2.87 7.95 3.85 16.72-5.2 20.78zm267.78 0c-81.25 22.54-134.14 69.67-147.28 151.69-3.58 22.32 1.42 5.46 16.55-5.86 49.4-36.96 146.53-23.88 160 60.56 27.13 149.48-159.78 175.36-215.1 92.8-12.87-19.19-21.39-41.59-24.46-66.19C256.43 159.99 311.25 64.7 407.58 19.94 425.4 11.66 444.17 5.18 464.39.43c10.12-2.05 17.47 3.46 20.86 12.77 2.87 7.95 3.85 16.72-5.2 20.78z"/></svg>
</div>''')

Work = collections.namedtuple('Work', ['title','tech','brief','desc','image'])
works = [
	Work(
		'Duolingo Plus Web',
		'React, Python, Stripe',
		'Web version of Duolingo subscription',
		'Implemented web frontend based on design. Architected and built Python backend with Stripe integration for subscription management.',
		'duo.png',
	),
	Work(
		"ayademler.com",
		"JS, HTML, sh, ffmpeg, Cloudflare",
		"Designer portfolio site with custom chunked video player",
		"Implemented web frontend based on design. Created novel canvas-based video player with custom prefetching algorithm for instant video loads. Set up Cloudflare pages site for free hosting.",
		"aya.png"
	),
	Work(
		"Pebblestream",
		"Clojure, Java, C#",
		"Compiler and runtime for high-performance Excel spreadsheet computing",
		"Optimized and extended compiler and runtime to enable a \"Big Four\" accounting firm to run one billion tax computations every month while retaining their core logic in Excel spreadsheets.",
		"pebblestream.png"
	),
	Work(
		"Mobile phone code editor",
		"Android, iOS, C, Vulkan, Metal",
		"Code editor / IDE with novel features for mobile phone",
		"Designed and built from scratch a cross-platform app using a C native library, rendering directly to a Vulkan/Metal surface, including custom text layout and rendering, autocorrect, and code formatting.",
		"mobilecode.png"
	),
	Work(
		"Custom code diff resolver",
		"C, macOS, Metal, diff algorithms",
		"Mac program to interactively diff code files",
		"Researched and implemented a novel diff algorithm from scratch to allow parallel independent development of similar codebases (e.g. two platforms of the same program) without constraining them to a shared interface library.",
		"synctool.png"
	),
	Work(
		"Webassembly debugger for Chrome",
		"C, JS, DWARF, Windows",
		"DWARF web assembly debugger",
		"After feeling frustration with Chrome’s webassembly debugger, I wrote a new one from scratch with instant stepping, communicating with Chrome over the Chrome DevTools Protocol.",
		"cwasmdbg.png"
	),
	Work(
		"TLS 1.2 Server",
		"C, cryptography",
		"From scratch TLS server, no openssl etc",
		"Implemented a TLS 1.2 server that was successfully used to host a HTTPS site from scratch without the use of existing libraries (such as for RSA signing).",
		"tls12wshark.png"
	),
	Work(
		"SSH with SFTP basic client",
		"C, SSH",
		"SSH and SFTP client from scratch",
		"Implemented a minimal SSH client without libraries which could also use SFTP to get and set files from a VPS.",
		"connectssh.png"
	),
	Work(
		"Browser automation for bank data",
		"C, Chrome DevTools Protocol",
		"Automatic bank logins and data download",
		"Wrote a windows program which connected to chrome via Chrome DevTools Protocol and automated the login and transaction downloading of five different websites.",
		"automate.png"
	),
	Work(
		"PDF renderer with Excel formulas in the browser",
		"JS, HTML, PDF, Canvas",
		None,
		"Wrote a web program for doing my own taxes that would parse tax form PDFs without a library, render them into an HTML canvas, and allow entering values that referenced other values in the form.",
		"tax.png"
	),
	Work(
		"Financial simulator in the browser",
		"JS, C, WebSockets, HTML",
		None,
		"Wrote a web program which simulates arbitrary financial events defined via Excel-esque formulas. Live sync across multiple users.",
		"moneylife.png"
	),
	Work(
		"AI Copilot for the shell",
		"C",
		"Wraps shell programs to give AI completions",
		"Created a program which wraps standard input and output of a program to offer GitHub Copilot-powered autocomplete suggestions transparently while typing input to the program.",
		"cpwrap.png"
	),
	Work(
		"WebGL expense organizer",
		"JS, C, WebGL",
		None,
		"Made a tool in C compiled to WebAssembly which runs in the browser via WebGL. It shows a series of expenses, waits for the user to tap the category they belong to, and finally syncs to a server for further processing.",
		"spendee.png"
	),
	Work(
		"JSON viewer with transparency",
		"C, Windows",
		None,
		"Made a program which listens for a global keyboard shortcut and displays the copied JSON in an interactive viewer. The viewer is transparent apart from the content and sticks to the top of the screen for easy use while debugging.",
		"json.png"
	),
	Work(
		"Windows remote file system (projected)",
		"C, Windows",
		None,
		"Made a Windows daemon which talks to a TCP server and presents a file from that server as a regular file via ProjFS.",
		"proj.png"
	)
]

for w in works:
	print(f'''<div style="margin:64px 0">
	<div class="hproj">
		<h2 style="margin:0">{w.title}</h2>
		<div class="dash"></div>
		<span class="tech">{w.tech}</span>
	</div>''')
	if w.brief:
			print(f'''	<div style="color:#606c38; font-style:italic; font-size:13px; opacity:0.7">{w.brief}</div>''')
	print(f'''	<div style="line-height:1.3; margin-top:12px">{w.desc}</div>
	<a href="{w.image}" target="_blank">
		<img class="pic" loading="lazy" src="{w.image or "https://placehold.co/1000x800"}">
	</a>
</div>''')

print('''<span>Education: Bachelor's of Computer Science and Arts at Carnegie Mellon University</span>''')
