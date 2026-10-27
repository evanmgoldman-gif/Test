"""Merge trips + reservations into app.html -> dist/travel-board.html."""
import datetime, glob, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
trips = json.load(open(os.path.join(HERE, "data", "trips.json")))
reservations = []
for path in sorted(glob.glob(os.path.join(HERE, "data", "reservations", "*.json"))):
    reservations += json.load(open(path))

ids = {t["id"] for t in trips}
orphans = [r for r in reservations if r.get("trip_id") not in ids]
if orphans:
    print("warning: reservations with unknown trip_id:", sorted({r.get("trip_id") for r in orphans}))

today = datetime.date.today()
alerts_path = os.path.join(HERE, "data", "alerts.json")
alerts = json.load(open(alerts_path)) if os.path.exists(alerts_path) else []
plans = {}
for path in sorted(glob.glob(os.path.join(HERE, "data", "plans", "*.json"))):
    plans[os.path.splitext(os.path.basename(path))[0]] = json.load(open(path))
data = {"updated": today.strftime("%b ") + str(today.day) + today.strftime(", %Y"), "trips": trips, "reservations": reservations, "alerts": alerts, "plans": plans}
blob = json.dumps(data, ensure_ascii=False, indent=1).replace("<", "\\u003c")
html = open(os.path.join(HERE, "app.html")).read().replace("__TRIP_DATA__", blob, 1)
os.makedirs(os.path.join(HERE, "dist"), exist_ok=True)
out = os.path.join(HERE, "dist", "travel-board.html")
open(out, "w").write(html)
print(f"{out}: {len(trips)} trips, {len(reservations)} reservations")
