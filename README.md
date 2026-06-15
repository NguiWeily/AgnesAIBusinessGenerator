# AgnesAI Business Generator

This repository is a fresh workspace scaffold created by GitHub Copilot.

Next steps:
- Add your project source code into the `src/` directory.
- Choose a language/framework and add relevant config files (e.g., `requirements.txt`, `package.json`).
- Commit and push to a remote repository if desired.

Agnes AI chat examples
----------------------

Secure examples for creating a chat completion with the Agnes AI API. Do NOT hardcode your API key; set it in your environment as shown below.

1) Environment

Create a `.env` or set the environment variable `AGNES_API_KEY` to your API key.

2) Curl (recommended)

Use the `curl` command and read the API key from the environment:

```bash
curl https://apihub.agnes-ai.com/v1/chat/completions \
	-H "Authorization: Bearer $AGNES_API_KEY" \
	-H "Content-Type: application/json" \
	-d '{
		"model": "agnes-2.0-flash",
		"messages": [
			{"role": "user", "content": "Hello!"}
		]
	}'
```

3) Bash helper script

See `scripts/chat.sh` for a small helper that reads `AGNES_API_KEY` and sends a message.

4) Python example

See `scripts/chat.py` for a minimal Python example using `requests`.

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
