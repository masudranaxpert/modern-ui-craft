"""Batch 2 (2026-09-30): organize 62 inbox images + update all category READMEs."""
import os, json, shutil, re

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "Galary")
GAL = os.path.join(BASE, "gallery")

# n: (folder, slug, pattern, palette, layout, note)
E = {
 1:("mobile/onboarding","mindpop-food-donation-2scr","Onboarding splash + value card (MindPop)","white + mint green blobs + black pill CTA","2scr: logo splash -> illustrated value card with black CTA","FB post embed — crop chrome before use"),
 2:("mobile/productivity","construction-site-tracking-3scr","Construction PM app (UI Lerner)","light + orange dominant cards + white","3scr: orange stat cards -> project list -> safety checklist rows","FB post embed"),
 3:("mobile/fitness","daily-reflection-wellness","Wellness daily reflection (Hassan Idris)","cream + green ring + soft pastel tiles","big 88% recovery ring hero + mood tiles + activity rows","FB post embed"),
 4:("_rejected_inbox","kit-collage-dark-dashboards","UI-kit promo collage","dark, multi-hue","mini dashboard collage","JUNK: collage, per-screen anatomy unreadable"),
 5:("_rejected_inbox","kit-collage-light-dashboards","UI-kit promo collage","light, multi-hue","mini dashboard collage","JUNK: collage, per-screen anatomy unreadable"),
 6:("mobile/productivity","ai-squad-assistant-3scr","AI assistant app (Ai-Squad)","light + amber hero + gray body","home w/ amber banner -> AI chat thread -> discover/template grid",""),
 7:("web/settings","mailbox-settings-modal","Mailbox settings modal","white modal on gray + violet Upgrade CTA","modal: tab row (General/Sync/Signature/Tracking/Sending) + dropdown + Cancel/Upgrade",""),
 8:("components","upcoming-followups-card","Upcoming-this-week list card","white card + gray text + outline buttons","avatar rows + due dates + Resolve outline buttons",""),
 9:("techniques","screen-spec-android-ios","Android vs iOS screen spec (Codi)","light diagram + green/teal labels","safe areas, app/tab bar zones, 4-col grid, gutter/margin values",""),
 10:("mobile/productivity","habi-calendar-events-6scr","Calendar + events app (Habi)","white + amber/orange accents","6scr: quick actions -> all events -> month view -> agenda -> detail -> create form",""),
 11:("components","member-status-card","Member status card","white + green/amber/gray dot rows","status rows with counts + share % right-aligned",""),
 12:("components","invoice-history-table","Invoice history table","white + green/amber/red status pills","date/plan/status/amount columns + PDF action links",""),
 13:("_rejected_inbox","zoom-desk-photo","Desk photo on Zoom call","n/a","person presenting, monitor photo","JUNK: not a UI reference"),
 14:("mobile/health","dr-jessica-telehealth-3scr","Telehealth booking + consult (Dr. Jessica)","pastel pink-lavender wash + white cards + black pill CTA","3scr: doctor profile w/ recovery ring -> booking calendar+time pills -> video consult chat",""),
 15:("components","status-pill-set-animated","Status pill specimen (8 states)","pastel fills (violet/blue/amber/red/green/cyan) + dark text","Queued/Scheduled/InProgress/HighPriority/Ready/Waiting/Paused/Reviewing pills","FB post embed"),
 16:("mobile/ecommerce","food-delivery-ab-compare","Food delivery A/B (DevDsgn)","A: dark-green rich cards; B: white + orange CTAs","2 variants side-by-side: density+info vs focus+fewer choices","TWO references in one image"),
 17:("techniques","border-radius-concentric","Concentric border radius rule","white diagram + orange/green arrows","outer R = inner R + padding; multiplier method for nested frames",""),
 18:("web/dashboard","agent-workflow-builder-modal","No-code agent workflow builder","light gray canvas + white nodes + dark left rail","node-graph canvas + step config modal + left rail w/ flows",""),
 19:("mobile/finance","human-car-prepurchase-3scr","Car pre-purchase check (HUMAN)","white + blue accents + black car hero","3scr: listing search -> Porsche 911 detail hero -> cost breakdown donut + leasing CTA",""),
 20:("web/landing","unvest-investing-collage","Investing landing collage (Unvest)","cream/beige + green buttons + dark banner","hero + feature cards + security strip + dark join banner + portfolio cards",""),
 21:("mobile/ecommerce","sneaker-store-cart-2scr","Sneaker store browse + cart","white + soft blue product tiles + black CTA","2scr: category grid w/ ratings -> cart w/ promo + black continue",""),
 22:("mobile/health","ai-fitness-compare-3tools","Fitness tracker, 3 AI variants","white + green ring accent + gray","compare: calorie ring 1,240 + macros + meal tiles + bottom pill nav","3 prompt outputs of same brief — style-compare reference"),
 23:("web/dashboard","fundora-transaction-detail","Transaction detail page (Fundora)","light + blue links + green paid banner","$35k paid banner + applied-timeline + details/verification sidebar",""),
 24:("components","account-menu-popover","Account menu popover","white + gray rows + bar meters","settings/language/docs rows + models list w/ usage meters",""),
 25:("web/dashboard","progflow-goals-qa","Goals + QA dashboard (ProgFlow)","light + green progress + gray body","94% goal progress + member goal rows + milestone bars + filter chips",""),
 26:("components","agent-activity-feed","Agentic run feed","white + green JSON syntax + gray rows","tool-run rows (commands, edits) + expandable JSON result",""),
 27:("components","agent-task-cards","Agent task cards","white + green/amber status chips","Completed/Running chips + task title + role + time meta",""),
 28:("web/dashboard","ats-candidate-kanban","ATS candidate kanban","light + blue links + purple upgrade btn","job header w/ meta chips + candidate columns + filter bar",""),
 29:("web/dashboard","options-trading-analytics","Options trading analytics (Prometheus)","light + blue/purple heatmaps + multicolor charts","option chain table + premium charts + call/put heatmap matrices",""),
 30:("web/dashboard","orbit-marketing-overview","Marketing overview (Orbit)","light + orange CTA + pastel charts","greeting + 4 KPI cards + area chart + traffic donut + campaigns table",""),
 31:("components","health-score-gauges","Health score gauges","white + green ring + striped bar","84% ring gauge + 72% striped progress bar pair","cropped fragment"),
 32:("components","task-cards-tags","Task cards w/ tags","white + lavender banner + icon chips","In-Progress header + task rows w/ ID + tag chips + avatars",""),
 33:("components","rituals-sidebar-specimen","Sidebar nav specimen (Cadence)","white + red New badge + blue progress","pill nav w/ views + ritual list + stat header w/ delta","cropped fragment"),
 34:("mobile/education","faith-daily-verse-6scr","Faith/verse learning app","cream + deep green + illustration","6scr: illustrated verse cards -> quiz -> poll -> streak stats",""),
 35:("mobile/onboarding","bloom-habit-onboarding-6scr","Habit app onboarding (Bloom)","white + ink mascot + black CTA","6scr: name -> focus select -> reminders -> permissions -> paywall $5/mo",""),
 36:("_rejected_inbox","portfolio-banner-ashutosh","Portfolio banner over landscape art","illustration + white text block","name + stack over painted landscape","JUNK: banner, no UI anatomy"),
 37:("web/landing","portfolio-hero-codedesign","Portfolio hero (CodeDesign)","black frame + white card + watercolor portrait","hero: portrait art + headline + Resume/Contact + social icons","post embed (README/tutorial promo)"),
 38:("web/dashboard","erp-notifications-panel","ERP dashboard + notifications drawer","light + green accents (mockup on photo bg)","KPI trio + workflow tables + notification feed drawer",""),
 39:("web/dashboard","nexaflow-integrations","Integrations hub (NexaFlow)","light + violet accents + white cards","app grid (Slack/Drive/Notion/Zoom...) + connect panel + actions",""),
 40:("web/dashboard","greenflow-project-tracker","Project tracker (GreenFlow)","sage shell + green accents + white cards","phase stepper w/ rings + task list w/ progress + 62% overview rail",""),
 41:("mobile/fitness","arcs-gamification-6scr","Gamified fitness onboarding (Arcs)","dark + warm card art + mint CTAs","6scr: create/join arcs -> streak badges -> interests -> goals -> signup",""),
 42:("mobile/finance","stanley-wallet-dark","Dark wallet home (Stanley)","near-black + white text + green/red deltas","black balance hero $85k + quick-send avatars + income/expense cards",""),
 43:("mobile/finance","stanley-wallet-dark-alt","Dark wallet home, tighter crop","near-black + white + green/red deltas","same screen, single-phone crop","near-duplicate of stanley-wallet-dark"),
 44:("web/landing","mindmate-saas-landing","SaaS landing (MindMate)","light + green CTA + pastel product shots","hero + logo strip + feature split + product shot + testimonial",""),
 45:("techniques","wireframe-to-design-pair","Wireframe -> design pairing","grayscale wireframe vs warm brown design","same coffee app: gray boxes vs finished hierarchy",""),
 46:("_rejected_inbox","code-input-meme","Chat placeholder meme","n/a","dummy code block + 'You, hopefully doing better'","JUNK: meme, no anatomy"),
 47:("components","monthly-sales-chart-card","Monthly sales chart card","white + coral line + soft fill","line chart + tooltip + Weekly/Monthly toggle",""),
 48:("web/dashboard","margin-analysis-waterfall","Margin analysis (margin)","light + blue bars + pink/violet waterfall","34% KPI + target/waterfall decomposition + 12-week bars + insight rail",""),
 49:("web/settings","danger-zone-destructive","Danger zone destructive settings","white + red warnings + red CTAs","irreversible actions list + export/remove/delete w/ confirm buttons",""),
 50:("mobile/ecommerce","fashion-auction-hand","Fashion auction app in hand","white + warm photo bg + green CTA","product cards w/ bid chips + live badges + green Shop pill","photo mockup — crop phone before use"),
 51:("mobile/health","body-age-dark-6scr","Body-age questionnaire (dark)","near-black + mint CTAs + gray inputs","6scr: goals -> posture chart -> body map -> age -> metrics -> result",""),
 52:("mobile/health","health-score-morning","Morning health score","white + purple rings + orange accents","weekday rings + body/heart tiles + goal rows + score cards",""),
 53:("mobile/finance","arman-dark-fintech-3scr","Dark fintech set (Arman)","near-black + violet-blue accents + green deltas","3scr: balance+quick actions -> analytics bars+donut -> VISA card+tx list",""),
 54:("web/dashboard","agent-ops-dark-amber","Agent ops dark (traces)","near-black + amber/violet charts + red alerts","SLA 91.4% KPIs + agent compliance table + latency/quality charts",""),
 55:("web/dashboard","paysmooth-earnings","Earnings dashboard (PaySmooth)","light + black stat cards + dark sidebar","dark KPI trio + bar chart w/ tooltips + transactions + card panel",""),
 56:("web/dashboard","cerum-glucose-clinical","Clinical glucose monitor (Cerum)","light + teal/blue charts + soft donut","glucose KPIs + trend line + range donut + events + time-in-range",""),
 57:("mobile/utility","prayer-times-dark","Prayer times app (dark)","near-black + gray tiles + red accent","today prayer tiles + explore grid (names/hadith/mosques) + bottom nav",""),
 58:("mobile/utility","prayer-times-dark-alt","Prayer times list view","near-black + gray rows","prayer time rows w/ current highlight + explore grid","companion of prayer-times-dark"),
 59:("mobile/health","serenify-mindfulness-3scr","Mindfulness app (Serenify)","sage green + cream + soft illustration","3scr: login -> meditation cards w/ 76% goals -> mood donut + activities",""),
 60:("web/dashboard","sellhive-seller-ops","Seller ops dashboard (SellHive)","light + green bars + white cards + amber alerts","sales chart + KPI rail + order table w/ status pills + notification centre",""),
 61:("mobile/health","medplus-medication-4scr","Medication tracker (Med Plus)","white + steel-blue gauges + soft tiles","4scr: care list -> schedule day pills -> tracked gauge -> profile/forms",""),
 62:("mobile/ecommerce","stylehub-fashion-3scr","Fashion shop set (StyleHub)","white + teal CTA + soft tiles","3scr: hero+categories -> product detail w/ color chips -> cart+checkout",""),
}

INTROS = {
 "components": ("Components — cards, gauges, pills, feeds, popovers",
  "Reusable component-level references cropped from real products: list cards, status pills, gauge pairs, agent activity feeds, menus, chart cards."),
 "techniques": ("Techniques — concrete how-to rules with visual proof",
  "Design-technique reference cards: concentric radius formula, Android/iOS spec anatomy, wireframe-to-design pairing."),
 "_rejected_inbox": ("Rejected inbox — non-reference material",
  "Screens removed from the inbox that are NOT usable gallery references: collages, memes, banners, photos. Kept for provenance; never cite as anatomy references."),
 "mobile/health": ("Mobile — Health",
  "Health, fitness-adjacent wellness, telehealth and medication apps."),
}
DEFAULT_INTROS = {
 "web/dashboard": ("Web — Dashboards", "Desktop web dashboard patterns."),
 "web/landing": ("Web — Landing Pages", "Marketing landing page patterns for SaaS products."),
 "web/settings": ("Web — Settings", "Desktop web settings/account screens."),
 "mobile/finance": ("Mobile — Finance", "Mobile fintech: wallets, exchanges, payouts."),
 "mobile/fitness": ("Mobile — Fitness", "Mobile fitness tracking and gamified activity apps."),
 "mobile/social": ("Mobile — Social", "Leaderboards, group and social screens."),
 "mobile/productivity": ("Mobile — Productivity", "Task managers, calendars and assistant apps."),
 "mobile/education": ("Mobile — Education", "E-learning and self-improvement apps."),
 "mobile/ecommerce": ("Mobile — E-commerce", "Mobile shopping flows."),
 "mobile/settings": ("Mobile — Settings", "Monochrome mobile settings screens."),
 "mobile/onboarding": ("Mobile — Onboarding", "Mobile onboarding/activation flows."),
 "mobile/utility": ("Mobile — Utility", "Mobile widgets and utility surfaces."),
}
INTROS = {**DEFAULT_INTROS, **INTROS}

def table_row(n, e):
    folder, slug, pattern, palette, layout, note = e
    f = f"`{slug}.jpg`"
    if note:
        f += f" — {note}"
    return f"| {n} | {f} | {pattern} | {palette} | {layout} |"

def update_readme(folder, entries):
    rd = os.path.join(GAL, folder, "README.md")
    rows = [table_row(n, E[n]) for n in entries]
    title, intro = INTROS[folder]
    if not os.path.exists(rd):
        body = f"# {title}\n\n{intro}\n\n**Screens:** {len(entries)}  \n\n" \
               f"| # | File | Pattern | Palette | Layout |\n|---|------|---------|---------|--------|\n" \
               + "\n".join(rows) + "\n"
        os.makedirs(os.path.dirname(rd), exist_ok=True)
        open(rd, "w").write(body)
        return f"created {folder}/README.md ({len(entries)})"
    lines = open(rd).read().splitlines()
    # find last table row
    last_tr = max(i for i, l in enumerate(lines) if l.startswith("|") and not l.startswith("|--")
                  and "---" not in l and not l.startswith("| #"))
    new_count = None
    for i, l in enumerate(lines):
        m = re.match(r"\*\*Screens:\*\* (\d+)", l)
        if m:
            new_count = int(m.group(1)) + len(entries)
            lines[i] = f"**Screens:** {new_count}  "
    lines[last_tr+1:last_tr+1] = rows
    open(rd, "w").write("\n".join(lines) + "\n")
    return f"updated {folder}/README.md (+{len(entries)} -> {new_count})"

# group accepted entries by folder preserving numeric order
from collections import defaultdict
by_folder = defaultdict(list)
moved, rejected = [], []
for n in sorted(E):
    folder, slug = E[n][0], E[n][1]
    src = os.path.join(SRC, f"photo_{n}_2026-09-30_14-02-25.jpg")
    dst = os.path.join(GAL, folder, f"{slug}.jpg")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.exists(src):  # already moved by an earlier crashed run?
        shutil.copy2(src, dst)
        os.remove(src)
    else:
        assert os.path.exists(dst), f"missing both: {src} and {dst}"
    by_folder[folder].append(n)
    (rejected if folder == "_rejected_inbox" else moved).append(n)

reports = [update_readme(f, ns) for f, ns in sorted(by_folder.items())]
manifest = {str(n): dict(zip(("folder","slug","pattern","palette","layout","note"), E[n]),
                         file=f"gallery/{E[n][0]}/{E[n][1]}.jpg") for n in E}
json.dump(manifest, open(os.path.join(BASE, "_grids", "batch2_manifest.json"), "w"), indent=1)

print(f"moved {len(moved)} accepted, {len(rejected)} rejected")
print("\n".join(reports))
left = [f for f in os.listdir(SRC) if not f.startswith("README")]
print(f"inbox remaining: {len(left)}")
