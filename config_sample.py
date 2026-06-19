# COPY-PASTE THIS FILE TO config.py AND FILL IN THE VALUES BELOW.
# config.py FILE SHALL BE IGNORED BY GIT TO PREVENT SECRET LEAK.
CLIENT_ID            =
CLIENT_SECRET        = ""
REDIRECT_URI         = "http://localhost:8727"

FORUM_ID             = 52
TOKEN_CACHE_FILE     = "osu_token_cache.json"
OSU_TOKEN_URL        = "https://osu.ppy.sh/oauth/token"
OSU_FORUM_URL        = "https://osu.ppy.sh/api/v2/forums/{forum_id}"

DB_PATH              = "database.json"
COMMAND_HISTORY_PATH = "command_history.json"
STATE_PATH           = "bot_state.json"
INTRO_PATH           = "post_intro.txt"

BOT_POST_ID          =
TICKS_PER_WEEK       = 40320
TAX_RATE             = 0.03
TAX_THRESHOLD        = 10000

BLACKLISTED_ITEMS    = ["admin_sword", "banhammer"]  # example blacklist
MAX_COMMAND_HISTORY  = 20

## RARITY CONFIG
RARITY_ORDER         = [
    ("common",      100),
    ("rare",        350),
    ("exotic",     1500),
    ("legendary", 10000),
    ("sacred",     None),  # no upgrades beyond sacred
]
# Total OT Bucks invested per item unit at each rarity (creation + all upgrades to reach it)
RARITY_TOTAL_COST = {
    "common":        1,   # 1 (creation)
    "rare":        101,   # 1 + 100
    "exotic":      451,   # 1 + 100 + 350
    "legendary":  1951,   # 1 + 100 + 350 + 1500
    "sacred":    11951,   # 1 + 100 + 350 + 1500 + 10000
}

## INVESTMENTS CONFIG
INVESTMENTS_PATH = "investments.json"

TIERS    = [ 10, 20, 30, 40, 50 ]
TIER_PCT = {
    10: 0.03,
    20: 0.07,
    30: 0.12,
    40: 0.25,
    50: 0.50,
}
# Full-reward window in hours per tier.
# Chosen time_limit ≤ base        -> ×1.0 reward
# base < time_limit ≤ 2×base     -> ×0.5 reward
# 2×base < time_limit ≤ 3×base   -> ×0.25 reward
# time_limit > 3×base             -> invalid (command fails)
TIER_BASE_HOURS = {
    10: 12,
    20: 24,
    30: 48,
    40: 72,
    50: 168,
}
