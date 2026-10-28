# LabKey: Test Engineering Manager, first interview prep

Interview: ~45-60 min with Audrey Yilmaz, HR Director. Expect a conversation about
background, leadership, motivation and logistics, not a coding test. (If unsure, reply to
the invitation and ask what to expect.)

## About the role (from the posting)
- Player-coach: lead a team of 2 test engineers, stay hands-on, report to the CTO.
- Test strategy for SaaS and on-prem products; decide what to automate vs test manually.
- Improve CI/CD, test stability, flaky tests; prefer established tools over bespoke frameworks.
- Load, stress and soak testing; security/compliance validation (auth, data segregation, PHI).
- Mentor, partner with other teams, support audits.
- Stack mentioned: Selenium / Playwright / Cypress, TeamCity / Jenkins / GitHub Actions,
  Java, Postgres, AWS, LLM-based testing.
- Pay listed at $60-70/hour (about $125k-$146k a year if full-time salaried). No visa sponsorship.

## 1. Tell me about yourself (about 60-75 seconds)
"I'm a Senior SDET with over 14 years of experience in test automation and release
validation. Most recently at VMware/Broadcom I owned release validation for Tanzu Mission
Control, a multi-cloud Kubernetes SaaS platform. I built the CI/CD validation pipelines that
fed a release-readiness dashboard for go/no-go decisions, which cut manual validation effort
by 40% and cloud validation costs by 35%, and I ran large-scale performance, scalability and
longevity testing. For a year and a half I led a two-engineer team that delivered two major and
two minor Self-Managed releases, so I've done the lead part of a player-coach role and stayed
hands-on in the Golang and Selenium/Python automation. Earlier, at Microfocus, I mentored a
ten-person QA team and served as Scrum Master, and at Accenture I built Selenium and API
frameworks in Java. I've been on a planned break for childcare since January, and I've stayed
hands-on, including building an AI-assisted test generation tool. Leading a small team while
still writing tests is the work I enjoy most."

## 2. Why this role / why LabKey  (YOUR ANSWER NEEDED)
Fill these in with your real reasons; the recruiter will hear whether they're genuine.
- Why manage a small team and stay hands-on rather than a pure IC role? ______
- What draws you to LabKey (research and scientific data, the product, the size, the CTO
  reporting line)? ______
- Why now, after your break? ______
Facts you can truthfully connect to: you've led a 2-person team before; the posting says
"adopt established tools over bespoke frameworks" and you've built both kinds; you have
SaaS and on-prem-style release validation experience (Tanzu Mission Control SaaS and
Self-Managed).

## 3. Leadership stories (use STAR: Situation, Task, Action, Result)
Stories you can tell from your resume:
- **Led a 2-engineer team for 1.5 years**, delivering 2 major and 2 minor Tanzu Mission Control
  Self-Managed releases, owning end-to-end and new-feature testing, and extending the Golang
  automation framework to cover new features (shorter release cycle). (Add: how you split work,
  reviewed code, handled priorities, what you'd do differently.)
- **Release-readiness dashboard:** CI/CD validation pipelines feeding a go/no-go dashboard.
  (Good for "how do you decide a release is ready" questions.)
- **Selenium/Python UI suite** for the Tanzu Mission Control web app, integrated into CI/CD.
- **Prometheus and Grafana** are on your resume; the posting lists production telemetry and
  monitoring as preferred. Only describe what you actually did with them: ______
- **Mentored a 10-member QA team** at Microfocus in Java and Golang automation; also Scrum Master.
  (Add: how you taught them, what improved.)
- **Automation coverage from 40% to 80%** with keyword-driven Java frameworks (Microfocus), and
  30% to 70% with data-driven reusable components (Accenture).
- **CI/CD gatekeeping and cost:** 40% less manual validation, 35% lower cloud validation cost.
Stories I do NOT know and you must supply honestly, one each:
- A time you handled an underperforming or struggling teammate: ______
- A disagreement with a developer or manager about quality or release readiness: ______
- A time you changed priorities or cut scope under a deadline: ______
- A time a release went wrong, and what you changed afterwards: ______

## 4. The career break (keep it short and calm)
"I took a planned break from January to look after my child. I kept my skills current, building
a small LLM-based test generation project and practicing newer tools like Playwright, and I'm
ready to return to a full-time role."

## 5. Gaps, answered honestly
- **Playwright / JavaScript / TypeScript, Cypress:** "My depth is Java, Python, Golang and
  Selenium. Playwright is newer, and I've been hands-on with it recently. I pick up tools quickly
  because the underlying skills (locators, waits, framework design) transfer."
- **SQL / Postgres:** ______ (state exactly how much you've used it; do not overstate)
- **Compliance (HIPAA, SOC 2), accessibility, concurrency, scientific software:** these are
  "preferred" in the posting. If you haven't done them: "Not directly, and I'd want to learn
  them." If you have related experience (for example high-availability testing of vSphere HA),
  describe it exactly.
- **"10 years with Selenium/Playwright/Cypress":** you have 13 years of automation framework
  design in several languages; Selenium directly at Accenture. Describe it that way.
- **LLM-based testing:** "I built the first phase of a test case generator: it takes a
  requirement document and generates functional, negative, boundary and edge cases using an
  LLM, with structured output validated against a schema, and exports to CSV, Excel, Markdown
  and JSON. Integrating with CI failure analysis and Playwright generation is what I'd build next."
  Be clear that phase 1 is built and the rest is planned.

## 6. Title and level
Your resume (the one you sent LabKey) says Senior Member of Technical Staff (Senior SDET),
14+ years. Use exactly that title and number in every answer, and make sure it matches your
official VMware title, since employment verification may check it. Moving to a manager role is
a natural step: "I've led a two-engineer team and mentored ten people, and I want that to be my
main responsibility, while staying hands-on. This role leads a small team directly and reports
to the CTO, which is what I'm after." (Adjust to your real reason.)
Do not mention the older "Staff Engineer / 13+ years" version of the resume.

## 7. Logistics (YOUR ANSWERS NEEDED)
- **Work authorization:** your resume says "Authorized to work in the U.S. (no sponsorship
  required)", and the posting offers no sponsorship. Answer "will you require sponsorship now or in
  the future" exactly and truthfully, in a way that matches that line: ______
  (If unsure how your status should be described, check with your immigration attorney first.)
- **Compensation:** your number or range: ______ . Ask first: is this salaried employment or
  contract, and what are the bonus and stock options?
- **Location:** you are in Seattle; the posting says Seattle and doesn't state remote. Ask
  about on-site expectations.
- **Start date / notice:** ______ (you are not currently employed).
- **Other interviews or offers:** answer honestly and briefly.

## 8. Questions to ask Audrey
- How is quality measured today, and what would success look like in the first six months?
- What does the current test stack look like, and what's the split between SaaS and on-prem?
- What's the team of two like (their experience, what they work on)?
- How does LabKey use or expect to use LLM-based testing?
- What are the steps and the timeline of the interview process?
- Is the role on-site, hybrid or remote?

## 9. Before the call
- Re-read the posting once. Have your resume open.
- Water, quiet room, camera and microphone check. Keep a notepad for her answers.
- Don't claim anything you can't explain: Playwright depth, SQL depth, compliance experience.
