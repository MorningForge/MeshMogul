/* Progressive, same-origin search. All browsing links already exist in the HTML. */
"use strict";

(async () => {
  const controls = document.getElementById("search-controls");
  const form = document.getElementById("guide-search");
  const query = document.getElementById("search-query");
  const subject = document.getElementById("subject-filter");
  const difficulty = document.getElementById("difficulty-filter");
  const status = document.getElementById("search-status");
  const empty = document.getElementById("empty-results");
  const cards = [...document.querySelectorAll("[data-guide]")];
  const sections = [...document.querySelectorAll(".guide-track")];
  const normalize = value => value.normalize("NFKD").toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, " ").trim();

  try {
    // Relative to the reviewed module, never to visitor input or query parameters.
    const response = await fetch("../assets/foundations-search-index.json", {
      mode: "same-origin", credentials: "omit", redirect: "error"
    });
    if (!response.ok) throw new Error("Index unavailable");
    const index = await response.json();
    if (!Array.isArray(index) || index.length !== cards.length) throw new Error("Incomplete index");
    const entries = new Map(index.map(entry => [entry.slug, {
      ...entry,
      searchable: normalize([entry.title, entry.summary, ...entry.tags,
        ...entry.symptoms, entry.content].join(" "))
    }]));
    if (cards.some(card => !entries.has(card.dataset.guide))) throw new Error("Missing guide");

    function update() {
      const terms = normalize(query.value).split(/\s+/).filter(Boolean);
      let count = 0;
      for (const card of cards) {
        const entry = entries.get(card.dataset.guide);
        const levels = entry.difficulty.split("-to-");
        const levelMatch = !difficulty.value || levels.includes(difficulty.value) ||
          (difficulty.value === "intermediate" && levels[0] === "beginner" && levels[1] === "advanced");
        const match = (!subject.value || entry.track === subject.value) && levelMatch &&
          terms.every(term => entry.searchable.includes(term));
        card.hidden = !match;
        if (match) count += 1;
      }
      for (const section of sections) {
        section.hidden = ![...section.querySelectorAll("[data-guide]")].some(card => !card.hidden);
      }
      empty.hidden = count !== 0;
      status.textContent = `${count} ${count === 1 ? "guide" : "guides"} found.`;
    }

    form.addEventListener("submit", event => { event.preventDefault(); update(); });
    query.addEventListener("input", update);
    subject.addEventListener("change", update);
    difficulty.addEventListener("change", update);
    for (const anchor of document.querySelectorAll(".foundations-tracks a")) {
      anchor.addEventListener("click", () => {
        query.value = "";
        difficulty.value = "";
        subject.value = anchor.hash.slice(1);
        update();
      });
    }
    form.addEventListener("reset", () => {
      query.value = "";
      subject.value = "";
      difficulty.value = "";
      update();
    });
    controls.hidden = false;
    update();
  } catch {
    // Failed or disabled enhancement leaves a complete static library.
    controls.hidden = true;
    for (const card of cards) card.hidden = false;
    for (const section of sections) section.hidden = false;
  }
})();
