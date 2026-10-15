"""Thử 1 đề trong Chromium (1280px và 390px): khoá/mở bài mẫu, chọn hết đáp án đúng -> 20/20,
popup từ vựng, tràn ngang, lỗi JS, nút Nộp bài (chặn docs.google.com, không có dòng nào vào sheet của cô).
    python3 test.py <thư mục ielts-table> T01 [thư mục lưu ảnh chụp]
"""
import json, sys, re
from playwright.sync_api import sync_playwright
site, lid = sys.argv[1], sys.argv[2]
out = sys.argv[3] if len(sys.argv) > 3 else "/tmp"
d = json.load(open(f"{site}/_tools/lessons/{lid}.json"))
posts = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in (1280, 390):
        pg = b.new_page(viewport={"width": w, "height": 900})
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.route("**/docs.google.com/**", lambda r: (posts.append(r.request.post_data), r.fulfill(status=200, body="ok")))
        pg.route("**/fonts.g*/**", lambda r: r.abort())
        pg.goto(f"file://{site}/{lid}.html")
        assert pg.locator("section.part:visible").count() == 3, "only parts 1-3 visible before unlock"
        assert pg.locator("#gate").is_visible()
        pg.fill("#stuName", "Test HS"); pg.select_option("#stuClass", "IELTS")
        # answer correctly: buttons via data, selects via answer index
        n = 0
        for pi, part in enumerate(d["parts"]):
            if pi == 3:
                assert pg.locator("section.part:visible").count() == 6, "unlocked"
                assert pg.locator("#unlockMsg").is_visible()
            if part["type"] == "questions":
                for q in part["questions"]:
                    n += 1
                    correct = q["options"][0]
                    btns = pg.locator(f"#q{n} .opt")
                    for k in range(btns.count()):
                        txt = btns.nth(k).locator("span").nth(1).inner_text()
                        if txt == re.sub(r"\*\*?([^*]+)\*\*?", r"\1", correct):
                            btns.nth(k).click(); break
                    else:
                        raise SystemExit(f"q{n} option not found")
            else:
                for it in part["items"]:
                    n += 1
                    pg.select_option(f"#q{n} .sel", str(it["answer"]))
        score = pg.inner_text("#bigScore")
        overflow = pg.evaluate("document.documentElement.scrollWidth > document.documentElement.clientWidth")
        # sample tab visible & popup
        if w == 390:
            pg.click("#fab"); pg.wait_for_timeout(200)
            box = "#drawerBody"
        else:
            box = "#reading"
        tab_txt = pg.inner_text(box)
        pg.locator(f"{box} .w").first.click(); pop = pg.is_visible("#pop")
        pg.screenshot(path=f"{out}/shot_{lid}_{w}.png")
        if w == 390: pg.click("#closeDr")
        pg.click("#btnSubmit"); pg.wait_for_timeout(500)
        st = pg.inner_text("#sendStatus")
        print(w, "score", score.replace("\n",""), "overflow", overflow, "pop", pop, "sample", "Bài mẫu" in tab_txt, "status", st, "errors", errs)
        # task tab table screenshot
        pg.evaluate("window.scrollTo(0,0)")
        if w==1280:
            pg.click("#reading .tab[data-tab=task]"); pg.screenshot(path=f"{out}/shot_{lid}_task.png")
    b.close()
print("posts", len(posts), posts[0][:300] if posts else None)
