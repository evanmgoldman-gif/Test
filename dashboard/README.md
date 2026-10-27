# Travel Board

A shareable travel dashboard. It uses the same columns as the family travel doc:
Dates · Destination · Purpose · Traveling Parties · Car · Flight · Flight Cost · Hotel · Hotel Cost.
Each trip also gets a day-by-day itinerary built from booking emails, with
confirmation numbers, times, addresses and a link back to the source email.

## Pieces

- `app.html`: the page. Its data is embedded in `<script id="trip-data">`.
- `data/trips.json`: one object per trip (see `data/trips.sample.json` for the shape).
- `data/reservations/*.json`: bookings pulled from Gmail / Outlook. Fields: `trip_id`, `type`
  (flight, hotel, car, cruise, train, transfer, parking, activity, dining, other), `title`, `provider`,
  `confirmation`, `start`/`end` (local ISO time), `location`, `details`, `travelers`, `cost`,
  `source`, `email_link`, `status`.
- `build.py`: merges the data into `dist/travel-board.html`.

`trips.json`, `reservations/` and `dist/` are git-ignored because this repo is public.

## Editing

The page is published as a claude.ai Artifact. The owner (and anyone given edit access) can
add or edit trips, add reservations, tick checklist items and write notes right on the page.
"Save for everyone" publishes a new version. Family members with the link get a read-only view.

The published page is the source of truth once it exists. Claude syncs new booking emails by
reading the live page's data, merging in new reservations, and republishing.
