const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const base = 'C:\\Users\\nswcl\\.gemini\\antigravity-ide\\scratch\\the-floor-that-does-not-rise';

// Copy ledgers
fs.copyFileSync(path.join(base, 'metadata', 'source_ledger.csv'), path.join(base, 'outputs', 'source_ledger_final.csv'));
fs.copyFileSync(path.join(base, 'metadata', 'checksum_manifest.csv'), path.join(base, 'outputs', 'checksum_manifest_final.csv'));
console.log('Final ledgers copied.');

// Generate PDF via Chrome
const chromeCandidates = [
  'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
  'C:\\Users\\nswcl\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
];

let chromePath = chromeCandidates.find(p => fs.existsSync(p));
if (chromePath) {
  const htmlPath = path.join(base, 'outputs', 'research_data_audit.html');
  const pdfPath = path.join(base, 'outputs', 'research_data_audit.pdf');
  const cmd = `"${chromePath}" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf="${pdfPath}" "${htmlPath}"`;
  console.log('Executing Chrome PDF conversion...');
  try {
    execSync(cmd, { stdio: 'inherit' });
    if (fs.existsSync(pdfPath)) {
      console.log('PDF Generated successfully! Size:', fs.statSync(pdfPath).size, 'bytes');
    }
  } catch (err) {
    console.error('Chrome PDF error:', err.message);
  }
} else {
  console.log('Chrome binary not found at candidate paths.');
}
