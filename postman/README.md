# Postman API Tests — Hotel Booking

Postman collection and environment for the Restful Booker Platform API
(`https://automationintesting.online`).

## Contents
- `HotelBooking.postman_collection.json` — the test collection
- `HotelBooking.postman_environment.json` — environment variables

## Collection structure (16 requests across 5 folders)

| Folder | Requests | Coverage |
|--------|----------|----------|
| Auth | Login valid / invalid | Token capture, 401 negative |
| Rooms | GET all / by id / invalid id / create / create-invalid | CRUD + validation |
| Booking | create / bad-dates / missing-field / get / delete-no-auth / delete | Positive, negative, auth |
| Message | valid / invalid email | Positive + validation |
| Branding | GET branding | Read + schema check |

Each request contains **test assertions** (status code, body fields, response time).
`token`, `roomid`, and `bookingid` are captured at runtime by earlier requests
and reused by later ones — so run the collection top-to-bottom (or with the
Collection Runner / Newman, which preserves order).

## How to run — Postman app (GUI)
1. Open Postman → **Import** → drag in both JSON files.
2. Top-right environment dropdown → select **Hotel Booking - Live**.
3. Click the collection → **Run** → **Run Hotel Booking API**.
4. Review the pass/fail results; screenshot for the project README.

## How to run — Newman (CLI, for CI)
Newman is Postman's command-line runner. Requires Node.js.

```bash
# install once (both packages: newman + the HTML reporter)
npm install -g newman newman-reporter-htmlextra

# run the collection with the environment and an HTML report
newman run postman/HotelBooking.postman_collection.json \
  -e postman/HotelBooking.postman_environment.json \
  -r cli,htmlextra \
  --reporter-htmlextra-export reports/newman-report.html
```

Or without a global install, via npx:

```bash
npx --package newman --package newman-reporter-htmlextra newman run \
  postman/HotelBooking.postman_collection.json \
  -e postman/HotelBooking.postman_environment.json \
  -r cli,htmlextra --reporter-htmlextra-export reports/newman-report.html
```

**Last verified run:** 16/16 requests, **28/28 assertions passed** against the live API.

The HTML report lands in `reports/newman-report.html` — link it from the main README.

## Notes
- This is a **shared public** test server; data may reset periodically and IDs
  change, which is why IDs are captured dynamically rather than hard-coded.
- The `password` and `token` variables are marked `secret`; never commit real
  secrets for private APIs (this one is a public demo credential).
