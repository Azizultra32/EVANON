// Frame-accurate recorder for the editorial motion piece.
const { chromium } = require('playwright');
const { spawnSync } = require('child_process');
const fs = require('fs'); const path = require('path');
const FF = require('ffmpeg-static');

(async () => {
  const FPS = Number(process.env.FPS) || 30;
  const url = 'file://' + path.join(process.cwd(), 'motion.html');
  const tmp = fs.mkdtempSync(path.join(process.cwd(), '.video-tmp-'));
  const out = process.argv[2] || 'out/housecall-editorial.mp4';
  fs.mkdirSync(path.dirname(out), { recursive: true });

  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
  await p.goto(url);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForFunction(() => window.__ready === true);
  await p.evaluate(() => { window.__recording = true; });
  await p.waitForTimeout(500);

  const DURATION = await p.evaluate(() => window.DURATION);
  const frames = Math.round(DURATION * FPS);
  for (let i = 0; i < frames; i++) {
    await p.evaluate((t) => window.__seek(t), i / FPS);
    await p.screenshot({ path: path.join(tmp, String(i).padStart(5, '0') + '.png') });
  }
  await b.close();

  const r = spawnSync(FF, ['-y', '-framerate', String(FPS), '-i', path.join(tmp, '%05d.png'),
    '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '17', '-preset', 'slow',
    '-movflags', '+faststart', out], { stdio: 'inherit' });
  fs.rmSync(tmp, { recursive: true, force: true });
  if (r.status !== 0) process.exit(r.status || 1);
  console.log('wrote', out, `(${frames} frames @ ${FPS}fps)`);
})();
