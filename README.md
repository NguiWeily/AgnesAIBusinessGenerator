# AgnesAI Business Generator
<img width="506" height="900" alt="image" src="https://github.com/user-attachments/assets/c305a4e5-c36a-4736-90a4-b91eba82990d" />

Home business plan generator
---------------------------

Generate a detailed home business plan from a short description.

Usage:

```bash
python scripts/business_plan.py "A home tutoring service for middle school math students"
```

Or with structured JSON output:

```bash
python scripts/business_plan.py "A local meal prep delivery service" --json
```

This tool returns a detailed plan with:
- revenue streams
- startup budget estimates
- cashflow milestones
- license requirements
- required skills
- first million timeline

Web app added:
- `web/index.html` for inputting a business idea and generating a plan
- `web/sample_plans.html` for browsing 100 sample home business plans
- `web/app.js` generator logic and `web/styles.css` styling

Files added: [scripts/chat.sh](scripts/chat.sh), [scripts/chat.py](scripts/chat.py), [.env.example](.env.example), [src/business_plan.py](src/business_plan.py), [scripts/business_plan.py](scripts/business_plan.py), [web/index.html](web/index.html), [web/sample_plans.html](web/sample_plans.html), [web/app.js](web/app.js), [web/styles.css](web/styles.css)
