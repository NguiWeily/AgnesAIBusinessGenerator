from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

@dataclass
class BusinessPlan:
    description: str
    model: str
    target_customers: str
    value_proposition: str
    revenue_streams: List[str]
    startup_budget: Dict[str, str]
    cashflow: Dict[str, str]
    license_requirements: List[str]
    required_skills: List[str]
    first_million_timeline: str
    milestones: List[str]
    risks: List[str]
    budget_summary: str
    cashflow_summary: str


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def choose_model(description: str) -> str:
    text = normalize(description)
    if any(word in text for word in ["saas", "software", "app", "platform"]):
        return "SaaS / Software"
    if any(word in text for word in ["course", "coaching", "training", "education", "tutoring"]):
        return "Digital education / coaching"
    if any(word in text for word in ["e-commerce", "store", "shop", "product", "retail"]):
        return "E-commerce / online store"
    if any(word in text for word in ["consulting", "agency", "freelance", "service"]):
        return "Service business / consulting"
    if any(word in text for word in ["subscription", "membership", "community"]):
        return "Subscription / membership"
    if any(word in text for word in ["content", "blog", "youtube", "podcast"]):
        return "Content creation / creator business"
    return "Home-based small business"


def choose_target(description: str) -> str:
    text = normalize(description)
    if "small business" in text or "startup" in text:
        return "Small business owners and founders looking for smart work solutions."
    if "family" in text or "parent" in text or "kids" in text:
        return "Busy families and parents who need convenient solutions."
    if "student" in text or "students" in text:
        return "Students and lifelong learners seeking practical skills."
    if "pet" in text or "animal" in text:
        return "Pet owners who want better care and convenience."
    if "health" in text or "wellness" in text or "fitness" in text:
        return "Health-conscious individuals who value lifestyle improvement."
    return "Local and online customers who want a simple, high-value solution from a trusted home business."


def choose_value_proposition(description: str) -> str:
    return f"Create a low-overhead home business offering {description.strip()}. Focus on fast delivery, clear pricing, and a strong online presence."


def estimate_revenue(description: str) -> List[str]:
    model = choose_model(description)
    options = []
    if model == "SaaS / Software":
        options = ["Monthly subscriptions", "Annual licenses", "White-label customization", "Premium support plans"]
    elif model == "Digital education / coaching":
        options = ["Course enrollment", "Coaching packages", "Group workshops", "Digital downloads"]
    elif model == "E-commerce / online store":
        options = ["Product sales", "Bundles", "Repeat purchases", "Cross-sell accessories"]
    elif model == "Service business / consulting":
        options = ["Project fees", "Hourly retainers", "Recurring support agreements", "Referral bonuses"]
    elif model == "Subscription / membership":
        options = ["Monthly memberships", "Premium tiers", "Community access", "Add-on services"]
    elif model == "Content creation / creator business":
        options = ["Ad revenue", "Sponsorships", "Affiliate sales", "Paid newsletters"]
    else:
        options = ["Direct service fees", "Small product sales", "Online offerings", "Referral income"]
    return options


def estimate_budget(description: str) -> Dict[str, str]:
    model = choose_model(description)
    if model == "SaaS / Software":
        return {
            "Website and hosting": "$300 - $1,200",
            "Domain and SSL": "$20 - $80",
            "Development tools": "$0 - $500",
            "Marketing / launch": "$500 - $2,000",
            "Legal / business setup": "$200 - $800",
        }
    if model == "Digital education / coaching":
        return {
            "Course platform / LMS": "$100 - $500",
            "Video / audio equipment": "$200 - $1,000",
            "Marketing / ads": "$300 - $1,500",
            "Website / landing page": "$100 - $400",
            "Legal / contracts": "$100 - $500",
        }
    if model == "E-commerce / online store":
        return {
            "Inventory / samples": "$500 - $3,000",
            "Shop setup": "$100 - $400",
            "Packaging / shipping": "$200 - $800",
            "Marketing / social ads": "$400 - $1,500",
            "Business registration": "$100 - $300",
        }
    if model == "Service business / consulting":
        return {
            "Website / professional profile": "$100 - $300",
            "Tools / software": "$50 - $300",
            "Marketing / networking": "$200 - $800",
            "Professional insurance": "$150 - $500",
            "Business license": "$50 - $250",
        }
    if model == "Subscription / membership":
        return {
            "Community platform": "$150 - $600",
            "Content creation": "$200 - $800",
            "Marketing": "$300 - $1,200",
            "Support systems": "$100 - $400",
            "Legal / terms": "$150 - $500",
        }
    return {
        "Basic website": "$100 - $300",
        "Home office setup": "$100 - $500",
        "Marketing": "$200 - $800",
        "Software tools": "$50 - $300",
        "Legal / registration": "$100 - $400",
    }


def estimate_cashflow(description: str) -> Dict[str, str]:
    model = choose_model(description)
    if model == "SaaS / Software":
        return {
            "Month 1-3": "Build MVP, begin outreach, invest in content.",
            "Month 4-6": "Acquire early subscribers, refine onboarding.",
            "Month 7-12": "Scale marketing, improve retention, target 100+ paid users.",
        }
    if model == "Digital education / coaching":
        return {
            "Month 1-3": "Create core course or coaching program, pre-launch to audience.",
            "Month 4-6": "Launch, collect testimonials, run ads and partnerships.",
            "Month 7-12": "Refine offers, enroll repeat clients, add upsells.",
        }
    if model == "E-commerce / online store":
        return {
            "Month 1-3": "Source products, build store, begin small campaigns.",
            "Month 4-6": "Increase advertising, monitor margins, optimize logistics.",
            "Month 7-12": "Expand product lines, increase repeat purchases.",
        }
    if model == "Service business / consulting":
        return {
            "Month 1-3": "Set up service portfolio, land first clients, refine pricing.",
            "Month 4-6": "Secure regular contracts and referrals.",
            "Month 7-12": "Build predictable monthly revenue and systemize delivery.",
        }
    if model == "Subscription / membership":
        return {
            "Month 1-3": "Validate the membership idea, gather founding members.",
            "Month 4-6": "Expand membership base and add premium benefits.",
            "Month 7-12": "Retain members, increase average revenue per user.",
        }
    return {
        "Month 1-3": "Validate the idea, test offers, set up operations.",
        "Month 4-6": "Grow awareness, book paying customers, manage cash carefully.",
        "Month 7-12": "Move toward consistent profit, reinvest in growth.",
    }


def estimate_licenses(description: str) -> List[str]:
    text = normalize(description)
    licenses = ["General business license / local registration"]
    if any(keyword in text for keyword in ["food", "cafe", "restaurant", "catering"]):
        licenses.append("Health department permit")
    if any(keyword in text for keyword in ["child", "kids", "education", "tutor"]):
        licenses.append("Home child care / education permit if needed")
    if any(keyword in text for keyword in ["construction", "electrician", "plumbing", "contractor"]):
        licenses.append("Trade or professional license")
    if "retail" in text or "shop" in text or "store" in text:
        licenses.append("Sales tax permit")
    if "professional" in text or "consulting" in text or "therapy" in text:
        licenses.append("Professional liability insurance and contracts")
    if "online" in text or "digital" in text:
        licenses.append("E-commerce compliance and privacy policy")
    return licenses


def estimate_skills(description: str) -> List[str]:
    skills = ["Customer research", "Basic bookkeeping", "Online marketing", "Project planning"]
    text = normalize(description)
    if any(word in text for word in ["website", "e-commerce", "online", "digital"]):
        skills.append("Web presence and digital marketing")
    if any(word in text for word in ["course", "coaching", "training"]):
        skills.append("Instructional design and client coaching")
    if any(word in text for word in ["consult", "service", "agency"]):
        skills.append("Client communication and sales")
    if any(word in text for word in ["product", "manufacturing", "shop"]):
        skills.append("Product sourcing and supply chain")
    if any(word in text for word in ["saas", "software", "app"]):
        skills.append("Product development and user experience")
    return sorted(set(skills))


def timeline_first_million(description: str) -> str:
    model = choose_model(description)
    if model == "SaaS / Software":
        return "18-30 months with aggressive user acquisition and recurring revenue."
    if model == "Digital education / coaching":
        return "12-24 months if you build a flagship high-ticket offer and scale with digital funnels."
    if model == "E-commerce / online store":
        return "24-36 months depending on margins and repeat purchases."
    if model == "Service business / consulting":
        return "24-48 months if you convert high-value clients and scale retention."
    if model == "Subscription / membership":
        return "18-30 months with strong retention and product-led growth."
    return "24-42 months for a home-business starting from scratch and reinvesting profits."


def plan_from_description(description: str) -> BusinessPlan:
    model = choose_model(description)
    revenue = estimate_revenue(description)
    budget = estimate_budget(description)
    cashflow = estimate_cashflow(description)
    license_reqs = estimate_licenses(description)
    skills = estimate_skills(description)
    timeline = timeline_first_million(description)
    summary = f"A focused home business plan built around {model.lower()} with a target market of {choose_target(description)}"
    budget_summary = (
        "Startup costs are designed to stay lean. Budget for website/tools, basic marketing, legal registration, "
        "and a small operational runway. Keep the first 90 days tightly controlled."
    )
    cashflow_summary = (
        "Expect initial negative or flat cashflow while validating the offer, then positive cashflow after landing regular customers. "
        "Reinvest early profits into marketing and customer experience."
    )
    milestones = [
        "Month 1-3: Validate the idea, launch a minimum viable offer, and close the first paying customer.",
        "Month 4-6: Improve the offer, build repeatable sales, and secure a reliable marketing channel.",
        "Month 7-12: Create systems for delivery, scale revenue, and prepare for the next growth phase.",
    ]
    risks = [
        "Slow customer acquisition if marketing or positioning is unclear.",
        "Cashflow pressure during the first 3-6 months if revenues lag expectations.",
        "Competition from other small businesses and online alternatives.",
    ]
    return BusinessPlan(
        description=description,
        model=model,
        target_customers=choose_target(description),
        value_proposition=choose_value_proposition(description),
        revenue_streams=revenue,
        startup_budget=budget,
        cashflow=cashflow,
        license_requirements=license_reqs,
        required_skills=skills,
        first_million_timeline=timeline,
        milestones=milestones,
        risks=risks,
        budget_summary=budget_summary,
        cashflow_summary=cashflow_summary,
    )


def format_plan(plan: BusinessPlan) -> str:
    lines = [
        "HOME BUSINESS PLAN",
        "==================",
        "",
        f"Business description: {plan.description}",
        f"Business model: {plan.model}",
        f"Target customers: {plan.target_customers}",
        "",
        "Value proposition:",
        plan.value_proposition,
        "",
        "Revenue streams:",
    ]
    lines.extend(f"- {item}" for item in plan.revenue_streams)
    lines.extend([
        "",
        "Startup budget estimates:",
    ])
    for category, estimate in plan.startup_budget.items():
        lines.append(f"- {category}: {estimate}")
    lines.extend([
        "",
        "Cashflow plan:",
    ])
    for period, detail in plan.cashflow.items():
        lines.append(f"- {period}: {detail}")
    lines.extend([
        "",
        "License and compliance:",
    ])
    for license_text in plan.license_requirements:
        lines.append(f"- {license_text}")
    lines.extend([
        "",
        "Required skills:",
    ])
    for skill in plan.required_skills:
        lines.append(f"- {skill}")
    lines.extend([
        "",
        f"First million timeline: {plan.first_million_timeline}",
        "",
        "Milestones:",
    ])
    for milestone in plan.milestones:
        lines.append(f"- {milestone}")
    lines.extend([
        "",
        "Key risks:",
    ])
    for risk in plan.risks:
        lines.append(f"- {risk}")
    lines.extend([
        "",
        "Budget summary:",
        plan.budget_summary,
        "",
        "Cashflow summary:",
        plan.cashflow_summary,
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate a home business plan from a brief description."
    )
    parser.add_argument(
        "description",
        nargs="?",
        help="Short description of the business idea."
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output the plan as JSON."
    )
    args = parser.parse_args()

    if args.description:
        description = args.description
    else:
        description = input("Enter a short home business description: ")

    plan = plan_from_description(description)

    if args.json:
        print(json.dumps(asdict(plan), indent=2))
    else:
        print(format_plan(plan))


if __name__ == "__main__":
    main()
