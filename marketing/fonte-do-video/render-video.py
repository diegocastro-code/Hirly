import sys, os, subprocess
from playwright.sync_api import sync_playwright

HTML = "file://" + os.path.abspath(os.path.join(os.path.dirname(__file__), "comercial.html"))
OUT = os.path.join(os.path.dirname(__file__), "out")
os.makedirs(OUT, exist_ok=True)
FPS = 30
SCENES = [(0, 4), (4, 7.2), (7.2, 13), (13, 16.2), (16.2, 19.5), (19.5, 23)]


def page_ctx(p):
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--force-color-profile=srgb"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920}, device_scale_factor=1)
    pg.goto(HTML)
    pg.wait_for_timeout(500)
    return b, pg


def stills(times):
    with sync_playwright() as p:
        b, pg = page_ctx(p)
        for t in times:
            pg.evaluate(f"setTime({t})")
            pg.screenshot(path=f"{OUT}/still_{t:05.2f}.jpg", type="jpeg", quality=92)
        b.close()


def scene(pg, i, a, z):
    tmp = f"{OUT}/scene{i}.tmp.mp4"
    final = f"{OUT}/scene{i}.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
                           "-c:v", "mjpeg", "-i", "-", "-c:v", "libx264", "-crf", "18", "-preset", "veryfast",
                           "-pix_fmt", "yuv420p", "-r", str(FPS), tmp], stdin=subprocess.PIPE)
    n = round((z - a) * FPS)
    for k in range(n):
        t = a + k / FPS
        pg.evaluate(f"setTime({t})")
        ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
    ff.stdin.close()
    if ff.wait() == 0:
        os.rename(tmp, final)
    else:
        raise SystemExit(f"scene {i} failed")


def full(which):
    with sync_playwright() as p:
        b, pg = page_ctx(p)
        for i in which:
            scene(pg, i, *SCENES[i])
            print("scene", i, "ok", flush=True)
        b.close()
    with open(f"{OUT}/list.txt", "w") as f:
        for i in range(len(SCENES)):
            f.write(f"file 'scene{i}.mp4'\n")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", f"{OUT}/list.txt",
                    "-c", "copy", "-movflags", "+faststart", f"{OUT}/hirly_comercial.mp4"], check=True)


if __name__ == "__main__":
    if sys.argv[1] == "stills":
        stills([float(x) for x in sys.argv[2:]])
    else:
        full([int(x) for x in sys.argv[2:]] or range(len(SCENES)))
