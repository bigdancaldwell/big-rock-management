// ===== Settings you may need to change =====
// 1. Formspree: create a free form at https://formspree.io that delivers to BigRockLMTD@gmail.com,
//    then paste its endpoint here (looks like "https://formspree.io/f/abcdwxyz").
//    Until then, the quote form opens the visitor's email app with everything filled in.
const FORM_ENDPOINT = "";
const EMAIL = "BigRockLMTD@gmail.com";
// ============================================

// Mobile menu
const toggle = document.querySelector(".nav-toggle");
const nav = document.getElementById("site-nav");
if (toggle && nav) {
  const setOpen = (open) => {
    nav.classList.toggle("is-open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  };
  toggle.addEventListener("click", () => setOpen(!nav.classList.contains("is-open")));
  nav.addEventListener("click", (e) => { if (e.target.closest("a")) setOpen(false); });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && nav.classList.contains("is-open")) { setOpen(false); toggle.focus(); }
  });
}

// Preselect the service when arriving from a service page, e.g. ?service=hauling#quote
const params = new URLSearchParams(location.search);
const serviceSelect = document.getElementById("q-service");
if (serviceSelect && params.get("service")) {
  const match = [...serviceSelect.options].find((o) => o.value === params.get("service"));
  if (match) serviceSelect.value = match.value;
}

// Quote form
const form = document.querySelector(".form");
if (form) {
  const status = form.querySelector(".form__status");
  const button = form.querySelector('button[type="submit"]');
  const buttonText = button.querySelector("span");

  const show = (kind, html) => {
    status.className = `form__status is-shown is-${kind}`;
    status.innerHTML = html;
    status.focus();
  };

  const mailtoFrom = (data) => {
    const service = serviceSelect ? serviceSelect.selectedOptions[0].textContent : "";
    const lines = [
      `Name: ${data.get("name")}`,
      `Email: ${data.get("email")}`,
      data.get("phone") ? `Phone: ${data.get("phone")}` : "",
      `Service: ${service}`,
      `Area: ${data.get("area")}`,
      "",
      data.get("details") || "",
    ].filter((l, i) => l !== "" || i === 5);
    return `mailto:${EMAIL}?subject=${encodeURIComponent(`Free quote request: ${service}`)}&body=${encodeURIComponent(lines.join("\n"))}`;
  };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const data = new FormData(form);
    if (data.get("_gotcha")) return;

    if (!FORM_ENDPOINT) {
      window.location.href = mailtoFrom(data);
      show("ok", `Your email app should open with your request filled in. Just hit send. If nothing opened, email us at <a href="mailto:${EMAIL}">${EMAIL}</a>.`);
      return;
    }

    button.disabled = true;
    buttonText.textContent = "Sending…";
    try {
      const res = await fetch(FORM_ENDPOINT, { method: "POST", body: data, headers: { Accept: "application/json" } });
      if (!res.ok) throw new Error(String(res.status));
      form.reset();
      show("ok", "Got it. We'll email you back with your free quote.");
    } catch {
      show("err", `That didn't send. Your details are still here, so try again, or <a href="${mailtoFrom(data)}">send it by email instead</a>.`);
    } finally {
      button.disabled = false;
      buttonText.textContent = "Send my quote request";
    }
  });
}
