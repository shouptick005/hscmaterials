// Replace pandoc's <span class="math inline|display">TeX</span> with KaTeX HTML.
// Usage: node katex_render.mjs < in.html > out.html
import { createRequire } from "module";
import { readFileSync } from "fs";
import os from "os";

const require = createRequire(import.meta.url);
const katex = require(os.homedir() + "/.local/share/hsc-tools/node_modules/katex");

const unescape = (s) =>
  s.replace(/&lt;/g, "<").replace(/&gt;/g, ">").replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&amp;/g, "&");

const html = readFileSync(0, "utf8");
let errors = 0;
const out = html.replace(
  /<span\s+class="math (inline|display)">([\s\S]*?)<\/span>/g,
  (_, mode, tex) => {
    try {
      return katex.renderToString(unescape(tex), { displayMode: mode === "display", throwOnError: true });
    } catch (e) {
      errors++;
      process.stderr.write(`KaTeX error: ${e.message}\n`);
      return `<span class="math-error">${tex}</span>`;
    }
  }
);
process.stdout.write(out);
process.exitCode = errors ? 1 : 0;
