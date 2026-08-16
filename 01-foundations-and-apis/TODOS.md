## TODOs / challenges

1. Write a Pydantic model for a "scraped page" result. Decide what fields
   are required vs optional, and what should be validated (e.g. a URL field
   that must actually be a URL).
2. Write an async function using `httpx.AsyncClient` that fetches a URL and
   returns the parsed result as your model. Handle: timeout, non-200
   response, malformed HTML — without crashing the caller.
3. Wrap it in a FastAPI app: one `POST` endpoint that accepts a URL, calls
   your scraper, returns the validated model as JSON. Confirm a bad input
   (not a URL) returns 422 *without you writing that check yourself* —
   that's Pydantic doing its job at the boundary.
4. Write 2+ tests with `httpx.AsyncClient` against the app (no live network
   call in the test — mock the fetch).
5. Challenge: add a semaphore to cap concurrent scrapes, and prove to
   yourself it works (e.g. by timing 20 requests with/without the cap).