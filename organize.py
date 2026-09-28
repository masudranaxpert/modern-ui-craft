"""Organize raw images from Galary/ into categorized gallery/ folders."""
import os
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "Galary")
GALLERY = os.path.join(BASE, "gallery")

# Historical mapping of initial 48 images
M = {
    1:  ("web/dashboard", "crm-pm-crestway-timeline"),
    2:  ("web/dashboard", "crm-analytics-orange-gauges"),
    3:  ("mobile/ecommerce", "floriva-flower-shop-3scr"),
    4:  ("web/dashboard", "crm-table-filters-modal"),
    5:  ("web/dashboard", "careflow-healthcare-ops"),
    6:  ("mobile/finance", "breet-wallet-teal-3scr"),
    7:  ("mobile/fitness", "body-readiness-dark-2scr"),
    8:  ("web/dashboard", "marketing-analytics-hubspot"),
    9:  ("mobile/finance", "payout-success-confirm"),
    10: ("mobile/finance", "send-payout-keypad"),
    11: ("web/landing", "sapick-finance-landing"),
    12: ("mobile/finance", "crypto-wallet-green-3ai"),
    13: ("web/dashboard", "spend-against-plan-card"),
    14: ("web/dashboard", "pm-linear-kanban-panels"),
    15: ("web/dashboard", "medspa-client-profile"),
    16: ("mobile/finance", "crypto-wallet-mint-home"),
    17: ("web/dashboard", "sales-widgets-minicharts"),
    18: ("web/dashboard", "databrain-realestate-analytics"),
    19: ("mobile/finance", "waley-pro-paywall-dark"),
    20: ("mobile/finance", "eth-exchange-3scr"),
    21: ("web/dashboard", "workflow-builder-nodes"),
    22: ("mobile/fitness", "fitness-week-metrics-dark"),
    23: ("mobile/social", "global-rank-leaderboard"),
    24: ("mobile/social", "amble-group-sheet"),
    25: ("web/dashboard", "trackly-dark-analytics"),
    26: ("web/dashboard", "knowojo-learning-dashboard"),
    27: ("web/dashboard", "mailvista-email-marketing"),
    28: ("mobile/finance", "crypto-wallet-blue-4scr"),
    29: ("mobile/finance", "crypto-analytics-bars-3scr"),
    30: ("mobile/utility", "system-monitor-widgets"),
    31: ("mobile/onboarding", "habit-wins-illustrated"),
    32: ("web/settings", "securevault-security-settings"),
    33: ("web/dashboard", "vantage-cmdk-palette"),
    34: ("web/dashboard", "support-analytics-yellow"),
    35: ("web/dashboard", "vantage-run-trace"),
    36: ("web/dashboard", "vantage-runs-overview"),
    37: ("web/dashboard", "vantage-runs-table"),
    38: ("web/dashboard", "sakanbeasa-logistics"),
    39: ("web/dashboard", "wiseproedit-forms-dashboard"),
    40: ("mobile/productivity", "task-manager-aurora-3scr"),
    41: ("web/dashboard", "sales-table-funnel"),
    42: ("web/dashboard", "acme-crm-sidebar"),
    43: ("mobile/education", "sephia-courses-2scr"),
    44: ("web/dashboard", "revenue-sidebar-tilted"),
    45: ("web/dashboard", "invoicing-finance-overview"),
    46: ("mobile/settings", "torin-settings-monochrome"),
    47: ("web/dashboard", "haulsight-freight-analytics"),
    48: ("web/dashboard", "orchestrateiq-agent-ops"),
}

def check_inbox():
    """List pending images in Galary/ inbox waiting to be categorized."""
    if not os.path.exists(SRC):
        os.makedirs(SRC, exist_ok=True)
        return []
    
    files = [
        f for f in os.listdir(SRC)
        if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
    ]
    return sorted(files)

if __name__ == "__main__":
    pending = check_inbox()
    if not pending:
        print("Inbox (Galary/) is empty. Drop raw screenshots here to organize them.")
    else:
        print(f"Found {len(pending)} pending image(s) in Galary/:")
        for f in pending:
            print(f" - {f}")
